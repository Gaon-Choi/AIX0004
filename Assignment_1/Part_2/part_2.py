from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# [Q5]  데이터 전처리 ------------------------------------------------------------------------------------------------
print("[문제 5번]\n")
# [Q5 - 1]  pandas 데이터 프레임 객체 생성
path = "C:\\Users\\choig\\Desktop\\파일\\1학년 2학기\\AIX R-PY 컴퓨팅\\과제\\Part 2\\boston_csv.csv"
df = pd.read_csv(path)
print("Successfully opened csv file.")

# Data Cleaning
df = df.replace("na", np.nan)  # "na" --> np.nan
df = df.replace("Nan", np.nan)  # "Nan" --> np.nan
print("\"na\", \"Nan\" --> np.nan")
# [Q5 - 2]  결측치를 포함한 관측치 삭제
df = df.dropna(axis=0)  # 해당 열을 삭제
print("Performed Data Cleaning successfully.")
# --------------------------------------------------------------------------------------------------------------------

# [Q6]  요약 통계 ----------------------------------------------------------------------------------------------------
print("\n\n[문제 6번]\n")
# [Q6 - 1]  변수별 요약 통계
print(df.describe())
# [Q6 - 2]  Heatmap 구현
plt.figure(figsize=(15, 15))
sns.heatmap(data=df.corr(), annot=True, cmap='Blues')
plt.show()  # Plot 표시
# --------------------------------------------------------------------------------------------------------------------

# [Q7]  단순회귀분석 모형 --------------------------------------------------------------------------------------------
print("\n\n[문제 7번]\n")
x1 = df[['LSTAT']]  # 독립변수: 하위계층의 비율(LSTAT)
y1 = df['MEDV']  # 종속변수: 본인 소유의 주택가격(중앙값)(MEDV)

x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=1 - 0.75, random_state=0)
# Training Set: x1_train, y1_train // Test Set: x1_test, y1_test
# Training Set이 표본의 75%를 차지한다.
lm = LinearRegression()
lm.fit(x1_train, y1_train)
y_hat = lm.predict(x1_train)

# 상관관계 분석
print("MEDV", " = ", lm.coef_[0], " * ", "LSTAT", " + ", lm.intercept_, sep="")
print(lm.coef_, lm.intercept_)
print("\nThe model performance for train set")
# Mean Squared Error
print("\tmean squared error: ", mean_squared_error(y1_train, y_hat))
# R Square
print("\tR square: ", lm.score(x1_train, y1_train))

print("\nThe model performance for test set")
y_pred1 = lm.predict(x1_test)
# Mean Squared Error
print("\tmean squared error: ", mean_squared_error(y1_test, y_pred1))

# [Q8]  다중회귀분석 모형 --------------------------------------------------------------------------------------------
print("\n\n[문제 8번]\n")
x2 = df[['LSTAT', 'TAX']]  # 독립변수: 하위계층의 비율(LSTAT), 10,000 달러 당 재산세율(TAX)
y2 = df['MEDV']  # 종속변수: 본인 소유의 주택가격(중앙값)(MEDV)

x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size=1 - 0.75, random_state=0)
# Training Set: x2_train, y2_train // Test Set: x2_test, y2_test
# Training Set이 표본의 75%를 차지한다.
lm2 = LinearRegression()
lm2.fit(x2_train, y2_train)
y_hat2 = lm2.predict(x2_train)

# 상관관계 분석
print("MEDV", " = ", lm2.coef_[0], " * ", "LSTAT", " + ", lm2.coef_[1], " * ", "TAX", " + ", lm2.intercept_, sep="")
print(lm2.coef_, lm2.intercept_)
print("\nThe model performance for train set")
# Mean Squared Error
print("\tmean squared error: ", mean_squared_error(y2_train, y_hat2))
# R Square
print("\tR square: ", lm2.score(x2_train, y2_train))

print("\nThe model performance for test set")
y_pred2 = lm2.predict(x2_test)
# Mean Squared Error
print("\tmean squared error: ", mean_squared_error(y2_test, y_pred2))
# --------------------------------------------------------------------------------------------------------------------
input()
