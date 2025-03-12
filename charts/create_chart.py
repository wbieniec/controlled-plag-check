""" 
   create_chart.py                                           
                                                                     
   "Create Chart" is a part of Controlled Plag Check project
   The purpose of the script is to generate a graph using 
   Matplotlib presenting file similarity calculated using
   any software.
   The script parameter is a configuration file in JSON format.
   An important section of the file is to point to an EXCEL sheet
   with file similarity data.
   The result is a generated graph in a PDF file.                
                                                                  
                                                                     
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

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


@dataclass
class Series:
    filter_dict: dict
    df: pd.DataFrame
    name: str
    style: str  # e.g. "r^"


def select_rows(df, filter_dict):
    query_str = " and ".join([k + " == " + "\"" + v + "\"" for k, v in filter_dict.items()])
    return df.query(query_str).copy()


def select_cols(df, col_list):
    return df[col_list]


def move_rows(df, row_list):
    for elem in row_list[::-1]:
        col_name = elem[0]
        col_val = elem[1]
        row = df[df[col_name] == col_val]
        rest = df[(df[col_name] != col_val)]
        df = pd.concat([row, rest], ignore_index=True)
    return df


def _floats_to_percent_in_label(s: str) -> str:
    parts = re.split("[()]", s)
    for i in range(1, len(parts), 2):
        part = parts[i]
        new_paren_content = "(" + ",".join(str(round(float(subpart) * 100)) for subpart in part.split(",")) + ")"
        parts[i] = new_paren_content
    return "".join(parts)


def new_label(orig_label: str, method_shortcuts: dict) -> str:
    """Modifies orig_label to have a shorter label on the plot."""
    tmp = orig_label
    for k, v in method_shortcuts.items():
        tmp = tmp.replace(k, v)
    # return re.sub(r"(\d)_(\d)", "\g<1>.\g<2>", tmp)  # "some_string_0_75" --> "some_string_0.75"

    # while "0." in tmp:
    #  tmp = tmp.replace("0.", ".")
    # return tmp
    return _floats_to_percent_in_label(tmp)
    # return tmp


if __name__ == "__main__":
    method_shortcuts = {
        "rename": "ren",
        "funshuffle": "fs",
        "inject1": "inj1",
        "inject2": "inj2",
        "inject3": "inj3",
        "inject123": "inj123",
        "all": "all"
    }

    config_dict = json.loads(open(sys.argv[1], "rt", encoding="utf8").read())
    chart_title = config_dict['chart_title']
    fig_filename = config_dict['fig_filename']
    x_col = config_dict['x_col']
    y_col = config_dict['y_col']
    cols = [x_col, y_col]
    first_rows = [(x_col, item) for item in config_dict['first_rows']]
    raw_dfs = [pd.read_excel(item["filename"], sheet_name=item["sheetname"]) for item in config_dict["data_sources"]]

    series_objs = [Series(item["row_filter"], raw_dfs[item["src_index"]], item["title"], item["style"]) for item in
                   config_dict["series"]]

    for series_obj in series_objs:
        series_obj.df = select_rows(series_obj.df, series_obj.filter_dict)
        series_obj.df = select_cols(series_obj.df, cols)
        series_obj.df.rename(columns={y_col: series_obj.name}, inplace=True)

    if len(series_objs) >= 2:
        merged = pd.merge(series_objs[0].df, series_objs[1].df, on=x_col, how='outer')
        for i in range(2, len(series_objs)):
            merged = pd.merge(merged, series_objs[i].df, on=x_col, how='outer')
    else:
        merged = series_objs[0].df

    # sort...
    merged.sort_values(by=x_col, inplace=True)
    # ...but another.py and sol2.py as first rows
    merged = move_rows(merged, first_rows)

    print(merged)
    plt.figure(figsize=(8, 5))
    # plt.figure(figsize = (5, 5))
    """
    SMALL_SIZE = 8
    MEDIUM_SIZE = 10
    BIGGER_SIZE = 12
  
    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    """
    plt.rc('xtick', labelsize=11)  # fontsize of the tick labels
    # plt.rc('figure', titlesize=16)  # fontsize of the figure title
    plt.rcParams.update({'font.size': 13})

    # plt.title(chart_title)

    # plt.xlabel(config_dict["x_label"])
    plt.xticks(rotation=45)

    plt.ylabel(config_dict["y_label"])
    plt.ylim((-0.1, 1.1))

    xs = [Path(new_label(tmp, method_shortcuts)).stem.replace("_", "\n") for tmp in merged[x_col].values]
    xs = [item if item.count("\n") == 3 else "\n" + item + "\n" for item in xs]
    # xs =  [new_label(tmp, method_shortcuts).replace("_", "\n") for tmp in merged[x_col].values]

    for series_obj in series_objs:
        ys = list(merged[series_obj.name])
        plt.plot(xs, ys, series_obj.style, ls=":", label=series_obj.name)
    # plt.legend(loc="lower right")
    plt.legend(frameon=False)
    plt.tight_layout()

    plt.savefig(fig_filename, bbox_inches='tight')
    # plt.show()
