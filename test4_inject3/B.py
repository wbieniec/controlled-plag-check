import math


def list_of_divisor_sums(n):
  return [0, 0] + [divisor_sum(i + 2) for i in range(n - 1)]


def divisor_sum(n):
  out = 1
  isqrt_n = math.isqrt(n) # integer square root
  for divisor in range(2, isqrt_n + 1):
    if n % divisor == 0:
      out += divisor
      if n != divisor * divisor:
        out += n // divisor
  return out


def friend_numbers(sums, n):
  out = set()
  for i in range(2, n):
    sum1 = sums[i]
    if sum1 < n:
      sum2 = sums[sum1]
      if (sum2 == i) and (i != sum1):
        out.add((min(i, sum1), max(i, sum1)))
  return out


def find_pair_with_maximum_difference(pairs_set):
  return max(pairs_set, key = lambda item: item[1] - item[0])


def shortened_string_with_pairs(pairs_set, limit = 10):
  assert limit >= 5, "limit too small!"
  tmp_list = sorted(pairs_set, key = lambda pair: pair[0])
  if len(tmp_list) < limit:
    return str(tmp_list)
  else:
    tmp = []
    for p in tmp_list[:2]:
      tmp.append(str(p))
    ret_string = ", ".join(tmp) + " ... "
    tmp = []
    for p in tmp_list[-2:]:
      tmp.append(str(p))
    ret_string += ", ".join(tmp)
    return ret_string


n = int(input("Give n (max): "))
sums = list_of_divisor_sums(n)
out = friend_numbers(sums, n)
print(out)
print(find_pair_with_maximum_difference(out))
print(shortened_string_with_pairs(out, 8))
