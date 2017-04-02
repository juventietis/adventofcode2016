#!/usr/bin/python3
'''Implementation of Advent of Code day 8 solution'''
import re

GRID_SIZE_Y = 6
GRID_SIZE_X = 50

input_data = None
with open("input.dat") as f:
    input_data = f.readlines()


rect_regex = re.compile(r"rect (?P<x>\d+)x(?P<y>\d+)")
rotate_col_regex = re.compile(r"rotate column x=(?P<x>\d+) by (?P<y>\d+)")
rotate_row_regex = re.compile(r"rotate row y=(?P<x>\d+) by (?P<y>\d+)")

def match_regex(regex, string):
    match = regex.match(string)
    if match:
        x = int(match.group("x"))
        y = int(match.group("y"))
        return True, (x, y)
    else:
        return False, None

def execute_command(grid, regex, command, action, print_output = False):
    matched, data = match_regex(regex, command)
    if matched:
        action(grid, data)
        if print_output:
            print(command)
            pprint_grid(grid)
        return True
    else:
        return False

def fill(grid, data):
    x,y = data
    for i in range(y):
        for o in range(x):
            grid[i][o] = 1


def rotate_col(grid, data):
    x, n = data
    col = [row[x] for row in grid]
    shifted_col = shift(col, n)
    for i in range(GRID_SIZE_Y):
        grid[i][x] = shifted_col[i]

def rotate_row(grid, data):
    y, n = data
    row = grid[y]
    shifted_row = shift(row, n)
    grid[y] = shifted_row

def shift(seq, n):
    n = len(seq) - (n % len(seq))
    return seq[n:] + seq[:n]


def pprint_grid(grid):
    print("----------")
    for i in range(GRID_SIZE_Y):
        for o in range(GRID_SIZE_X):
            cel = grid[i][o]
            if cel == 1:
                print("#", end=" ") 
            else:
                print(" ", end=" ")
        print()
    print("----------")


def calculate_on(grid):
    acc = 0
    for row in grid:
        for cel in row:
            acc += cel
    return acc

grid = [[0 for o in range(GRID_SIZE_X)] for i in range(GRID_SIZE_Y)]
for row in input_data:
    execute_command(grid, rect_regex, row, fill)
    execute_command(grid, rotate_col_regex, row, rotate_col)
    execute_command(grid, rotate_row_regex, row, rotate_row)

print("Screen:")
pprint_grid(grid)
print("Number of on pixel: {0}".format(calculate_on(grid)))
