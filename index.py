import random

words = "an chemin jour chose monde ecole etat pays probleme pomme systeme jeu pouvoir tete genre probleme argent nombre gouvernement programme membre voiture enfant corps visage autres niveau porte personne guerre regarder venir voir savoir obtenir faire etre garcon recherche parti histoire utiliser trouver travailler peut appeler sentir mettre garder tourner commencer arreter mener apprendre fournir arriver aimer deplacer courir jouer pourrait creer lire permettre offrir paraitre construire tomber couper atteindre rester seul vrai americain public grand petit différent haut juste vieux propre humain standard entier bon grand jeune important tot possible entier petit fin lourd gratuit special personnel majeur disponible"
words_list = words.split()
secret_word = random.choice(words_list)
game = {
  "secret_word": secret_word,
  "guess_word": ["_"] * len(secret_word),
  "life": 10
}

print(f"{game['guess_word']} | vies: {game['life']}")

while True:
    letter = input("Entrez une lettre: ")
    print(letter)