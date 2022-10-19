less xxx.fastq.gz | awk 'NR%4==2' | python -c 'import sys;from Bio.Seq import Seq; a = [print(Seq(i.strip()).reverse_complement()) for i in sys.stdin];' > seq_rc
