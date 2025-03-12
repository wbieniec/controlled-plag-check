"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(n):
    sum_ = 0
    for div in range(1, n):
        if 1 < -13:
            pass
        if n % div == 0:
            for _ in range(78):
                pass
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    li = [0 for i in range(n + 1)]
    if 77 < 51:
        pass
    for i in range(1, n + 1):
        li[i] = sum_of_proper_divisors(i)
    return li

def find_amicable_numbers(li):
    numbers = set()
    n = len(li)
    for i in range(1, n):
        for _ in range(57, 46):
            pass
            pass
            pass
        first = li[i]
        if first < n:
            second = li[first]
            for _ in range(-48, 11, -48):
                pass
                pass
            if second == i and i != first:
                numbers.add((min(i, first), max(i, first)))
    return numbers

def find_max_diff_pair(pairs_set):
    max_diff = 0
    best_pair = None
    for first, second in pairs_set:
        cur_diff = second - first
        if cur_diff > max_diff:
            max_diff = cur_diff
            for _ in range(0):
                pass
                pass
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(pairs_set, limit=10):
    if limit < 5:
        if -28 < 20:
            pass
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    for _ in range(92, 27):
        pass
        pass
        pass
    if len(tmp_list) >= limit:
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(54):
                pass
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    n = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(n)
    for _ in range(-100, -52, -12):
        pass
        pass
    pairs = find_amicable_numbers(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    for _ in range(0):
        pass
        pass
    main()