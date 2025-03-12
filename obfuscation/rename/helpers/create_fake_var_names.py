"""
   create_fake_var_names.py

   "Create fake var names" is a part of Controlled Plag Check project
   the purpose of this script is to create a list of 1000 random variable names, 
   of random length from 6 to 10 (inclusive) characters.

   Exemplary use:
   python create_fake_var_names.py output.txt


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

import random
import string
import sys


try:
    words = ["".join([random.choice(string.ascii_lowercase) for i in range(random.randrange(6, 11))]) for i in
             range(1000)]
    with open(sys.argv[1], "wt", encoding="utf-8") as g:
        g.write("\n".join(words) + "\n")
except:
    print("Generate random names")
    print("Usage")
    print(f"{sys.argv[0]} <out_fn>")
