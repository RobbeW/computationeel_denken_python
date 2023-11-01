t = int( input(  ) )
for i in range( t ):
    # Alle invoer verwerken
    N = int(input( ) ) # aantal stations
    m = []
    for _ in range( N ):
        regel = input()
        m.append( [int(n) for n in regel.split()] )
    P = int(input()) # aantal personen
    v_str = input()
    a_str = input()
    v = [int(n) for n in v_str.split()]
    a = [int(n) for n in a_str.split()]
    
    # Verwerking
    v_edit = v.copy()
    a_edit = a.copy()
    winst = 0
    flag = True
    while( flag ):
        winst_max = 0
        index_p1 = -1
        index_p2 = -1
        for j in range(len(v_edit)):
            for k in range(len(v_edit)):
                v1 = v_edit[j]
                a1 = a_edit[j]
                v2 = v_edit[k]
                a2 = a_edit[k]
                k1 = m[v1-1][a1-1] - m[v1-1][a2-1] #individuele kost
                k2 = m[v2-1][a2-1] - m[v2-1][a1-1]
                # totale winst
                winst_totaal = m[v1-1][a1-1] + m[v2-1][a2-1] - m[v1-1][a2-1] -  m[v2-1][a1-1]
                if a1 == v2 and k1 > 0 and k2 > 0 and winst_totaal > winst_max: #voldoet, dus wisselen
                    winst_max = winst_totaal
                    index_p2 = k
                    index_p1 = j
        if index_p1 != -1: #wissel gevonden, doorvoeren
            winst += winst_max
            v_edit.pop(index_p1)
            v_edit.pop(index_p2-1)
            a_edit.pop(index_p1)
            a_edit.pop(index_p2-1)

        flag = index_p1 != -1 # Er werd een wissel doorgevoerd, probeer nog eens
    
    print(i+1, winst)
