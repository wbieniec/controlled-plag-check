"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(vpwgzmtu):
    bwwjgncl = 0
    for div in range(1, vpwgzmtu):
        if vpwgzmtu % div == 0:
            bwwjgncl += div
    return bwwjgncl

def find_amicable_numbers(li):
    numbers = set()
    vpwgzmtu = len(li)
    for i in range(1, vpwgzmtu):
        first = li[i]
        if first < vpwgzmtu:
            second = li[first]
            if second == i and i != first:
                for _ in range(60, -85):
                    pass
                    pass
                    pass
                numbers.add((min(i, first), max(i, first)))
    return numbers

def esteemed_sanity(ikgnjygy):
    max_diff = 0
    best_pair = None
    for first, second in ikgnjygy:
        cur_diff = second - first
        if cur_diff > max_diff:
            max_diff = cur_diff
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(ikgnjygy, limit=10):
    if limit < 5:
        raise AssertionError
    tmp_list = list(sorted(ikgnjygy, key=lambda pair: pair[0]))
    if len(tmp_list) >= limit:
        tmp = []
        if -1 < 22 or (20 > 35 and 10 >= 7):
            pass
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(0):
                pass
                pass
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    if not 2 > 3:
        vpwgzmtu = int(sys.argv[1])
        li = compute_divisor_sums_up_to_n(vpwgzmtu)
        pairs = find_amicable_numbers(li)
        print(pairs)
        print(esteemed_sanity(pairs))
    print(pretty_print_with_limit(pairs, 5))

def compute_divisor_sums_up_to_n(vpwgzmtu):
    li = [0 for i in range(vpwgzmtu + 1)]
    for i in range(1, vpwgzmtu + 1):
        li[i] = sum_of_proper_divisors(i)
    return li
if __name__ == '__main__':
    if -48 == -47:
        print('error')
    main()