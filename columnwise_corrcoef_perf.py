# Performance of column-wise correlation coefficient
#
# http://stackoverflow.com/questions/19401078/efficient-columnwise-correlation-coefficient-calculation-with-numpy
#
# Ilya Kizhvatov, stackoverflow community (see attribution below) 

import numpy as np

### Functions for correlating matrix to a column
# O - (n,t) array of observations: n traces with t samples each
# P - column of n predictions

# initial version, copied from my Matlab code
def ColumnWiseCorrcoef(O, P):
    n = P.size
    DO = O - (np.sum(O, 0) / np.double(n))
    DP = P - (np.sum(P) / np.double(n))
    return np.dot(DP, DO) / np.sqrt(np.sum(DO ** 2, 0) * np.sum(DP ** 2))

# the slow naive version using the built-in function
def ColumnWiseCorrcoefNaive(O, P):
    return np.corrcoef(P,O.T)[0,1:O[0].size+1]

# improvement over the initial one from Daniel at stackoverflow.com
# note that it modifies P  (however, the gain in performance from it appears to be insignificant)
def newColumnWiseCorrcoef(O, P):
    n = P.size
    DO = O - (np.einsum('ij->j',O) / np.double(n))
    P -= (np.einsum('i->',P) / np.double(n))
    tmp = np.einsum('ij,ij->j',DO,DO)
    tmp *= np.einsum('i,i->',P,P)          #Dot or vdot doesnt really change much.
    return np.dot(P, DO) / np.sqrt(tmp)


### Functions for correlating matrix to a matrix
# O - (n,t) array of observations: n traces with t samples each
# P - (n,m) array of n predictions for each of the m candidates
# C - (optional) pre-allocated (m,t) array for correlation traces of length t for each of the m candidates

# Naively using an outer loop with the function from above, as a reference for comparing performance
def loopedNewColumnWiseCorrcoef(O, P, C):
    for i in range(0,256):
        C[i] = newColumnWiseCorrcoef(O, P[:,i])

# this one has the naive loop over columns of P internally
def AlmightyCorrcoefNaive(O, P, C):
    (n, t) = O.shape      # n traces of t samples
    (n_bis, m) = P.shape  # n predictions for each of m candidates

    DO = O - (np.sum(O, 0) / np.double(n)) # compute O - mean(O); note that mean(O) will be appleid row-wise to O
    DP = P - (np.sum(P, 0) / np.double(n)) # compute P - mean(P)

    
    for i in np.arange(0, m):
        tmp = np.sum(DO ** 2, 0)
        tmp *= np.sum(DP[:,i] ** 2)
        C[:,i] = np.dot(DP[:,i], DO) / np.sqrt(tmp)

# here the loop is avoided by matrix operations
# returns (m,t) correaltion matrix of m traces t samples each
def AlmightyCorrcoef(O, P):
    (n, t) = O.shape      # n traces of t samples
    (n_bis, m) = P.shape  # n predictions for each of m candidates

    DO = O - (np.sum(O, 0) / np.double(n)) # compute O - mean(O)
    DP = P - (np.sum(P, 0) / np.double(n)) # compute P - mean(P)
    # note that mean row will be appleid row-wise to original matrices
    
    cov = np.einsum("nt,nm->tm", DO, DP)

    varO = np.sum(DO ** 2, 0)
    varP = np.sum(DP ** 2, 0)
    tmp = np.outer(varO, varP)

    return cov / np.sqrt(tmp)

# Here the einsum is applied to speed up the computations
# O - (n,t) array of n traces with t samples each
# P - (n,m) array of n predictions for each of the m candidates
# returns (m,t) correaltion matrix of m traces t samples each
def AlmightyCorrcoefEinsum(O, P):
    (n, t) = O.shape      # n traces of t samples
    (n_bis, m) = P.shape  # n predictions for each of m candidates

    DO = O - (np.einsum("nt->t", O) / np.double(n)) # compute O - mean(O)
    DP = P - (np.einsum("nm->m", P) / np.double(n)) # compute P - mean(P)
    
    cov = np.einsum("nm,nt->mt", DP, DO)

    varP = np.einsum("nm,nm->m", DP, DP)
    varO = np.einsum("nt,nt->t", DO, DO)
    tmp = np.einsum("m,t->mt", varP, varO)

    return cov / np.sqrt(tmp)

# check computation correctness
def testCorrectness():
    
    O = np.random.rand(int(1E3), int(1E2))
    P = np.random.rand(int(1E3), 256)

    C = AlmightyCorrcoefEinsum(O,P)
    firstRow = ColumnWiseCorrcoef(O,P[:, 0])
    secondRow = ColumnWiseCorrcoef(O,P[:,1])

    firstRowOk = np.allclose(C[0], firstRow)
    secondRowOk = np.allclose(C[1], secondRow)

    if firstRowOk and secondRowOk:
        print("Test passed")
    else:
        print("Test failed")

def testCorrectnessBis():
    
    O = np.random.rand(int(1E3), int(1E2))
    P = np.random.rand(int(1E3), 256)
    C = np.zeros((256, int(1E2)))

    loopedNewColumnWiseCorrcoef(O, P, C)
    Z = AlmightyCorrcoefEinsum(O,P)

    if np.allclose(C,Z):
        print("Test passed")
    else:
        print("Test failed")


if __name__ == '__main__':

    import timeit
    import sys

    # system information
    print("Python: " + sys.version)
    print("Numpy : " + np.version.version)
    np.__config__.show()

    # setup snippet
    timingSetup = """
import numpy as np
from __main__ import AlmightyCorrcoefEinsum
O = np.random.rand(int(1E5),int(1E3))
P = np.random.rand(int(1E5), 256)
"""
    # timing
    print(min(timeit.repeat("AlmightyCorrcoefEinsum(O, P)", setup=timingSetup, repeat=3, number=1)))
