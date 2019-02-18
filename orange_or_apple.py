from sklearn import tree

# 1 on feature meaning smooth, 0 is bumpy
# 0 on labels meaning apple and 1 is orange
features = [[140, 1], [130, 1], [135, 1], [145, 0], [150, 0]]
labels = [0, 0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)


def result(data):
    if data == 0:
        return "Apple"
    else:
        return "Orange"


weight = float(input("Please input fruit weight! \nAnswer: "))
texture = int(input("Are fruit is smooth? \n1. Yes || 0. No \nAnswer:"))
hasil = clf.predict([[weight, texture]])

print("\n======================================\n")
print("The result is "+ result(hasil))
