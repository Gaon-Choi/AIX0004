import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


def show_accuracy(X, Y, prediction):
    num = 0
    for x in range(len(X)):
        if (prediction[x] == Y[x]):
            num += 1
    print("\tAccuracy: ", (num / len(X)) * 100, "%")


# [Q1-1]
print("(Q1-1)")
path = "C:\\Users\\choig\\Downloads\\wine_data.csv"
wine = pd.read_csv(path)
print("opened CSV file successfully.\n")

# [Q1-2]
print("(Q1-2)")
print(wine.describe())
print()

# [Q1-3]
print("(Q1-3)")
print("data split into train / test")
X = wine.iloc[:, 1:]
y = wine[["Class"]]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1 - 0.7, random_state=0)
print()

# [Q1-4]
print("(Q1-4)")
print("KNeighborsClassifier object knn(k = 5) and fitting")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train.values.ravel())
print()

# [Q1-5]
print("(Q1-5)")
print("prediction of X_train")
prediction = knn.predict(X_train)
y_train_ = y_train.values.ravel()
print("training set 예측에 대한 정확도")
show_accuracy(X_train, y_train_, prediction)
print()

# [Q1-6]
print("(Q1-6)")
print("prediction of X_test")
prediction2 = knn.predict(X_test)
y_test_ = y_test.values.ravel()
print("test set 예측에 대한 정확도")
show_accuracy(X_test, y_test_, prediction2)
print()

# [Q1-7]
print("(Q1-7)")
print("KNeighborsClassifier object knn2(k = 3) and fitting")
knn2 = KNeighborsClassifier(n_neighbors=3)
knn2.fit(X_train, y_train.values.ravel())
prediction3 = knn2.predict(X_train)
print("training set 예측에 대한 정확도")
show_accuracy(X_train, y_train_, prediction3)

prediction4 = knn2.predict(X_test)
print("test set 예측에 대한 정확도")
show_accuracy(X_test, y_test_, prediction4)
print()

# [Q1-8]
print("(Q1-8)")
print("X = Alcohol, Malic acid, Ash, Alcalinity of ash")
X2 = wine.iloc[:, 1:5]
    # y는 위에서 만들어진 y를 그대로 사용함.
X2_train, X2_test = train_test_split(X2, test_size=1 - 0.7, random_state=0)
print("KNeighborsClassifier object knn3(k = 5) and fitting")
knn3 = KNeighborsClassifier(n_neighbors=5)
knn3.fit(X2_train, y_train.values.ravel())

prediction5 = knn3.predict(X2_train)
print("train 예측에 대한 정확도")
show_accuracy(X2_train, y_train_, prediction5)

prediction6 = knn3.predict(X2_test)
print("test set 예측에 대한 정확도")
show_accuracy(X2_test, y_test_, prediction6)
