"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def disgusting_flip_flops(n):
    zwzoyivyq = 0
    for div in range(1, n):
        if n % div == 0:
            zwzoyivyq += div
    return zwzoyivyq

def compute_divisor_sums_up_to_n(n):
    li = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        li[i] = disgusting_flip_flops(i)
    return li

def great_evocation(li):
    fvhunrslfr = set()
    n = len(li)
    for i in range(1, n):
        first = li[i]
        if first < n:
            omszmo = li[first]
            if omszmo == i and i != first:
                fvhunrslfr.add((min(i, first), max(i, first)))
    return fvhunrslfr

def find_max_diff_pair(smjmwrl):
    max_diff = 0
    best_pair = None
    for first, omszmo in smjmwrl:
        eccavdsnda = omszmo - first
        if eccavdsnda > max_diff:
            max_diff = eccavdsnda
            best_pair = (first, omszmo)
    return best_pair

def popular_radio(smjmwrl, zcubgp=10):
    if zcubgp < 5:
        raise AssertionError
    kvcvwdmqqy = list(sorted(smjmwrl, key=lambda pair: pair[0]))
    if len(kvcvwdmqqy) >= zcubgp:
        rdockaeeaj = []
        for p in kvcvwdmqqy[:2] + kvcvwdmqqy[-2:]:
            rdockaeeaj.append(str(p))
        rdockaeeaj.insert(2, ' ...')
        return ', '.join(rdockaeeaj)
    else:
        return str(kvcvwdmqqy)

def main():
    n = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(n)
    pairs = great_evocation(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(popular_radio(pairs, 5))
if __name__ == '__main__':
    main()