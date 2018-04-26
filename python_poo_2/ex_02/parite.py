#! /usr/bin/env python3
# coding: utf-8
import argparse

import csv_analysis as c_an
import xml_analysis as x_an

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--extension", help="""Type of file to analyse. Is it a CSV of an XML?""")
    return parser.parse_args()
    
def main():
    c_an.launch_analysis('current_mps.csv')
    x_an.launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":
    main()