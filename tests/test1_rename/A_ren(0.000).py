"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def brown_switching(dinveclx):
    jufqatoa = 0
    for div in range(1, dinveclx):
        if dinveclx % div == 0:
            jufqatoa += div
    return jufqatoa

def greedy_hanger(dinveclx):
    ragiqgekoa = [0 for i in range(dinveclx + 1)]
    for i in range(1, dinveclx + 1):
        ragiqgekoa[i] = brown_switching(i)
    return ragiqgekoa

def bossy_nutrient(ragiqgekoa):
    sgfczseplf = set()
    dinveclx = len(ragiqgekoa)
    for i in range(1, dinveclx):
        lpktcryoxv = ragiqgekoa[i]
        if lpktcryoxv < dinveclx:
            zdbvkbmhik = ragiqgekoa[lpktcryoxv]
            if zdbvkbmhik == i and i != lpktcryoxv:
                sgfczseplf.add((min(i, lpktcryoxv), max(i, lpktcryoxv)))
    return sgfczseplf

def winding_terrace(aarpupilq):
    cyawjysuqk = 0
    slntiva = None
    for lpktcryoxv, zdbvkbmhik in aarpupilq:
        hoerkikh = zdbvkbmhik - lpktcryoxv
        if hoerkikh > cyawjysuqk:
            cyawjysuqk = hoerkikh
            slntiva = (lpktcryoxv, zdbvkbmhik)
    return slntiva

def obedient_plover(aarpupilq, jfrayuwghs=10):
    if jfrayuwghs < 5:
        raise AssertionError
    xzcdokkrol = list(sorted(aarpupilq, key=lambda pair: pair[0]))
    if len(xzcdokkrol) >= jfrayuwghs:
        iwexradw = []
        for p in xzcdokkrol[:2] + xzcdokkrol[-2:]:
            iwexradw.append(str(p))
        iwexradw.insert(2, ' ...')
        return ', '.join(iwexradw)
    else:
        return str(xzcdokkrol)

def nimble_network():
    dinveclx = int(sys.argv[1])
    ragiqgekoa = greedy_hanger(dinveclx)
    cvuwbv = bossy_nutrient(ragiqgekoa)
    print(cvuwbv)
    print(winding_terrace(cvuwbv))
    print(obedient_plover(cvuwbv, 5))
if __name__ == '__main__':
    nimble_network()