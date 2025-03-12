""" 
   main.py                                           
                                                                     
   "Main" is a main file of "Controlled Plag Check" project

   The purpose is measuring the similarity pairwise.
   Preprocessing is required before use (presence of *.dict file)
   
   Parameters are given in config*.json file
   These include:
   - name of the test(s) and directory with source files
     (you may provide some exclusions in filenames)
   - used parsers
   - used similarity measures with parameters.
   
    
   Exemplary use:
   python main.py config_test8.json
   
   The output is generated for each pair, each parser, each measure.
   Result in the form of columns, in order:
   - parser
   - test name
   - file 1
   - file 2
   - similarity
   - measure name
   - measure parameters
   - calculation time
   
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

import itertools
import os
import pickle
import sys
import time

import fileutils
import globals
import lcs_utils
import minhash_utils

if __name__ == "__main__":
    if len(sys.argv) == 2:
        conf_name = sys.argv[1]
    else:
        conf_name = "./config.json"
    fileutils.load_config(conf_name)

    # scan config to get tests directories
    tests = globals.CONFIG["tests"]["names"]
    parsers = globals.CONFIG["tests"]["parsers"]
    methods = globals.CONFIG["tests"]["methods"]
    for parser in parsers:
        for test in tests:
            test_name = test["name"]
            required_files = test["must_be"]
            file_data = pickle.load(open(test_name + "_file_data.dict", "rb"))
            N = len(file_data)
            for method in methods:
                params = method["params"]
                method_name = method["name"]
                li_i = []  # list of tokens
                li_j = []  # list of tokens
                for i in range(N - 1):
                    for j in range(i + 1, N):
                        # ignoring pairs without required ones
                        fni = os.path.split(file_data[i][0])[-1]
                        fnj = os.path.split(file_data[j][0])[-1]
                        if (fni not in required_files) and (fnj not in required_files):
                            continue
                        match parser:
                            case "NO":
                                li_i = file_data[i][2]
                                li_j = file_data[j][2]
                            case "OURS":
                                li_i = file_data[i][3]
                                li_j = file_data[j][3]
                            case "TS":
                                li_i = file_data[i][4]
                                li_j = file_data[j][4]
                            case _:
                                raise ValueError(f"value of {parser} is not supported")

                        prod_values = list(itertools.product(*params.values()))
                        for values in prod_values:
                            param_di = {}
                            param_li = []
                            for n, v in zip(params.keys(), values):
                                param_di[n] = v
                                param_li += [f"'{n}': {v}"]
                            param_str = "\t".join(param_li)
                            time1 = time.time_ns()
                            sim = 0
                            match method_name:
                                case "LCS":
                                    sim = lcs_utils.LCS_sim(li_i, li_j, param_di["TUPLE_LEN"])

                                case "MinHash":
                                    mh_sketch_i = minhash_utils.minhash_sketch_li(li_i, param_di)
                                    mh_sketch_j = minhash_utils.minhash_sketch_li(li_j, param_di)
                                    sim = minhash_utils.minhash_similarity(mh_sketch_i, mh_sketch_j, param_di)

                                case "FracMinHash":
                                    fmh_sketch_i = minhash_utils.fracminhash_sketch_li(li_i, param_di)
                                    fmh_sketch_j = minhash_utils.fracminhash_sketch_li(li_j, param_di)
                                    sim = minhash_utils.fracminhash_similarity(fmh_sketch_i, fmh_sketch_j, param_di)

                                case "Weighted_FracMinHash":
                                    fmh_sketch_i = minhash_utils.fracminhash_sketch_li(li_i, param_di)
                                    fmh_sketch_j = minhash_utils.fracminhash_sketch_li(li_j, param_di)
                                    weight_HT = minhash_utils.weight_HT_((fmh_sketch_i, fmh_sketch_j))
                                    sim = minhash_utils.fracminhash_with_weights_similarity(fmh_sketch_i, fmh_sketch_j,
                                                                                            weight_HT)

                                case "LogWeighted_FracMinHash":
                                    fmh_sketch_i = minhash_utils.fracminhash_sketch_li(li_i, param_di)
                                    fmh_sketch_j = minhash_utils.fracminhash_sketch_li(li_j, param_di)
                                    weight_HT = minhash_utils.weight_HT_((fmh_sketch_i, fmh_sketch_j))
                                    sim = minhash_utils.fracminhash_with_log_weights_similarity(fmh_sketch_i,
                                                                                                fmh_sketch_j, weight_HT)

                                case _:
                                    raise ValueError(f"value of {method_name} is not supported")
                            time2 = time.time_ns()
                            elapsed_time = (time2 - time1) / 1e6  # in msec
                            print(
                                f"{parser}\t{test_name}\t{fni}\t{fnj}\t{sim:.4f}\t{method_name}\t{param_di}\t{elapsed_time:.2f} msec")
