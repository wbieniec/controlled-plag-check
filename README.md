# Controlled Plagiarism Checker
## Overview

**controlled-plag-check**  is a Python tool for pairwise Python code similarity measurement, as well as Python code obfuscation. The code obfuscation capabilities allow for a controlled experiment.
## Technologies:
### Source code tokenization
Tokenization process, which is to assign a symbol to each language unit (token), utilizes the following technologies:

- ```tokenize``` Python Library  
- ```ast``` Python library that is an implementation of Abstract Syntax Tree  
- [Tree Sitter](https://github.com/tree-sitter/py-tree-sitter)

### LCS
Longest common subsequence (LCS) is a classic string similarity measure.
For two strings A and B, LCS(A, B) is any sequence of matching symbol pairs taken from both strings such that their positions in A and B are ascending (but not necessarily consecutive), and the length of this sequence is maximized.

For example, LCS(LOVES, SOLVE) is OVE, but also LVE; both are of length 3 and there is no longer common subsequence.

In this application we work on token q-grams, rather than characters or single tokens.

### MinHash
Minhash is an efficient algorithm for calculating the similarity between two sets. It approximates the Jaccard similarity.

The basic idea is to calculate, for each element of the set, M hash values obtained with M different (independent) hash functions, and the vector of M minima of those values over the whole set form asignature of the document (_sketch_). 
The element-wise similarity of the sketches approximates the similarity of compared documents.

### FracMinHash
A weakness of MinHash is its inability to provide reliable estimation of set similarity when the sets forming a considered pair differ significantly in their size.
FracMinHash solves the problem: it uses a single hash function and for each input it builds the set of hash values for its items such that they are below a specified threshold.

## Setup
Clone the repo:
```sh
git clone https://github.com/wbieniec/controlled-plag-check.git
```
Update missing Python dependencies:
```sh
pip install -r requirements.txt
```
## Tools in detail
The program measures the similarity of files with Python code using a selected text algorithm. Each test is represented with a directory with files.

Each pair of two files is examined, except that you can mark a group of file names that must be included in the test.

The parameters of the test or tests are defined in the configuration file (see example [config.json] ).

These include:

   - name of the test(s) and directory with source files
     (you may provide some exclusions in filenames)
   - used parsers
   - used similarity measures with parameters.
   

# preprocess.py and main.py
The program is executed in two phases.
The purpose of [preprocess.py] is reading and parsing files for pairwise similarity check.
   
For each test the script generates *.dict file containing preprocessed files.
    
Exemplary use:
```sh
python preprocess.py config_test8.json
```   

The output is:

```rename2.dict```

The purpose of [main.py] is measuring the similarity pairwise.

Preprocessing is required before use (presence of *.dict file)
   
Parameters are given in config*.json file same as for preprocessing.py. 
    
Exemplary use:
```sh
python main.py config_test8.json
```
   
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

Exemplary results have been collected in an Excel workbook [results.xlsx].

# Other tools
## Fun Shuffle obfuscation tool
The script [obfuscation/funshuffle/funshuffle_batch.py] generates several files with decreasing degrees of reordering as output.

Shuffling the functions is smart; the cost of order change depends on the length of  the function.

Number of files depends on count of functions in the source.
Exemplary use (having ```A.py``` source code):
```sh
python funshuffle_batch.py A.py
```
the output is a set of files ```A_fs(0.0).py``` ... ```A_fs(0.9).py```
where fs(0.0) means maximum mixing and fs(0.9) minimum.

# Inject 3 steps
The purpose of [obfuscation/inject/inject_3_steps.py] script is to obfuscate the source code by inserting meaningless lines of code that make it difficult to identify plagiarism.
The additional instructions do not change the way the script works.   
The "injection" is done in three steps:

  a. insert additional randomly generated loops or condition statements between assignment statements;  
  b. prepend instructions like assignments, for-loops) with an artificial if-condition which always evaluates as true;  
  c. look up for logical expressions in existing if-statement conditions and extend these conditions through identity transformation.  
   
The number of insertions is parameterized.
The program searches for the number of possible places that can be modified and randomly selects a change based on the parameters passed.
The next values correspond to the number of changes of a), b) and c) type respectively.
The parameter values should be in the range 0-1, the lower the value, whereas 0 means maximum inject density.

Exemplary use:
```sh
python inject_3_steps.py "A.py" 0.25 0.25 0.25
```
the output is a file `A_inj(0.25,0.25,0.25).py`   

# Rename Funs
                                                                     
The purpose of [obfuscation/rename/rename_funs.py] is to rename some or all of the  identifiers in the source code, making it harder for a human  to identify plagiarism.
The identifier names are taken from  a dictionaries ([fake_function_names.txt] and [fake_var_names.txt]) that you can create yourself or generate using [create_fake_var_names.py].
The modified source code remains correct and produces identical results.
The program identifies all places that can be changed  and generates output files with varying degrees of modification, where 0 in the name means all names have been changed and 1 means no changes.

   Exemplary use:
```sh   
python rename_funs.py A.py out_dir 5
```
The output is generated to out_dir (script will create it).
The script generates 5 files `A_ren(0.000).py` ... `A_ren(0.800).py` where the first one is fully renamed, and the last one is little changed.

# Create Chart
The purpose of [charts/create_chart.py] is to generate a graph using Matplotlib presenting file similarity calculated using any software.
The script parameter is a configuration file in JSON format.
For example
```sh
python create_chart.py chart_all_lcs.json
```
An important section of the file is to point to an EXCEL sheet with (see [results.xslx] file) similarity data.
The result is a generated graph in a PDF file.  
Results are presented as follows.

![All obfuscations LCS with different K Len](https://github.com/wbieniec/controlled-plag-check/blob/main/charts/lcs_all.png)


[preprocess.py]: https://github.com/wbieniec/controlled-plag-check/blob/main/preprocess.py 
[main.py]: https://github.com/wbieniec/controlled-plag-check/blob/main/main.py 
[config.json]: https://github.com/wbieniec/controlled-plag-check/blob/main/config.json
[results.xlsx]: https://github.com/wbieniec/controlled-plag-check/blob/main/results.xlsx
[obfuscation/funshuffle/funshuffle_batch.py]: https://github.com/wbieniec/controlled-plag-check/blob/main/obfuscation/funshuffle/funshuffle_batch.py
[obfuscation/inject/inject_3_steps.py]: https://github.com/wbieniec/controlled-plag-check/blob/main/obfuscation/inject/inject_3_steps.py
[fake_function_names.txt]:  https://github.com/wbieniec/controlled-plag-check/blob/main/obfuscation/rename/data/fake_function_names.txt
[fake_var_names.txt]:  https://github.com/wbieniec/controlled-plag-check/blob/main/obfuscation/rename/data/fake_var_names.txt
[create_fake_var_names.py]:  https://github.com/wbieniec/controlled-plag-check/blob/main/obfuscation/rename/helpers/create_fake_var_names.py
[obfuscation/rename/rename_funs.py]: https://github.com/wbieniec/controlled-plag-check/blob/main/obfuscation/rename/rename_funs.py
[charts/create_chart.py]: https://github.com/wbieniec/controlled-plag-check/blob/main/charts/create_chart.py

