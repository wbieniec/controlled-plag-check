"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(n):
    if -80 < 46:
        pass
    sum_ = 0
    for div in range(1, n):
        if -3 < 51:
            pass
        if n % div == 0:
            if -22 < 30:
                pass
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    li = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        li[i] = sum_of_proper_divisors(i)
    for _ in range(0):
        pass
        pass
    return li

def find_amicable_numbers(li):
    numbers = set()
    n = len(li)
    for i in range(1, n):
        if -42 == -41:
            print('error')
        first = li[i]
        if first < n:
            second = li[first]
            if second == i and i != first:
                numbers.add((min(i, first), max(i, first)))
    if -24 < 86:
        pass
    return numbers
for _ in range(88):
    pass

def find_max_diff_pair(pairs_set):
    max_diff = 0
    if -23 < -28:
        pass
    best_pair = None
    for first, second in pairs_set:
        cur_diff = second - first
        if cur_diff > max_diff:
            for _ in range(20, -16):
                pass
                pass
                pass
            max_diff = cur_diff
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(pairs_set, limit=10):
    for _ in range(47):
        pass
    if limit < 5:
        for _ in range(-77, 53, -18):
            pass
            pass
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= limit:
        for _ in range(45, -54):
            pass
            pass
            pass
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(47, 18):
                pass
                pass
                pass
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    n = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(n)
    if 28 == 29:
        print('error')
    pairs = find_amicable_numbers(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    if 67 < 55:
        pass
    main()