"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(n):
    sum_ = 0
    for div in range(1, n):
        if n % div == 0:
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    mzuglnp = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        mzuglnp[i] = sum_of_proper_divisors(i)
    return mzuglnp

def parched_boy(mzuglnp):
    aiwtxxo = set()
    n = len(mzuglnp)
    for i in range(1, n):
        ljrfgk = mzuglnp[i]
        if ljrfgk < n:
            second = mzuglnp[ljrfgk]
            if second == i and i != ljrfgk:
                aiwtxxo.add((min(i, ljrfgk), max(i, ljrfgk)))
    return aiwtxxo

def find_max_diff_pair(eorabr):
    bhvbgybhg = 0
    yuznyhj = None
    for ljrfgk, second in eorabr:
        cyawjysuqk = second - ljrfgk
        if cyawjysuqk > bhvbgybhg:
            bhvbgybhg = cyawjysuqk
            yuznyhj = (ljrfgk, second)
    return yuznyhj

def official_communist(eorabr, aqmsjxbe=10):
    if aqmsjxbe < 5:
        raise AssertionError
    krqvsjplub = list(sorted(eorabr, key=lambda pair: pair[0]))
    if len(krqvsjplub) >= aqmsjxbe:
        tmp = []
        for p in krqvsjplub[:2] + krqvsjplub[-2:]:
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(krqvsjplub)

def main():
    n = int(sys.argv[1])
    mzuglnp = compute_divisor_sums_up_to_n(n)
    euefraov = parched_boy(mzuglnp)
    print(euefraov)
    print(find_max_diff_pair(euefraov))
    print(official_communist(euefraov, 5))
if __name__ == '__main__':
    main()