#!/usr/bin/env bash

python word_count.py ./wc_input ./wc_output/wc_result.txt
python running_median.py ./wc_input ./wc_output/med_result.txt
