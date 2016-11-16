# pipeline created via {ML} recipes tutorial

from sklearn import datasets
from sklearn.cross_validation import train_test_split
from scipy.spatial import distance
# from sklearn import tree
from sklearn.metrics import accuracy_score
# import random


# from sklearn.neighbors import KNeighborsClassifier
def euc(a, b):
    return distance.euclidean(a, b)


class basicKNNClassifier():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions


iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)
# my_Classifier = tree.DecisionTreeClassifier()
my_Classifier = basicKNNClassifier()

my_Classifier.fit(X_train, y_train)

predictions = my_Classifier.predict(X_test)

print predictions
print accuracy_score(y_test, predictions)
