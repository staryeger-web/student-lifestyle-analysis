import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.family'] = ['Malgun Gothic', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('C:/Users/stary/Downloads/archive/student_habits_performance.csv')
df['media_total_hours'] = df['social_media_hours'] + df['netflix_hours']
os.makedirs('plots', exist_ok=True)

# 1. correlation heatmap
cols = ['study_hours_per_day', 'sleep_hours', 'attendance_percentage', 'exercise_frequency',
        'mental_health_rating', 'social_media_hours', 'netflix_hours', 'exam_score']
lab = ['공부시간', '수면시간', '출석률', '운동', '정신건강', 'SNS', '넷플릭스', '시험점수']
corr = df[cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdBu_r', center=0,
            xticklabels=lab, yticklabels=lab, vmin=-1, vmax=1,
            annot_kws={'size': 11}, cbar_kws={'shrink': 0.8})
plt.title('변수 간 상관관계 히트맵', fontsize=14, pad=12)
plt.tight_layout()
plt.savefig('plots/corr_heatmap.png', dpi=150)
plt.close()

# 2. exam score distribution
plt.figure(figsize=(7, 4.5))
sns.histplot(df['exam_score'], bins=30, color='#1f77b4', edgecolor='white')
plt.axvline(df['exam_score'].mean(), color='#d62728', ls='--', lw=2,
            label=f'평균 {df["exam_score"].mean():.1f}점')
plt.axvline(60, color='#2ca02c', ls=':', lw=2, label='60점 기준')
plt.title('최종 시험 점수 분포', fontsize=13)
plt.xlabel('시험 점수')
plt.ylabel('학생 수')
plt.legend()
plt.tight_layout()
plt.savefig('plots/exam_dist.png', dpi=150)
plt.close()

# 3. study quartile bar
df['study_q'] = pd.qcut(df['study_hours_per_day'], 4, duplicates='drop')
q = df.groupby('study_q', observed=True)['exam_score'].mean()
labels = ['≤2.6시간\n(하위 25%)', '2.6~3.5시간', '3.5~4.5시간', '4.5시간 초과\n(상위 25%)']
colors = ['#adb5bd', '#6c9bd2', '#2f7fd3', '#0d5cb6']
plt.figure(figsize=(7, 4.2))
b = plt.bar(labels, q.values, color=colors, edgecolor='white')
plt.bar_label(b, fmt='%.1f', fontsize=11, padding=3)
plt.ylim(0, 100)
plt.title('공부 시간 4분위별 평균 시험 점수', fontsize=13)
plt.ylabel('평균 점수')
plt.tight_layout()
plt.savefig('plots/study_quartile_bar.png', dpi=150)
plt.close()

# 4. sleep bucket bar
sb = pd.cut(df['sleep_hours'], [0, 5, 6, 7, 8, 24],
            labels=['~5시간', '5~6시간', '6~7시간', '7~8시간', '8시간+'])
g = df.groupby(sb, observed=True)['exam_score'].mean()
plt.figure(figsize=(7, 4.2))
b = plt.bar(g.index.astype(str), g.values, color='#20c997', edgecolor='white')
plt.bar_label(b, fmt='%.1f', fontsize=11, padding=3)
plt.ylim(0, 100)
plt.title('수면 시간 구간별 평균 시험 점수', fontsize=13)
plt.ylabel('평균 점수')
plt.xlabel('하루 수면 시간')
plt.tight_layout()
plt.savefig('plots/sleep_bucket_bar.png', dpi=150)
plt.close()

# 5. media bucket bar
mb = pd.cut(df['media_total_hours'], [0, 2, 3, 4, 5, 99],
            labels=['~2시간', '2~3시간', '3~4시간', '4~5시간', '5시간+'])
g2 = df.groupby(mb, observed=True)['exam_score'].mean()
plt.figure(figsize=(7, 4.2))
b = plt.bar(g2.index.astype(str), g2.values, color='#fd7e14', edgecolor='white')
plt.bar_label(b, fmt='%.1f', fontsize=11, padding=3)
plt.ylim(0, 100)
plt.title('SNS+넷플릭스 총 사용 시간별 평균 시험 점수', fontsize=13)
plt.ylabel('평균 점수')
plt.xlabel('SNS + 넷플릭스 합계 (시간/일)')
plt.tight_layout()
plt.savefig('plots/media_bucket_bar.png', dpi=150)
plt.close()

# 6. correlation bars with exam score
cc = df[cols].corr()['exam_score'].drop('exam_score').sort_values()
plt.figure(figsize=(7, 4.2))
cols_bar = ['#d62728' if v < 0 else '#1f77b4' for v in cc.values]
names = ['넷플릭스', 'SNS', '출석률', '수면시간', '운동', '정신건강', '공부시간']
b = plt.barh(names, cc.values, color=cols_bar, edgecolor='white')
plt.bar_label(b, fmt='%+.3f', fontsize=10, padding=4)
plt.axvline(0, color='#333', lw=1)
plt.xlim(-0.35, 1.0)
plt.title('시험 점수와의 상관계수', fontsize=13)
plt.xlabel('Pearson r')
plt.tight_layout()
plt.savefig('plots/corr_bar.png', dpi=150)
plt.close()

print('done')
