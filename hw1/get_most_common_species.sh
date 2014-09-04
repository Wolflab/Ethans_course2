#!/bin/bash
curl -O http://www.programmingforbiologists.org/data/data_drycanyon_2013.txt
sort -k 3 -n data_drycanyon_2013.txt |
head -1 > least_common_species.txt