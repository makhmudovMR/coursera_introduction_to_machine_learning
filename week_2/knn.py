import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


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
            # dist = euclidian_distances(feature, predict)
            euclid_dist = np.linalg.norm(np.array(feature) - np.array(predict))
            distances.append([euclid_dist, group])
    votes = [i[1] for i in sorted(distances)[:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]

    return vote_result


def main():
    dataset = {'k': [[1, 2], [2, 1], [3, 2], [3, 2]], 'r': [[6, 7], [9, 5], [6, 5], [9, 9]]}
    print(knn(dataset, [1,3], k=3))


if __name__ == '__main__':
    main()