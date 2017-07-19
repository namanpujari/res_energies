### This is a temporary parameter file made for residue C12 ###
### Make sure that all the parameters are verified before using this file as a global parameter file ###

CONFLIST C12        C12BK 

NATOM    C12BK      22

IATOM    C12BK  C1     0
IATOM    C12BK  N2     1
IATOM    C12BK  CA2    2
IATOM    C12BK  CG1    3
IATOM    C12BK  OG1    4
IATOM    C12BK  C2     5
IATOM    C12BK  O2     6
IATOM    C12BK  N3     7
IATOM    C12BK  CA1    8
IATOM    C12BK  N1     9
IATOM    C12BK  CB1   10
IATOM    C12BK  CA3   11
IATOM    C12BK  C3    12
IATOM    C12BK  O3    13
IATOM    C12BK  CB2   14
IATOM    C12BK  CG2   15
IATOM    C12BK  CD1   16
IATOM    C12BK  CE1   17
IATOM    C12BK  CD2   18
IATOM    C12BK  CE2   19
IATOM    C12BK  CZ    20
IATOM    C12BK  OH    21

ATOMNAME C12BK    0  C1 
ATOMNAME C12BK    1  N2 
ATOMNAME C12BK    2  CA2
ATOMNAME C12BK    3  CG1
ATOMNAME C12BK    4  OG1
ATOMNAME C12BK    5  C2 
ATOMNAME C12BK    6  O2 
ATOMNAME C12BK    7  N3 
ATOMNAME C12BK    8  CA1
ATOMNAME C12BK    9  N1 
ATOMNAME C12BK   10  CB1
ATOMNAME C12BK   11  CA3
ATOMNAME C12BK   12  C3 
ATOMNAME C12BK   13  O3 
ATOMNAME C12BK   14  CB2
ATOMNAME C12BK   15  CG2
ATOMNAME C12BK   16  CD1
ATOMNAME C12BK   17  CE1
ATOMNAME C12BK   18  CD2
ATOMNAME C12BK   19  CE2
ATOMNAME C12BK   20  CZ 
ATOMNAME C12BK   21  OH 

CONNECT  C12BK  C1  ion        0    N2   0    N3   0    CA1
CONNECT  C12BK  N2  ion        0    C1   0    CA2
CONNECT  C12BK  CA2 ion        0    N2   0    C2   0    CB2
CONNECT  C12BK  CG1 ion        0    CB1
CONNECT  C12BK  OG1 ion        0    CB1
CONNECT  C12BK  C2  ion        0    CA2  0    O2   0    N3 
CONNECT  C12BK  O2  ion        0    C2 
CONNECT  C12BK  N3  ion        0    C1   0    C2   0    CA3
CONNECT  C12BK  CA1 ion        0    C1   0    N1   0    CB1
CONNECT  C12BK  N1  ion        0    CA1
CONNECT  C12BK  CB1 ion        0    CG1  0    OG1  0    CA1
CONNECT  C12BK  CA3 ion        0    N3   0    C3 
CONNECT  C12BK  C3  ion        0    CA3  0    O3 
CONNECT  C12BK  O3  ion        0    C3 
CONNECT  C12BK  CB2 ion        0    CA2  0    CG2
CONNECT  C12BK  CG2 ion        0    CB2  0    CD1  0    CD2
CONNECT  C12BK  CD1 ion        0    CG2  0    CE1
CONNECT  C12BK  CE1 ion        0    CD1  0    CZ 
CONNECT  C12BK  CD2 ion        0    CG2  0    CE2
CONNECT  C12BK  CE2 ion        0    CD2  0    CZ 
CONNECT  C12BK  CZ  ion        0    CE1  0    CE2  0    OH 
CONNECT  C12BK  OH  ion        0    CZ 

