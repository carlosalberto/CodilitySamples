
def triangles(A):
    n = len(A)
    result = 0

    for x in xrange(n):
        z = x + 2
        for y in xrange(x + 1, n):
            while z < n and A[x] + A[y] > A[z]:
                z += 1

            result += z - y - 1;

    return result

if __name__ == '__main__':
    assert triangles([1, 2, 3]) == 0
    assert triangles([2, 3, 4]) == 1
    assert triangles([1, 2, 3, 4, 5, 6]) == 7
    assert triangles([3, 4, 5, 6, 7, 8]) == 17

