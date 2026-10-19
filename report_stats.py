import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/stary/Downloads/archive/student_habits_performance.csv')

print('shape', df.shape)
num = df.select_dtypes('number')
print('\n=== describe ===')
print(df.describe().T[['mean','std','min','50%','max']].round(2).to_string())

print('\n=== corr with exam_score ===')
c = num.corr()['exam_score'].drop('exam_score').sort_values(ascending=False)
print(c.round(3).to_string())

print('\n=== study R2 ===')
r = num.corr()['exam_score']['study_hours_per_day']
print('r', round(r,3), 'r2', round(r**2,3))
slope, intercept = np.polyfit(df['study_hours_per_day'], df['exam_score'], 1)
print('slope', round(slope,2), 'intercept', round(intercept,2))

print('\n=== study quartiles vs score ===')
df['study_q'] = pd.qcut(df['study_hours_per_day'], 4, duplicates='drop')
print(df.groupby('study_q', observed=True)['exam_score'].agg(['count','mean','min','max']).round(1).to_string())

print('\n=== sleep buckets ===')
sb = pd.cut(df['sleep_hours'], [0,5,6,7,8,9,24])
print(df.groupby(sb, observed=True)['exam_score'].agg(['count','mean']).round(1).to_string())
low = df[df['sleep_hours'] < 6]['exam_score']
ok = df[(df['sleep_hours'] >= 7) & (df['sleep_hours'] <= 8)]['exam_score']
print('sleep<6 mean', round(low.mean(),1), 'sleep7-8 mean', round(ok.mean(),1), 'diff', round(ok.mean()-low.mean(),1))

print('\n=== media buckets ===')
df['media_total'] = df['social_media_hours'] + df['netflix_hours']
mb = pd.cut(df['media_total'], [0,2,3,4,5,6,99])
print(df.groupby(mb, observed=True)['exam_score'].agg(['count','mean']).round(1).to_string())
hi = df[df['media_total'] >= 5]['exam_score']
lo = df[df['media_total'] < 3]['exam_score']
print('media>=5 mean', round(hi.mean(),1), 'media<3 mean', round(lo.mean(),1), 'diff', round(lo.mean()-hi.mean(),1))

print('\n=== rates ===')
print('study<3h:', round((df['study_hours_per_day']<3).mean()*100,1))
print('sleep<6h:', round((df['sleep_hours']<6).mean()*100,1))
print('media>4h:', round((df['media_total']>4).mean()*100,1))
print('exam<60:', round((df['exam_score']<60).mean()*100,1))
print('attendance<80:', round((df['attendance_percentage']<80).mean()*100,1))

print('\n=== attendance / mental health / exercise corr ===')
for col in ['attendance_percentage','mental_health_rating','exercise_frequency','internet_quality','diet_quality']:
    if col in num.columns:
        print(col, round(num.corr()['exam_score'][col],3))

print('\n=== categorical groups ===')
for col in ['part_time_job','diet_quality','extracurricular_participation','parental_education_level','gender']:
    g = df.groupby(col, observed=True)['exam_score'].mean().round(1)
    print(col, g.to_dict())

print('\n=== high study vs low study, keeping media same ===')
top = df[df['study_hours_per_day'] >= 5]['exam_score'].mean()
bot = df[df['study_hours_per_day'] < 2]['exam_score'].mean()
print('study>=5', round(top,1), 'study<2', round(bot,1), 'diff', round(top-bot,1))

print('\n=== multivariate: simple OLS via numpy ===')
X = df[['study_hours_per_day','sleep_hours','social_media_hours','netflix_hours','attendance_percentage']].to_numpy()
X = np.c_[np.ones(len(X)), X]
y = df['exam_score'].to_numpy()
beta, *_ = np.linalg.lstsq(X, y, rcond=None)
names = ['const','study','sleep','sns','netflix','attendance']
pred = X @ beta
ss_res = ((y - pred)**2).sum()
ss_tot = ((y - y.mean())**2).sum()
print(dict(zip(names, np.round(beta,3))))
print('R2', round(1 - ss_res/ss_tot,3))
