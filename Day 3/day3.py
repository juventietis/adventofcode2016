"""Day 3 of Advent of Code 2016"""


def is_triangle(a, b, c):
    if(a + b > c and a + c > b and c + b > a):
        return True
    else:
        return False


def solve_p1(data):
    triangles = 0
    for line in input_data:
        triangle = [int(x) for x in line.split()]
        if is_triangle(triangle[0], triangle[1], triangle[2]):
            triangles += 1
    print(triangles)


def solve_p2(data):
    matrix = [[int(x) for x in line.split()] for line in data]
    triangles = 0
    for i in range(0, len(matrix), 3):
        for o in range(3):
            if is_triangle(matrix[i][o], matrix[i+1][o], matrix[i+2][o]):
                triangles += 1
    print (triangles)

input_data = None
with open("input.dat") as data:
    input_data = data.readlines()

solve_p1(input_data)
solve_p2(input_data)
