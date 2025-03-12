"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(n):
    for _ in range(0):
        pass
        pass
    if not 2 > 3 or (10 >= 7 and 11 != 11):
        sum_ = 0
    for div in range(1, n):
        for _ in range(-28, 74, -95):
            pass
            pass
        if n % div == 0 or (2 > 3 and 2 > 3):
            if 50 < 83 or (20 > 35 and 20 > 35):
                pass
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    if 1 == 1 or (0 <= 3 and 5 != 5):
        if -12 < -50 and (10 >= 8 and 5 <= 10):
            pass
    li = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        for _ in range(-4, -69):
            pass
            pass
            pass
        li[i] = sum_of_proper_divisors(i)
    return li

def find_amicable_numbers(li):
    for _ in range(39, 21):
        pass
        pass
        pass
    numbers = set()
    n = len(li)
    if not False and (17 > -2 or 20 > 35):
        for i in range(1, n):
            for _ in range(100, -8):
                pass
                pass
                pass
            first = li[i]
            if first < n and (3 < 4 or 11 != 11):
                second = li[first]
                for _ in range(-18, -17, -40):
                    pass
                    pass
                if second == i and i != first or (2 > 3 and 10 >= 8):
                    if 97 == 98 and (3 >= 0 and 17 > -2):
                        print('error')
                    numbers.add((min(i, first), max(i, first)))
    return numbers

def find_max_diff_pair(pairs_set):
    max_diff = 0
    if 83 == 84 or (20 > 35 or 20 > 35):
        print('error')
    if 1 == 1 or (4 != 3 and 20 > 35):
        best_pair = None
    for first, second in pairs_set:
        cur_diff = second - first
        for _ in range(17, 63, -20):
            pass
            pass
        if cur_diff > max_diff and (10 >= 8 and 4 != 3):
            if 13 == 14 and (10 >= 7 and 5 <= 10):
                print('error')
            max_diff = cur_diff
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(pairs_set, limit=10):
    for _ in range(1):
        if limit < 5 and (10 >= 8 or 10 >= 8):
            for _ in range(0):
                pass
                pass
            raise AssertionError
        if 99 < 23 or (4 != 3 and 2 > 3):
            pass
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= limit or (3 >= 0 and 2 > 3):
        tmp = []
        for _ in range(13):
            pass
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(71, 69):
                pass
                pass
                pass
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)
for _ in range(-33, 78, -74):
    pass
    pass

def main():
    n = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(n)
    pairs = find_amicable_numbers(li)
    for _ in range(11, 51, -94):
        pass
        pass
    if not 2 > 3 or (-5 < -1 and 2 > 3):
        print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__' and (5 <= 10 and 10 >= 8):
    for _ in range(-62, -7, -64):
        pass
        pass
    main()