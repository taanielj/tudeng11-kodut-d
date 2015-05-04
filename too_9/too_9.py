#!/usr/bin/env python3

__author__ = "Taaniel Jakobson"
__version__ = "0.0002a"
import os
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Alphabet import IUPAC


"""
 Siin on defineeritud kasutatavad funktsioonid: find_fasta() leiab aktiivsest folderist fasta failid ja tekitab nende loetelu, read_fasta loeb ette antud fasta faili sisu ja otsib sealt j2rjestuste ID'd ja j2rjestused ning nende pikkused.
"""


def find_fasta():
    fasta_files = [f for f in os.listdir("./") if f.endswith('.fasta')]      #otsib antud folderist k6ik .fasta l6puga failid
    return(fasta_files)

def read_fasta(sisend) :
    for seq_record in SeqIO.parse(sisend, "fasta", IUPAC.unambiguous_dna):   #loeb fasta failist v2lja DNA sekventsi
        print("name = ",seq_record.id)                                       #annab fasta failist ID
        print(repr(seq_record.seq))                                          #annab v2lja representatiivse sekventsi jupi
        print("length =", len(seq_record))
    return(seq_record.seq)                                                   #tagastab DNA sekventsi




"""
Siit algab programm ise, programmi ylesanne on leida aktiivsest folderist fasta failid. Siis kysida, kas transleerida valgusekventsiks
"""

def main():
    
    if len(find_fasta()) == 0:                                             #otsib .fasta failid, kui fasta faile ei lea l6peb programm
        print("no .fasta files in current folder")
    else:
        print("fasta files found:")                                        #kui .fasta failid leitakse
        print(find_fasta())                                                #siis prinditakse nende nimekiri
        sisend = input("File name: ")                                      #ja kysitakse kasutajalt soovitud fasta faili nime
        coding_dna = read_fasta(sisend)                                    
        print("Would you like to translate the DNA sequence to a protein sequence?(y/n)")
        sisend2 = input(">")
    
        if sisend2 == "y" or sisend2 == "yes":                             #kui kasutaja soovib, siis transleeritakse dna sekvents valguks.
            prot_sequence = coding_dna.translate()                         #siin v6iks olla ka osa, mis tunneb 2ra start koodoni, ja kas tegemist on yldse dna v6i rna j2rjestusega
            print(prot_sequence)                                           #ylej22nud on analoogne 8. kodut44ga.
            text_file = open("protein_sequence.txt", "w")
            text_file.write(str(prot_sequence))
            text_file.close()
            print('sequence saved to "protein_sequence.txt"')
        else:
            print("Bye!")

        

if __name__ == "__main__":
    main()





