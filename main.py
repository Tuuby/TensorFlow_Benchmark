import random
import statistics
import time
import json
import tensorflow as tf
import csv
import config

# Uncomment to run on CPU
# tf.config.experimental.set_visible_devices([], 'GPU')

# Define Benchmark variables
operations = config.benchmark_params['operations_count']
iteration_count = config.benchmark_params['iteration_count']
matrix_dimension = config.benchmark_params['matrix_dimension']

# Start preparing benchmark data
print("TensorFlow version: ", tf.__version__)
print("Preparing benchmark data")

with open("matrices.json", "r") as openfile:
    json_object = json.load(openfile)

json_size = len(json_object)
matrices = []

for i in range(json_size):
    matrix = tf.constant(json_object[i], shape=[matrix_dimension, matrix_dimension])
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

with open(f"results_{config.benchmark_params['benchmark_label']}_op{operations}_d{matrix_dimension}.csv", "w", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow(["sep=,"])
    for i in range(iteration_count):
        writer.writerow([f"Iteration {i + 1}", f"{times[i]}s"])
    writer.writerow(["Mean", f"{mean}s"])
