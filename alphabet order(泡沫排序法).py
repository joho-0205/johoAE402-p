#HW:將["aaa","abb","ccc"] 排列 (先轉成ASCII)
data = ["aaa","abb","bzz","bzy","wrg","qef","qer","erh","sge","qwr","wtr"]
for i in range(len(data)):
    i_ascii = ord(data[i][0])
    for j in range(len(data)):
        j_ascii = ord(data[j][0])
        if i_ascii < j_ascii:
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
        elif i_ascii == j_ascii:
            i_ascii = ord(data[i][1])
            j_ascii = ord(data[j][1])
            if i_ascii < j_ascii:
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
            elif i_ascii == j_ascii:
                i_ascii = ord(data[i][2])
                j_ascii = ord(data[j][2])
                if i_ascii < j_ascii:
                    temp = data[i]
                    data[i] = data[j]
                    data[j] = temp
        print(data)


