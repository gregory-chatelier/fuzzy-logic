# Système de logique flou

Ce projet est un port sous Python de l'implémentation C# d'un moteur de logique floue qui accompagne le livre [*L'Intelligence Artificielle pour les développeurs Concepts et implémentations en C#*](https://www.editions-eni.fr/livre/l-intelligence-artificielle-pour-les-developpeurs-concepts-et-implementations-en-c-2e-edition-9782409011405), par Virginie MATHIVET, ouvrage paru aux éditions ENI.

Tous les concepts sont détaillés dans le livre, le code Python ne sera pas documenté.

Cette implémentation reprend les tests et projets de tests de l'implémentation C#. Elle n'a pas fait l'objet de tests plus approfondis. Cette version Python est une migration que j'espère assez fidèle du code C#. Comme il s'agit d'une retranscription, l'écriture du code n'est pas toujours la plus *Pythonique* qui soit.



## Pourquoi cette migration ? 

Je n'ai pas trouvé de système de logique flou en Python qui soit simple à prendre en main et efficace aussi j'ai réalisé cette migration vers Python 3.6 afin de tester un système de règles flou qui permette de contrôler automatiquement la vitesse de lecture de vidéos Youtube en fonction de la fréquence en mots par minutes des orateurs et de la spécialisation des propos. L'objectif sera d'optimiser le temps de visionnage à la baisse en accélérant les temps morts et les discours lorsque le débit de paroles n'est pas trop élevé et que le langage reste assez commun. Ce projet est à venir.



## Par où commencer

Le système flou prend en entrée une liste de variables linguistiques et une liste de règles et il produit en sortie une variable linguistique.

Chaque variable peut prendre plusieurs valeurs floues (imprécises) définies sur des ensembles flous.


La logique floue permet de prendre de décisions lorsque les variables en entrée du système sont soumises à interprétation. Dans le script *example_app2.py* il s'agit de contrôler la hauteur d'ouverture d'un store en fonction de la température et de l'éclairage ambiants.



### Création un système de logique flou pour le projet.

```python
from fuzzy_system import *

system = FuzzySystem("Gestion du store")
```



### Ajout des variables linguistiques en entrée pour indiquer la température et la luminosité.

```python
print("1) Ajout des variables")
```

La température est une variable floue qui sera définie par quatre valeurs linguistiques "Froid", "Frais", "Bon", "Chaud" qui représentent des plages de valeurs sur des ensembles flous.

```python
print('Ajout de la variable linguistique "Température"')
temp = LinguisticVariable("Temperature", 0, 35)
temp.add_value(LinguisticValue("Froid", LeftFuzzySet(0, 35, 10, 12)))
temp.add_value(LinguisticValue("Frais", TrapezoidalFuzzySet(0, 35, 10, 12, 15, 17)))
temp.add_value(LinguisticValue("Bon", TrapezoidalFuzzySet(0, 35, 15, 17, 20, 25)))
temp.add_value(LinguisticValue("Chaud", RightFuzzySet(0, 35, 20, 25)))
system.add_input_variable(temp)
```

Représentation graphique des ensembles flous pour chaque valeur :
*Les coordonnées (x, y) correspondent à la température et au degré d'appartenance.* 

Par exemple la valeur "Froid" sera plus ou moins vraie (un degré entre 0 et 1) sur la plage de température entre 0 et 35 degrés. Elle sera vraie (y=1) sous 10 degrés, fausse au dessus de 12 degrés (y=0) et entre les 2 (0<y<1) entre 10 et 12 degrés.

![](C:\Users\gchat\source\repos\fuzzy_system\fuzzy_system\resources\images\linguistic_values.png)

La variable température est définie par ces 4 ensembles.

![](C:\Users\gchat\source\repos\fuzzy_system\fuzzy_system\resources\images\linguistic_variable.png)

Pour une température en entrée de 22 degrés, les ensembles pour les valeurs "Bon" et "Chaud" sont tous les deux activés, le degré d'appartenance est supérieur à zéro, par contre il ne fait ni "Froid", ni "Frais". De même à 16 degrés, il fait à la fois "Froid" et "Bon".


L'éclairage est la seconde variable floue en entrée du système, elle exprime la luminosité en Lumens sur une plage de 0 à 125 000 lumens.

```python
print('Ajout de la variable linguistique "Eclairage"')
eclair = LinguisticVariable("Eclairage", 0, 125000)
eclair.add_value(LinguisticValue("Sombre", LeftFuzzySet(0, 125000, 20000, 30000)))
eclair.add_value(LinguisticValue("Moyen", TrapezoidalFuzzySet(0, 125000, 20000, 30000, 65000, 85000)))
eclair.add_value(LinguisticValue("Fort", RightFuzzySet(0, 125000, 65000, 85000)))
system.add_input_variable(eclair)
```



### Ajout d'une variable linguistique en sortie pour indiquer la hauteur de store

Finalement le dernier ensemble flou correspond à la variable en sortie qui représente le résultat attendu pour la hauteur du store pour un store standard entre 0 et 115cm.

```python
print('Ajout de la variable linguistique "Store"')
store = LinguisticVariable("Store", 0, 115)
store.add_value(LinguisticValue("Ferme", LeftFuzzySet(0, 115, 25, 40)))
store.add_value(LinguisticValue("MiHauteur", TrapezoidalFuzzySet(0, 115, 25, 40, 85, 100)))
store.add_value(LinguisticValue("Remonte", RightFuzzySet(0, 115, 85, 100)))
system.add_output_variable(store)
```



### Ajout des règles linguistiques

La résolution du problème passe par la création de règles floues qui sont constituées d'expressions en prémisse et en conclusion. Les règles sont exprimées sous une forme textuelle, elle sont analysées pour être décomposées en expressions applicables aux valeurs floues exprimées dans chaque règle.

```python
print("2) Ajout des règles")

system.add_fuzzy_rule("IF Eclairage IS Sombre THEN Store IS Remonte")
system.add_fuzzy_rule("IF Eclairage IS Moyen AND Temperature IS Froid THEN Store IS Remonte")
system.add_fuzzy_rule("IF Eclairage IS Moyen AND Temperature IS Frais THEN Store IS Remonte")
system.add_fuzzy_rule("IF Eclairage IS Moyen AND Temperature IS Bon THEN Store IS MiHauteur")
system.add_fuzzy_rule("IF Eclairage IS Moyen AND Temperature IS Chaud THEN Store IS MiHauteur")
system.add_fuzzy_rule("IF Eclairage IS Fort AND Temperature IS Froid THEN Store IS Remonte")
system.add_fuzzy_rule("IF Eclairage IS Fort AND Temperature IS Frais THEN Store IS MiHauteur")
system.add_fuzzy_rule("IF Eclairage IS Fort AND Temperature IS Bon THEN Store IS Ferme")
system.add_fuzzy_rule("IF Eclairage IS Fort AND Temperature IS Chaud THEN Store IS Ferme")
```



### Résolution du problème

Renseigne les entrées pour une température de 21 degrés et un éclairage de 80 000 lumens. Le résultat attendu est un store plutôt fermé.

```python
print("T = 21 (80% bon, 20% chaud)")
print("E = 80 000 (25% moyen, 75% fort)")
system.set_input_variable(temp, 21)
system.set_input_variable(eclair, 80000)

print("Résultat : %s" % system.solve())
```

L'exécution retourne un résultat de 34cm pour le degré d'ouverture du store, ce qui est conforme aux attentes.

```bash
>python example_app2.py
1) Ajout des variables
Ajout de la variable linguistique "Température"
Ajout de la variable linguistique "Eclairage"
Ajout de la variable linguistique "Store"
2) Ajout des règles
9 règles ajoutées
Résolution des cas pratiques
Cas 1:
T = 21 (80% bon, 20% chaud)
E = 80 000 (25% moyen, 75% fort)
Attendu : store plutôt fermé
Résultat : 34.05864197530864
```

