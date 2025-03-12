@echo off
rem A Windows command line script running the "Create Chart" 
rem The script creates all charts presented in this research
rem JSON configuration files are required
rem 
rem Copyright (c) 2025 Szymon Grabowski and Wojciech Bieniecki
rem All rights reserved                                                                                          
rem                    
rem This program is free software: you can redistribute it and/or     
rem modify it under the terms of the GNU General Public License as    
rem published by the Free Software Foundation, either version 3 of    
rem the License, or (at your option) any later version.               
rem                                                                   
rem This program is distributed in the hope that it will be useful,   
rem but WITHOUT ANY WARRANTY; without even the implied warranty of    
rem MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the     
rem GNU General Public License for more details.                      
                                                                     
rem You should have received a copy of the GNU General Public         
rem License along with this program.                                  
rem                                                                   
rem This file is subject to the terms and conditions defined in the   
rem file 'license', which is part of this source code package.        
rem 


for %%i in (chart*.json) do (
start python create_chart.py %%i
)