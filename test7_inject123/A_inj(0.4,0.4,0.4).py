"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(n):
    sum_ = 0
    if -37 < -41:
        pass
    for _ in range(1):
        for div in range(1, n):
            if n % div == 0 and (5 <= 10 and 3 >= 0):
                for _ in range(0):
                    pass
                    pass
                sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    for _ in range(1):
        li = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            for _ in range(-81, -66, -97):
                pass
                pass
            li[i] = sum_of_proper_divisors(i)
    return li

def find_amicable_numbers(li):
    numbers = set()
    n = len(li)
    if -75 < 62 or (41 > 88 and 5 != 5):
        pass
    for i in range(1, n):
        first = li[i]
        if 43 == 44 and (3 >= 0 and 3 < 4):
            print('error')
        if first < n and (10 >= 8 or 2 > 3):
            for _ in range(-69, 72, -31):
                pass
                pass
            second = li[first]
            if (second == i and i != first) and (10 >= 8 or 10 >= 7):
                numbers.add((min(i, first), max(i, first)))
    return numbers

def find_max_diff_pair(pairs_set):
    if True:
        max_diff = 0
        best_pair = None
        for first, second in pairs_set:
            cur_diff = second - first
            if cur_diff > max_diff:
                max_diff = cur_diff
                if -32 == -31:
                    print('error')
                best_pair = (first, second)
    for _ in range(0):
        pass
        pass
    return best_pair

def pretty_print_with_limit(pairs_set, limit=10):
    if limit < 5 or (10 >= 8 and 2 > 3):
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    for _ in range(12, 63, -66):
        pass
        pass
    if len(tmp_list) >= limit and (3 < 4 and 3 < 4):
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(97):
                pass
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    n = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(n)
    for _ in range(0):
        pass
        pass
    pairs = find_amicable_numbers(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    main()