# import matplotlib.pyplot as plt
#
# with open("Log/hhDlPdcpStats_5_10_01_08_2018_05_25_01.txt", 'r') as f:
#     data = f.read().strip()
# data = data.split("\n")
#
# prev = 0
# cur = 0
# total = 0
# throughput = []
# for line in data:
#     tmp_line = map(float, line.strip().split(" ")[1:])
#     if cur != tmp_line[0]:
#         prev = cur
#         cur = tmp_line[0]
#         throughput.append(total*(1/(cur-prev))/1024/1024)
#         total = 0
#     if cur == tmp_line[0]:
#         total += tmp_line[4]
#
# for data in throughput[:100]:
#     print data
#
# #
# # plt.figure()
# # plt.xlabel("Time")
# # plt.ylabel("Throughput")


with open("etc/mcDlPdcpStats_1_4_02_08_2018_07_52_33.txt", 'r') as f:
    data = f.read().strip().split("\n")

bit = 0

for line in data:
    bit += map(float, line.strip().split(" ")[1:])[4]

print bit/1024/1024/1024/(float(data[-1].split(" ")[1]))