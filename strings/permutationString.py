
def permutationByIteration(elems):
    level = [elems[0]]
    for i in range(1, len(elems)):
        nlist = []
        for item in level:
            nlist.append(item+elems[i])
            pass 

        #  Incomplete 