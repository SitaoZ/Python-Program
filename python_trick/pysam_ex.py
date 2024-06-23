import pysam

# 打开 BAM 文件
bam_file = pysam.AlignmentFile("AT4G20830.1.mapped.sorted.bam", "rb")

i = 0
# 选择一条read进行打印比对情况
for read in bam_file:
    read_sequence = read.query_sequence
    ref_sequence = ""
    ref_start_pos = read.reference_start
    cigar_tuples = read.cigartuples
    print(read)
    for cigar_type, cigar_length in cigar_tuples:
        if cigar_type == 0:  # M (match) or = (match) or X (mismatch)
            ref_sequence += read.get_reference_sequence()
            ref_start_pos += cigar_length
        elif cigar_type == 1:  # I (insertion)
            ref_sequence += "-" * cigar_length
        elif cigar_type == 2:  # D (deletion)
            ref_sequence += "D" * cigar_length
            ref_start_pos += cigar_length
        elif cigar_type == 4:  # S (softclip)
            read_sequence = read_sequence[:-cigar_length]
    
    print("Read      Sequence:", read.query_sequence)
    print("Reference Sequence:", ref_sequence)
    print("\n")
    i += 1
    if i == 3: break 

# 关闭 BAM 文件
bam_file.close()
