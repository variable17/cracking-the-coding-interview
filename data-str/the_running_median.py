import bisect


n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
    a_t = int(input().strip())
    bisect.insort_right(a, a_t)
    if a_i == 0:
        print('%.1f' %a[a_i])
    elif a_i % 2 == 0:
        print('%.1f' %a[a_i//2])
    else:
        p = a_i//2
        print('%.1f' %((a[p]+a[p+1])/2))