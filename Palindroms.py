def is_palin(word):
    ori = []
    for w in word:
        ori.append(w)
        oriTmp = ori[::-1]
    l = len(ori)
    l = l - 1
    pal = True
    while  -1 < l:
        oT = oriTmp.pop()
        if(ori[l] != oT):
            pal = False
            break
        else:
            pal = True
            l -= 1
    if(pal):
        return True
    else:
        return False
