import pandas as pd
from sklearn.cluster import KMeans

# [Q3-1]
print("(Q3-1)")
print("opened CSV file successfully.")
path = "C:\\Users\\choig\\Downloads\\wine_data.csv"
wine = pd.read_csv(path)

print("Data Setting")
X = wine.iloc[:, 1:]
y = wine[['Class']]
print()

# [Q3-2]
print("(Q3-2)")
print("KMeans Clustering Model (n_clusters=3)")
model = KMeans(n_clusters=3)
print("Model Fitting")
model.fit(X)
print()

# [Q3-3]
print("(Q3-3)")
print("Prediction : X")
prediction = model.predict(X)
print("CrossTab : (prediction) * (real label)")
ct = pd.crosstab(prediction, y.values.ravel())
print(ct)
print()

# [Q3-4]
print("(Q3-4)")
ks = range(1, 10)
inertias = []

for k in ks:
    model2 = KMeans(n_clusters=k)
    model2.fit(X)
    inertias.append(model2.inertia_)
print("k = i --> (inertia when k = i)")
for k in ks:
    print("k =", k, "-->", inertias[k - 1])
