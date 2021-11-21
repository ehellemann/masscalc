# This file contains the class Residue and creates all natural residues class objects.

class Protein:
    global residues
    def __init__(self, name, sequence, labeling=None):
        self.name = name
        self.sequence = self.get_list_residues(sequence)
        self.text_sequence = self.get_sequence(self.sequence)
        self.molecular_weight = self.calc_mol_weight()

    def get_list_residues(self, sequence):
        list_residues =[]
        for res in sequence:
            list_residues.append(residues[res])
        return list_residues
    
    def get_sequence(self,list_residues):
        sequence = ""
        for res in list_residues:
            sequence += res.one_letter
        return sequence

    def calc_mol_weight(self, labeling=None):
        molecular_weight = 0

        # get mass for each residue
        for res in self.sequence:
            molecular_weight += res.get_mass(labeling)

        # subtract weight of water molecule for each peptidic bond in the protein
        molecular_weight -= (len(self.sequence) - 1) * 18.015

        return molecular_weight


class Residue: 
    def __init__(self, one_letter, three_letter, formula, mass, num_C, num_N, num_H, ilv):
        self.one_letter = one_letter
        self.three_letter = three_letter
        self.formula = formula
        self.mass = mass
        self.num_C = num_C
        self.num_N = num_N
        # non-exchengable hydrogens
        self.num_H = num_H
        self.ilv = ilv

    def get_mass(self, labeling=None):
        '''
        A method that takes a labeling scheme and returns the mass of the labeled residue.
        available labeling schemes are carbon, nitrogen, deuterium and ilv. You can mix carbon, nitrogen and deuterium. 
        ilv assumes that the protein is deuteriated except the methyl groups in I, L and V residues.
        '''
        mass = self.mass
        if labeling is None:
            return mass
        if "carbon" in labeling:
            mass += self.num_C
        if "nitrogen" in labeling:
            mass += self.num_N
        if "deuterium" in labeling:
            mass += self.num_H
        if labeling == "ilv":
            mass += self.num_H + self.ilv  # TODO need to revisit this line, it is likely wrong

        return mass


# hydrophobic residues
# residues are defined as class residue with one letter code, three letter code
# chemical formula, mass, num_C, num_N, num_H, ilv
alanine = Residue('A', 'Ala', 'C3H7NO2', 89.094, 3, 1, 4, 0)
leucine = Residue('L', 'Leu', 'C6H13NO2', 131.175, 6, 1, 10, 1)
isoleucine = Residue('I', 'Ile', 'C6H13NO2', 131.175, 6, 1, 10, 1)
valine = Residue('V', 'Val', 'C5H11NO2', 117.148, 5, 1, 8, 1)
methionine = Residue('M', 'Met', 'C5H11NO2S', 149.208, 5, 1, 8, 0)
phenylalanine = Residue('F', 'Phe', ' C9H11NO2', 165.192, 9, 1, 8, 0)
tyrosine = Residue('Y', 'Tyr', 'C9H11NO3', 181.191, 9, 1, 8, 0)
tryptophan = Residue('W', 'Trp', 'C11H12N2O2', 204.229, 11, 2, 8, 0)

# special cases residues

cysteine = Residue('C', 'Cys', 'C3H7NO2S', 121.154, 3, 1, 3, 0)
glycine = Residue('G', 'Gly', 'C2H5NO2', 75.067, 2, 1, 2, 0)
proline = Residue('P', 'Pro', 'C5H9NO2', 115.132, 5, 1, 7, 0)
selenocysteine = Residue('U', 'Sec', 'C3H7NO2Se', 167.057, 3, 1, 3, 0)
pyrrolysine = Residue('O', 'Pyl', 'C12H21N3O3', 255.318, 12, 3, 17, 0)

# neutral polar residues

serine = Residue('S', 'Ser', 'C3H7NO3', 105.093, 3, 1, 3, 0)
threonine = Residue('T', 'Thr', 'C4H9NO3', 119.120, 4, 1, 6, 0)
asparagine = Residue('N', 'Asn', 'C4H8N2O3', 132.119, 4, 2, 3, 0)
glutamine = Residue('Q', 'Gln', 'C5H10N2O3', 146.146, 5, 2, 5, 0)

# positively charged residues

arginine = Residue('R', 'Arg', 'C6H14N4O2', 174.204, 6, 4, 7, 0)
histidine = Residue('H', 'His', 'C6H9N3O2', 155.157, 6, 3, 5, 0)
lysine = Residue('K', 'lys', 'C6H14N2O2', 146.190, 6, 2, 9, 0)

# negatively charged amino acids

aspartic_acid = Residue('D', 'Asp', 'C4H7NO4', 133.103, 4, 1, 3, 0)
glutamic_acid = Residue('E', 'Glu', 'C5H9NO4', 147.130, 5, 1, 5, 0)


residues = {"A": alanine, 
            "L": leucine, 
            "I": isoleucine, 
            "V": valine, 
            "M": methionine, 
            "F": phenylalanine, 
            "Y": tyrosine, 
            "W": tryptophan, 
            "C": cysteine,
            "G": glycine, 
            "P": proline, 
            "S": serine, 
            "T": threonine, 
            "N": asparagine, 
            "Q": glutamine, 
            "R": arginine, 
            "H": histidine, 
            "K": lysine,
            "D": aspartic_acid, 
            "E": glutamic_acid, 
            "U": selenocysteine, 
            "O": pyrrolysine
            }
