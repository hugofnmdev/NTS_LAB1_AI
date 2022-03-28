
def transformPoint(p,height):
    return p[0],height-p[1]-1

def inversePoints(l, height, baseheight):
    if l == []:
        return []
    lres = []
    lres.append(transformPoint((l[0][0],baseheight),height))
    for i in range(len(l)):
        lres.append(transformPoint(l[i],height))
    lres.append(transformPoint((l[-1][0],baseheight),height))
    return lres
    

