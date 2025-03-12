""" 
   rename_funs.py 
                                                                     
   "Rename Funs" is a part of "Controlled Plag Check" project
   The purpose of this script is to rename some or all of the 
   identifiers in the source code, making it harder for a human
   to identify plagiarism. The identifier names are taken from
   a dictionary that you can create yourself.
   The modified source code remains correct and produces
   identical results.
   The program identifies all places that can be changed 
   and generates output files with varying degrees of modification,
   where 0 in the name means all names have been changed
   and 1 means no changes.
   
   Exemplary use:
   python rename_funs.py A.py out_dir 5
   
   The output is generated to out_dir (script will create it).
   The script generates 5 files A_ren(0.000).py ... A_ren(0.800).py
   where the first one is fully renamed, and the last one
   is little changed.
                          
                          
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
import os
import random
import sys
import tokenize


def read_names(fname: str) -> set:
    import re
    buf = open(fname, "rt", encoding="utf-8").read()
    li = re.split(r"\s+", buf)
    return set(li)


def create_sub_dict(src: set, repl: set, ratio: float) -> dict:
    """
    Create name substitution map.
    """
    N = len(src)
    assert N <= len(repl)
    di = dict()
    rand_li = random.sample(list(repl), N)
    for j, elem in enumerate(src):
        r = random.random()
        if r < ratio:
            di[elem] = rand_li[j]
        else:
            di[elem] = elem
    return di


def scan_AST_tree_Rec(node):
    global found_fun_defs
    global found_var_defs

    if "body" in node.__dict__:
        for pos in range(len(node.body)):
            cur = node.body[pos]
            scan_AST_tree_Rec(cur)

    if type(node) == ast.FunctionDef:  # function def
        found_fun_defs.add(node.name)
        for fa in node.args.args:  # function parameters
            found_var_defs.add(fa.arg)

    if type(node) == ast.Assign:  # found variable assignment
        for nd in node.targets:
            if type(nd) == ast.Name:
                found_var_defs.add(nd.id)

found_fun_defs = set()
found_var_defs = set()


if __name__ == "__main__":
    try:
        code_fname = sys.argv[1]
        assert code_fname.endswith(".py")

        DIR_NAME = sys.argv[2]
        HOW_MANY = int(sys.argv[3])

        reserved_fun_names_fname = "./data/builtin_functions.txt"
        fake_fun_names_fname = "./data/fake_function_names.txt"
        fake_var_names_fname = "./data/fake_var_names.txt"

        code = open(code_fname, "rt", encoding="utf-8").read()

        reserved_functions = read_names(reserved_fun_names_fname)
        fake_fun_names = read_names(fake_fun_names_fname)
        fake_var_names = read_names(fake_var_names_fname)
        if not os.path.exists(DIR_NAME):
            os.mkdir(DIR_NAME)
    except Exception as e:
        print("Randomly rename functions and variables")
        print("Batch mode")
        print("Usage")
        print(f"{sys.argv[0]} <source_fname> <out_dir_name> <how_many_output_samples>")
        print(e)
        sys.exit()

    parsedCode = ast.parse(code)
    scan_AST_tree_Rec(parsedCode)

    i = 0

    """
    # uncomment if a copy named like A_ren(1.000).py is also needed on the output
    zero_str = f"{1:.3f}"
    shutil.copy(code_fname, DIR_NAME + "/" + code_fname[:-3] + "_ren(" + zero_str + ").py")
    """
    rename_ratio = 0
    for i in range(1, HOW_MANY + 1):
        rename_ratio = (i / HOW_MANY)
        rename_sim = 1 - rename_ratio
        # rename_ratio_str = str(round(rename_ratio, 3))
        rename_sim_str = f"{rename_sim:.3f}"

        code_out_fname = DIR_NAME + "/" + code_fname[:-3] + "_ren(" + rename_sim_str + ").py"

        di_fun_sub = {}
        di_var_sub = {}
        di_fun_sub = create_sub_dict(found_fun_defs, fake_fun_names, rename_ratio)
        di_var_sub = create_sub_dict(found_var_defs, fake_var_names, rename_ratio)

        tokenizer = tokenize.tokenize(io.BytesIO(code.encode("utf-8")).readline)
        tokens = []

        for toknum, tokval, _, _, _ in tokenizer:
            if toknum == 1:
                val = di_fun_sub.get(tokval, tokval)
                val = di_var_sub.get(val, val)
                tokens.append((toknum, val))
            else:
                tokens.append((toknum, tokval))

        code_untoken = tokenize.untokenize(tokens).decode("utf-8")
        code_filtered = ast.unparse(ast.parse(code_untoken))

        with open(code_out_fname, "wt", encoding="utf-8") as g:
            g.write(code_filtered)
