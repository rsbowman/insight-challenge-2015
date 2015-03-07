# -*- coding: utf-8 -*-

from unittest import TestCase, main

from util import process_line
from word_count import WordMap
from running_median import RunningMedian

def process_line_join(l):
    return " ".join(process_line(l))

class UtilTests(TestCase):
    def test_process_line(self):
        self.assertEqual(process_line_join("Go To LOWERCASE"),
                         "go to lowercase")
        self.assertEqual(process_line_join("skips   lots of  spaces"),
                         "skips lots of spaces")
        self.assertEqual(process_line_join("skip! punctuation, too? "),
                         "skip punctuation too")
        self.assertEqual(process_line_join("don't skip 1 2 3 numbers 39"),
                         "dont skip 1 2 3 numbers 39")
        self.assertEqual(process_line_join("re-move hyphens"),
                         "remove hyphens")

class WordCountTests(TestCase):
    def test_simple_count(self):
        wm = WordMap()
        wm.add_line("this is a simple test like this")
        self.assertEqual(wm.get("this"), 2)
        self.assertEqual(wm.get("simple"), 1)
        self.assertEqual(wm.get("a"), 1)
        self.assertEqual(wm.get("sassafras"), None)

    def test_sorted(self):
        wm = WordMap()
        wm.add_line("very test zoo and ant aardvark")
        items = wm.sorted_items()
        self.assertEqual(items[0][0], "aardvark")
        self.assertEqual(items[1][0], "and")
        self.assertEqual(items[-1][0], "zoo")

    def test_punctuation_etc(self):
        wm = WordMap()
        wm.add_line("This is a test. Of #punctuation# & capitalization.")
        self.assertEqual(wm.get("test"), 1)
        self.assertEqual(wm.get("punctuation"), 1)
        self.assertEqual(wm.get("of"), 1)
        self.assertEqual(wm.get(" "), None)

    def test_multiple_lines(self):
        wm = WordMap()
        wm.add_line("We R Are Y")
        wm.add_line("Are Y Are We")
        wm.add_line("Toys R Us")
        self.assertEqual(wm.get("we"), 2)
        self.assertEqual(wm.get("are"), 3)
        self.assertEqual(wm.get("r"), 2)

    def test_max_wordlen(self):
        wm = WordMap()
        wm.add_line("this is a test")
        wm.add_line("with a looong word")
        self.assertEqual(wm.max_wordlen(), 6)
        
class MedianTests(TestCase):
    def test_median(self):
        rm = RunningMedian()
        rm.add(1)
        self.assertEqual(rm.median(), 1.0)
        rm.add(5)
        self.assertEqual(rm.median(), 3.0)
        rm.add(3)
        self.assertEqual(rm.median(), 3.0)
        rm.add(7)
        self.assertEqual(rm.median(), 4.0)
        rm.add(6)
        self.assertEqual(rm.median(), 5.0)
        rm.add(4)
        self.assertEqual(rm.median(), 4.5)
        

if __name__ == '__main__':
    main()
        
        
        
