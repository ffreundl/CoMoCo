# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 08:48:48 2018

@author: Frederic Freundler 
"""

from __future__ import print_function  # Only necessary in Python 2

import biolog  # import biolog for log messages
import numpy as np  # Import numpy as np

def isMagic(M):
    biolog.info("The M matrix is : \n{}".format(M))
    biolog.info("Its size is {}.".format(len(M)))

    rows = list(range(len(M)))

    rowsums = [] # creates an empty list to list the sums on rows
    colsums = [] # creates an empty list to list the sums on columns
    diagsum = 0 # creates a variable for the sum on the diagonal of the matrix
    for i in rows: # iterates on rows indices
        tempsum = 0 # creates a temporary variable to contain the sum of this row
        tempcol = 0 # creates a temporary variable to contain the sum of this colums
        for j in rows: # iterates on columns indices (which are the same as for rows since it's a square matrix)
            tempsum += M[i][j]
            tempcol += M[j][i]
        rowsums.append(tempsum)
        colsums.append(tempcol)
        diagsum += M[i][i]
    biolog.info("The sums on every row is: {}.".format(rowsums))
    biolog.info("The sums on every column is: {}.".format(colsums))
    biolog.info("The sum of the diagonal elements of the matrix is : {}.".format(diagsum))

    zeros = np.array(np.zeros(len(rows), int)) # creates an numpy array of 0 of type int for comparison
    trial = (np.array(rowsums) - np.array(colsums)) # subtracts the sums on rows and that on columns. Shoulc result in a null array if the matrix is magic.
    truth = (trial == zeros) # = true if the preceding subtraction is indeed null, false else.
    if((truth.all()) and ((diagsum - rowsums[0]) == 0)): # Condition: sums of every row and column must equal that of diagonal
        biolog.info("The matrix is a magic square! Yeaaay! Good for you... good for you...")
        return True
    else:
        biolog.error("Your matrix is not a magic square. It's rubbish.")
        return False