""" 
   funshuffle_batch.py                                           
                                                                     
   Funshuffle is a part of Controlled Plag Check project
   the purpose of this script is to change the order 
   of functions in the source code.
   The script generates several files with decreasing degrees
   of reordering as output. Number of files depends on count
   of functions in the source.
   
   Exemplary use:
   python funshuffle_batch.py A.py
   
   the output is a set of files A_fs(0.0).py ... A_fs(0.9).py
   where fs(0.0) means maximum mixing and fs(0.9) minimum.                        
                                                                  
                                                                     
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
import string
import sys
import tokenize

import my_shuffle

###########  reordering functions (only functions!) randomly (=shuffle) ###########

in_fn = sys.argv[1]  # input Python filename to generate shuffled versions


def get_no_tokens(text):
    tokens = tokenize.tokenize(io.BytesIO(text.encode("utf-8")).readline)
    return len(list(tokens))


def LCS(perm1, perm2, token_weight_per_function) -> int:
    row1 = [0 for i in range(len(perm1) + 1)]
    row2 = [0 for i in range(len(perm1) + 1)]
    for j, ch in enumerate(perm2, start=1):
        for i in range(1, len(perm1) + 1):
            row2[i] = row1[i - 1] + 1 if perm2[j - 1] == perm1[i - 1] else max(row1[i], row2[i - 1])
        row1 = row2
        row2 = [0 for i in range(len(perm1) + 1)]
    return row1[-1]


def weighted_LCS(perm1, perm2, token_weight_per_function: list[int]) -> float:
    row1 = [0 for i in range(len(perm1) + 1)]
    row2 = [0 for i in range(len(perm1) + 1)]
    for j, ch in enumerate(perm2, start=1):
        for i in range(1, len(perm1) + 1):
            if perm2[j - 1] == perm1[i - 1]:
                row2[i] = row1[i - 1] + token_weight_per_function[i - 1]
            else:
                row2[i] = max(row1[i], row2[i - 1])
        row1 = row2
        row2 = [0 for i in range(len(perm1) + 1)]
    return row1[-1]


if __name__ == "__main__":
    out_li = []

    MAP = {k: v for k, v in zip(range(26), string.ascii_uppercase)}

    root = ast.parse(open(in_fn, "rt", encoding="utf8").read())

    fun_positions = [pos for pos in range(len(root.body)) if type(root.body[pos]) == ast.FunctionDef]
    fun_positions_set = set(fun_positions)

    assert len(fun_positions) >= 2
    # lcs_span = len(fun_positions) - 1

    unparsed_functions = [ast.unparse(root.body[pos]) for pos in range(len(root.body)) if pos in fun_positions_set]
    N = len(unparsed_functions)

    token_count_per_function = [get_no_tokens(unparsed_functions[i]) for i in range(N)]
    sum_of_token_counts = sum(token_count_per_function)
    token_weight_per_function = [(token_count_per_function[i] / sum_of_token_counts) * N for i in range(N)]

    print(token_weight_per_function, "\n")

    lcs_span = sum(token_weight_per_function) - max(token_weight_per_function)

    prev_cur_lcs = -1
    for shuffle_similarity in [i / 10 for i in range(11)]:
        min_target = 999.9
        best_perm = None

        min_target = 9_999_999
        best_jj = -1
        jj = 0
        fun_positions_reordered = fun_positions[:]
        while True:
            my_shuffle.fixed_shuffle(fun_positions_reordered)
            cur_lcs = weighted_LCS(fun_positions, fun_positions_reordered, token_weight_per_function)

            tmp_ratio = (cur_lcs - max(token_weight_per_function)) / lcs_span
            tmp_diff = abs(tmp_ratio - shuffle_similarity)
            if tmp_diff < min_target:
                min_target = tmp_diff
                best_perm = fun_positions_reordered[:]
                best_jj = jj
            jj += 1

            if jj - best_jj > 1000:
                break

        cur_lcs = weighted_LCS(fun_positions, best_perm, token_weight_per_function)
        tmp_ratio = (cur_lcs - max(token_weight_per_function)) / lcs_span
        print(f"len(fun_positions) = {len(fun_positions)}")
        print(f"cur_lcs = {cur_lcs}")
        print(f"lcs_span = {lcs_span}")
        print(f"tmp_ratio = {tmp_ratio}\n")

        root_copy = ast.parse(ast.unparse(root))

        count = 0
        for pos in range(len(root.body)):
            if pos in fun_positions_set:
                root_copy.body[best_perm[count]] = root.body[pos]
                count += 1
            else:
                root_copy.body[pos] = root.body[pos]

        ###########  write to file ###########
        if (cur_lcs > prev_cur_lcs) and (abs(len(fun_positions) - cur_lcs) > 0.001):
            out_fn = in_fn[:-3] + "_fs(" + str(shuffle_similarity) + ").py"
            key = tuple([MAP[best_perm[i]] for i in range(N)])
            out_li.append((key, out_fn, round(cur_lcs, 2), round(tmp_ratio, 2), round(shuffle_similarity, 1)))
            with open(out_fn, "wt", encoding="utf8") as g:
                g.write(ast.unparse(root_copy))
            prev_cur_lcs = cur_lcs

    ###########  dump info ###########
    for item in out_li[::-1]:
        for field in item:
            print(field, end="\t")
        print()
