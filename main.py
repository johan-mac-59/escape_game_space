import random
CODE_FINAL = "013"

def perdre_vie():
    """Retire une vie et l'annonce."""
    global vies
    vies -= 1
    if vies > 0 :
      return print(f"Vous avez perdu une vie, il vous en reste {vies}")
    if vies <= 0:
      return print(f"L'oxygène vient à manquer....\n---------------------------\n       GAME OVER \n---------------------------")

def afficher_inventaire():
    """Affiche proprement la liste des objets."""
    texte_inventaire = f"Voici la liste des objets de votre inventaire :\n"
    for objet in inventaire :
      texte_inventaire += objet+"\n"
    return print(texte_inventaire)

def normaliser(texte):
    """Prepare un texte pour la comparaison (majuscules, espaces)."""
    texte=texte.lower()
    texte=texte.strip()
    return texte

def salle_1():
    print("""
        ===🛰 Bienvenue dans l'Escape Game 🚀 ===
        Vous êtes dans une station spatiale. Il y a un problème avec le module de recyclage d'air. 😨
        Le mode survie est enclenché, vous devez retourner dans la navette de sauvetage qui possède un système actif et autonome.
        Pour vous en sortir vivant, vous devez passer d'une pièce à une autre pour atteindre la navette.
        Répondez aux enigmes pour débloquer l'ouverture des sas.
        Commandes possibles : 'inventaire'👜, 'indice'💡
        """)
    print("Pour quitter la zone actuelle, vous devez trouver le code du sas.")
    print("Le code est compris entre 1 et 50")
    print("A tout moment, vous pouvez demander un indice en tapant 'indice'.")
    print("Vous démarrez avec 7 vies.")

    nb_secret = random.randint(1,50)

    while vies > 0:
        reponse = input("⏳ Quel est le code du sas / commande : \n")
        reponse = normaliser(reponse)
        if reponse == "inventaire":
                afficher_inventaire()
        elif reponse == "indice":
            print(f"Indice: le nombre est entre {nb_secret-random.randint(0,7)} et {nb_secret+random.randint(0,7)}")
            perdre_vie()
        else:
            nb = int(reponse)
            if nb == nb_secret:
                print("Bravo, vous avez gagné un marteau [0]👏")
                inventaire.append("un marteau [0]")
                break
            elif nb > nb_secret:
                print("C'est plus petit")
                perdre_vie()
            else:
                print("C'est plus grand")
                perdre_vie()

    return

def salle_2():
    global inventaire

    print("\nVous arrivez dans la salle du réacteur ☢️")
    print("Vous devez remettre l'électricité pour ouvrir la porte")
    print("Trouvez la fréquence secrète entre 1 et 100.")
    print("Un post-it collé sur coin de l'écran indique : nombre de 2 chiffres dont l'un est le double de l'autre.")
    print("Vous pouvez consulter l'indice à tout moment via la commande 'indice'.")
    print("Votre code :")

    nombre_secret = 42

    while vies > 0 :

        reponse = input("> ")

        if reponse.lower() == "inventaire":
            afficher_inventaire()
            continue

        if reponse.lower() == "indice":
            perdre_vie()
            print("💡 multiple de 2 mais pas de 4")
            continue

        try:
            nombre = int(reponse)

            if nombre == nombre_secret:
                print("✅ Réacteur redémarré !")
                inventaire.append("Cellule d'énergie [1]")
                return "Vous ramassez la cellule d'énergie [1]👏"

            elif nombre < nombre_secret:
                print("⬆️ Plus haut")
                perdre_vie()

            else:
                print("⬇️ Plus bas")
                perdre_vie()

        except:
            print("⏳Entrez un nombre.")

def salle_3():
  print("\nvous arrivez au hangar.")
  print("L'oxygnène a atteint un niveau critique.")
  print("Vous enfilez une combinaison 🧑‍🚀, ce qui vous redonne une petite réserve d'air.")
  print("Pour pouvoir sortir de la station, vous allez devoir déverrouiller la porte du hangar.")
  print("Sur la console de la porte, vous voyez que l'ouverture vous réclame un mot de passe.")
  print("Vous testez le code 123456 mais rien ne se passe.")
  print("Vous tentez la réponse à la question mystère.")
  print("La voici :")
  question_mystere()
  return

def question_mystere():
  while vies > 0 :
    reponse_myst = input ("⏳Qui a fait le premier pas sur la lune ?\nEcris indice si tu souhaites un indice.\n")
    reponse_myst=normaliser(reponse_myst)
    if reponse_myst == "inventaire":
      afficher_inventaire()
    elif reponse_myst == "indice":
      print("Voici un indice : \nUn petit pas pour l'homme, un grand pas pour l'humanité.\nCeci vous coûte une vie")
      perdre_vie()
    else :
        if reponse_myst == "neil armstrong" or reponse_myst=="armstrong":
          print(f"!!! déverrouillage du sas !!!")
          print("décompression dans 10... 9....")
          print(f"Vous courez vers la navette !")
          print("Vous récupérez une clé à pipe de taille [3]👏")
          global inventaire
          inventaire.append("clé à pipe de taille [3]")
          break
        else :
          print("Ceci n'est pas la bonne réponse")
          print("La console vous envoie une décharge électrique !")
          perdre_vie()
  return

def porte_de_sortie():
    print("""\nVous arrivez devant la navette de secours.
La porte est verrouillée.
A l'aide des objets trouvés précédemment, trouvez le code de déverrouillage.
A tout moment, vouc pouvez consulter votre inventaire""")
    while vies > 0 :
      code_navette = input("Code de la navette : \n")
      code_navette = normaliser(code_navette)
      if code_navette == "inventaire":
        afficher_inventaire()
      elif code_navette == CODE_FINAL:
        print("""\n
La porte de la navette s'ouvre.
Le décompte se poursuit... Décompression dans 5...4....
Vous entrez, fermez la porte, vous vous jetez sur le poste de pilotage.
Vous démarrez la navette alors que le sas du hangar est en train de s'ouvrir
Vous quittez la station spatiale.
Au loin, vous apercevez la Terre, vous en rejoindrez bientôt la surface.
Bravo !!! 🙌"""
          )
        break
      else :
        print("Code incorrect !")
        perdre_vie()

    return

def jouer():
    global vies
    global inventaire
    inventaire = []
    vies = 7

    salle_1()
    if vies > 0:
      salle_2()
    if vies > 0:
      salle_3()
    if vies > 0:
      porte_de_sortie()

    return

jouer()