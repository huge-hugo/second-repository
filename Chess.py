from copy import deepcopy

n = 8
walk = 0

black_figures = {
    (0, 0): 'r', (0, 1): 'h', (0, 2): 'e', (0, 3): 'q', (0, 4): 'k', (0, 5): 'e', (0, 6): 'h', (0, 7): 'r',
    (1, 0): 'p', (1, 1): 'p', (1, 2): 'p', (1, 3): 'p', (1, 4): 'p', (1, 5): 'p', (1, 6): 'p', (1, 7): 'p'
}

white_figures = {
    (7, 0): 'R', (7, 1): 'H', (7, 2): 'E', (7, 3): 'Q', (7, 4): 'K', (7, 5): 'E', (7, 6): 'H', (7, 7): 'R',
    (6, 0): 'P', (6, 1): 'P', (6, 2): 'P', (6, 3): 'P', (6, 4): 'P', (6, 5): 'P', (6, 6): 'P', (6, 7): 'P'
}

mtrx = [['.' if (i + j) % 2 == 0 else ' ' for j in range(n)] for i in range(n)]
m = deepcopy(mtrx)

class Ches_board:
    '''класс для создания и отрисовки доски'''

    def create_board(self):
        # создает доску

        for i in range(n):
            for j in range(n):
                if (i, j) in black_figures:
                    m[i][j] = black_figures[(i, j)]
                elif (i, j) in white_figures:
                    m[i][j] = white_figures[(i, j)]

    def print_board(self):
        # отрисовывает доску

        print('   ', *'abcdefgh', sep='  ')
        print()
        for i in range(n):
            print(n - i, end='    ')
            for j in range(n):
                print(m[i][j], end='  ')
            print(' ', n - i, end='')
            print()
        print()
        print('   ', *'abcdefgh', sep='  ')


class REQ:
    def __init__(self, coords: tuple, tup, column):
        self.coords = coords
        self.tup = tup
        self.column = column

    def req_move(self):

        for i in range(self.column):
            move = self.coords
            for j in range(n):
                move = move[0] - self.tup[i][0], move[1] - self.tup[i][1]
                x, y = move[0], move[1]

                if 0 > x or x > n - 1 or 0 > y or y > n - 1:  # если координаты выходят за границы
                    break
                elif move in black_figures or move in white_figures:  # если стоит вражеская фигура
                    if walk % 2 == 0 and move in black_figures:
                        m[x][y] = '!'
                    elif walk % 2 != 0 and move in white_figures:
                        m[x][y] = '!'
                    break
                else:
                    m[x][y] = '*'


class Rook(REQ):
    '''класс ладьи'''

    def __init__(self, coords: tuple):
        tup = (1, 0), (0, 1), (0, -1), (-1, 0)  # для отрисовки звездочек
        column = 4
        super().__init__(coords, tup, column)

    def move(self):
        REQ.req_move(self)


class Hourse:
    '''класс коня'''

    def __init__(self, coords: tuple):
        self.coords = coords

    def move(self):
        x, y = self.coords[0], self.coords[1]
        for i in range(n):
            for j in range(n):
                if abs(x - i) * abs(y - j) == 2:
                    if (i, j) in black_figures or (i, j) in white_figures:  # если стоит вражеская фигура
                        if walk % 2 == 0 and (i, j) in black_figures:
                            m[i][j] = '!'
                        elif walk % 2 != 0 and (i, j) in white_figures:
                            m[i][j] = '!'
                    else:
                        m[i][j] = '*'


class Elephant(REQ):
    '''класс слона'''

    def __init__(self, coords):
        self.coords = coords
        tup = (1, 1), (1, -1), (-1, -1), (-1, 1)  # для отрисовки звездочек
        column = 4
        super().__init__(coords, tup, column)

    def move(self):
        REQ.req_move(self)


class Queen(REQ):
    '''класс ферзя'''

    def __init__(self, coords):
        self.coords = coords
        tup = (1, 0), (0, 1), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)  # для отрисовки звездочек
        column = 8
        super().__init__(coords, tup, column)

    def move(self):
        REQ.req_move(self)


