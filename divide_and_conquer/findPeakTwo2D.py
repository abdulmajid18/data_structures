import random
import pprint


def peakIn2DBrute(matrix):
    left, right, up, bottom = 0, 0, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            left, right, up, bottom = 0, 0, 0, 0
            left, right, up, bottom = 0, 0, 0, 0
            if j > 0:
                left = matrix[i][j-1]
            if j < len(matrix[0]) - 1:
                pass
