def compareTriplets(a, b):
    pointsA = 0
    pointsB = 0

    for i in range(len(a)):
        if a[i] > b[i]:
            pointsA += 1
        elif a[i] < b[i]:
            pointsB += 1
    score = [pointsA, pointsB]
    return score


a = [1, 2, 3]
b = [3, 2, 1]
res = compareTriplets(a, b)
print(res)
