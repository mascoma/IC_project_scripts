import re 
def main():
    output1 = open("DS2_2_R2_unmerged.fastq", 'w')
    readslist = []
    flag = False
    count1 = 0
    try:   
        f1 = open("DS2-2_R2_paired.fastq", 'r')
        f = open("DS2_2_R2_unmerged_tag.txt", 'r')
        print("Open success!")
        for line in f:
            readslist.append(line.rstrip('\n'))   
        print("total reads:", len(readslist))
        for line1 in f1: 
            count = 0 
            if flag:   
                if not line1.startswith('@M00704'):
                    print(line1, file = output1, end = '')  
                if line1.startswith('@M00704'):
                    flag = False                      
            tmp = re.search("@(M00704:49:000000000-AFW6D\:\d+\:\d+\:\d+\:\d+)",line1)                
            if tmp:
                index1 = tmp.group(1)  
                while (count < len(readslist)):
                    read = readslist[count] 
                    if index1 == read: 
                        flag = True
                        print(line1, file = output1, end = '') 
                        break 
                    count = count + 1                      
    except IOError:
        print ("no such file!")  
if __name__ == "__main__": main() 