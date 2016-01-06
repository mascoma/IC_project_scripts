#!/usr/bin/python3
import re
class Subsampling:
    def include(self,inputhandle,readlist,outputhandle):        
        flag = False
        for line in inputhandle: 
                if flag:
                    if not line.startswith('>'):
                        print(line, file = outputhandle, end = '')  
                    if line.startswith('>'):
                        flag = False      
                tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)      
                if tmp:
                    index = tmp.group(1) 
                    if index in readlist:
                        flag = True
                        print(line, file = outputhandle, end = '')
                        continue
    
    def exclude(self,inputhandle,readlist,outputhandle):        
        flag = False
        for line in inputhandle: 
                if flag:
                    if not line.startswith('>'):
                        print(line, file = outputhandle, end = '')  
                    if line.startswith('>'):
                        flag = False      
                tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)      
                if tmp:
                    index = tmp.group(1) 
                    if index not in readlist:
                        flag = True
                        print(line, file = outputhandle, end = '')
                        continue