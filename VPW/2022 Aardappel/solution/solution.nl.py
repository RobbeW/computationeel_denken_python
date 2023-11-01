t = int(input())
for j in range(t):
    str = input( )
    aantal = [int(n) for n in str.split()]
    
    G = aantal[0]
    n = aantal[1]
    aantal.pop(0)
    aantal.pop(0)
    
    flag = True
    n_cuts = 0
    patat = aantal.copy()
    while flag:
        patat_temp = []
        kleinste = min(patat)
        for i in range(len(patat)):
            size = patat[i]
            # Perhaps this can be simplified
            if not abs(size - kleinste) <= G : #cut once
                n_cuts += 1
                patat_temp.append(size // 2)
                patat_temp.append(size // 2 + size % 2)
                flag = False
            else:
                patat_temp.append(size)
        patat = patat_temp
        flag = not flag 
        
    print(j+1, n_cuts)

