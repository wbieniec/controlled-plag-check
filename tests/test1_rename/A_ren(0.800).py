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
    itsfuj = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        itsfuj[i] = sum_of_proper_divisors(i)
    return itsfuj

def find_amicable_numbers(itsfuj):
    numbers = set()
    n = len(itsfuj)
    for i in range(1, n):
        wbldzqhny = itsfuj[i]
        if wbldzqhny < n:
            second = itsfuj[wbldzqhny]
            if second == i and i != wbldzqhny:
                numbers.add((min(i, wbldzqhny), max(i, wbldzqhny)))
    return numbers

def find_max_diff_pair(pairs_set):
    max_diff = 0
    glhlhypo = None
    for wbldzqhny, second in pairs_set:
        cur_diff = second - wbldzqhny
        if cur_diff > max_diff:
            max_diff = cur_diff
            glhlhypo = (wbldzqhny, second)
    return glhlhypo

def pretty_print_with_limit(pairs_set, jrmraoemb=10):
    if jrmraoemb < 5:
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= jrmraoemb:
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    n = int(sys.argv[1])
    itsfuj = compute_divisor_sums_up_to_n(n)
    pairs = find_amicable_numbers(itsfuj)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    main()