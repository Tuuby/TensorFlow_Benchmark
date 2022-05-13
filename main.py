import time
import math

import tensorflow as tf

print("TensorFlow version: ", tf.__version__)
print("Preparing benchmark data")

length = 100000

matrices = []
for i in range(length):
    values = []
    for j in range(100):
        values.append(math.sin(i + j))
    matrix = tf.constant(values, shape=[10, 10])
    matrices.append(matrix)

halflength = len(matrices) // 2
final = tf.constant([0] * 100, shape=[10, 10])

print(f"Starting benchmark with {length} matrices")
start = time.perf_counter()

for i in range(halflength):
    result = tf.matmul(matrices[i], matrices[i + halflength])

finish = time.perf_counter()

print(f"Benchmark finished in {finish - start:0.10f} seconds.")
