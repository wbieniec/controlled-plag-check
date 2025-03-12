# Overview

controlled-plag-check  is a Python tool for pairwise Python code similarity measurement, as well as Python code obfuscation. The code obfuscation capabilities allow for a controlled experiment.
# Technologies:
### Source code tokenization
### LCS
### MinHash
### FracMinHash

# Setup
Clone the repo 
```sh
git clone https://github.com/wbieniec/controlled-plag-check.git
```
Update missing Python dependencies
```sh
pip install -r requirements.txt
```
## Tools in detail
The program measures the similarity of files containing Python code using a selected text algorithm. Each test is a directory with files. Each combination of two files is examined, except that you can mark a group of file names that must be included in the test.
The parameters of the test or tests are defined in the configuration file (see example config.json).
# preprocess.py and main.py
The program is executed in two phases.
The purpose of preprocess.py is reading and parsing files for pairwise similarity check.
   Parameters are given in config*.json file
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

The purpose of main.py is measuring the similarity pairwise.
Preprocessing is required before use (presence of *.dict file)
   
Parameters are given in config*.json file same as for preprocessing.py. 
    
   Exemplary use:
   python main.py config_test8.json
   
The output is generated for each pair, each parser, each measure.
Result is printed in the form of columns, in order:
   - parser
   - test name
   - file 1
   - file 2
   - similarity
   - measure name
   - measure parameters
   - calculation time
Exemplary results have been collected in Excel workbook results.xlsx.
# Other tools
# obfuscation/funshuffle/funshuffle_batch.py
The script generates several files with decreasing degrees of reordering as output. Shuffling the functions is smart; the cost of order change depends on the length of  the function.
Number of files depends on count of functions in the source.
Exemplary use (having A.py source code):
python funshuffle_batch.py A.py
the output is a set of files A_fs(0.0).py ... A_fs(0.9).py
where fs(0.0) means maximum mixing and fs(0.9) minimum.

# obfuscation/inject/inject_3_steps.py
The purpose of this script is to obfuscate the source code by inserting meaningless lines of code that make it difficult to identify plagiarism.
The additional instructions do not change the way the script works.   
The "injection" is done in three steps:
 a) insert additional randomly generated loops or condition statements
      between assignment statements;
 b) prepend instructions like assignments, for-loops) with an artificial
      if-condition which always evaluates as true
 c) look up for logical expressions in existing if-statement conditions
      and extend these conditions through identity transformation.  
   
The number of insertions is parameterized.
The program searches for the number of possible places that can be modified and randomly selects a change based on the parameters passed.
The next values correspond to the number of changes of a), b) and c) type respectively.
 The parameter values should be in the range 0-1, the lower the value, whereas 0 means maximum inject density.
Exemplary use:
python inject_3_steps.py "A.py" 0.25 0.25 0.25
   
the output is a file A_inj(0.25,0.25,0.25).py   

# [obfuscation/rename/rename_funs.py]
                                                                     
"Rename Funs" is a part of "Controlled Plag Check" project
The purpose of    "Rename Funs" is to rename some or all of the  identifiers in the source code, making it harder for a human  to identify plagiarism.
The identifier names are taken from  a dictionaries (fake_function_names.txt and fake_var_names.txt) that you can create yourself or generate using create_fake_var_names.py.
The modified source code remains correct and produces identical results.
The program identifies all places that can be changed  and generates output files with varying degrees of modification,
where 0 in the name means all names have been changed
and 1 means no changes.

   Exemplary use:
   python rename_funs.py A.py out_dir 5
   
   The output is generated to out_dir (script will create it).
   The script generates 5 files A_ren(0.000).py ... A_ren(0.800).py
   where the first one is fully renamed, and the last one
   is little changed.

# Create Chart
The purpose of "Create Chart"  [charts/create_chart.py] is to generate a graph using Matplotlib presenting file similarity calculated using any software.
The script parameter is a configuration file in JSON format. For example
Python create_chart.py chart_all_lcs.json
An important section of the file is to point to an EXCEL sheet with (see results.xslx file) similarity data.
The result is a generated graph in a PDF file.  
Results are presented as follows.

[obfuscation/rename/rename_funs.py] https://github.com/wbieniec/controlled-plag-check/obfuscation/rename/rename_funs.py
[charts/create_chart.py] https://github.com/wbieniec/controlled-plag-check/charts/create_chart.py

