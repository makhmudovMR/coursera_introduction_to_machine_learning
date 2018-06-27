import numpy as np
import matplotlib.pyplot as plt

'''
Создаем датасет
'''

X_train = np.array([[1,1],
                    [1,2],
                    [3,5],
                    [4,2],
                    [1,3],
                    [8,9],
                    [7,10],
                    [9,8],
                    [8,8]])
y_train = np.array([0,0,0,0,0,1,1,1,1])

plt.scatter(X_train[:,0], X_train[:,1], c=y_train)
plt.grid()
plt.show()

'''
Строим модель
'''

def decision_tree(X):
    cls = []
    for i in X:
        if i[0] < 5.5 and i[1] < 6:
            cls.append(0)
        elif i[0] > 5.5 and i[1] > 6:
            cls.append(1)
    cls = np.array(cls, ndmin=2).T
    result = np.concatenate((X, cls), axis=1)
    return result

print(decision_tree(X_train))