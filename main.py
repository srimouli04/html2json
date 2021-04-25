from Src.Argument_Parser.h2j_argparser import html2json_parser
from Src.consoleDisp import tab_printer
from Src.file_ops.general import *

#main function where all intialization and triggering happens 
def html2json_main(args):
    '''

	'''
    tab_printer.tab_printer(args)
    INPUT_FILE = args.input
    OUTPUT_DIR = 'Json_data'
    NUMBER_OF_THREADS = 1
    create_dir(OUTPUT_DIR)
    create_workers(NUMBER_OF_THREADS)
    create_jobs(INPUT_FILE)

def main():
    if __name__ == "__main__":
        args = html2json_parser()
        html2json_main(args)

main()





