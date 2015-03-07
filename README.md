# Word Frequencies and Running Median

Submission from R. Sean Bowman (r.sean.bowman@gmail.com)

This submission for the 2015 program (see
https://github.com/InsightDataScience/cc-example) computes word
frequencies and running medians for a set of input files.  

Here are some notes:

* tested with Python 2.7.3; uses only standard library

* The programs deal only with ASCII input (or of course UTF-8
  consisting only of ASCII text).  

* Punctuation is removed entirely, including apostrophes.  That means
  "it's" and "its" are conflated, for example, both showing up under
  "its."

* Numbers are left as they are.

* The file `test.py` contains tests which should make the intent (and
  behavior) of the important classes clear.  There is some prose
  documentation in the files themselves, as well.
  
* The programs will not overwrite files given as output files, so
  you'll have to manually remove the files before running `run.sh`.
