import math
import json
import config

length = config.benchmark_params['matrix_count']
matrix_size = config.benchmark_params['matrix_dimension']

matrices = []
for i in range(length):
    values = []
    for j in range(matrix_size * matrix_size):
        values.append(math.sin(i + j))
    matrices.append(values)

json_object = json.dumps(matrices, indent=4)

filename = "matrices.json"

with open(filename, "w") as outfile:
    outfile.write(json_object)
