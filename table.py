tab=["bonjour",33,{'age':22,'nom':'ahmed'},44.5]
print(tab)
objet={"pays":'tunisie',"capitale":"Tunis"}
objet2={"pays":'Iraq',"capitale":"Baghdad"}
pays=[]
pays.append(objet) #ajouter un élément
pays.append(objet2)
print(pays) 
simple=[0,10,12,13,4]
print(simple[1])
simple.insert(2,6) #inséré dans un indice
print(simple)
simple.remove(6) #éliminer un élément
print(simple)
print({"pays":'tunisie',"capitale":"Tunis"} in pays) # verifier l'existance
print(len(tab))
print("le maximum du tableau est %d et le minimum est %d la somme est %d"%(max(simple),min(simple),sum(simple))) #min max somme
print(sorted(simple)) # tri
print(list(reversed(simple))) # inversion