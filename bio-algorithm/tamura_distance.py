from math import log
def Tamuradistance(seq1,seq2):
    """
    Tamura distance = -C log( 1 - P/C - Q ) - 0.5( 1 - C )log( 1 - 2Q )
    where:
    P = transition frequency
    Q = transversion frequency
    C = GC1 + GC2 - 2 * GC1 * GC2
    GC1 = GC-content of sequence 1
    GC2 = GC-coontent of sequence 2
    """
    pairs = []
    
    #collect ungapped pairs
    for x in zip(seq1,seq2):
        if '-' not in x: pairs.append(x)
        
    ts_count=0
    tv_count=0
    length = len(pairs)
    
    transitions = [ "AG", "GA", "CT", "TC"]
    transversions = [ "AC", "CA", "AT", "TA",
                      "GC", "CG", "GT", "TG" ]

    for (x,y) in pairs:
        if x+y in transitions: ts_count += 1 
        elif x+y in transversions: tv_count += 1
    
    p = float(ts_count) / length
    q = float(tv_count) / length
    gc1 = sum(estimate_nucleotide_frequencies(seq1)[1:3])
    gc2 = sum(estimate_nucleotide_frequencies(seq2)[1:3])
    c = gc1 + gc2 - 2 * gc1 * gc2

    try: d = -c * log( 1 - p/c - q) - 0.5 * ( 1 - c ) * log ( 1 - 2*q )
    except ValueError: 
        print "Tried to take log of a negative number"
        return None
    return d
