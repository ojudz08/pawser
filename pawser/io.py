# get input file type
# 1. pdf
# 2. ppt
# 3. docx


# save result or output in different formats
# 1. dataframe
# 2. csv
# 3. json

import os, sys
from typing import Any, Dict, Iterable, List, Optional, Union

class read_pdf:
    """file_path: Union[str, os.PathLike],
       page_num: int, output_format: str,  output_path: str"""

    _page_num: int

    def __init__(self,
                 page_num: int
                 ):
        #self.init_dir = os.path.abspath(os.path.dirname(sys.argv[0]))
        self._page_num = page_num
    
    @property
    def page_num(self) -> int:
        """The page number of the pdf file where the table is"""
        return self._page_num

if __name__ == '__main__':

    test = read_pdf(2)
    print(test)
