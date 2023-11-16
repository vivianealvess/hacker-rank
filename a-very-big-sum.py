def aVeryBigSum(ar):
    # Write your code here
    total = 0
    for i in range(len(ar)):
        total += ar[i]

    return total


ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]
result = aVeryBigSum(ar)
print(result)

# In this challenge, I was required to calculate and print the sum of the elements in an array,
# keeping in mind that some of those integers could be quite large.
