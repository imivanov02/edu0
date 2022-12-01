def parent(a,b): #a родитель b?
    if a == b:
        return True
    if b not in err:
        return False
    if a in err[b]:
        return True
    elif 'none' in err[b]:
        return False
    else:
        for i in err[b]:
            if parent(a,i) == True:
                return True
        return False
err = {}
err_pr = []
n = int(input())
for i in range(n):
    tmp = input().split()
    if len(tmp) == 1:
        err[tmp[0]] = ['none']
    else:
        for i in tmp[2:]:
            if i not in err:
                err[i] = 'none'
        for i in tmp[2:]:
            err[tmp[0]] = []
        for i in tmp[2:]:
            err[tmp[0]].append(i)

m = int(input())
for i in range(m):
    _flag = False
    tmp = input()
    err_pr.append(tmp)
    if len(err_pr) > 1:
        for i in range(0,len(err_pr)-1):
            if parent(err_pr[i],tmp) == True:
                _flag = True
        if _flag == True: print(tmp)


