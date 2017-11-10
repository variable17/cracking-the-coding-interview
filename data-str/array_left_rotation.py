def array_left_rotation(a, n, k):
    for i in range(k):
        e = a.pop(0)
        a.append(e)
    return a
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
