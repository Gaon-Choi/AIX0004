import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

result_path = "C:\\Users\\choig\\Desktop\\파일\\1학년 2학기\\AIX R-PY 컴퓨팅\\과제\\최종 보고서\\result.json"
result = pd.read_json(result_path)

disability_score = result[['disability', 'score']]

disability_yes = pd.to_numeric(disability_score[disability_score['disability'] == 'Y']['score'])
disability_no = pd.to_numeric(disability_score[disability_score['disability'] == 'N']['score'])

plt.hist(disability_no.dropna(), np.linspace(0, 100, 10), color='orange')
plt.show()