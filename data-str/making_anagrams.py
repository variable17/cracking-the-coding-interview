def number_needed(a, b):
    mag = {}
    ran = {}
    for m in a:
        if m in mag:
            mag[m] += 1
        else:
            mag[m] = 1
    for r in b:
        if r in ran:
            ran[r] += 1
        else:
            ran[r] = 1
    i = 0
    for each in mag.keys():
        if each not in ran:
            i = i + mag[each]
        elif mag[each] > ran[each]:
            i = i + mag[each] - ran[each]
    for each in ran.keys():
        if each not in mag:
            i = i + ran[each]
        elif ran[each] > mag[each]:
            i = i + ran[each] - mag[each]
    return i

a = input().strip()
b = input().strip()

print(number_needed(a, b))
