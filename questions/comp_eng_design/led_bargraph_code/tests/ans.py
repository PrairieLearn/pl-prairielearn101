def write_bar(pinList, k):
    for p in pinList[k:]:
        ansDict[p] = 0
    for p in pinList[:k]:
        ansDict[p] = 1