import re
import numpy as np

file = open('input.txt', 'r')
all_lines = file.readlines()
file.close()

fabric_matrix = np.zeros((1000, 1000))
for line in all_lines:
    pattern_instuctions = re.match('#(?P<pattern_no>\d*)\s@\s(?P<x_start>\d*),(?P<y_start>\d*):\s(?P<x_len>\d*)x(?P<y_len>\d*)', line)
    x_start = int(pattern_instuctions.group('x_start'))
    y_start = int(pattern_instuctions.group('y_start'))
    x_len = int(pattern_instuctions.group('x_len'))
    y_len = int(pattern_instuctions.group('y_len'))
    fabric_matrix[x_start:x_start + x_len, y_start:y_start + y_len] += 1

print(sum(map(lambda x: 1 if x > 1 else 0, fabric_matrix.flatten())))
