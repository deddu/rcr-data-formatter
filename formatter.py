import pandas as pd
import sys

date_fields = [
    'Funding - NSF Earns Begin / Journal From Date',
    'Student Curriculum Due Date',
    'Student Curriculum Acquired On',
    'Person Terminated On',
    'Student Curriculum Assigned On'
]


def rename_cols(c):
    return c.replace('Funding - National Science Foundation', 'NSF-')\
        .replace('Person', '')\
        .replace(' ', '')

infile = sys.argv[1]
outfile = infile[:-4] + '_fmt.csv'
skip = int(sys.argv[2]) if len(sys.argv) > 2 else 0
if len(sys.argv) < 2:
    print "usage: python formatter inputfile.csv [skip lines]"

data = pd.read_csv('./rcr_feb.csv', parse_dates=date_fields, infer_datetime_format=True)
data.columns = map(rename_cols, data.columns)
data.to_csv(outfile, index_label='rid', na_rep='\N')

# load data infile '/Users/deddu/wk/misc/co/rcr_feb_fmt.csv' ignore into table feb17 fields terminated by ',' ignore 1 lines;
#  SHOW WARNINGS;
