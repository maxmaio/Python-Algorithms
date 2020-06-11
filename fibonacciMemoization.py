def fibonacci(n):

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    dp = {}
    if n in dp:
        return dp[n]
    
    fibonacciNum = fibonacci(n-1) +fibonacci(n-2)

    dp[n] = fibonacciNum

    return fibonacciNum


if __name__ == '__main__':
    s1 = int(input())

    result = fibonacci(s1)
    print(result)
