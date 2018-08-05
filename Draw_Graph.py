file_dir = "Raw/"
target_dir = "Graph/"

import matplotlib.pyplot as plt

def multiply(data):
    result = []
    idx = 500.0 / len(data)
    for i in range(len(data)):
        result.append(i * idx)
    return result


def draw(file_name):
    with open(file_dir + file_name, "r") as f:
        data = f.read().strip()
    data = data.split("\n")

    data1 = [data[0].split("\t")[0]]
    data2 = [data[0].split("\t")[1]]
    data3 = [data[0].split("\t")[2]]

    for line in data[1:]:
        data1.append(line.split("\t")[0])
        data2.append(line.split("\t")[1])
        data3.append(line.split("\t")[2])

    plt.figure(figsize=(19, 8))
    plt.title(" ".join(file_name.split(".")[0].split("_")) + " (No HARQ)")
    plt.xlabel("Distance")
    plt.ylabel("SINR")

    plt.grid(True)

    plt.plot(multiply(data1[1:]), data1[1:], label=data1[0])
    plt.plot(multiply(data2[1:]), data2[1:], label=data2[0])
    plt.plot(multiply(data3[1:]), data3[1:], label=data3[0])

    plt.legend(loc="upper right", frameon=True)
    plt.savefig(target_dir + file_name.split(".")[0])
    plt.close()