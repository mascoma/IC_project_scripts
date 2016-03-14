import re 
import csv

def main():
    output = open("/isi/olga/xin/Halophile_project/output/Dec072015/contig_bl_dd_unassigned.fasta", 'w')
    try:
        all_reads = open("/isi/olga/xin/Halophile_project/output/Dec072015/contig_bl_unassigned.fasta", 'r')
    except IOError:
        print ("no such file!") 
    readslist = []
    readslist1 = []
    flag = False
    with open('/isi/olga/xin/Halophile_project/output/Dec072015/contig_CLC_diamond_reads_genus.csv', 'r') as inputfile:
        input = csv.DictReader(inputfile, delimiter =",", fieldnames=['reads','genus'])
        for row in input:
            readslist.append(row['reads']) # all the reads
        print("total reads:", len(readslist)) 
        
        for line in all_reads: 
            if flag:
                if not line.startswith('>'):
                    print >> output, line.rstrip()  
                if line.startswith('>'):
                    flag = False      
            tmp = re.search(">(DS2\-1\(paired\)\_trimmed\_\(paired\)\_contig\_\d+)\s",line)      
            if tmp:
                index = tmp.group(1) 
                if index not in readslist:
                    readslist1.append(index)# unassigned reads after blastn
                    flag = True
                    print >> output, line.rstrip()
                    continue
                     
        print("unassigned reads:", len(readslist1))    
                
if __name__ == "__main__": main() 
