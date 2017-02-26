"""Day 3 of Advent of Code 2016"""


def is_triangle(a, b, c):
    if(a + b > c and a + c > b and c + b > a):
        return True
    else:
        return False


input_data = None
with open("input.dat") as data:
    input_data = data.readlines()


triangles = 0
for line in input_data:
    triangle = [int(x) for x in line.split()]
    if is_triangle(triangle[0], triangle[1], triangle[2]):
        triangles += 1

print (triangles)