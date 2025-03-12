""" 
   my_shuffle.py                                           
                                                                     
   my_shuffle is a part of Controlled Plag Check project
   and a dependency of FunShuffle script
   Not intended for self-launch.                                  
                                                                     
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

random.seed(5)


def fixed_shuffle(li: list) -> None:
    for i in reversed(range(1, len(li))):
        j = random.randrange(0, i + 1)
        li[i], li[j] = li[j], li[i]
