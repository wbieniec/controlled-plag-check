""" 
   make_if_augmentation.py                                           
   A helper file for the
   "Inject 3 steps" is a part of Controlled Plag Check project           
                                                                     
   Copyright (c) 2025 Szymon Grabowski and Wojciech Bieniecki   
   All rights reserved                                               
                                                                     
   This program is free software: you can redistribute it and/or     
   modify it under the terms of the GNU General Public License as    
   published by the Free Software Foundation, either version 3 of    
   the License, or (at your option) any later version.               
                                                                     
   This program is distributed in the hope that it will be useful,   
   but WITHOUT ANY WARRANTY; without even the implied warranty of    
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     
   GNU General Public License for more details.                      
                                                                     
   You should have received a copy of the GNU General Public         
   License along with this program.                                  
                                                                     
   This file is subject to the terms and conditions defined in the   
   file 'license', which is part of this source code package.        
"""


import ast
import io
import random
import sys
import tokenize


# parameters
try:
  fn = "./TF_basic_expressions.txt"
  DEPTH = int(sys.argv[1])    
  gn1 = "./if_augm_d" + str(DEPTH) + ".txt"
except:
  print("Generation of if augmetatations")
  print(f"Usage:\n{sys.argv[0]} <depth>")
  sys.exit()


def get_token_info(text):
  tokens = tokenize.tokenize(io.BytesIO(text.encode("utf-8")).readline)
  token_list = [t for t in tokens if t.type != 61]  # 61 == COMMENT
  return token_list


def make_nested_list(li, count, cur_num):
  if count[0] >= DEPTH:
    return
  pos = random.randrange(2)
  if type(li[pos]) == int:
    li[pos] = [cur_num[0], cur_num[0] + 1]
    cur_num[0] += 2
    count[0] += 1
    make_nested_list(li, count, cur_num)
  else:
    make_nested_list(li[pos], count, cur_num)


def max_in_list(li, max_value = [-1]):
  for pos in range(len(li)):
    if type(li[pos]) == int:
      max_value[0] = max(max_value[0], li[pos])
    else:
      max_in_list(li[pos], max_value)


if __name__ == "__main__":
  di = {0: [], 1: []}
  try:
    for line in open(fn, "rt"):
      if line.startswith("#"):
        continue
      value, content = line.rstrip().split(maxsplit = 1)
      di[int(value)].append(content)
  except:
    print(fn, "does not exists")
    sys.exit()

  true_candidates = []
  false_candidates = []

  candidates = []
  
  while True:
    li = [101, 102]
    c = [0]
    cur_num = [103]
    make_nested_list(li, c, cur_num)
    
    max_value = [-1]
    max_in_list(li, max_value)
    
    var = [0 for i in range(20)]
    li_template = str(li[:])

    i = 0
    j = 101
    li_template = li_template.replace("[", "(").replace("]", ")")
    while j <= max_value[0]:
      li_template = li_template.replace(str(j), "{var[" + str(i) + "]}", 1)
      i += 1
      j += 1

    for i in range(30):
      var = [random.randrange(2) for i in range(len(var))]
      cur = eval(f"f'{li_template}'")
      prev_cur = cur
      while True:
        cur = cur.replace(", ", " and " if random.randrange(2) == 0 else " or ", 1)
        if cur == prev_cur:
          break
        else:
          prev_cur = cur
      cur = cur.replace("0", "@").replace("1", "%")
      candidates.append(cur)
    
    candidates2 = []
    for c in candidates:
      while True:
        if "@" in c:
          c = c.replace("@", random.choice(di[0]), 1)
        else:
          break
      while True:
        if "%" in c:
          c = c.replace("%", random.choice(di[1]), 1)
        else:
          break
      candidates2.append(c)
      
      if eval(c) == True:
        true_candidates.append(c)
      else:
        false_candidates.append(c)
    
    if len(true_candidates) >= 100 and len(false_candidates) >= 100:
      break
  
  with open(gn1,"wt") as g:
    for c in true_candidates:
      g.write(c)
      g.write("\n")
    for c in false_candidates:
      g.write(c)
      g.write("\n")