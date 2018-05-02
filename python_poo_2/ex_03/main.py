import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

un_panda = [100, 5, 20, 80]
un_panda_numpy = np.array(un_panda)

print("voici un panda:\n", un_panda_numpy)

print("Voici un panda divisé par deux:\n", un_panda_numpy / 2)

famille_panda = [
    [100, 5, 20, 80], # maman panda
    [50, 2.5, 10, 40], # bébé panda
    [110, 6, 22, 80], # papa panda
]

famille_panda_numpy = np.array(famille_panda)

print("Voici la famille panda:\n", famille_panda_numpy)

print("Voici le papa panda à l'index [2]:\n", famille_panda_numpy[2])

print("Voici la taille des pattes de papa panda à l'index[2][0]:\n", famille_panda_numpy[2][0])

print("Voici la taille des pattes de papa panda à l'index[2,0]:\n", famille_panda_numpy[2,0])

famille_panda_df = pd.DataFrame(famille_panda_numpy, index = ['Paman:', 'Bebe:', 'Bapa:'], columns = ['Pattes:', 'Poil:', 'Queue:', 'Ventre:'])

print("Voici un table qui affiche les caractéristiques de la famille panda:\n", famille_panda_df)