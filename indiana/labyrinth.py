import pytest


CHAR_INDIANA = '@'
CHAR_WALL = '#'
CHAR_FREE = '.'
visited = {}


def labyrinth_to_string(m, pos):
    y_len, x_len = shape(m)
    labyrinth = ''

    for y in range(y_len):
        for x in range(x_len):
            if y == pos[0] and x == pos[1]:
                labyrinth += CHAR_INDIANA
            elif m[y][x]:
                labyrinth += CHAR_FREE
            else:
                labyrinth += CHAR_WALL
        labyrinth += '\n'

    return labyrinth


def shape(m):
    return len(m), len(m[0])


def neighbours(m, pos):
    free = []
    y_len, x_len = shape(m)

    if pos[0] != 0 and m[pos[0]-1][pos[1]]:
        free.append((pos[0]-1, pos[1]))
    if pos[0] != y_len - 1 and m[pos[0]+1][pos[1]]:
        free.append((pos[0]+1, pos[1]))
    if pos[1] != 0 and m[pos[0]][pos[1]-1]:
        free.append((pos[0], pos[1]-1))
    if pos[1] != x_len - 1 and m[pos[0]][pos[1]+1]:
        free.append((pos[0], pos[1]+1))

    return free


def find_route(m, pos):
    visited[pos] = True
    y_len, x_len = shape(m)
    if pos[0] == 0 or pos[1] == 0 or pos[0] == y_len-1 or pos[1] == x_len-1:
        return pos
    
    route = []
    for neighbour in set(neighbours(m, pos)):
        if neighbour not in visited:
            route.append(pos)
            route.append(find_route(m, neighbour))
            return route

    return route


def test_neighbours():
    m = [[False, False, False, False],
        [False, True, False, True],
        [False, True, False, True],
        [True, True, False, False]]

    assert [(1, 1), (1, 3)] == neighbours(m, (1,2))
    assert [(2, 1)] == neighbours(m, (1,1)) 


def test_find_route():
    m = [[False, False, False, False],
        [False, True, False, True],
        [False, True, False, True],
        [True, True, False, False],
    ]
    start = (2, 1)

    assert [(2, 1), (3, 1)] == find_route(m, start)
