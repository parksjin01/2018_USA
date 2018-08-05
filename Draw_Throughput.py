file_dir = "Log/"
target_dir = "Graph/"

import matplotlib.pyplot as plt

def draw(file_name):
    with open(file_dir + file_name, "r") as f:
        data = f.read().strip()
    data = data.split("\n")

    throughput = ["Throughput"]
    time = []

    for line in data[1:]:
        if "Throughput" in line:
            throughput.append(float(line.split("\t")[2]))
            time.append(float(line.split("\t")[1]) - 0.5)

    plt.figure(figsize=(19, 8))
    plt.title(" ".join(file_name.split(".")[0].split("_")) + " (No HARQ)")
    plt.xlabel("Time")
    plt.ylabel("Throughput(Mbps)")

    plt.grid(True)

    plt.plot(time, throughput[1:], label=throughput[0])

    plt.legend(loc="upper right", frameon=True)
    plt.savefig(target_dir + file_name.split(".")[0] + "_throughput")
    plt.close()