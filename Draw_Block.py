file_dir = "Log/"
target_dir = "Block/"

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle

def draw(file_name):
    with open(file_dir + file_name, "r") as f:
        data = f.read().strip()
    data = data.split("\n")

    minx = 0
    maxx = 500
    miny = 0
    maxy = 0

    block = []
    for line in data:
        if "Building:" in line:
            print repr(line)
            block.append(map(float, line.split("\t")[1:5]))
            if minx > block[-1][0]:
                minx = block[-1][0]
            if maxx < block[-1][1]:
                maxx = block[-1][1]
            if miny > block[-1][2]:
                miny = block[-1][2]
            if maxy < block[-1][3]:
                maxy = block[-1][3]

    plt.figure(figsize=(19, 8))
    plt.title(" ".join(file_name.split(".")[0].split("_")) + "_Buildings")
    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.xlim([minx - 100, maxx + 100])
    plt.ylim([miny - 100, maxy + 100])

    plt.grid(True)
    current_axis = plt.gca()
    for each_block in block:
        current_axis.add_patch(Rectangle([each_block[0], each_block[2]], each_block[1] - each_block[0], each_block[3] - each_block[2], fill=None, alpha=1))
        plt.text((each_block[0] + each_block[1])/2, (each_block[2] + each_block[3])/2, "Building", horizontalalignment='center')

    current_axis.add_patch(Circle((0, 0), 5, color="skyblue", label = "UE"))
    current_axis.add_patch(Circle((5, 50), 5, color="lightgreen", label = "eNB1"))
    current_axis.add_patch(Circle((405, 50), 5, color="pink", label = "eNB2"))
    plt.legend(loc="upper right", frameon=True)

    # if maxy == 0:
    #     maxy = 100
    # current_axis.add_artist(plt.Circle((500, maxy + 15), 5, color="skyblue"))
    # current_axis.add_artist(plt.Circle((500, maxy + 30), 5, color="lightgreen"))
    # current_axis.add_artist(plt.Circle((500, maxy + 45), 5, color="pink"))

    plt.arrow(0, 0, 500, 0, shape="full", head_width=10, label="path")
    plt.text(250, -10, "UE moving path", horizontalalignment='center')

    plt.savefig(target_dir+file_name.split(".log")[0]+"_obstacle")
    plt.close()

if __name__ == '__main__':
    draw("car_with_block.log")