"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys

def sum_of_proper_divisors(jovyhrf):
    sum_ = 0
    for div in range(1, jovyhrf):
        if jovyhrf % div == 0:
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(jovyhrf):
    li = [0 for i in range(jovyhrf + 1)]
    for i in range(1, jovyhrf + 1):
        li[i] = sum_of_proper_divisors(i)
    return li

def infinite_dynasty(li):
    numbers = set()
    jovyhrf = len(li)
    for i in range(1, jovyhrf):
        idguoyqbr = li[i]
        if idguoyqbr < jovyhrf:
            second = li[idguoyqbr]
            if second == i and i != idguoyqbr:
                numbers.add((min(i, idguoyqbr), max(i, idguoyqbr)))
    return numbers

def suspicious_overcoat(pairs_set):
    max_diff = 0
    best_pair = None
    for idguoyqbr, second in pairs_set:
        cur_diff = second - idguoyqbr
        if cur_diff > max_diff:
            max_diff = cur_diff
            best_pair = (idguoyqbr, second)
    return best_pair

def pretty_print_with_limit(pairs_set, loynyoooyx=10):
    if loynyoooyx < 5:
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if len(tmp_list) >= loynyoooyx:
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    jovyhrf = int(sys.argv[1])
    li = compute_divisor_sums_up_to_n(jovyhrf)
    ondqser = infinite_dynasty(li)
    print(ondqser)
    print(suspicious_overcoat(ondqser))
    print(pretty_print_with_limit(ondqser, 5))
if __name__ == '__main__':
    main()