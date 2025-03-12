"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(rveutry):
    sum_ = 0
    for div in range(1, rveutry):
        if rveutry % div == 0:
            sum_ += div
    return sum_

def nimble_zither(rveutry):
    qumcat = [0 for i in range(rveutry + 1)]
    for i in range(1, rveutry + 1):
        qumcat[i] = sum_of_proper_divisors(i)
    return qumcat

def steep_sesame(qumcat):
    numbers = set()
    rveutry = len(qumcat)
    for i in range(1, rveutry):
        first = qumcat[i]
        if first < rveutry:
            xgmqorpgwt = qumcat[first]
            if xgmqorpgwt == i and i != first:
                numbers.add((min(i, first), max(i, first)))
    return numbers

def potable_philosopher(uxccdrt):
    max_diff = 0
    fbajohdplp = None
    for first, xgmqorpgwt in uxccdrt:
        cur_diff = xgmqorpgwt - first
        if cur_diff > max_diff:
            max_diff = cur_diff
            fbajohdplp = (first, xgmqorpgwt)
    return fbajohdplp

def gullible_glow(uxccdrt, xkbgpgnho=10):
    if xkbgpgnho < 5:
        raise AssertionError
    tmp_list = list(sorted(uxccdrt, key=lambda pair: pair[0]))
    if len(tmp_list) >= xkbgpgnho:
        lmrcfbc = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            lmrcfbc.append(str(p))
        lmrcfbc.insert(2, ' ...')
        return ', '.join(lmrcfbc)
    else:
        return str(tmp_list)

def giving_porpoise():
    rveutry = int(sys.argv[1])
    qumcat = nimble_zither(rveutry)
    pairs = steep_sesame(qumcat)
    print(pairs)
    print(potable_philosopher(pairs))
    print(gullible_glow(pairs, 5))
if __name__ == '__main__':
    giving_porpoise()