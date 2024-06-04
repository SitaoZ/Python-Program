def estimate_nucleotide_frequencies(seq):
    seq = seq.replace('-','').upper()
    A = seq.count('A')
    C = seq.count('C')
    G = seq.count('G')
    T = seq.count('T')
    length = float(len(seq))
    return [ x/length for x in [A,C,G,T] ]

def pdistance(seq1, seq2):
    p = 0
    pairs = []
    for x in zip(seq1,seq2):
        if '-' not in x: pairs.append(x)
    #for (x,y) in zip(seq1,seq2):
    for (x,y) in pairs:
        if x != y:
            p += 1
    #length = (len(seq1) + len(seq2)) / 2
    length = len(pairs)
    return float(p) / length
  
def TNdistance(seq1, seq2):
    """ 
    Tajima-Nei distance = -b log(1 - p / b)
    where:
    b = 0.5 * [ 1 - Sum i from A to T(Gi^2+p^2/h) ]
    h = Sum i from A to G( Sum j from C to T (Xij^2/2*Gi*Gj))
    p = p-distance, i.e. uncorrected distance between seq1 and seq2
    Xij = frequency of pair (i,j) in seq1 and seq2, with gaps removed
    Gi = frequency of base i over seq1 and seq2 """
    from math import log

    ns = ['A','C','G','T']
    G = estimate_nucleotide_frequencies(seq1 + seq2)
    p = pdistance(seq1,seq2)
    pairs = []
    h = 0

    #collect ungapped pairs
    for x in zip(seq1,seq2):
        if '-' not in x: pairs.append(x)
       
    #pair frequencies are calculated for AC, AG, AT, CG, CT, GT (and reverse order)
    for i in range(len(ns)-1):
        for j in range(i+1,len(ns)):
            if i != j: paircount = pairs.count( (ns[i], ns[j]) ) + pairs.count( (ns[j], ns[i]) )
            Xij_sq = (float(paircount)/len(pairs))**2
            GiGj = G[i]*G[j]
            h += 0.5*Xij_sq/GiGj  #h value used to calculate b
    
    b = 0.5*(1-sum([x**2 for x in G])+p**2/h)
    try: d = -b * log(1 - p/b)
    except ValueError: 
        print "Tried to take log of a negative number"
        return None
    return d
