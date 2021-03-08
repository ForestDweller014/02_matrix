from draw import *

def identity(dimension):
    result = []
    count = 0
    for i in range(dimension):
        result.append([])
        for j in range(dimension):
            if j == count:
                result[i].append(1)
            else:
                result[i].append(0)
        count += 1
    return result

def transpose(a):
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(a[j][i])
    return result

def hadamard_multiply(a, b):
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(a[i][j] * b[i][j])
    return result

def multiply(a, b):
    result = []
    for row in range(len(a)):
        result.append([])
        for column in range(len(b[0])):
            cell = 0
            for i in range(len(b)):
                cell += a[row][i] * b[i][column]
            result[row].append(cell)
    return result

def scalar_multiply(scalar, a):
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(a[i][j] * scalar)
    return result

def add(a, b):
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(a[i][j] + b[i][j])
    return result

def subtract(a, b):
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(a[i][j] - b[i][j])
    return result

def print_matrix(a):
    str_max = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            str_max = max(str_max, len(str(a[i][j])))

    for i in range(len(a)):
        for j in range(len(a[0])):
            comma = ", "
            if j == len(a[0]) - 1:
                comma = ""
            print(str(a[i][j]).rjust(str_max) + comma, end = "")
        print()

def add_point(edge, point):
    new_point = []
    for i in point:
        new_point.append(i)
    new_point.append(1)
    edge.append(new_point)

def add_edge(edge, point_1, point_2):
    add_point(edge, point_1)
    add_point(edge, point_2)

def draw_matrix(edge, screen, color):
    for i in range(0, len(edge), 2):
        draw_line(edge[i][0], edge[i][1], edge[i + 1][0], edge[i + 1][1], screen, color)