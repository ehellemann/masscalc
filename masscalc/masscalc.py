"""
masscalc.py
This is a module that will take a protein sequence and a labeling method and calculate the proteins moelcular weight.

Handles the primary functions
"""

import os
import sys
import re
from variables import *
import argparse
#import tkinter as tk


def start_gui():
    sys.exit()


def formating_seq(input_sequence):
    input_sequence = input_sequence.upper()
    input_sequence = input_sequence.replace(' ', '')
    protein_sequence = re.sub('\d', '', input_sequence)
    return protein_sequence #TODO add error if there is something wrong


def read_fasta(filename):
    # opening the fasta file 
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            text = f.readlines()
    else:
        print("File: {} does not exist".format(filename))
        sys.exit() #TODO maybe add logging
    # Parses the fasta file 
    if not text[0].startswith(">"):
        print("make sure fasta file is formated correctly")
    proteins = []
    lines_with_start = []
    for n, line in enumerate(text):
        if line.startswith(">"):
            lines_with_start.append(n)
    for i in range(len(lines_with_start) - 1):
        sequence = ""
        for line in text[lines_with_start[i] + 1 : lines_with_text[i + 1]]:
            new_line = re.sub("\n", "", line)
            sequence += new_line
        try:
            proteins.append(Protein([text[lines_with_start[i][1:]]],sequence))
        except:
            print("There is an error with sequence: \n{}\n Make sure it is a valid sequence".format(current_protein))
            sys.exit() #TODO maybe add logging
        
        return proteins


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    parser = argparse.ArgumentParser(
        description="Mass calculator for labeled proteins.")
    parser.add_argument("-f", "--file", type=str, help="Define the fasta file to be processed.")
    parser.add_argument("-s", "--seq", type=str, help="sequence to calculate molecular weight.")
    parser.add_argument("-l", "--label", nargs="*", type=str, help="labeling method. Options carbon, nitrogen, deuterium and ILV")
    parser.add_argument("-g", "--gui", action="store_true", help="GUI version for the program")
    args = parser.parse_args()
    
    if args.gui:
        start_gui()
    
    if args.label:
        labeling = parse_labeling(args.label)
    else:
        labeling = None
        
    if args.file:
        if args.file.split(".")[-1] == "pdb":
            proteins = read_pdb(args.file)
        else:
            proteins = read_fasta(args.file)
        
        lines_to_print = []
        length = 0
        for protein in proteins:
            line = "The molecular weight is: {} g/mole".format(protein.calc_mol_weight(labeling))
            lines_to_print.append((protein.name,line))
            if len(line) > length:
                length = len(line)
        for name, line in lines_to_print:
            print("=" * length)
            print(name)
            print(line)
        print("=" * length)
    
    elif args.seq:
        sequence = formating_seq(args.seq)
        protein = Protein("Protein", sequence)
        line = "The molecular weight is: {} g/mole".format(protein.calc_mol_weight(labeling))
        print("=" * len(line))
        print(line)
        print("=" * len(line))
    
    else:
        print("""There was no argument given. Please add arguments to the script. For help type:
        python masscalc.py --help""")
    
