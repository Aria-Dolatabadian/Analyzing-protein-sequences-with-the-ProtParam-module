from Bio.SeqUtils.ProtParam import ProteinAnalysis
my_seq = (
     "MAEGEITTFTALTEKFNLPPGNYKKPKLLYCSNGGHFLRILPDGTVDGTRDRSDQHIQLQ"
     "LSAESVGEVYIKSTETGQYLAMDTSGLLYGSQTPSEECLFLERLEENHYNTYTSKKHAKN"
     "WFVGLKKNGSCKRGPRTHYGQKAILFLPLPV"
)
analysed_seq = ProteinAnalysis(my_seq)
print(analysed_seq.molecular_weight()) #Returns molecular weight of entire sequence.
print(analysed_seq.gravy())
print(analysed_seq.count_amino_acids()) #Simply counts the number times an amino acid is repeated in the protein sequence.
print(analysed_seq.get_amino_acids_percent()) #Returns the number in percentage of entire sequence.
print(analysed_seq.aromaticity()) #Calculates the aromaticity value of a protein according to Lobry & Gautier (1994)
print(analysed_seq.instability_index()) #This method tests a protein for stability. Any value above 40 means the protein is unstable (=has a short half life).
print(analysed_seq.flexibility()) #Implementation of the flexibility method of Vihinen et al. (1994, Proteins, 19, 141-149).
print(analysed_seq.isoelectric_point()) #Calculate the pI of a protein.
print(analysed_seq.secondary_structure_fraction())
#This methods returns a list of the fraction of amino acids which tend to be in helix, turn or sheet.
# Amino acids in helix: V, I, Y, F, W, L.
# Amino acids in turn: N, P, G, S.
# Amino acids in sheet: E, M, A, L.
