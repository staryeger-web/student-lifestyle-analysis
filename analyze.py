import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
data_path = 'C:/Users/stary/Downloads/archive/student_habits_performance.csv'
df = pd.read_csv(data_path)

# Basic info
print('Shape:', df.shape)
print('Columns:', df.columns.tolist())
print('\nFirst 5 rows:')
print(df.head())
print('\nDescribe:')
print(df.describe())

# Correlations
cols = ['study_hours_per_day', 'sleep_hours', 'social_media_hours', 'netflix_hours', 'exam_score']
print('\n=== Correlation Matrix ===')
print(df[cols].corr())

# Plots
os.makedirs('plots', exist_ok=True)

# Study hours vs exam score
plt.figure(figsize=(6,4))
sns.regplot(x='study_hours_per_day', y='exam_score', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Study Hours per Day vs Exam Score')
plt.xlabel('Study Hours per Day')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('plots/study_vs_score.png', dpi=150)
plt.close()

# Sleep hours vs exam score
plt.figure(figsize=(6,4))
sns.regplot(x='sleep_hours', y='exam_score', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Sleep Hours vs Exam Score')
plt.xlabel('Sleep Hours')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('plots/sleep_vs_score.png', dpi=150)
plt.close()

# Social media hours vs exam score
plt.figure(figsize=(6,4))
sns.regplot(x='social_media_hours', y='exam_score', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Social Media Hours vs Exam Score')
plt.xlabel('Social Media Hours')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('plots/social_vs_score.png', dpi=150)
plt.close()

# Netflix hours vs exam score
plt.figure(figsize=(6,4))
sns.regplot(x='netflix_hours', y='exam_score', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Netflix Hours vs Exam Score')
plt.xlabel('Netflix Hours')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('plots/netflix_vs_score.png', dpi=150)
plt.close()

# Combined SNS (social + netflix) vs exam score
df['sns_total_hours'] = df['social_media_hours'] + df['netflix_hours']
plt.figure(figsize=(6,4))
sns.regplot(x='sns_total_hours', y='exam_score', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Total SNS (Social+Netflix) Hours vs Exam Score')
plt.xlabel('Total SNS Hours')
plt.ylabel('Exam Score')
plt.tight_layout()
plt.savefig('plots/sns_total_vs_score.png', dpi=150)
plt.close()

print('\nAll plots saved to plots/')
