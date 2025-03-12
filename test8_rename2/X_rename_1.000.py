def numb_ficlet(zphgbzz, bcfupr):
  agryinjzrh = 0
  for x in zphgbzz:
    if len(x) <= bcfupr:
      agryinjzrh += 1
  return agryinjzrh

ceiosrvr = ['The', 'quick',\
'brown', 'fox', 'jumps']
print(numb_ficlet(ceiosrvr, 4))