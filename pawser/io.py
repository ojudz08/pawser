# get input file type
# 1. pdf
# 2. ppt
# 3. docx


# save result or output in different formats
# 1. dataframe
# 2. csv
# 3. json

from typing import Any, Dict, Iterable, List, Optional, Union
import os, sys

init_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
sys.path.insert(1, os.path.join(init_dir, "pawser"))

from utils import debug, timer, init_dir

#class read_pdf:
#    """file_path: Union[str, os.PathLike],
#       page_num: int, output_format: str,  output_path: str"""

class TimeWaster:
    @debug
    def __init__(self, max_num):
        self.max_num = max_num

    @timer
    def waste_time(self, num_times):
        for _ in range(num_times):
            sum([number**2 for number in range(self.max_num)])
    
    @init_dir
    def test(self):
        


tw = TimeWaster(1000)
tw.waste_time(999)