# deal with file handle
def parse_fastq(file_path):
    with open(file_path, 'r') as f:
        for entry in zip(f,f,f,f):
            ID, Seq, Desc, Qual = entry
            # remove \n
            ID, Seq, Desc, Qual = [ i.strip() for i in (ID, Seq, Desc, Qual)]
            yield ID, Seq, Desc, Qual

# list to dict
fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
dict(zip(fields, values))
a_dict = dict(zip(fields, values))
