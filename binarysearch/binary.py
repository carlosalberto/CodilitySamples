
def bsearch(A, k):
    N = len(A)

    start = 0
    end = len(A) - 1

    while start <= end:
        middle = (start + end) / 2
        if A[middle] == k:
            return middle

        if A[middle] > k:
            end = middle - 1
        else:
            start = middle + 1

    return -1

if __name__ == '__main__':
    print bsearch([ 1, 2, 3, 4, 5 ], 3)
    print bsearch([ 1, 2, 3, 4, 5, 6 ], 3)
    print bsearch([ -10, -7, -3, 1, 2, 2, 7 ], -3)
    print ''

    print bsearch([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 1)
    print bsearch([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 10)
    print bsearch([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 6)
    print bsearch([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ], 7)
    print ''

    print bsearch([], 10)
    print bsearch([ 0, 1, 2, 2, 7 ], 13)
    print bsearch([ 0, 1, 2, 2, 7 ], -4)

