def parent(a,b):
    if a == b:
        return True
    if b not in inheritance:
        return False
    if a in inheritance[b]:
        return True
    elif 'object' in inheritance[b]:
        return False
    else:
        for i in inheritance[b]:
            if parent(a,i) == True:
                return True
        return False
inheritance = {}
n = int(input())
for i in range(n):
    n1 = input().split()
    if len(n1) == 1:
        inheritance[n1[0]] = ['object']
    else:
        for i in n1[2:]:
            if i not in inheritance:
                inheritance[i] = 'object'
        for i in n1[2:]:
            inheritance[n1[0]] = []
        for i in n1[2:]:
            inheritance[n1[0]].append(i)


q = int(input())
for i in range(q):
    n1 = input().split()
    if parent(n1[0],n1[1]) == True:
        print('Yes')
    else:
        print('No')
