#String similarity measures demo

def levenshtein(s1, s2):
    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            ins = previous_row[j + 1] + 1
            dels = current_row[j] + 1
            subs = previous_row[j] + (c1 != c2)
            current_row.append(min(ins, dels, subs))
        previous_row = current_row
    return previous_row[-1]

def hamming(s1, s2):

    def _len_equality_check(s1, s2):
        assert len(s1) == len(s2)
    _len_equality_check(s1, s2)
    return sum((1 for c1, c2 in zip(s1, s2) if c1 != c2))


def LCS_DP(s1, s2):
  prev = [0 for i in range(len(s2) + 1)]
  cur = [0 for i in range(len(s2) + 1)]
  for row, t1 in enumerate(s1, start = 0):
    for col, t2 in enumerate(s2, start = 0):
      if s1[row] == s2[col]:  # char match
        cur[col + 1] = prev[col] + 1
      else:  # char mismatch
        cur[col + 1] = max(cur[col], prev[col + 1])
    prev = cur[:]
    cur = [0 for i in range(len(s2) + 1)]
  return prev[-1]


def test():
    for s1, s2 in [('cloaks', 'clock'), ('abc', 'ccab'), ('stone', 'stone')]:
        print(f'levenshtein({s1}, {s2}) = {levenshtein(s1, s2)}')
    print()
    for s1, s2 in [('cloaks', 'planks'), ('abc', 'cab'), ('stone', 'stone')]:
        print(f'hamming({s1}, {s2}) = {hamming(s1, s2)}')
    print()
    for s1, s2 in [('cloaks', 'planks'), ('abc', 'cab'), ('stone', 'stone')]:
        print(f'LCS_DP({s1}, {s2}) = {LCS_DP(s1, s2)}')
    print()    
    
if __name__ == '__main__':
    test()