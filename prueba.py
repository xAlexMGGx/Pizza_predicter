'''
Change string number to integer. For example: 'one' to 1. Use the following libraries: re, numpy, pandas
'''

from word2number import w2n
import re
import pandas as pd

date1 = pd.to_datetime('2015-12-31 23:00:00')
date2 = pd.to_datetime('2015-12-31 23:59:00')

print(date2 >= date1)