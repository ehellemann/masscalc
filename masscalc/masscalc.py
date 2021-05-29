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
        print("make sure fasta file is foramted correctly")
    proteins = {}
    current_protein = None
    for line in text:
        if line[0] == '>':
            current_protein = line[1:]
            proteins[current_protein] = ""
        else:
            proteins[current_protein] += re.sub("\n", "", line)

    prot_list = []
    for protein in proteins.keys():
        seq = proteins[protein]
        sequence = formating_seq(seq)
        if sequence == "ERROR":
            print("There is an error with sequence: \n{}\n Make sure it is a valid sequence".format(current_protein))
            sys.exit() #TODO maybe add logging
        else:
            prot_list.append(Protein(protein, seq))
    return prot_list


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    parser = argparse.ArgumentParser(
        description="Mass calculator for labeled proteins.")
    parser.add_argument("fasta_file", type=str, help="Define the fasta file to be processed. It is required")
    args = parser.parse_args()

    proteins = read_fasta(args.fasta_file)
    print("hello")