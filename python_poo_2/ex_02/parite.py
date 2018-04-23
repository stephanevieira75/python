#! /usr/bin/env python3
# coding: utf-8

import csv_analysis as c_an
import xml_analysis as x_an

def main():
    c_an.launch_analysis('current_mps.csv')
    x_an.launch_analysis('SyceronBrut.xml')

if __name__ == "__main__":
    main()