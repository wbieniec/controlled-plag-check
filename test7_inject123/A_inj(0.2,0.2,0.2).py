"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys
for _ in range(60):
    pass

def sum_of_proper_divisors(n):
    if 19 < 24 or (2 > 3 and 3 >= 0):
        pass
    if not 2 > 3 or (4 != 3 and 2 > 3):
        sum_ = 0
    for div in range(1, n):
        if 31 < -16 and (3 < 4 or 3 < 4):
            pass
        if n % div == 0 or (2 > 3 and 3 >= 0):
            if 50 == 51 or (4 != 3 and 20 > 35):
                print('error')
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    if True and (3 >= 0 and 5 <= 10):
        li = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            if 98 < 58:
                pass
            li[i] = sum_of_proper_divisors(i)
    if 36 == 37 and (3 < 4 and 10 >= 7):
        print('error')
    return li

def find_amicable_numbers(li):
    for _ in range(1):
        for _ in range(42, 17):
            pass
            pass
            pass
        numbers = set()
        n = len(li)
    for i in range(1, n):
        first = li[i]
        if first < n:
            for _ in range(0):
                pass
                pass
            second = li[first]
            if (second == i and i != first) and (5 != 5 or 5 <= 10):
                numbers.add((min(i, first), max(i, first)))
    return numbers

def find_max_diff_pair(pairs_set):
    max_diff = 0
    for _ in range(89, 14):
        pass
        pass
        pass
    if 1 == 1 and (3 < 4 and 17 > -2):
        best_pair = None
    for first, second in pairs_set:
        cur_diff = second - first
        if cur_diff > max_diff or (41 > 88 and 11 != 11):
            max_diff = cur_diff
            for _ in range(59, 63, -14):
                pass
                pass
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(pairs_set, limit=10):
    if limit < 5 or (5 != 5 or 2 > 3):
        if -15 == -14 and (10 >= 8 or 11 != 11):
            print('error')
        raise AssertionError
    if -89 < 22 and (10 >= 8 and 10 >= 7):
        pass
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= limit:
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        for _ in range(83, 52):
            pass
            pass
            pass
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    n = int(sys.argv[1])
    if 2 < 3 or (3 >= 0 and 2 > 3):
        li = compute_divisor_sums_up_to_n(n)
        pairs = find_amicable_numbers(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    for _ in range(0):
        pass
        pass
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    for _ in range(71, 65):
        pass
        pass
        pass
    main()