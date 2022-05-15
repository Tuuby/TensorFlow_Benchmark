import random
import statistics
import time
import json
import tensorflow as tf
import csv

# Define Benchmark variables
operations = 100000
iteration_count = 10

# Start preparing benchmark data
print("TensorFlow version: ", tf.__version__)
print("Preparing benchmark data")

with open("matrices.json", "r") as openfile:
    json_object = json.load(openfile)

json_size = len(json_object)
matrices = []

for i in range(json_size):
    matrix = tf.constant(json_object[i], shape=[20, 20])
    matrices.append(matrix)

matrix_count = len(matrices)

times = []

# Begin timer and actual benchmark
for i in range(iteration_count):
    print(f"[{i + 1}/{iteration_count}] Running benchmark iteration {i + 1} with {operations} operations...")
    start = time.perf_counter()

    for x in range(operations):
        result = tf.matmul(matrices[random.randrange(matrix_count)], matrices[random.randrange(matrix_count)])

    finish = time.perf_counter()
    time_taken = round(finish - start, 10)
    times.append(time_taken)
    print(f"...finished in {time_taken} seconds.\n--------------------------------------")

# Process and present the results
mean = statistics.mean(times)
print(f"[Complete] {iteration_count} benchmarks finished.\nIdividual times in seconds: {times} | mean: {mean} seconds")

with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["sep=,"])
    for i in range(iteration_count):
        writer.writerow([f"Iteration {i + 1}", f"{times[i]}s"])
    writer.writerow(["Mean", f"{mean}s"])
