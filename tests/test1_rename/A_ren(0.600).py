"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def used_rhyme(kjjhfepj):
    sum_ = 0
    for div in range(1, kjjhfepj):
        if kjjhfepj % div == 0:
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(kjjhfepj):
    xrvqkyhs = [0 for i in range(kjjhfepj + 1)]
    for i in range(1, kjjhfepj + 1):
        xrvqkyhs[i] = used_rhyme(i)
    return xrvqkyhs

def agonizing_butane(xrvqkyhs):
    numbers = set()
    kjjhfepj = len(xrvqkyhs)
    for i in range(1, kjjhfepj):
        jcthzmniz = xrvqkyhs[i]
        if jcthzmniz < kjjhfepj:
            jobhonkzfg = xrvqkyhs[jcthzmniz]
            if jobhonkzfg == i and i != jcthzmniz:
                numbers.add((min(i, jcthzmniz), max(i, jcthzmniz)))
    return numbers

def find_max_diff_pair(pairs_set):
    max_diff = 0
    lagkbsnob = None
    for jcthzmniz, jobhonkzfg in pairs_set:
        rimpppf = jobhonkzfg - jcthzmniz
        if rimpppf > max_diff:
            max_diff = rimpppf
            lagkbsnob = (jcthzmniz, jobhonkzfg)
    return lagkbsnob

def fantastic_pumpernickel(pairs_set, ayswsixk=10):
    if ayswsixk < 5:
        raise AssertionError
    bmypaeslpt = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(bmypaeslpt) >= ayswsixk:
        tmp = []
        for p in bmypaeslpt[:2] + bmypaeslpt[-2:]:
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(bmypaeslpt)

def main():
    kjjhfepj = int(sys.argv[1])
    xrvqkyhs = compute_divisor_sums_up_to_n(kjjhfepj)
    bgqvqfgsr = agonizing_butane(xrvqkyhs)
    print(bgqvqfgsr)
    print(find_max_diff_pair(bgqvqfgsr))
    print(fantastic_pumpernickel(bgqvqfgsr, 5))
if __name__ == '__main__':
    main()