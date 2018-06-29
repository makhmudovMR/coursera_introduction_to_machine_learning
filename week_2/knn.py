import math
import numpy as np
import matplotlib.pyplot as plt

def euclidian_distances(x,y):
    x, y = np.array(x), np.array(y)
    return math.sqrt(sum((x-y)**2))
    pass

def knn(data, predict, k=1):
    if len(data) >= k:
        print('predict can\'t be execute')

    predict = np.array(predict)
    distances = []
    for group in data:
        for feature in data[group]:
            dist = euclidian_distances(feature, predict)
            distances.append([dist, group])

    neighbors = distances[:k]
    print(neighbors)
    pass

def main():
    dataset = {'k': [[1, 2], [2, 1], [3, 2], [3, 2]], 'r': [[6, 7], [9, 5], [6, 5], [9, 9]]}
    knn(dataset, [1,3])


if __name__ == '__main__':
    main()