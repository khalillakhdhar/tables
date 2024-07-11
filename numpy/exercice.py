import numpy as np

# Créer un tableau de 10 valeurs aléatoires comprises entre 3 et 100
tableau = np.random.randint(3, 101, size=10)
print("Tableau initial:", tableau)

# 1. Afficher les éléments impairs
impairs = tableau[tableau % 2 != 0]
print("Éléments impairs:", impairs)

# Récupérer un entier x au clavier
x = int(input("Entrez un entier x: "))

# 2a. Dire s'il existe dans la liste
existe = x in tableau
print(f"Le nombre {x} existe dans le tableau: {existe}")

# 2b. Afficher les éléments > à x
superieurs = tableau[tableau > x]
print(f"Éléments supérieurs à {x}:", superieurs)

# 2c. Afficher les éléments divisibles par x
divisibles = tableau[tableau % x == 0]
print(f"Éléments divisibles par {x}:", divisibles)
