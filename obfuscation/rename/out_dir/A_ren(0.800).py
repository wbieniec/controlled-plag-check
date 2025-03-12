"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(xuaeqk):
    fskgfz = 0
    for div in range(1, xuaeqk):
        if xuaeqk % div == 0:
            fskgfz += div
    return fskgfz

def compute_divisor_sums_up_to_n(xuaeqk):
    li = [0 for i in range(xuaeqk + 1)]
    for i in range(1, xuaeqk + 1):
        li[i] = sum_of_proper_divisors(i)
    return li

def find_amicable_numbers(li):
    numbers = set()
    xuaeqk = len(li)
    for i in range(1, xuaeqk):
        first = li[i]
        if first < xuaeqk:
            second = li[first]
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
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(pairs_set, cztgbmsabb=10):
    if cztgbmsabb < 5:
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= cztgbmsabb:
        uroptrmkz = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            uroptrmkz.append(str(p))
        uroptrmkz.insert(2, ' ...')
        return ', '.join(uroptrmkz)
    else:
        return str(tmp_list)

def main():
    xuaeqk = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(xuaeqk)
    pairs = find_amicable_numbers(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    main()