import numpy as np

# Étape 1 : Créez un tableau NumPy de 10 éléments
tableau = np.random.randint(1, 21, size=10)  # Crée un tableau avec des nombres aléatoires entre 1 et 20
print("Tableau initial:", tableau)

# Étape 2 : Récupérez un entier X au clavier
X = int(input("Entrez un entier X: "))

# Étape 3 : Créez les tableaux 'inf' et 'sup'
inf = tableau[tableau < X]
sup = tableau[tableau > X]

# Étape 4 : Affichez les tableaux 'inf' et 'sup'
print("Éléments inférieurs à X:", inf)
print("Éléments supérieurs à X:", sup)
print("Elements supérier à 4:",np.where(tableau>4))

# Étape 5 : Affichez le nombre des occurrences de X dans le tableau sans comparaison directe
occurrences_X = np.sum(tableau == X)
print("Nombre d'occurrences de X:", occurrences_X)
