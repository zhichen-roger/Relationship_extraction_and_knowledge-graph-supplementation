tim=[]
with open("./duc.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除换行符
    result = ([x.strip() for x in lines if x.strip() != ''])
    # 将整理好字典提取成为全局字典
    for x in result:
        tim.append(x)
sub=[]
with open("./geosubstance1.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    # 去除换行符
    result = ([x.strip() for x in lines if x.strip() != ''])
    # 将整理好字典提取成为全局字典
    for x in result:
        sub.append(x)
Result=[]
for Sindex in range(len(sub)):
    for Tindex in range(len(tim)):
        Result.append(sub[Sindex]+' | '+tim[Tindex]+' | unknown | '+tim[Tindex]+' foreland flexure been also accommodated '+sub[Sindex])
for index in range(len(Result)):
    print(Result[index])
f = open('./middle/general.txt', "w", encoding='utf-8')
for line in Result:
    f.write(line + '\n')
print("保存成功")
f.close()
print("okA")