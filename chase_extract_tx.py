"""
Copy and paste the entire contents of chase statmement pdf
Extract only those lines that represent transactions and export to new file

Exacmple of lines we want to extract:
10/05 AUTOMATIC PAYMENT - THANK YOU -3,826.72
09/09 NJT MOBILE 3001 NEWARK NJ 26.00

Example of lines we want to ignore:
Minimum Payment: $25.00
09/21 CZECH KORUNA
175.00 X 0.046171428 (EXCHG RATE)
Previous points balance 193,092

The following observations are important:
- tx amounts don't have dollar signs, and are always preceded by a space
- tx amounts might be negative
- tx lines allways end in ".XX"
- tx amounts might be in the thousands (and thus have commas)

Added as a sanity check:
- tx lines always start with a date "XX/XX"
"""

import re

def main():

    lines = None
    with open("../../temp/mirek_2018_raw.txt", "r") as f_read:
        lines = f_read.read().splitlines()

    matches = []
    for line in lines:
        exp = r'^[0-9]{2}/[0-9]{2}.*\ [-]{0,1}[0-9,]*\.[0-9]{2}$'
        if re.match(exp, line):
            print line
            matches.append(line)

    print "\n".join(matches)

    out_filename = "../../temp/mirek_2018_tx.csv"
    with open(out_filename, "w") as f_write:
        for tx_line in matches:
            f_write.write(tx_line + "\n")

    print "Wrote {} tx to '{}'".format(len(matches), out_filename)

if __name__ == '__main__':
    main()
