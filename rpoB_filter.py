import re
import csv
def main():
    output1 = open("/Users/Xin/Desktop/IC_project/output/Dec102015/ICW_rpoB.fasta", 'w')
    readslist = []
    flag = False
    try:
        f1 = open("/Users/Xin/Desktop/IC_project/input/merged_reads_CLC/ICW_CLC.fasta", 'r')
        f = open("/Users/Xin/Desktop/IC_project/output/reads_assigned_bl_dd/ICW_rpoB_reads.csv" ,'r')
        print("Open success!")
    except IOError:
        print ("no such file!")
    for line in f:
        tmp0 = re.search("^(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)",line)
        if tmp0:
            read = tmp0.group(1)
            readslist.append(read)
    print("total reads:", len(readslist))
    for line1 in f1:
        count = 0
        if flag:
            if not line1.startswith('>'):
                print(line1.rstrip(), file = output1)
            if line1.startswith('>'):
                flag = False
        tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)",line1)
        if tmp:
            index1 = tmp.group(1)
            if index1 in readslist:
                flag = True
                print(line1.rstrip(), file = output1)
                count = count + 1
                continue
                

if __name__ == "__main__": main()