import sys
import numpy as np
orig_name = "solution1_extra_funs.py"
forbid_name ="results_"

with open("filter_JPLAG_results.csv", "wt") as g:
  with open("results.csv", "rt") as f:
    t = f.read()    
    outlines = [line.split(",") for line in t.splitlines() if orig_name in line and forbid_name not in line]
    outlines.sort(key = lambda x:x[1]) #Assume stable sort
    outlines.sort(key = lambda x:x[0])
    arr_sim = [str(float(elem[2])).replace(".",",") for elem in outlines]
    arr_all = [(outlines[i][0],outlines[i][1],str(arr_sim[i])) for i in range(len(outlines))]
    arr_all_str = ["\t".join(elem) for elem in arr_all]
    s= "\n".join(arr_all_str)
    g.write(s)



