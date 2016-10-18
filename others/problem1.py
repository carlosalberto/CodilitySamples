
def flat_impl(res, A):
    for x in A:
        if type(x) == int:
            res.append(x)
        else:
            flat_impl(res, x)

    return res

def flat(A):
    res = []
    flat_impl(res, A)

    return res

if __name__ == '__main__':
    print flat([1,2,[3],[4,[5,6]],[[7]], 8])
    print flat([1, 2, [3], [4, [5, 6], 5, 6], [[7], [8, [9]]], 10])
    print flat([1, 2, [3], [4, [5, 6], 5, 6], [[7], [8, [9]]], 10, [[[11], 12]]])

