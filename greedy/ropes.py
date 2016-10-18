
def solution(K, A):
    length = 0
    ropes = 0

    for i in xrange(len(A)):
        if A[i] < 0:
            continue

        length += A[i]
        if length >= K:
            ropes += 1
            length = 0

    return ropes

if __name__ == '__main__':
    assert solution(1, [ 0 ]) == 0
    assert solution(1, [ 1 ]) == 1
    assert solution(1, [ 1, 1 ]) == 2
    assert solution(1, [ 1, 2, 3 ]) == 3

    assert solution(4, [ 1, 2, 3, 4, 1, 1, 3 ]) == 3
    assert solution(1001, [ 1, 1004, 3, 1002, 2, 1007, 5, 1, 1000]) == 4

    print 'OK'

