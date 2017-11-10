def is_matched(expression):
    a = []
    b = {'(':1, '{':2, '[':3}
    c = {')':1, '}':2, ']':3}
    for i in expression:
        if i in b:
            a.append(i)
        else:
            try:
                b[a[len(a)-1]]
            except:
                return False
                
            if i in c and c[i] == b[a[len(a)-1]]:
                a.pop()
            else:
                return False
    if len(a) < 1:
        return True

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")