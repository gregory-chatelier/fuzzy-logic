from fuzzy_system import *

system = FuzzySystem("Gestion du store")

print("1) Ajout des variables")

print('Ajout de la variable linguistique "Température"')
temp = LinguisticVariable("Temperature", 0, 35)
temp.add_value(LinguisticValue("Froid", LeftFuzzySet(0, 35, 10, 12)))
temp.add_value(LinguisticValue("Frais", TrapezoidalFuzzySet(0, 35, 10, 12, 15, 17)))
temp.add_value(LinguisticValue("Bon", TrapezoidalFuzzySet(0, 35, 15, 17, 20, 25)))
temp.add_value(LinguisticValue("Chaud", RightFuzzySet(0, 35, 20, 25)))
system.add_input_variable(temp)

print('Ajout de la variable linguistique "Eclairage"')
eclair = LinguisticVariable("Eclairage", 0, 125000)
eclair.add_value(LinguisticValue("Sombre", LeftFuzzySet(0, 125000, 20000, 30000)))
eclair.add_value(LinguisticValue("Moyen", TrapezoidalFuzzySet(0, 125000, 20000, 30000, 65000, 85000)))
eclair.add_value(LinguisticValue("Fort", RightFuzzySet(0, 125000, 65000, 85000)))
system.add_input_variable(eclair)

print('Ajout de la variable linguistique "Store"')
store = LinguisticVariable("Store", 0, 115)
store.add_value(LinguisticValue("Ferme", LeftFuzzySet(0, 115, 25, 40)))
store.add_value(LinguisticValue("MiHauteur", TrapezoidalFuzzySet(0, 115, 25, 40, 85, 100)))
store.add_value(LinguisticValue("Remonte", RightFuzzySet(0, 115, 85, 100)))
system.add_output_variable(store)


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
print("9 règles ajoutées")

print("Résolution des cas pratiques")

print("Cas 1:")
print("T = 21 (80% bon, 20% chaud)")
print("E = 80 000 (25% moyen, 75% fort)")
system.set_input_variable(temp, 21)
system.set_input_variable(eclair, 80000)
print("Attendu : store plutôt fermé")
print("Résultat : %s" % system.solve())

print("\nDone.")