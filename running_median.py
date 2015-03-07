"""
Program that keeps track of running median of line lengths for
files in a given directory, alphebatized, and outputs running median
to a given output file.  See `README.md` and `test.py` for more
details.
"""

from __future__ import print_function
import sys, os, heapq

from util import main_setup, CmdLineParameterException, process_line

class RunningMedian(object):
    def __init__(self):
        """keep track of running median of a list of numbers.  For performance
        on large data sets, use two heaps to store larger and smaller
        numbers seen so far. Maintain the invariants that (A) all
        elements of the max_heap are greater than or equal to all
        elements of the min_heap, and (B) the max_heap has at most
        one more element than the min_heap.  In this way, we easily
        find the median (in O(1) time) by looking at the heads of one
        or both queues, depending on whether the number of entries so
        far is even or odd.

        """
        self.max_heap = []
        self.min_heap = []
        self.n = 0 ## how many entries we've seen

    def add(self, entry):
        """add a number to the heaps, maintaining above invariants.  Note
        that to keep the min heap in the correct order (the maximum
        element on top), we use the somewhat hacky method of inserting
        negative numbers there.  This method is O(ln n) where n is the
        size of the lists.
        """
        if self.n % 2 == 0: ## maintain invariant (B)
            heapq.heappush(self.max_heap, entry)
        else:
            heapq.heappush(self.min_heap, -entry)
        self.n += 1
        if self.n <= 1:
            return
        ## maintain invariant (A)
        if -self.min_heap[0] > self.max_heap[0]: ## switch
            tmp1 = heapq.heappop(self.max_heap)
            tmp2 = heapq.heappushpop(self.min_heap, -tmp1)
            heapq.heappush(self.max_heap, -tmp2)

    def median(self):
        """return current median.  Raises IndexError if called before adding
        any entries.
        """
        if self.n % 2 == 0:
            middle_high = self.max_heap[0]
            middle_low = -self.min_heap[0]
            return float(middle_high + middle_low) /  2.0
        else:
            return float(self.max_heap[0])

def main(argv):
    try:
        input_dir, output_file = main_setup(argv)
    except CmdLineParameterException as e:
        print(e)
        return 1

    ## collect all input files and sort alphabetically
    sorted_input_files = []
    for root, _, files in os.walk(input_dir):
        for fname in files:
            sorted_input_files.append(os.path.join(root, fname))
    sorted_input_files.sort()

    ## for each input file, write running median to output file
    rm = RunningMedian()
    with open(output_file, "w") as output_file:
        for fname in sorted_input_files:
            with open(fname, "r") as input_file:
                for line in input_file:
                    words = process_line(line)
                    rm.add(len(words))
                    output_file.write("{:.1f}\n".format(
                        rm.median()))
                
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
