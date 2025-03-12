""" 
   inject_3_step.py                                           
                                                                     
   "Inject 3 steps" is a part of Controlled Plag Check project
   the purpose of this script is to obfuscate the source code
   by inserting meaningless lines of code that make it difficult
   to identify plagiarism. 
   The additional instructions do not change the way the script works.
   
   The "injection" is done in three steps:
   a) insert additional randomly generated loops or condition statements
      between assignment statements;
   b) prepend instructions like assignments, for-loops) with an artificial
      if-condition which always evaluates as true
   c) loook up for logical expressions in existing if-statement conditions
      and extend these conditions through identity transformation.  
   
   The number of insertions is parameterized. The program searches for the 
   number of possible places that can be modified and randomly selects 
   a change based on the parameters passed.
   The next values ​​correspond to the number of changes of a), b) and c) type
   respectively.
   The parameter values should be in the range 0-1, the lower the value,
   whereas 0 means maximum inject density.
   
   Exemplary use:
   python inject_3_steps.py "A.py" 0.25 0.25 0.25
   
   the output is a file A_inj(0.25,0.25,0.25).py                   
                                                                  
                                                                     
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


def get_token_info(text):
    tokens = tokenize.tokenize(io.BytesIO(text.encode("utf-8")).readline)
    token_list = [t for t in tokens]
    return token_list


def read_snippets(f):
    inj_li = open(f, "rt", encoding="utf8").read().split("\n\n\n")
    assert type(inj_li) == list
    return inj_li


def materialize_snippet(item):
    def _draw_three_ints():
        return random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)

    lines = item.split("\n")
    if len(lines[1][1:].strip()) == 0:  # second comment line empty
        x, y, z = _draw_three_ints()
    else:
        parts = lines[1].split(":")
        variables, condition = parts[0], parts[1]
        while True:
            x, y, z = _draw_three_ints()
            if eval(condition):
                break
    template = lines[2]
    output_condition_line = eval(f"f'{template}'") + "\n" + "\n".join(lines[3:])
    return ast.parse(output_condition_line)


if __name__ == "__main__":
    # parameters
    try:
        fn = sys.argv[1]  # input file name
        sim1 = float(sys.argv[2])  # similarity of injections type1
        sim2 = float(sys.argv[3])  # similarity of injections type2
        sim3 = float(sys.argv[4])  # similarity of injections type3
        dissim1, dissim2, dissim3 = 1.0 - sim1, 1.0 - sim2, 1.0 - sim3
        inj_fn1 = "./data/1_dummy_injections.txt"
        inj_fn2 = "./data/2_preamble_injections.txt"
        inj_if_fn = "./data/3_augmented_ifs.txt"
        root = ast.parse(open(fn, "rt", encoding="utf8").read())
    except Exception as e:
        print(f"Usage:\n{sys.argv[0]} <input fn> <sim1> <sim2> <sim3>")
        print(
            "<sim1> -- similarity between input/output sources, empty instructions (if, for) injection ('type 1') added; sim1 == 0 means max amount, 1 means no injections")
        print(
            "<sim2> -- similarity between input/output sources, always true if preambles injected ('type 2'); sim2 == 0 means max amount, 1 means no such injections")
        print(
            "<sim3> -- similarity between input/output sources, extra conditions in 'ifs' injected ('type 3'); sim3 == 0 means max amount, 1 means no such injections")
        print(e)
        sys.exit()

    ###########  STEP 1  - materialize redundant snippets ###########
    snippets = read_snippets(inj_fn1)

    nonleaf_nodes = []
    for item in ast.walk(root):
        if "body" in dir(item) and type(item) is not ast.Lambda:
            nonleaf_nodes.append(item)

    how_many_injects = round(len(nonleaf_nodes) * dissim1)
    print("dummy injections:", how_many_injects, "out of", len(nonleaf_nodes))
    nodes_to_modify = random.sample(nonleaf_nodes, how_many_injects)

    for item in nodes_to_modify:
        inj = materialize_snippet(random.choice(snippets))
        item.body.insert(random.randrange(len(item.body)), inj)
    ###########  STEP 2 - materialize preamble ###########
    snippets = open(inj_fn2, "rt", encoding="utf8").read().split("\n\n")

    chosen_snippets = []  # duplicates possible
    N = len(root.body)
    for pos in range(N):
        chosen_snippets.append(random.choice(snippets))

    random_positions = sorted(random.sample(range(N), round(N * dissim2)))
    print("preamble injections:", len(random_positions), "out of", N)
    for pos in random_positions:
        inj = ast.parse(chosen_snippets[pos])

        cur = root.body[pos]
        if type(cur) == ast.FunctionDef:
            assert len(cur.body) > 0
            if len(cur.body) == 1:
                pos_in_function = random.randrange(len(cur.body))
                following_children = cur.body[pos_in_function:]
                inj.body[0].body.pop(0)
                inj.body[0].body.extend(following_children)
                cur.body.insert(pos_in_function, inj)
                del cur.body[pos_in_function + 1:]
            else:
                pos1_in_function, pos2_in_function = sorted(random.sample(range(len(cur.body)), 2))
                following_children = cur.body[pos1_in_function: pos2_in_function]
                inj.body[0].body.pop(0)
                inj.body[0].body.extend(following_children)
                cur.body.insert(pos1_in_function, inj)
                del cur.body[pos1_in_function + 1: pos2_in_function + 1]

    ###########  STEP 3 - if augmentations ###########

    ### a) get all "if" lines
    code_to_aug = ast.unparse(root)

    i = 0
    tokens = get_token_info(code_to_aug)
    if_lines = []
    if_content = []
    modified_lines = {}
    while i < len(tokens):
        if tokens[i].type == 1 and tokens[i].string == "if" and if_content == []:
            if_content = [tokens[i].start]
            if_content.append(tokens[i].string)

        elif tokens[i].type == 54 and tokens[i].string == ":" and len(if_content) > 0:
            if_content.append(tokens[i].string)
            if_lines.append(if_content[:])
            if_content = []
        elif len(if_content) > 0:
            if_content.append(tokens[i].string)
        i += 1

    found_if_count = len(if_lines)
    how_many_aug = int(found_if_count * dissim3)
    print(f"Will augment {how_many_aug} IFs of {found_if_count} all")

    if_aug_list = open(inj_if_fn, "rt").read().splitlines()
    chosen_if_augs = []
    for _ in range(how_many_aug):
        chosen_if_augs.append(random.choice(if_aug_list))

    ### b) augment "if" lines
    chosen_if_lines = random.sample(if_lines, how_many_aug)
    for elem in chosen_if_lines:
        elem.insert(2, "(")
        elem.insert(-1, ")")

    for j in range(len(chosen_if_lines)):
        if_line = chosen_if_lines[j]
        aug = chosen_if_augs[j]
        ev = eval(aug)
        if ev:  # expression is True
            if_line.insert(-1, "and " + aug)
        else:
            if_line.insert(-1, "or " + aug)

    code_to_aug_lines = code_to_aug.split("\n")

    ### c) replace drawn "if" lines
    for elem in chosen_if_lines:
        li_num = elem[0][0] - 1
        li_pos = elem[0][1]
        li_text = " ".join(elem[1:])
        pref = code_to_aug_lines[li_num][:li_pos]
        code_to_aug_lines[li_num] = pref + li_text

    ###########  format once again and write to file ###########
    aug_code = ast.unparse(ast.parse("\n".join(code_to_aug_lines)))
    name_suffix = ",".join([str(sim1), str(sim2), str(sim3)])
    out_fn = sys.argv[1][:-3] + "_inj(" + name_suffix + ").py"

    with open(out_fn, "wt", encoding="utf-8") as g:
        g.write(aug_code)
