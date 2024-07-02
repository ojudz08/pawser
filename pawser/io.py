# get input file type
# 1. pdf
# 2. ppt
# 3. docx


# save result or output in different formats
# 1. dataframe
# 2. csv
# 3. json

from typing import Any, Dict, Iterable, List, Optional, Union

from utils import init_dir


class read_pdf:
    """file_path: Union[str, os.PathLike],
       page_num: int, output_format: str,  output_path: str"""

    @init_dir
    def __init__(self, page_num: int ):
        self._page_num = page_num
    

    def file_path(self):
        """The page number of the pdf file where the table is"""
        return "test"

if __name__ == '__main__':

    test = read_pdf(2)
    print(test.file_path)
