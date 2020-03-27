import seaborn as sns
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

result_path = "C:\\Users\\choig\\Desktop\\파일\\1학년 2학기\\AIX R-PY 컴퓨팅\\과제\\최종 보고서\\result.json"
result = pd.read_json(result_path)

region_score = result[['region', 'score']]
x_value = region_score['region']
y_value = region_score['score']

x = np.arange(len(set(x_value)))
my_xticks = list(set(x_value))
my_xticks.sort()

for i in range(len(my_xticks)):
    x_value = x_value.replace(my_xticks[i], i)

plt.xticks(x, my_xticks, fontsize=4)
x_value = np.array(x_value)
y_value = np.array(y_value)

plt.show()
