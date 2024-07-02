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

from utils import init_dir

#class read_pdf:
#    """file_path: Union[str, os.PathLike],
#       page_num: int, output_format: str,  output_path: str"""

@init_dir
class read_pdf:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(f"Name: {self.name}")
        print(f"Initial Directory: {self.initial_directory}")

# Example usage
if __name__ == "__main__":
    obj = read_pdf("Example")
    obj.print_info()