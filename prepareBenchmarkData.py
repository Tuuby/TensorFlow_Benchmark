import math
import json

length = 50
matrix_size = 400

matrices = []
for i in range(length):
    values = []
    for j in range(matrix_size):
        values.append(math.sin(i + j))
    matrices.append(values)

json_object = json.dumps(matrices, indent=4)

matrix_dimension = round(math.sqrt(matrix_size))
filename = "matrices.json"

with open(filename, "w") as outfile:
    outfile.write(json_object)
