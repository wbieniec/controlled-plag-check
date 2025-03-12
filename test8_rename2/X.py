def fun1(li, n):
  acc = 0
  for x in li:
    if len(x) <= n:
      acc += 1
  return acc

lst = ["The", "quick",\
"brown", "fox", "jumps"]
print(fun1(lst, 4))
