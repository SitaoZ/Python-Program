import sys
from itertools import groupby

"""
Author  : Zhu Sitao, zhusitao@genomics.cn
Version : 1.0
Date    : 2018-2-1
Aim     : get each fasta ID length
"""
class FastaFile:
        def __init__(self,path):
                self.path = path
                self._map = {}
                self.__fasta_iter()
        def __str__(self):
                return self._map.__str__()
        def __fasta_iter(self):
                fh = open(self.path)
                faiter =(x[1] for x in groupby(fh,lambda line : line[0] == ">"))
                for header in faiter:
                        header = header.next()[1:].strip()
                        header = header.split()[0]
                        seq ="".join(s.strip() for s in faiter.next())
                        self._map[header] = seq
def usage():
        USAGE = """
Ddescription:
        get each fasta ID length
        The program should be running in python2.7
Example:
        python length.py xx.fa
                """
        print USAGE
if __name__ == '__main__':
        if len(sys.argv) == 1:
                usage()
                sys.exit(1)
        fileIn = sys.argv[1]
        fastaDict = FastaFile(fileIn)._map
        for i in sorted(fastaDict.keys()):
                print ">%s\t%s"%(i,len(fastaDict[i]))
