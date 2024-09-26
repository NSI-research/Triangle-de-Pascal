
def Pascal(N, Liste=[]):
    if N == 0:
        Liste.append([1])
        return Liste
    Liste = Pascal(N-1, Liste)
    Liste.append([1])
    for i in range(len(Liste[N-1])-1):
        Liste[-1].append(Liste[N-1][i]+Liste[N-1][i+1])
    Liste[-1].append(1)
    return Liste
