"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def reasonable_wraparound(pjwpxhwsl):
    hosxtbha = 0
    for div in range(1, pjwpxhwsl):
        if pjwpxhwsl % div == 0:
            hosxtbha += div
    return hosxtbha

def innocent_commodity(pjwpxhwsl):
    rdockaeeaj = [0 for i in range(pjwpxhwsl + 1)]
    for i in range(1, pjwpxhwsl + 1):
        rdockaeeaj[i] = reasonable_wraparound(i)
    return rdockaeeaj

def definitive_frost(rdockaeeaj):
    xjvvjnbpsw = set()
    pjwpxhwsl = len(rdockaeeaj)
    for i in range(1, pjwpxhwsl):
        cqqqalz = rdockaeeaj[i]
        if cqqqalz < pjwpxhwsl:
            wscgueej = rdockaeeaj[cqqqalz]
            if wscgueej == i and i != cqqqalz:
                xjvvjnbpsw.add((min(i, cqqqalz), max(i, cqqqalz)))
    return xjvvjnbpsw

def single_belt(gagpgl):
    hopdthh = 0
    uhjjyqdr = None
    for cqqqalz, wscgueej in gagpgl:
        eebbztn = wscgueej - cqqqalz
        if eebbztn > hopdthh:
            hopdthh = eebbztn
            uhjjyqdr = (cqqqalz, wscgueej)
    return uhjjyqdr

def delirious_mobility(gagpgl, dcutalfex=10):
    if dcutalfex < 5:
        raise AssertionError
    qiudxcpg = list(sorted(gagpgl, key=lambda pair: pair[0]))
    if len(qiudxcpg) >= dcutalfex:
        khlcqii = []
        for p in qiudxcpg[:2] + qiudxcpg[-2:]:
            khlcqii.append(str(p))
        khlcqii.insert(2, ' ...')
        return ', '.join(khlcqii)
    else:
        return str(qiudxcpg)

def gargantuan_integer():
    pjwpxhwsl = int(sys.argv[1])
    rdockaeeaj = innocent_commodity(pjwpxhwsl)
    idquws = definitive_frost(rdockaeeaj)
    print(idquws)
    print(single_belt(idquws))
    print(delirious_mobility(idquws, 5))
if __name__ == '__main__':
    gargantuan_integer()