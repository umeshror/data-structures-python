"""
Given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


def rotate_sol1(M):
    """
    :type matrix: List[List[int]]
    :rtype: matrix: List[List[int]]
    """
    n = len(M)
    for i in range(n // 2):
        for j in range(n - (n // 2)):
            """
            m = [1,2,3] : m[~0]
            m[~0] : 3, m[~1] : 2
            [~i] === [n-1-i].
            e.g [
              [1,2,3],
              [4,5,6],
              [7,8,9]
            ]
            m[0][0] : m [3][0]
            m[3][0] : m [3][3]
            m[3][3] : m [0][3]
            m[0][3] : m [0][0]
            """

            M[i][j],  M[~j][i],  M[~i][~j], M[j][~i] = \
            M[~j][i], M[~i][~j], M[j][~i],  M[i][j]
    return M


def rotate_sol_2(matrix):
    matrix[:] = zip(*matrix[::-1])
    return matrix


def rotate_sol3(M):
    M.reverse()
    for i in range(len(M)):
        for j in range(i):
            M[i][j], M[j][i] = M[j][i], M[i][j]
    return M


rotate_sol1([
    [15, 13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7, 10, 11]
])
