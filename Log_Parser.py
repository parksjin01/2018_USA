file_dir = "Log/"
target_dir = "Raw/"

def parse(file_name):
    with open(file_dir + file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    enb1 = ["eNB1"]
    enb2 = ["eNB2"]
    used = ["Using"]

    for line in data:
        if "Cell 2" in line:
            enb1.append(line.split(" ")[-1])
        if "Cell 3" in line:
            enb2.append(line.split(" ")[-1])
        if "Current SINR" in line:
            used.append(line.split(" ")[-1])

    with open(target_dir+file_name.split(".")[0]+".dat", 'w') as f:
        f.write(enb1[0] + "\t" + enb2[0] + "\t" + used[0] + "\n")
        idx2 = 1
        for idx in xrange(1, min(len(enb1), len(enb2))):
            if used[idx2] == "-inf":
                f.write(enb1[idx] + "\t" + enb2[idx] + "\t" + "0" + "\n")
                idx2 += 1
            elif used[idx2] == enb1[idx] or used[idx2] == enb2[idx]:
                f.write(enb1[idx] + "\t" + enb2[idx] + "\t" + used[idx2] + "\n")
                idx2 += 1
