from collections import Counter

def solve(n, arr):
    if n==0 or len(arr) ==0:
        return 'YES'
    #must be divisible by n
    if len(arr)%n != 0:
        return 'NO'
    count = Counter(arr)
    print(count)
    for x in count:
        print(count[x])
        if count[x] > len(arr)/n:
            return "NO"
    return "YES"
    

if __name__ == '__main__':
    print(solve(2,[2,2,3,4]))