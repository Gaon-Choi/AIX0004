import pandas as pd
from sklearn.model_selection import train_test_split


def show_accuracy(X, Y, prediction):
    num = 0
    for x in range(len(X)):
        if (prediction[x] == Y[x]):
            num += 1
    print("\tAccuracy: ", (num / len(X)) * 100, "%")


# [Q2-1]
print("(Q2-1)")
from sklearn.svm import SVC

print("Import SVC(Support Vector Machine)\n")

# [Q2-2]
print("(Q2-2)")
print("SVC object")
svc = SVC(kernel='linear', C=1.0, gamma='auto')
print()

# [Q2-3]
print("(Q2-3)")
print("Reading csv file...")
path = "C:\\Users\\choig\\Downloads\\wine_data.csv"
wine = pd.read_csv(path)
# Data Slicing
X = wine.iloc[:, 1:]
y = wine[["Class"]]
# Data Split
print("Data Split into train / test")
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=1 - 0.3, random_state=0)
y_train_ = y_train.values.ravel()
y_test_ = y_test.values.ravel()
print("Fitting")
svc.fit(X_train, y_train_)
print()

# [Q2-4]
print("(Q2-4)")
print("prediction1 : X_train")
prediction1 = svc.predict(X_train)
show_accuracy(X_train, y_train_, prediction1)
print()

# [Q2-5]
print("(Q2-5)")
print("prediction2 : X_test")
prediction2 = svc.predict(X_test)
show_accuracy(X_test, y_test_, prediction2)
print()
