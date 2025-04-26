import argparse
import sys
import os
from antlr4 import *
from ANTLR.CobolLexer import CobolLexer
from ANTLR.CobolParser import CobolParser
import re

def remove_cobol_comments(source_code: str, remove_metadata: bool = True) -> str:
    """
    Remove comments from COBOL source code.
    
    Args:
        source_code (str): The COBOL source code.
        remove_metadata (bool): If True, remove developer metadata lines like "MO1624* ... *".
    
    Returns:
        str: The source code with comments removed.
    """
    cleaned_lines = []
    for line in source_code.splitlines():
        line = line.rstrip()
        
        # Ignore full-line comments (asterisk in column 7, 0-based index 6)
        if len(line) > 6 and line[6] == '*':
            continue
        
        # Ignore developer metadata lines like "MO1624* ... *" if enabled
        if remove_metadata and re.match(r'^[A-Z0-9]+[*].*\*$', line.strip()):
            continue
        
        # Remove inline comments starting with " *>" (space before *>, modern COBOL)
        if ' *>' in line:
            line = line.split(' *>', 1)[0].rstrip()
        
        cleaned_lines.append(line)
    return '\n'.join(cleaned_lines)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate AST from COBOL source file")
    parser.add_argument("input_file", help="Path to the input COBOL file (.cbl)")
    parser.add_argument("--comments", choices=["enable", "disable"], default="disable",
                        help="Enable or disable comment removal (default: disable)")
    
    args = parser.parse_args()
    
    # Verify file exists and has .cbl extension
    if not os.path.isfile(args.input_file):
        print(f"Error: File '{args.input_file}' does not exist")
        sys.exit(1)
    if not args.input_file.lower().endswith('.cbl'):
        print("Warning: Input file should have .cbl extension")
    
    # Get the directory and base filename
    input_dir = os.path.dirname(args.input_file) or '.'
    base_name = os.path.splitext(os.path.basename(args.input_file))[0]
    output_file = os.path.join(input_dir, f"{base_name} AST.txt")
    
    # Read and process the COBOL code
    with open(args.input_file, 'r') as f:
        cobol_code = f.read()
        
        # Apply comment removal if enabled
        if args.comments == "enable":
            cobol_code = remove_cobol_comments(cobol_code)
    
    # Generate AST
    input_stream = InputStream(cobol_code)
    lexer = CobolLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = CobolParser(token_stream)
    tree = parser.startRule()
    
    # Write AST to output file
    with open(output_file, 'w') as out_file:
        out_file.write(tree.toStringTree(recog=parser))
    
    print(f"AST generated successfully: {output_file}")

if __name__ == "__main__":
    main()