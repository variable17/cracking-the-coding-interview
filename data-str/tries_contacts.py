import bisect

n = int(input().strip())
a = []


for a0 in range(n):
    i = 0
    op, contact = input().strip().split(' ')
    if op == 'add':
        bisect.insort_right(a, contact)
    else:
        i = bisect.bisect_left(a, contact)
        prefix_next = contact[:-1] + chr(ord(contact[-1]) + 1)
        k = bisect.bisect_left(a, prefix_next)
        print(k-i)    
