import csv
import glob
import re

import matplotlib.pyplot as plt

# TODO: group results by benchmarks

data_1st_bm = []
data_2nd_bm = []
data_3rd_bm = []
data_4th_bm = []

for file in glob.glob("*.csv"):

    hw_name = re.search('results_(.+?)_op', file).group(1)
    bm_name = re.search('_op(.+?).csv', file).group(1)

    with open(file, newline='') as csvfile:
        fig = plt.figure(figsize=(10, 7))

        data = []
        reader = csv.reader(csvfile)
        for row in reader:
            if "Iteration" in row[0]:
                number = row[1][:-1]
                data.append(float(number))

        if bm_name == "100000_d1000":
            data_1st_bm.append(data)
        elif bm_name == "100000_d100":
            data_2nd_bm.append(data)
        elif bm_name == "1000000_d100":
            data_3rd_bm.append(data)
        else:
            data_4th_bm.append(data)

labels=['GTX1070', 'M1_SoC', 'Ryzen 3600X', 'TPUv3']

plt.boxplot(data_1st_bm, labels=labels)
plt.title("100,000 operations / 1000x1000")
plt.show()

plt.boxplot(data_2nd_bm, labels=labels)
plt.title("100,000 operations / 100x100")
plt.show()

plt.boxplot(data_3rd_bm, labels=labels)
plt.title("1,000,000 operations / 100x100")
plt.show()

plt.boxplot(data_4th_bm, labels=labels)
plt.title("10,000 operations / 5000x5000")
plt.show()
