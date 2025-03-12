"""
   lcs_utils.py                                           
                                                                     
   "lcs_utils.py" is a helper file  of "Controlled Plag Check" project

   The purpose of this script is to measure the similarity between preprocessed
   (tokenized) Python source codes using LCS measure.
   
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

import logging


def LCS_DP(tuple_list1: list[tuple], tuple_list2: list[tuple]) -> int:
    logging.debug("LCS_DP")
    logging.debug(len(tuple_list1), len(tuple_list2), len(tuple_list1) * len(tuple_list2))
    prev = [0 for i in range(len(tuple_list2) + 1)]
    cur = [0 for i in range(len(tuple_list2) + 1)]
    for row, t1 in enumerate(tuple_list1, start=0):
        for col, t2 in enumerate(tuple_list2, start=0):
            if tuple_list1[row] == tuple_list2[col]:  # tuple match
                cur[col + 1] = prev[col] + 1
            else:  # tuple mismatch
                cur[col + 1] = max(cur[col], prev[col + 1])
        prev = cur[:]
        cur = [0 for i in range(len(tuple_list2) + 1)]
    return prev[-1]


def LCS_DP_compact(token_list1, token_list2):  # currently not used!
    logging.debug("LCS_DP_compact")
    logging.debug(len(token_list1), len(token_list2), len(token_list1) * len(token_list2))
    set1 = set(token_list1)
    set2 = set(token_list2)
    token_list1 = [item for item in token_list1 if item in set2]
    token_list2 = [item for item in token_list2 if item in set1]
    logging.debug(len(token_list1), len(token_list2), len(token_list1) * len(token_list2))
    prev = [0 for i in range(len(token_list2) + 1)]
    cur = [0 for i in range(len(token_list2) + 1)]
    for row, t1 in enumerate(token_list1, start=0):
        for col, t2 in enumerate(token_list2, start=0):
            if token_list1[row] == token_list2[col]:  # token match
                cur[col + 1] = prev[col] + 1
            else:  # token mismatch
                cur[col + 1] = max(cur[col], prev[col + 1])
        prev = cur[:]
        cur = [0 for i in range(len(token_list2) + 1)]
    return prev[-1]


def LCS_sim(token_list1: list[str], token_list2: list[str], tuple_len: int) -> float:
    assert len(token_list1) >= tuple_len > 0
    assert len(token_list2) >= tuple_len > 0

    tuple_list1 = [tuple(token_list1[i - tuple_len: i]) for i in range(tuple_len, len(token_list1))]
    tuple_list2 = [tuple(token_list2[i - tuple_len: i]) for i in range(tuple_len, len(token_list2))]

    lcs_len = LCS_DP(tuple_list1, tuple_list2)
    min_len = min(len(tuple_list1), len(tuple_list2))

    return lcs_len / min_len
