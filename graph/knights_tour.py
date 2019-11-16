class KnightTour(object):
    moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def __init__(self, dimension):
        self.dimension = dimension
        self.chess_board = [[-1] * self.dimension for x in range(dimension)]
        self.steps_taken = 0

    def is_valid_move(self, i, j):
        if 0 <= i < self.dimension and 0 <= j < self.dimension:
            if self.chess_board[i][j] == -1:
                return True
        return False

    def knight_tour(self, i, j):
        if self.steps_taken + 1 == self.dimension * self.dimension:
            return True
        for move in self.moves:
            next_i = i + move[0]
            next_j = j + move[1]

            if self.is_valid_move(next_i, next_j):
                self.steps_taken += 1
                self.chess_board[next_i][next_j] = self.steps_taken
                if self.knight_tour(next_i, next_j):
                    return True
        return False

    def start_knight_tour(self, i=0, j=0):
        steps_taken = 0
        self.chess_board[i][j] = steps_taken
        tour_finished = self.knight_tour(i, j)
        for row in self.chess_board:
            print(row)
        return tour_finished


k = KnightTour(8)
print(k.start_knight_tour())
"""
[0, 59, 38, 33, 30, 17, 8, 63]
[37, 34, 31, 60, 9, 62, 29, 16]
[58, 1, 36, 39, 32, 27, 18, 7]
[35, 48, 41, 26, 61, 10, 15, 28]
[42, 57, 2, 49, 40, 23, 6, 19]
[47, 50, 45, 54, 25, 20, 11, 14]
[56, 43, 52, 3, 22, 13, 24, 5]
[51, 46, 55, 44, 53, 4, 21, 12]
True

"""
