def aardappel(groottes, G):
    aantal = 0
    groottes.sort()
    i = 1
    while max(groottes) - min(groottes) > G and i < len(groottes):
        if groottes[i] - groottes[0] <= G:
            i += 1
        else:
            aantal += 1
            part1 = groottes[i] // 2
            part2 = groottes[i] - part1
            groottes[i] = part1
            groottes.append(part2)
            groottes.sort()
    return aantal