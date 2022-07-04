import csv
import glob

import matplotlib.pyplot as plt

# TODO: group results by benchmarks

for file in glob.glob("*.csv"):
    print(file)
    with open(file, newline='') as csvfile:
        fig = plt.figure(figsize=(10, 7))

        data = []
        reader = csv.reader(csvfile)
        for row in reader:
            if "Iteration" in row[0]:
                number = row[1][:-1]
                data.append(float(number))

        plt.boxplot(data)

        plt.show()