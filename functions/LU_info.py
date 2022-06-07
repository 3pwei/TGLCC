## Definition of functions
# "LU_Processing" is used to show the land-use types on a map and count the number of land-use types. 
# I/O: 2-D classified map/ 1.return a input map 2.the types of classification 3.count number of land-use types.
def LU_info(LU_map):
    LU = np.zeros((LU_map.shape))
    LU[:] = LU_map
    for i in range(LU.shape[0]):
        for j in range(LU.shape[1]):
            if LU[i,j]!=LU[i,j]:
                LU[i,j]=-999
    unique, counts = np.unique(LU, return_counts=True)
    LU_code = unique.tolist()
    LU_counts = counts.tolist()
    LU_code.pop(0)
    LU_counts.pop(0)
    return LU_code, LU_counts
