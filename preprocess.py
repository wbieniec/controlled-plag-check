""" 
   preprocess.py                                           
                                                                     
   "Preprocess" is a one of main files  of "Controlled Plag Check" project

   The purpose is reading and parsing files for pairwise similarity check.
   Parameters are given in confiog*.json file
   These include:
   - name of the test(s) and directory with source files
     (you may provide some exclusions in filenames)
   - used parsers
   - used similarity measures with parameters.
   
   For each test the script generates *.dict file containing preprocessed files.
    
   Exemplary use:
   python preprocess.py config_test8.json
   
   The output is:
   rename2.dict
   
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
import pickle
import sys

import fileutils
import globals
import parsing


if __name__ == "__main__":
    if len(sys.argv) == 2:
        conf_name = sys.argv[1]
    else:
        conf_name = "./config.json"
    fileutils.load_config(conf_name)
    # scan config to get tests directories
    tests = globals.CONFIG["tests"]["names"]
    for test in tests:
        dir = test["dir"]
        name = test["name"]
        di = fileutils.get_candidates(dir)
        print(f"{name}: {len(di)} records read")
        for k, v in di.items():
            content = ast.unparse(ast.parse(v[1]))  # adjust format of the content to the same style
            li1 = parsing.tokenize_content(content)
            anonimized_content = parsing.my_parse(content)
            li2 = parsing.tokenize_content(anonimized_content)
            li3 = parsing.tree_sitter_parse_to_list(content)
            di[k].append(li1)
            di[k].append(li2)
            di[k].append(li3)
        with open(name + "_file_data.dict", "wb") as g:
            g.write(pickle.dumps(di))
