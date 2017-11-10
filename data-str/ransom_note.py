def ransom_note(magazine, ransom):
    for r in ransom:
        if r in magazine:
            magazine.remove(r)
        else:
            return False
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else: