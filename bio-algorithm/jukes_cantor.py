import re math
# From alignments to distances
# Jukes-Cantor Distance on sequences

def distance(seq1, seq2):
	# Jukes Cantor distance formula: (-3/4)ln[1-p*(4/3)]
	p = percent_difference_of_nucleotides(seq1, seq2)
	return -0.75 * math.log(1 - (p*4/3)) if p else 0


def percent_difference_of_nucleotides (seq1, seq2, nucleobases=set('ACGT')):
	# percentage of nucleotide difference in two sequences
	diff_count = 0 # number of nucleotide differences
	valid_nucleotides_count = 0.0 # number of valid nucleotides (value is float for computing percentage)
	for a, b in zip(seq1, seq2):
		if a in nucleobases and b in nucleobases:
			valid_nucleotides_count += 1
			if a != b: diff_count += 1
	
	return diff_count / valid_nucleotides_count if valid_nucleotides_count else 0
