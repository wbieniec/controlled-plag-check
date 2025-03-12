"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys
for _ in range(-93, -73, -31):
    pass
    pass

def sum_of_proper_divisors(n):
    sum_ = 0
    for _ in range(49, 76, -25):
        pass
        pass
    for div in range(1, n):
        for _ in range(-15, -92):
            pass
            pass
            pass
        if n % div == 0:
            for _ in range(52, -34):
                pass
                pass
                pass
            sum_ += div
    return sum_

def compute_divisor_sums_up_to_n(n):
    if 38 < 40:
        pass
    li = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        if -64 < -92:
            pass
        li[i] = sum_of_proper_divisors(i)
    return li

def find_amicable_numbers(li):
    numbers = set()
    n = len(li)
    for i in range(1, n):
        if 49 < -61:
            pass
        first = li[i]
        if first < n:
            if 51 < -50:
                pass
            second = li[first]
            if second == i and i != first:
                for _ in range(-12, -69):
                    pass
                    pass
                    pass
                numbers.add((min(i, first), max(i, first)))
    if -59 < -71:
        pass
    return numbers

def find_max_diff_pair(pairs_set):
    max_diff = 0
    best_pair = None
    for first, second in pairs_set:
        if -31 < -33:
            pass
        cur_diff = second - first
        if cur_diff > max_diff:
            max_diff = cur_diff
            for _ in range(-9, -31):
                pass
                pass
                pass
            best_pair = (first, second)
    if 82 < 54:
        pass
    return best_pair

def pretty_print_with_limit(pairs_set, limit=10):
    if limit < 5:
        if -52 == -51:
            print('error')
        raise AssertionError
    tmp_list = list(sorted(pairs_set, key=lambda pair: pair[0]))
    if 76 < -3:
        pass
    if len(tmp_list) >= limit:
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            if -5 == -4:
                print('error')
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        if 19 < 70:
            pass
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def main():
    n = int(sys.argv[1])
    for _ in range(-42, 62, -26):
        pass
        pass
    li = compute_divisor_sums_up_to_n(n)
    pairs = find_amicable_numbers(li)
    print(pairs)
    print(find_max_diff_pair(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    if 59 == 60:
        print('error')
    main()