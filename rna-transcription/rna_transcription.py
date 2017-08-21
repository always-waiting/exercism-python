def to_rna(dna):
    dna_rna = {"G":"C","C":"G","T":"A","A":"U"}
    dna_up = dna.upper()
    rna = []
    for i in dna_up:
        try:
            rna.append(dna_rna[i])
        except:
            return ""
    return "".join(rna)
