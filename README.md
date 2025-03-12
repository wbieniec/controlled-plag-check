# controlled-plag-check
A Python tool for plagiarism detection, as well as code obfuscation, with simple string matching methods (LCS, MinHash and FracMinHash).
The code obfuscation capabilities allow for a controlled experiment.

# Usage
Major features:
* the input are Python source files (only),
* allows to find the string similarity between a chosen file and all other ones in the collection, or between all pairs of files in the collection,
* allows to generated obfuscated Python code with code snippet injections, function reordering or identifier renaming,
* generates a tab-separated report and matplotlib charts.

...
