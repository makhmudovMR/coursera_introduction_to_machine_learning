import numpy as np

import pandas as pd

from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('titanic.csv')
data = data[['Pclass', 'Fare', 'Age', 'Sex', 'Survived']]
data = data.dropna()
target = data[['Survived']]
data = data[['Pclass', 'Fare', 'Age', 'Sex']]
# print(data[:30])
data['Sex'] = list(map(lambda sex: 1 if sex=='male' else 0, data['Sex'])) # male:1, female:0
# print(data.head())


clf = DecisionTreeClassifier(random_state=241)
clf.fit(data, target)
importances = clf.feature_importances_
print(importances)
