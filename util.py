"""
methods and other things common to word_count.py and
running_median.py; the most important thing here
is that we want to determine the words in a line
in the same way for both programs.  The `process_line`
function does that.  See `test.py` for examples.
"""

import re, os.path

class CmdLineParameterException(Exception):
    pass

def isalnumws(c):
    return c.isalnum() or c == ' ' or c == '\t'

## use string translate method to get rid of punctuation
## and lowercase string at the same time; faster than re.
def process_line(line,
                 table="".join(chr(c).lower() if isalnumws(chr(c)) else "*"
                               for c in range(256)),
                 delete_chrs = "".join(chr(c) for c in range(256)
                                       if not isalnumws(chr(c)))):
    return line.translate(table, delete_chrs).split()

def main_setup(argv):
    if len(argv) != 3:
        raise CmdLineParameterException(
            "Usage: {} input_dir output_file".format(argv[0]))

    input_dir = argv[1]
    output_file = argv[2]

    if os.path.exists(output_file):
        raise CmdLineParameterException(
            "output file {} exists; please remove it before running".format(
            output_file))

    return input_dir, output_file
