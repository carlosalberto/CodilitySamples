
def problem2(S):
    if len(S) == 0:
        return 0

    def separate_part(part):
        return part.split('-')

    max_count = 1
    count = 1
    parts = S.split(',')
    latest = separate_part(parts[0])[1]

    # work in indices and try on all of them.
    for i in xrange(1, len(parts)):
        part = parts[i]
        l, r = separate_part(part)
        if latest == l:
            count += 1
        else:
            count = 1

        latest = r
        max_count = max(max_count, count)

    return max_count

if __name__ == '__main__':
    print problem2('6-3,3-7,7-5,1-5')
    print problem2('1-3,2-4,6-3,3-7,7-5,1-5')
    print problem2('1-3,4-7,9-13,1-99')
    print problem2('1-2,2-3,99-100,1-7,7-99,99-10,10-9,7-1,2-3')
    print ''

    print problem2('1-1')
    print problem2('1-2,1-2')
    print problem2('3-2,2-1,1-4,4-4,5-4,4-2,2-1')
    print problem2('5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5')

