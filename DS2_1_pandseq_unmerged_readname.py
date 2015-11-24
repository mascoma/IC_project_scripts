import re 
def main():
    output = open("DS2_1_unmerged_R1_tag.txt", 'w')
    readslist1 = []
    readslist2 = []
    readslist = []
    try:
        f1 = open("DS2_1_R1_paired_tag.txt", 'r')
        f2 = open("DS2_1_merged_tag.txt", 'r')
        print("successful open!")
        for line1 in f1:
            readslist1.append(line1.rstrip('\n'))   
        print("total reads of DS2_1_paired_R1_tag: ",len(readslist1))
        for line2 in f2:
            readslist2.append(line2.rstrip('\n'))   
        print("total reads of DS2_1_merged_tag: ",len(readslist2))
        overlap = set(readslist1).intersection(readslist2) # reads hits in diamond fast  
        print(len(overlap))
        for i in range(0, len(readslist1)):
            if readslist1[i] not in readslist2:
                readslist.append(readslist1[i]) 
        print(readslist, file = output, end = '')        # reads hits in diamond fast                   
    except IOError:
       print ("no such file!")                   
if __name__ == "__main__": main() 