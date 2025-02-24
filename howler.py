#!/usr/bin/env python3
"""Howler"""
 
import argparse
import os
import sys
 
 
# --------------------------------------------------
def get_args():
    """
    Parse command-line arguments for the Howler program.

    This function sets up the argument parser and defines the expected
    command-line arguments. It handles both direct text input and file input,
    reading the contents of the file if a valid file path is provided.

    Returns:
        argparse.Namespace: An object containing the parsed arguments:
            - text (str): The input text to be converted to uppercase.
                          If a file path is provided, this will contain the file's contents.
            - outfile (str): The name of the output file. If not provided,
                             the program will use standard output.

    Raises:
        SystemExit: If invalid arguments are provided.
    """
    parser = argparse.ArgumentParser(
        description='Howler (upper-case input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',                                          
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',                                            
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    args = parser.parse_args()                                           

    if os.path.isfile(args.text):                                        
        args.text = open(args.text).read().rstrip()                      

    return args
 
 
# --------------------------------------------------
def main():
    """
    Execute the main functionality of the Howler program.

    This function performs the following steps:
    1. Retrieves command-line arguments.
    2. Opens the output file (or uses stdout if no file is specified).
    3. Converts the input text to uppercase.
    4. Writes the uppercase text to the output.
    5. Closes the output file handle if one was opened.

    The function doesn't take any parameters as it uses command-line arguments
    parsed by the get_args() function.

    Returns:
        None
    """
    args = get_args()                                                   
    out_fh = open(args.outfile, 'wt') if args.outfile else sys.stdout   
    out_fh.write(args.text.upper() + '\n')                              
    out_fh.close()
 
 
# --------------------------------------------------
if __name__ == '__main__':
    main()