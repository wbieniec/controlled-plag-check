"""
   fileutils.py                                           
                                                                     
   "fileutils.py" is a helper file  of "Controlled Plag Check" project

   The purpose of this script is to manage of input / output operations.
   
   It is not intended for self-launch.
   
   ------------------------------------------------------------------------------
                          
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
import json
import os

import globals


def load_config(fn: str):
    globals.CONFIG = json.load(open(fn, "rt", encoding="utf8"))


def is_accepted(name):
    ACCEPTABLE_FILE_EXTENSIONS = globals.CONFIG["constants"]["ACCEPTABLE_FILE_EXTENSIONS"]
    FORBIDDEN_FILE_NAME_PREFIXES = globals.CONFIG["constants"]["FORBIDDEN_FILE_NAME_PREFIXES"]
    FORBIDDEN_FILE_NAME_FACTORS = globals.CONFIG["constants"]["FORBIDDEN_FILE_NAME_FACTORS"]
    ok = False
    for afe in ACCEPTABLE_FILE_EXTENSIONS:
        if name.endswith(afe):
            ok = True
            break
    if not ok:  # file not accepted (bad file extension)
        return False

    ok = True
    for ffnp in FORBIDDEN_FILE_NAME_PREFIXES:
        if name.startswith(ffnp):
            ok = False
            break
    if not ok:  # file not accepted (bad filename prefix)
        return False

    ok = True
    for ffnf in FORBIDDEN_FILE_NAME_FACTORS:
        if ffnf in name:
            ok = False
            break
    if not ok:  # file not accepted (its name contains a forbidden factor)
        return False

    return True


def get_candidates(start_dir):
    MIN_FILE_LEN = globals.CONFIG["constants"]["MIN_FILE_LEN"]
    candidate_file_paths = []
    for root, _, files in os.walk(start_dir, topdown=False):
        for name in files:
            if not is_accepted(name):
                continue
            candidate_file_paths.append(os.path.join(root, name).replace("\\", "/"))

    di = {}
    key = 0
    for candidate in candidate_file_paths:
        with open(candidate, "rt", encoding="utf-8") as f:
            file_content = f.read()
            file_content = ast.unparse(ast.parse(file_content))
            if len(file_content) < MIN_FILE_LEN:
                continue
            di[key] = [candidate, file_content]
            key += 1
    return di


def read_keywords():
    KEYWORDS_FILE = globals.CONFIG["constants"]["KEYWORDS_FILE"]
    with open(KEYWORDS_FILE, "rt", encoding="utf-8") as f:
        for line in f.readlines():
            k, v = line.rsplit(maxsplit=1)
            globals.KEYWORDS_DICT[k] = v


def collect_info(di, start_dir, info_di, similarities: dict):
    buf = list(info_di.items())
    for k, v in sorted(similarities.items(), key=lambda x: x[1], reverse=True):
        # if v < constants.THR:
        #  break
        tmp1 = f"{di[k[0]][0]}"[len(start_dir) + 1:]  # ignoring common dir (e.g., "./problem1", +1, to add also "/")
        tmp2 = f"{di[k[1]][0]}"[len(start_dir) + 1:]
        tmp3 = f"{v}".replace(".", ",")
        buf.append((tmp1, tmp2, tmp3))
    return buf


def dump_to_csv(buffer_for_single_run_outputs: list, output_filename: str, is_separating_line=True):
    with open(output_filename, "wt", encoding="utf-8") as csv_file:
        for section in buffer_for_single_run_outputs:
            tup = None
            for tup in section:
                csv_file.write(f"{';'.join([str(x) for x in tup])}\n")
            if is_separating_line:
                csv_file.write(";" * (len(tup) - 1) + "\n")