class King:
    '''класс короля'''

    def __init__(self, coords):
        self.coords = coords

    def move(self):
        x, y = self.coords[0], self.coords[1]
        for i in range(n):
            for j in range(n):
                absx = abs(x-i)
                absy = abs(y-j)
                if absx + absy == 1 or (absx == 1 and absy == 1):
                    if (i, j) in black_figures or (i, j) in white_figures:  # если стоит вражеская фигура
                        if walk % 2 == 0 and (i, j) in black_figures:
                            m[i][j] = '!'
                        elif walk % 2 != 0 and (i, j) in white_figures:
                            m[i][j] = '!'
                    else:
                        m[i][j] = '*'

class Pawn:
    '''класс пешек'''

    def __init__(self, coords=None):
        self.coords = coords

    def move(self):
        if walk % 2 == 0: tup, wlk = 1, 1
        else: tup, wlk = -1, 0
        x, y = self.coords[0], self.coords[1]

        x0 = self.coords[0] - tup
        y0 = 1
        for i in range(2):
            if ((x0, y - y0) in black_figures and wlk) or ((x0, y - y0) in white_figures and not wlk):
                if x0 == 0 or x0 == 7:
                    m[x0][y - y0] = '^'
                else:
                    m[x0][y - y0] = '!'
            y0 = -y0

        if (wlk and x == 6) or (not wlk and x == 1):
            for i in range(2):
                x -= tup
                if (x, y) not in figures:
                    m[x][y] = '*'
        else:
            x -= tup
            if (x, y) not in figures:
                if x == 0 or x == 7:
                    m[x][y] = '^'
                else:
                    m[x][y] = '*'

    def pawn_upgrade(self):
        print('выбери фигуру от 1 до 4 -- Q R E H')
        try:
            upgr = 'QREH'[int(input())-1]
        except:
            upgr = 'Q'
        if wlk:
            if (xw, yw) in black_figures:
                del black_figures[(xw, yw)]
                del white_figures[(x, y)]
                white_figures[(xw, yw)] = upgr

            elif (xw, yw) not in figures:
                del white_figures[(x, y)]
                white_figures[(xw, yw)] = upgr
        else:
            if (xw, yw) in white_figures:
                del white_figures[(xw, yw)]
                del black_figures[(x, y)]
                black_figures[(xw, yw)] = upgr.lower()

            elif (xw, yw) not in figures:
                del black_figures[(x, y)]
                black_figures[(xw, yw)] = upgr.lower()


define = {'r': Rook, 'h': Hourse, 'e': Elephant, 'q': Queen, 'k': King, 'p': Pawn}

def input_coords():
    true = True
    while true:
        try:
            inpt = tuple(input())
            y, x = 'abcdefgh'.find(inpt[0]), n - int(inpt[1])
        except:
            true = True
        else:
            return x, y

def create_stars(x, y):
    true2 = True
    if (wlk and (x, y) in white_figures) or (not wlk and (x, y) in black_figures):
        true2 = False

        fig = define[figures[(x, y)].lower()]((x, y))
        fig.move()
        board.create_board()
        board.print_board()
        fig.move()


    return x, y, true2

run = True
while run:
    figures = white_figures | black_figures
    board = Ches_board()
    board.create_board()
    board.print_board()

    if walk % 2 == 0:
        wlk = 1
        print('ХОД БЕЛЫХ')
    else:
        wlk = 0
        print('ХОД ЧЕРНЫХ')

    true1 = True
    true2 = True
    while true1:
        while true2:
            x, y = input_coords()
            x, y, true2 = create_stars(x, y)

        xw, yw = input_coords()
        if (wlk and (xw, yw) in white_figures) or (not wlk and (xw, yw) in black_figures):
            m = deepcopy(mtrx)
            board.create_board()
            x, y, true2 = create_stars(xw, yw)

        elif m[xw][yw] == '*':
            if wlk:
                white_figures[(xw, yw)] = white_figures.pop((x, y))
            else:
                black_figures[(xw, yw)] = black_figures.pop((x, y))
            true1 = False
        elif m[xw][yw] == '!':
            if figures[(xw, yw)] in 'kK':
                print('ШАХ и МАТ')
                run = False
                true1 = False
            if wlk:
                del black_figures[(xw, yw)]
                white_figures[(xw, yw)] = white_figures.pop((x, y))
            else:
                del white_figures[(xw, yw)]
                black_figures[(xw, yw)] = black_figures.pop((x, y))
            true1 = False
        elif m[xw][yw] == '^':
            p = Pawn()
            p.pawn_upgrade()
            true1 = False
    walk += 1
    print()
    m = deepcopy(mtrx)