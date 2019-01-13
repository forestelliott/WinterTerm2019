import numpy as np


def L_i(x, y, W):
    delta = 1.0
    #Calculate the score
    scores = W.dot(x)
    correct_class_score = scores[y]
    #Get the dim of W
    D = W.shape[0]
    loss_i = 0.0
    for j in range(D):
        if (j == y):
            continue
        loss_i += max(0, scores[j] - correct_class_score + delta)
    return loss_i


def L_i_vectorized(x, y, W):
    delta = 1.0
    scores = W.dot(x)
    margins = np.maximum(0, scores - scores[y] + delta)
    margins[y] = 0
    loss_i = np.sum(margins)
    return loss_i


def main():
    #these parameters should give high loss
    W = np.array([[1, 0, 0, 0], [1.5, 1.3, 2.1, 0.0], [0, .25, .2, -.3]])
    x = np.array([1, 201, 2013, 324])
    y = 0
    print(L_i_vectorized(x, y, W))


main()
