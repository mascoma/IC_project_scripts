#this script is to summarize the ICC_DS2 mapping unique and overlap taxonomy
import re 
def main():
    output = open("overlap.txt", 'w')
    output1 = open("DS2_1_family_unique.txt",'w')
    output2 = open("ICC_DS2_1_family_unique.txt",'w')
    output3 = open("DS2_1_family_overlap.txt", 'w')
    output4 = open("ICC_DS2_1_family_overlap.txt", 'w')
    readslist1 = []
    readslist2 = []
    try:
        f1 = open("DS2_1_all_diam_family.txt", 'r')
        f2 = open("ICC_all_diam_family.txt", 'r')
        print("Open success!")
        for line1 in f1:
            
            index1 = (re.search("^(.+)\,", line1)).group(1)
            readslist1.append(index1)   
        print(len(readslist1))
        for line2 in f2:
            index2 = (re.search("^(.+)\,", line2)).group(1)
            readslist2.append(index2)   
        print(len(readslist2))
        overlap = set(readslist1).intersection(readslist2) # reads hits in diamond fast  
        print(len(overlap))
        print(overlap, file = output, end = '')
        f1.close()
        f2.close()
       # reads hits in diamond fast   
        f1 = open("DS2_1_all_diam_family.txt", 'r')
        f2 = open("ICC_all_diam_family.txt", 'r')
        for line3 in f1:
            index3 = (re.search("^(.+)\,", line3)).group(1)
            if index3 not in overlap:
                print(line3, file = output1, end = '')  
            if index3 in overlap:
                print(line3, file = output3, end = '')
        for line4 in f2:
            index4 = (re.search("^(.+)\,", line4)).group(1)
            if index4 not in overlap:
                print(line4, file = output2, end = '')
            if index4 in overlap:
                print(line4, file = output4, end = '')
    except IOError:
        print ("no such file!")                   
if __name__ == "__main__": main() 