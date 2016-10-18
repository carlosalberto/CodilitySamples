
def solution(A):
    n = len(A)
    dp = [0] * n
    dp[0] = A[0]

    for i in xrange(1, n):
        steps = min(6, i)

        dp[i] = dp[i - steps] + A[i]
        for j in xrange(1, steps):
            dp[i] = max(dp[i], dp[i - j] + A[i])

    return dp[n - 1]

if __name__ == '__main__':
    assert solution([ 1, -2, 0, 9, -1, -2 ]) == 8
    assert solution([ 1, -2, 0, 9, -1, -2, -2, -2, -2, -2, -2 ]) == 7
    assert solution([ 1, -2, 0, 9, -1, 100 ]) == 110

    print 'OK'

