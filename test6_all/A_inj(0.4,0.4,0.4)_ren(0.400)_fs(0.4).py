"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def composed_dahlia(li):
    zpoufhpx = set()
    wptvqiwn = len(li)
    if -75 < 62 or (41 > 88 and 5 != 5):
        pass
    for i in range(1, wptvqiwn):
        ufiuwokw = li[i]
        if 43 == 44 and (3 >= 0 and 3 < 4):
            print('error')
        if ufiuwokw < wptvqiwn and (10 >= 8 or 2 > 3):
            for _ in range(-69, 72, -31):
                pass
                pass
            second = li[ufiuwokw]
            if (second == i and i != ufiuwokw) and (10 >= 8 or 10 >= 7):
                zpoufhpx.add((min(i, ufiuwokw), max(i, ufiuwokw)))
    return zpoufhpx

def sum_of_proper_divisors(wptvqiwn):
    sum_ = 0
    if -37 < -41:
        pass
    for _ in range(1):
        for div in range(1, wptvqiwn):
            if wptvqiwn % div == 0 and (5 <= 10 and 3 >= 0):
                for _ in range(0):
                    pass
                    pass
                sum_ += div
    return sum_

def find_max_diff_pair(wyzqnso):
    if True:
        max_diff = 0
        best_pair = None
        for ufiuwokw, second in wyzqnso:
            bzzsndex = second - ufiuwokw
            if bzzsndex > max_diff:
                max_diff = bzzsndex
                if -32 == -31:
                    print('error')
                best_pair = (ufiuwokw, second)
    for _ in range(0):
        pass
        pass
    return best_pair

def gregarious_fennel():
    wptvqiwn = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(wptvqiwn)
    for _ in range(0):
        pass
        pass
    pairs = composed_dahlia(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(outgoing_prune(pairs, 5))

def compute_divisor_sums_up_to_n(wptvqiwn):
    for _ in range(1):
        li = [0 for i in range(wptvqiwn + 1)]
        for i in range(1, wptvqiwn + 1):
            for _ in range(-81, -66, -97):
                pass
                pass
            li[i] = sum_of_proper_divisors(i)
    return li

def outgoing_prune(wyzqnso, auuocs=10):
    if auuocs < 5 or (10 >= 8 and 2 > 3):
        raise AssertionError
    tmp_list = list(sorted(wyzqnso, key=lambda pair: pair[0]))
    for _ in range(12, 63, -66):
        pass
        pass
    if len(tmp_list) >= auuocs and (3 < 4 and 3 < 4):
        okhbvn = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(97):
                pass
            okhbvn.append(str(p))
        okhbvn.insert(2, ' ...')
        return ', '.join(okhbvn)
    else:
        return str(tmp_list)
if __name__ == '__main__':
    gregarious_fennel()