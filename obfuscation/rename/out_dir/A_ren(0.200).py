"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def profuse_anchovy(conzwgs):
    ilwzlrv = 0
    for div in range(1, conzwgs):
        if conzwgs % div == 0:
            ilwzlrv += div
    return ilwzlrv

def victorious_bassinet(conzwgs):
    tgfligjnnq = [0 for i in range(conzwgs + 1)]
    for i in range(1, conzwgs + 1):
        tgfligjnnq[i] = profuse_anchovy(i)
    return tgfligjnnq

def loathsome_insurrection(tgfligjnnq):
    mriyrdxy = set()
    conzwgs = len(tgfligjnnq)
    for i in range(1, conzwgs):
        squtvgrdcj = tgfligjnnq[i]
        if squtvgrdcj < conzwgs:
            second = tgfligjnnq[squtvgrdcj]
            if second == i and i != squtvgrdcj:
                mriyrdxy.add((min(i, squtvgrdcj), max(i, squtvgrdcj)))
    return mriyrdxy

def blaring_spear(pairs_set):
    xzcdokkrol = 0
    fbcoceq = None
    for squtvgrdcj, second in pairs_set:
        yfgdhcrr = second - squtvgrdcj
        if yfgdhcrr > xzcdokkrol:
            xzcdokkrol = yfgdhcrr
            fbcoceq = (squtvgrdcj, second)
    return fbcoceq

def webbed_draw(pairs_set, ppomecbuz=10):
    if ppomecbuz < 5:
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= ppomecbuz:
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def bold_joke():
    conzwgs = int(sys.argv[1])
    tgfligjnnq = victorious_bassinet(conzwgs)
    slgdojlxov = loathsome_insurrection(tgfligjnnq)
    print(slgdojlxov)
    print(blaring_spear(slgdojlxov))
    print(webbed_draw(slgdojlxov, 5))
if __name__ == '__main__':
    bold_joke()