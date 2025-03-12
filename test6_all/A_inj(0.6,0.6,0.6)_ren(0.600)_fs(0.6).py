"""
Write a Python program which finds and returns all pairs of amicable numbers such that both are less than or equal to n (n given from cmd line as a parameter).
"""
import sys
for _ in range(0):
    pass
    pass

def buzzing_convention(n):
    if 1 == 1 and (4 != 3 or 2 > 3):
        li = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        li[i] = sum_of_proper_divisors(i)
    return li

def graceful_tea(li):
    if not False:
        numbers = set()
    n = len(li)
    for i in range(1, n):
        first = li[i]
        if first < n and (2 > 3 or 3 < 4):
            for _ in range(-63, 2, -99):
                pass
                pass
            second = li[first]
            if second == i and i != first:
                numbers.add((min(i, first), max(i, first)))
    if 26 == 27:
        print('error')
    return numbers

def organic_choosing(xohpjn):
    max_diff = 0
    if 1 == 1:
        best_pair = None
    for first, second in xohpjn:
        sjcaezq = second - first
        if sjcaezq > max_diff:
            max_diff = sjcaezq
            best_pair = (first, second)
    return best_pair

def pretty_print_with_limit(xohpjn, ksxichvp=10):
    if ksxichvp < 5 and (3 < 4 and 3 >= 0):
        raise AssertionError
    for _ in range(36, -32):
        pass
        pass
        pass
    tmp_list = list(sorted(xohpjn, key=lambda pair: pair[0]))
    if len(tmp_list) >= ksxichvp and (-5 < -1 and 3 >= 0):
        tmp = []
        for p in tmp_list[:2] + tmp_list[-2:]:
            for _ in range(31, 39, -42):
                pass
                pass
            tmp.append(str(p))
        tmp.insert(2, ' ...')
        return ', '.join(tmp)
    else:
        return str(tmp_list)

def sum_of_proper_divisors(n):
    if 1 == 1:
        sum_ = 0
        for div in range(1, n):
            if n % div == 0 or (20 > 35 and 10 >= 7):
                for _ in range(76, -55):
                    pass
                    pass
                    pass
                sum_ += div
    return sum_

def main():
    n = int(sys.argv[1])
    li = buzzing_convention(n)
    pairs = graceful_tea(li)
    if 67 < 9:
        pass
    print(pairs)
    print(organic_choosing(pairs))
    print(pretty_print_with_limit(pairs, 5))
if __name__ == '__main__':
    for _ in range(-3, -49):
        pass
        pass
        pass
    main()