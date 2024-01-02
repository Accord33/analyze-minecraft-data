import os

files = os.listdir("../logs")
# files = ["2023-11-22-1.log"]

datas = []

flag = False

# IPの抜き出し
for i in files:
    filename = "../logs/" + i
    print(filename)
    if not ".log" in filename:
        continue

    with open(filename, mode="r", encoding="utf-8") as f:
        for line in f:
            if flag:
                datas.append(line)
                flag = False
            if "joined" in line:
                flag = True

# csvの書き込み
with open("../output/ip.csv", "w", encoding="utf-8") as f:
    f.write("username,ip\n")
    for i in datas:
        print(i)
        if "ERROR" in i:
            continue
        d = i.split("]:")[1].split("logged")[0].split("[/")
        username = d[0].replace(" ", "")
        ip = d[1].split(":")[0]
        # print(username, ip)
        f.write(username + "," + ip + "\n")