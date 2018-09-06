file_dir = "Log/"
target_dir = "CWND/"

import matplotlib.pyplot as plt


def draw(file_name):
    with open(file_dir + file_name, "r") as f:
        data = f.read().strip()
    data = data.split("\n")

    time = []
    cwnd = []

    for line in data:
        line = line.split("\t")
        if "CWND" == line[0]:
            time.append(float(line[1]))
            cwnd.append(map(float, line[2:]))
            cwnd[-1] = cwnd[-1] / 1024

    assert len(cwnd) != 0

    cwnd = map(list, zip(*cwnd))
    plt.figure(figsize=(19, 8))
    plt.title(" ".join(file_name.split(".")[0].split("_")) + " (No HARQ)")
    plt.xlabel("Time")
    plt.ylabel("CWND (Byte)")

    plt.grid(True)

    for idx in range(len(cwnd)):
        plt.plot(time, cwnd[idx], label="Connection" + str(idx + 1))

    plt.legend(loc="upper right", frameon=True)
    plt.savefig(target_dir + file_name.split(".")[0])
    plt.close()
