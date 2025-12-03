import csv
import sys

def xkey(x):
    module = x["所属程序模块"] if len(x["所属程序模块"]) > 0 else "000"
    b = x["指标名称"] if len(x["指标名称"]) > 0 else "000"
    c = x["指标类型"] if len(x["指标类型"]) > 0 else "000"
    res = f"{module}{b}{c}"
    print(res)
    return res

fields = ["优先级","代码形式","指标类型","指标名称","指标含义","apps 目录入口","所属程序模块"]
fh = open(sys.argv[1])
reader = csv.DictReader(fh, fields)

content = []
for item in reader:
    item = {k: v.strip() for (k, v) in item.items()}
    if item["apps 目录入口"] == "未使用":
        continue
    content.append(item)

data = content[1:]
result = sorted(data, key=xkey)

fh.close()

print(result)

fh = open("example.csv", "a+")
w = csv.DictWriter(fh, fields)
w.writerows(list(result))