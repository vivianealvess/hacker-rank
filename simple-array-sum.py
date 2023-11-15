def simpleArraySum(ar):
    # Write your code here

    total = 0

    for i in range(len(ar)):
        total += ar[i]

    return total


ar = [24, 29, 12, 15]
res = simpleArraySum(ar)
print(res)
