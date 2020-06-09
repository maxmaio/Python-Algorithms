def getK(arr):
    n = len(arr)
    for x in range(n):
        if arr[x] == 0:
            arr[x] = -1
    totalSum = sum(arr)
    curr = 0

    for x in range(n):
        if curr > totalSum:
            return x
        curr += arr[x]
        totalSum -= arr[x]


if __name__ == '__main__':

   print(getK([1,0,0,1,0]))
   print(getK([1,0,0,1,1]))
   print(getK([1,1,1,0,1]))

