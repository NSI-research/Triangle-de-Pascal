
def Pascal(N, Liste=[]):
    
    if N == 0:            # Cas terminal
        Liste.append([1]) # On pose le 1 du haut du triangle
        return Liste
    
    Liste = Pascal(N-1, Liste) # Appel récursif
    Liste.append([1])    # On pose le 1 de début de ligne
    
    for i in range(len(Liste[N-1])-1):
        Liste[-1].append(Liste[N-1][i]+Liste[N-1][i+1])    # On génère les valeurs intermédiaires
    
    Liste[-1].append(1)   # On pose le 1 de fin de ligne
    return Liste
