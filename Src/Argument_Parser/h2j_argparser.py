import argparse

''' This module is used to parse the inputs for program'''

def html2json_parser():

        parser = argparse.ArgumentParser(description="Run HTML2JSON_parser")
        parser.add_argument('--input', nargs='?', default='input/Websites2Parse.txt', help='Enter Websites which you want to parse in this file')
        parser.add_argument('--Threads', nargs='?', default=8, help='No of threads')
        
        return parser.parse_args()
