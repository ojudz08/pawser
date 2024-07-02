"""
    Author: Ojelle Rogero
    Created on: June 23, 2024
    About:
        Parses the transactions of a bank statement
"""

from tkinter import filedialog
import pymupdf, tabula
import os, sys
from config import config01
import pandas as pd
import numpy as np



class bank_estatement():

    def __init__(self):
        self.init_dir = os.path.abspath(os.path.dirname(sys.argv[0]))


    def config(self):
        config_csv = os.path.join(self.init_dir, r"config\parserConfig.csv")
        pdf_configs = pd.read_csv(config_csv)
        return pdf_configs
        
    

if __name__ == '__main__':
    bnk = "BDO"

    result = bank_estatement().config()
    print(result)