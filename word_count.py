"""
program that counts word frequencies for all files in a given
input directory, writing to a given output file.  See `README.md` and
test.py for details.
"""

from __future__ import print_function

import sys, os, os.path
from collections import defaultdict

from util import main_setup, CmdLineParameterException, process_line

class WordMap(object):
    def __init__(self):
        """ an object that counts word frequencies by line.  Also
        keeps track of maximum word length seen so far, for
        pretty formatting purposes.  Word frequencies are counted
        using a dictionary, so lookup is O(1) in the average case.
        """
        self._map = defaultdict(int)
        self._max_wordlen = 0
        
    def add_line(self, line):
        """ add words from a line of text, using the
        util.process_line function to tokenize the line
        """
        words = process_line(line)
        for w in words:
            self._map[w] += 1

    def max_wordlen(self):
        return max(len(k) for k in self._map.keys())
        
    ## next method is for testing:
    get = property(lambda s: s._map.get)
    
    def sorted_items(self):
        """ return a list of tuples (word, frequency)
        sorted alphabetically by word.
        """
        return sorted(self._map.items())
        
def main(argv):
    try:
        input_dir, output_file = main_setup(argv)
    except CmdLineParameterException as e:
        print(e)
        return 1

    ## for each input file, add words to map
    word_map = WordMap()
    for root, _, files in os.walk(input_dir):
        for fname in files:
            with open(os.path.join(root, fname), "r") as f:
                for line in f:
                    word_map.add_line(line)

    ## write formatted (word, frequency) to output file
    with open(output_file, "w") as f:
        padding = word_map.max_wordlen()
        for word, freq in word_map.sorted_items():
            try:
                f.write("{}    {}\n".format(word.ljust(padding), freq))
            except:
                print(word, padding, freq)
        
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
