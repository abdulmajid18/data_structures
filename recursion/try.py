import time
def smooth(inlist, h):
    N = len(inlist)
    outlist = [0.0] * N

    # first h elements
    for i in range(h+1):
        outlist[i] = sum(inlist[:h+i+1]) / (h+i+1)

    # middle elements
    window = inlist[:2*h+1]
    for i in range(h+1, N-h):
        window.append(inlist[i+h])
        window.pop(0)
        outlist[i] = sum(window) / len(window)

    # last h elements
    for i in range(N-h, N):
        window.pop(0)
        outlist[i] = sum(window) / len(window)
    print(outlist)
    return outlist


# Grab Currrent Time Before Running the Code
start = time.time_ns()

inlist = [x for x in range(1,21)]
smooth(inlist, 2)


# Grab Currrent Time After Running the Code
end = time.time_ns()

#Subtract Start Time from The End Time
total_time = end - start
print("\n"+ str(total_time))