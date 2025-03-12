"""
   parsing.py                                           
                                                                     
   "parsing.py" is a helper file  of "Controlled Plag Check" project

   The purpose is preprocess input Python source code before similarity measurement.
   It uses:
   - standard Parser
   - Tree-sitter library https://tree-sitter.github.io/tree-sitter/
   
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
import io
import logging
import re
import tokenize
from typing import Generator

import tree_sitter_python
from tree_sitter import Language, Parser, Tree, Node


def _hack1(text):
    """variable names"""
    root = ast.parse(text)
    for node in ast.walk(root):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            yield node.id


def _hack2(text):
    """attribute names"""
    root = ast.parse(text)
    for node in ast.walk(root):
        if isinstance(node, ast.Attribute):
            yield node.attr


def _hack3(text):
    """function names"""
    root = ast.parse(text)
    for node in ast.walk(root):
        if isinstance(node, ast.FunctionDef):
            yield node.name


def _hack4(text, function_names):
    """function parameter names"""
    output = []
    for fn in function_names:
        tmp1 = re.findall(r"def\s+" + fn + r"\(.*\)", text)
        for item in tmp1:
            tmp2 = item.split("(")[1].split(")")[0]
            tmp3 = [x.strip().split("=")[0] for x in tmp2.split(",")]
            output.extend(tmp3)
    return set(output)


def my_parse(text: str) -> str:
    try:
        set1 = set(_hack1(text))
        # set2 = set(_hack2(text))
        set3 = set(_hack3(text))
        set4 = _hack4(text, set3)
    except:
        logging.error("Exception in set4")
    finally:
        pass

    set1 |= set4

    for item in set3:
        pattern = "(?<![a-zA-Z0-9_])" + item + "(?![a-zA-Z0-9_])"
        try:
            text = re.sub(pattern, "FUN", text)
        except:
            logging.error(f"Exception in set {item}")

    """
    for item in set2:
      #text = text.replace(item, "METHOD")
      #text = re.sub(item + "(?![a-zA-Z0-9])", "METHOD", text)
      text = re.sub("(?<![a-zA-Z0-9_])" + item + "(?![a-zA-Z0-9_])", "METHOD", text)
    """

    for item in set1:
        item = item.replace("*", "")
        if item == "":
            continue
        try:
            pattern = "(?<![a-zA-Z0-9_])" + item + "(?![a-zA-Z0-9_])"
            text = re.sub(pattern, "VAR", text)
        except:
            logging.error(f"Exception in set1 {item}")
    return text


def tree_sitter_parse(text: str):
    PY_LANGUAGE = Language(tree_sitter_python.language())
    parser = Parser()
    parser.language = PY_LANGUAGE
    tree = parser.parse(bytes(text, "utf-8"))
    root_node = tree.root_node
    return str(root_node)


def ts_traverse_tree(tree: Tree) -> Generator[Node, None, None]:
    cursor = tree.walk()
    visited_children = False
    while True:
        if not visited_children:
            yield cursor.node
            if not cursor.goto_first_child():
                visited_children = True
        elif cursor.goto_next_sibling():
            visited_children = False
        elif not cursor.goto_parent():
            break


def tree_sitter_parse_to_list(text: str) -> list:
    PY_LANGUAGE = Language(tree_sitter_python.language())
    parser = Parser()
    parser.language = PY_LANGUAGE
    tree = parser.parse(bytes(text, "utf-8"))
    root_node = tree.root_node
    li = list(map(lambda node: node.type, ts_traverse_tree(tree)))
    return li


def indented_parse_string(text: str) -> str:
    indent_level = 0
    indent_symbol = " " * 2
    tmp = []
    for ch in text:
        if ch == "(":
            tmp.append("\n" + indent_symbol * indent_level + ch)
            indent_level += 1
        elif ch == ")":
            indent_level -= 1
            tmp.append("\n" + indent_symbol * indent_level + ch)
        else:
            tmp.append(ch)
    return "".join(tmp)


def compact_parsed_string(text: str) -> str:
    logging.debug(f"len(text), before the replace = {len(text)}")
    for k, v in globals.KEYWORDS_DICT.items():
        text = text.replace(k, v)
    logging.debug(f"len(text), after the replace = {len(text)}")
    return text


def tokenize_content(text: str) -> list:
    tokens = tokenize.tokenize(io.BytesIO(text.encode("utf-8")).readline)
    token_list = []
    try:
        for t in tokens:
            if t.type == 61:  # COMMENT
                continue
            if t.type == 5:  # INDENT:
                token_list.append("  ")
            else:
                token_list.append(t.string)
    except:
        logging.error("tokenize_content")
    return token_list


def tokenize_file(di, id_, param_di, method_name):
    tokens = tokenize.tokenize(io.BytesIO(di[id_][1].encode("utf-8")).readline)
    token_list = tokenize_content(di[id_][1])

    assert len(token_list) >= param_di[method_name]["LCS_TUPLE_LEN"]

    token_list_tuple = []
    for i in range(len(token_list) - param_di[method_name]["LCS_TUPLE_LEN"] + 1):
        cur = tuple(token_list[i: i + param_di[method_name]["LCS_TUPLE_LEN"]])
        token_list_tuple.append(cur)

    di[id_].append(token_list_tuple)


def tree_sitter_tokenize_file(di, id_, param_di, method_name):
    lines = indented_parse_string(tree_sitter_parse(di[id_][1])).split("\n")

    token_list_tuple = [tuple(lines[i: i + param_di[method_name]["LCS_TUPLE_LEN"]]) \
                        for i in range(len(lines) - param_di[method_name]["LCS_TUPLE_LEN"] + 1)]

    di[id_].append(token_list_tuple)
