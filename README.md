# 대학생 라이프스타일과 학업 성과 분석

대학생 가상 생활 습관 데이터(1,000명)를 기반으로 라이프스타일과 최종 시험 점수 간 관계를 EDA(탐색적 데이터 분석)한 프로젝트입니다.

## 웹사이트
- 발표용 프레젠테이션: https://staryeger-web.github.io/student-lifestyle-analysis/
- 대시보드 리포트: https://staryeger-web.github.io/student-lifestyle-analysis/dashboard.html

## 파일
- student_habits_performance.csv - 원본 데이터
- analyze.py - 기초 분석 및 시각화 스크립트
- report_stats.py - 수치/집계 검증 스크립트
- dashboard_plots.py - 대시보드용 PNG 생성
- index.html - reveal.js 발표 자료
- dashboard.html - 웹 대시보드 리포트
- plots/ - 분석 시각화 이미지

## 주요 인사이트
- 공부시간과 시험점수: r = 0.825 (강한 양의 상관)
- 공부 4분위: 상위 25%(≥4.5h) 평균 87.6점 vs 하위 25%(≤2.6h) 52.3점
- 수면: 7~8시간에서 평균 점수 최고
- SNS+넷플릭스 총합: 사용량 증가 시 평균 점수 소폭 하락
- 다중회귀(R²): 0.763 (공부·수면·미디어·출석 중심)

## 실행
python report_stats.py
python dashboard_plots.py

