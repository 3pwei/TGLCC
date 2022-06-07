# "LUSS" is used to calculate the posibility of future land-use change(PLC) in LU_code = [1, 2, 4, 8, 13, 26, 52]
# I/O: 2-D classified map/ 7-D PLC map(base on 7 classifications)
# LU_codes are represented as following [1] Forest [2]Grass [4]Agriculture [8]City [13]Water [26]Bare Soil [52]Agriculture(Irrigate)

import numpy as np

def PLC(LU_map,LU_code):
    LU = LU_map
    array = np.zeros((len(LU_code),LU.shape[0],LU.shape[1]))
    
    for i in range(LU.shape[0]):
        for j in range(LU.shape[1]):
            for k in range(len(LU_code)):
                if LU[i,j] == LU_code[k]:
                    array[k,i,j]=array[k,i,j]+1
                    try:
                        array[k,i+1,j]=array[k,i+1,j]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i,j+1]=array[k,i,j+1]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i+1,j+1]=array[k,i+1,j+1]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i-1,j]=array[k,i-1,j]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i,j-1]=array[k,i,j-1]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i-1,j-1]=array[k,i-1,j-1]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i+1,j-1]=array[k,i+1,j-1]+1
                    except IndexError:
                        pass
                    try:
                        array[k,i-1,j+1]=array[k,i-1,j+1]+1
                    except IndexError:
                        pass 
        
    PLUSS = (array/9*100)
    return PLUSS

