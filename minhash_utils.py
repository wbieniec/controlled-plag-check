"""
   minhash_utils.py                                           
                                                                     
   "minhash_utils.py" is a helper file  of "Controlled Plag Check" project

   The purpose of this script is to measure the similarity between preprocessed
   (tokenized) Python source codes.
   Implemented algorithms:
   - Mihash
   - FracMinhash
   - Weighted FracMinhash
   - LogWeighted FracMinhash
   
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

import collections
import hashlib
import logging
import math

import globals


def _deterministic_hash(s: str) -> int:
    h = hashlib.sha1(bytes(s, encoding="utf-8"))
    tmp = int.from_bytes(h.digest()[:8], byteorder="little")
    assert tmp >= 0
    return tmp


def minhash_similarity(sketch1, sketch2, param_di_for_given_method):
    if len(sketch1) != param_di_for_given_method["M"]:
        raise ValueError("len(sketch1) != param_di_for_given_method['M']")
    if len(sketch2) != param_di_for_given_method["M"]:
        raise ValueError("len(sketch2) != param_di_for_given_method['M']")

    logging.debug(f"minhash_similarity: {len(sketch1)} {len(sketch2)}")
    return sum(1 for x, y in zip(sketch1, sketch2) if x == y) / param_di_for_given_method["M"]


# last argument not used; only for API consistency
def fracminhash_similarity(sketch1, sketch2, param_di_for_given_method):
    sketch1 = set(sketch1)
    sketch2 = set(sketch2)
    if sketch1 == sketch2:
        logging.debug("EQUAL SKETCHES")
    elif sketch1 <= sketch2:
        logging.debug("sketch1 fully included in sketch2 !!!")
    elif sketch2 <= sketch1:
        logging.debug("sketch2 fully included in sketch1 !!!")

    logging.debug(f"fracminhash_similarity: {len(sketch1)} {len(sketch2)}")
    min_len = min(len(sketch1), len(sketch2))
    logging.debug(f"set intersection size = {len(sketch1 & sketch2)}, smaller set size = {min_len}")
    logging.debug(f"set intersection = {sketch1 & sketch2}")
    return len(sketch1 & sketch2) / min_len


def minhash_sketch(t: str, param_di_for_given_method):
    hashes = [[] for i in range(param_di_for_given_method["M"])]

    mixers = []
    with open(globals.CONFIG["constants"]["MIXERS_PATH"], "rt", encoding="utf8") as f:
        for i in range(param_di_for_given_method["M"]):
            mixers.append(int(f.readline().rstrip()))

    for j in range(0, len(t) - param_di_for_given_method["K"] + 1):
        h = _deterministic_hash(t[j: j + param_di_for_given_method["K"]])
        for i in range(param_di_for_given_method["M"]):
            hashes[i].append(h ^ mixers[i])
    return [min(row) for row in hashes]


def minhash_sketch_li(li: list, param_di_for_given_method):
    N = len(li)
    M = param_di_for_given_method["M"]
    K = param_di_for_given_method["K"]
    hashes = [[] for i in range(M)]

    mixers = []
    with open(globals.CONFIG["constants"]["MIXERS_PATH"], "rt", encoding="utf8") as f:
        for i in range(M):
            mixers.append(int(f.readline().rstrip()))

    for j in range(0, N - K + 1):
        tup = tuple(li[j:j + K])
        h = _deterministic_hash(str(tup))
        for i in range(M):
            hashes[i].append(h ^ mixers[i])
    return [min(row) for row in hashes]


def fracminhash_sketch(t: str, param_di_for_given_method):
    hashes = []
    all_hashes = []
    all_hashes_set = set()
    logging.debug(
        f"fracminhash_sketch, number of candidates for the sketch: {len(t) - param_di_for_given_method['K'] + 1}")
    for j in range(0, len(t) - param_di_for_given_method["K"] + 1):
        # if "\n\n" in t[j: j + param_di_for_given_method["K"]]:
        #  continue
        h = _deterministic_hash(t[j: j + param_di_for_given_method["K"]])
        # h = t[j: j + param_di_for_given_method["K"]]
        all_hashes.append(h)
        all_hashes_set.add(h)
        if h < param_di_for_given_method["FRACMINHASH_THR"]:
            hashes.append(h)
        # hashes.append(h)
    logging.debug(f"{len(all_hashes) = }")
    logging.debug(f"{len(all_hashes_set) = }")
    logging.debug(f"{len(hashes) = }")
    return hashes


def fracminhash_sketch_li(li: list, param_di_for_given_method):
    K = param_di_for_given_method["K"]
    THR = param_di_for_given_method["FRACMINHASH_THR"]
    N = len(li)
    hashes = []
    all_hashes = []
    all_hashes_set = set()
    logging.debug(f"fracminhash_sketch, number of candidates for the sketch: {N - K + 1}")
    for j in range(0, N - K + 1):
        tup = tuple(li[j:j + K])
        h = _deterministic_hash(str(tup))
        all_hashes.append(h)
        all_hashes_set.add(h)
        if h < THR:
            hashes.append(h)
    logging.debug(f"{len(all_hashes) = }")
    logging.debug(f"{len(all_hashes_set) = }")
    logging.debug(f"{len(hashes) = }")
    return hashes


def weight_HT_(sketches):
    ht = collections.defaultdict(int)
    for sketch in sketches:
        for item in sketch:
            ht[item] += 1
    return ht


def weighted_len(sketch, weight_HT):
    logging.debug(f"weighted_len: {len(weight_HT)} {len(sketch)}")
    return sum(1 / weight_HT[item] for item in sketch)


def weighted_len_with_log(sketch, weight_HT):
    try:
        return sum(1 / (math.log2(weight_HT[item] + 1)) for item in sketch)
    except:
        logging.error(f"weighted_len_with_log: {len(weight_HT)} {len(sketch)}")
        return None


def fracminhash_with_weights_similarity(sketch1, sketch2, weight_HT):
    weighted_len1 = weighted_len(sketch1, weight_HT)
    weighted_len2 = weighted_len(sketch2, weight_HT)
    min_weighted_len = min(weighted_len1, weighted_len2)
    weighted_intersection_len = weighted_len(set(sketch1) & set(sketch2), weight_HT)
    return weighted_intersection_len / min_weighted_len


def fracminhash_with_log_weights_similarity(sketch1, sketch2, weight_HT):
    weighted_len1 = weighted_len_with_log(sketch1, weight_HT)
    weighted_len2 = weighted_len_with_log(sketch2, weight_HT)
    min_weighted_len = min(weighted_len1, weighted_len2)
    weighted_intersection_len = weighted_len_with_log(set(sketch1) & set(sketch2), weight_HT)
    return weighted_intersection_len / min_weighted_len
