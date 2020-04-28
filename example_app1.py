from fuzzy_system import *


system = FuzzySystem("Gestion du zoom GPS")

print("1) Ajout des variables")

print('Ajout de la variable linguistique "Distance" (de 0 à 500 000m)')
distance = LinguisticVariable("Distance", 0, 500000)
distance.add_value(LinguisticValue("Faible", LeftFuzzySet(0, 500000, 30, 50)))
distance.add_value(LinguisticValue("Moyenne", TrapezoidalFuzzySet(0, 500000, 40, 50, 100, 150)))
distance.add_value(LinguisticValue("Grande", RightFuzzySet(0, 500000, 100, 150)))
system.add_input_variable(distance)
print('Ajout de la variable linguistique "Vitesse" (de 0 à 200)')
speed = LinguisticVariable("Vitesse", 0, 200)
speed.add_value(LinguisticValue("Lente", LeftFuzzySet(0, 200, 20, 30)))
speed.add_value(LinguisticValue("PeuRapide", TrapezoidalFuzzySet(0, 200, 20, 30, 70, 80)))
speed.add_value(LinguisticValue("Rapide", TrapezoidalFuzzySet(0, 200, 70, 80, 90, 110)))
speed.add_value(LinguisticValue("TresRapide", RightFuzzySet(0, 200, 90, 110)))
system.add_input_variable(speed)
print('Ajout de la variable linguistique "Zoom" (de 1 à 5)')
zoom = LinguisticVariable("Zoom", 0, 5)
zoom.add_value(LinguisticValue("Petit", LeftFuzzySet(0, 5, 1, 2)))
zoom.add_value(LinguisticValue("Normal", TrapezoidalFuzzySet(0, 5, 1, 2, 3, 4)))
zoom.add_value(LinguisticValue("Gros", RightFuzzySet(0, 5, 3, 4)))
system.add_output_variable(zoom)

print("2) Ajout des règles")

system.add_fuzzy_rule("IF Distance IS Grande THEN Zoom IS Petit")
system.add_fuzzy_rule("IF Distance IS Faible AND Vitesse IS Lente THEN Zoom IS Normal")
system.add_fuzzy_rule("IF Distance IS Faible AND Vitesse IS PeuRapide THEN Zoom IS Normal")
system.add_fuzzy_rule("IF Distance IS Faible AND Vitesse IS Rapide THEN Zoom IS Gros")
system.add_fuzzy_rule("IF Distance IS Faible AND Vitesse IS TresRapide THEN Zoom IS Gros")
system.add_fuzzy_rule("IF Distance IS Moyenne AND Vitesse IS Lente THEN Zoom IS Petit")
system.add_fuzzy_rule("IF Distance IS Moyenne AND Vitesse IS PeuRapide THEN Zoom IS Normal")
system.add_fuzzy_rule("IF Distance IS Moyenne AND Vitesse IS Rapide THEN Zoom IS Normal")
system.add_fuzzy_rule("IF Distance IS Moyenne AND Vitesse IS TresRapide THEN Zoom IS Gros")
print("9 règles ajoutées")

print("Résolution des cas pratiques")

print("Cas 1:")
system.set_input_variable(speed, 35)
system.set_input_variable(distance, 70)
print("Résultat : %s" % system.solve())

print("Cas 2:")
system.reset_case()
system.set_input_variable(speed, 25)
system.set_input_variable(distance, 70)
print("Résultat : %s" % system.solve())

print("Cas 3:")
system.reset_case()
system.set_input_variable(speed, 72.5)
system.set_input_variable(distance, 40)
print("Résultat : %s" % system.solve())

print("Cas 4:")
system.reset_case()
system.set_input_variable(speed, 100)
system.set_input_variable(distance, 110)
print("Résultat : %s" % system.solve())

print("Cas 5:")
system.reset_case()
system.set_input_variable(speed, 45)
system.set_input_variable(distance, 160)
print("Résultat : %s" % system.solve())


print("\nDone.")