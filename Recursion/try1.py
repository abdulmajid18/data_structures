from functools import reduce
import time

def smooth(inlist, h):
    """ This function performs a basic smoothing
    of inlist and returns the result (outlist).
    Both lists have the same length, N. Each
    item in inlist is assumed to have type 'float'
    and 'h' is assumed to be an integer. For each
    i, outlist[i] will be the average of inlist[k]
    over all k that satisfy i-h <= k <= i+h
    and 0 <= k <= N-1. """

    N = len(inlist)
    # outlist stores the average for individual ith element
    outlist = [0] * (N)
    # iterate from the begining index and stop at the end index
    for i in range(0,N):
        # store the lower range of i-h in variable lower_k
        lower_k  = i - h
        # store the upper range of i+h in variable higher_k
        higher_k = i + h
        # check k constraint ie 0 <= k <= N-1
        if lower_k <  0:
            # if lower_k < 0 set lower_k = 0
            lower_k = 0
        if higher_k > (N - 1):
            # if higher_k > N-1 it exceeds the given range so reduce it to n-1
            higher_k = N - 1
        # obtain the sub array that contains the given k range
        average =  sum(inlist[lower_k:higher_k+1]) / len(inlist[lower_k:higher_k+1])
        outlist[i] = average
    print(f"{outlist}")
    return outlist



# Grab Currrent Time Before Running the Code
# Grab Currrent Time Before Running the Code
start = time.time_ns()

inlist = [x for x in range(1,21)]
smooth(inlist, 2)


# Grab Currrent Time After Running the Code
end = time.time_ns()

#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))