#!/usr/bin/python3
import re
class Subsampling:
    def include_fa(self,inputhandle,readlist,outputhandle):        
        flag = False
        for line in inputhandle: 
                if flag:
                    if not line.startswith('>'):
                        print >> outputhandle, line.rstrip('\n')  
                    if line.startswith('>'):
                        flag = False      
                tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)      
                if tmp:
                    index = tmp.group(1) 
                    if index in readlist:
                        flag = True
                        print >> outputhandle, line.rstrip('\n')
                        continue
    
    def exclude_fa(self,inputhandle,readlist,outputhandle):        
        flag = False
        for line in inputhandle: 
                if flag:
                    if not line.startswith('>'):
                        print >> outputhandle, line.rstrip('\n')  
                    if line.startswith('>'):
                        flag = False      
                tmp = re.search(">(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)      
                if tmp:
                    index = tmp.group(1) 
                    if index not in readlist:
                        flag = True
                        print >> outputhandle, line.rstrip('\n')
                        continue

    def include_fq(self,inputhandle,readlist,outputhandle):
        flag = False
        for line in inputhandle:
                if flag:
                    if not line.startswith('@M00704'):
                        print >> outputhandle, line.rstrip('\n')
                    if line.startswith('@M00704'):
                        flag = False
                tmp = re.search("@(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)
                if tmp:
                    index = tmp.group(1)
                    if index in readlist:
                        flag = True
                        print >> outputhandle, line.rstrip('\n')
                        continue

    def exclude_fq(self,inputhandle,readlist,outputhandle):
        flag = False
        for line in inputhandle:
                if flag:
                    if not line.startswith('@M00704'):
                        print >> outputhandle, line.rstrip('\n')
                    if line.startswith('@M00704'):
                        flag = False
                tmp = re.search("@(M00704:49:000000000-AFW6D[\d\:\w\/\_\-]+)\s",line)
                if tmp:
                    index = tmp.group(1)
                    if index not in readlist:
                        flag = True
                        print >> outputhandle, line.rstrip('\n')
                        continue

