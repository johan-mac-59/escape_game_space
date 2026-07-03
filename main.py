import random

# Codes couleur ANSI natifs
MAUVE = "\033[35m"
RESET = "\033[0m"
ROUGE = "\033[31m"
VERT = "\033[32m"
CYAN = "\033[36m"
JAUNE = "\033[33m"

CODE_FINAL = "013"

def perdre_vie():
    """Retire une vie et l'annonce."""
    global vies
    vies -= 1
    if vies > 0 :
      return print(f"Vous avez perdu une vie 💔, il vous en reste {vies}")
    if vies <= 0:
      return print(f"Vous n'avez plus de vie.\nL'oxygène vient à manquer....\n---------------------------\n       GAME OVER \n---------------------------")

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
        Utiliser un indice vous coûtera une vie.
        """)
    print(f"""
    {CYAN}╔══════════════════════════════════════════════════════════════╗
    ║                 🛰️  MODULE DE SURVIE - SALLE [01]             ║
    ╚══════════════════════════════════════════════════════════════╝{RESET}
    
         ______________________________________________________
        |                                                      |
        |     [ UNITÉ DE RECYCLAGE ] ⚠️ (Défaillance)          |
        |               │                                      |
        |               ▼                                      |
        |       {MAUVE}[ POSTE DE CONTRÔLE ]{RESET}                          |
        |               │                                      |
        |               ▼                                      |
        |         {VERT}╔═════════════════╗{RESET}                          |
        |         {VERT}║   SAS VERS 02   ║{RESET} 🔒 [ CODE REQUIS ]        |
        |         {VERT}╚═════════════════╝{RESET}                          |
        |______________________________________________________|
    {JAUNE}Commandes utiles :{RESET} 'inventaire' 👜, 'indice' 💡
    ----------------------------------------------------------------
    ⚙️  Pour quitter cette zone, trouvez le code d'ouverture du sas.
    ⚙️  Le code est un nombre entier compris {JAUNE}entre 1 et 50{RESET}.
    ⚙️  Vous démarrez l'aventure avec {ROUGE}7 vies{RESET} ❤️.
    """)
    print("Pour quitter la zone actuelle, vous devez trouver le code du sas.")
    print("Le code est compris entre 1 et 50")

    nb_secret = random.randint(1,50)

    while vies > 0:
        reponse = input("⏳ Quel est le code du sas / commande : \n> ")
        reponse = normaliser(reponse)
        if reponse == "inventaire":
                afficher_inventaire()
        elif reponse == "indice":
            # Calcul des bornes brutes
            borne_inf_brute = nb_secret - random.randint(1, 7)
            borne_sup_brute = nb_secret + random.randint(1, 7)

            # Sécurisation des bornes entre 1 et 100
            borne_inf = max(1, borne_inf_brute)
            borne_sup = min(100, borne_sup_brute)
            print(f"Indice: le nombre est entre {borne_inf} et {borne_sup}.\nCeci vous coûte une vie.")
            perdre_vie()
        else:
            try:
              nb = int(reponse)
              if nb == nb_secret:
                print("Bravo, vous avez gagné un marteau [0]👏")
                inventaire.append("un marteau [0]")
                break
              elif nb > nb_secret:
                print("C'est plus petit.\n >")
                perdre_vie()
              else:
                print("C'est plus grand.\n >")
                perdre_vie()
            except:
              print("⏳Entrez un nombre.\n >")
    return

def salle_2():
    global inventaire

    print(f"""
    {CYAN}╔══════════════════════════════════════════════════════════════╗
    ║                   ⚡ LA SALLE DU RÉACTEUR [02] ⚡              ║
    ╚══════════════════════════════════════════════════════════════╝{RESET}
    
         ______________________________________________________
        |                                                      |
        |     [ SAS 1 ] ───► {MAUVE}⚡ RÉACTEUR PRINCIPAL ⚡{RESET}               |
        |                           │                          |
        |                           ▼                          |
        |                       [ ÉCRAN ] 📝 (Post-it collé)   |
        |                           │                          |
        |                           ▼                          |
        |                     {VERT}╔═════════════════╗{RESET}        |
        |                     {VERT}║   SAS VERS 03   ║{RESET} 🔒 [ VERROUILLÉ ]  |
        |                     {VERT}╚═════════════════╝{RESET}        |
        |______________________________________________________|
    
    Vous arrivez dans la {MAUVE}salle du réacteur{RESET} ☢️
    Vous devez impérativement remettre l'électricité pour ouvrir la porte.
    
    ⚙️  Trouvez la fréquence secrète entre {JAUNE}1 et 100{RESET}.
    ⚙️  Un post-it collé sur le coin de l'écran indique : 
        {JAUNE}"Nombre de 2 chiffres dont l'un est le double de l'autre."{RESET}
    ⚙️  Vous pouvez consulter l'indice à tout moment via la commande 'indice'.
    Il vous reste {vies} vies ❤️     
    """)

    print("Votre code :")

    nombre_secret = 42

    while vies > 0 :

        reponse = input("> ")

        if reponse.lower() == "inventaire":
            afficher_inventaire()
            continue

        if reponse.lower() == "indice":
            perdre_vie()
            print("💡 multiple de 2 mais pas de 4.\nCeci vous coûte une vie.")
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
                print("⬇️ Plus bas.\nCeci vous coûte une vie.")
                perdre_vie()

        except:
            print("⏳Entrez un nombre.")

def salle_3():
# Affichage graphique de la salle 3
  print(f"""
    {CYAN}╔══════════════════════════════════════════════════════════════╗
    ║                   🚀 LE HANGAR PRINCIPAL [03]                ║
    ╚══════════════════════════════════════════════════════════════╝{RESET}
    
         ______________________________________________________
        |  [SAS 2] ──┐                                         |
        |            │     ___________                         |
        |            ▼    |           |    {VERT}╔═════════════════╗{RESET} |
        |        [CONSOLE]│  NAVETTE  | ── {VERT}║  PORTE DU SAS   ║{RESET} |
        |            │    | _  _  _   |    {VERT}║  (VERROUILLÉE)  ║{RESET} |
        |            ▼    |___________|    {VERT}╚═════════════════╝{RESET} |
        |   [COMBINAISONS]                                     |
        |______________________________________________________|
    
    {ROUGE}🚨 ALERTE : L'oxygène a atteint un niveau critique.{RESET}
    Vous enfilez rapidement une combinaison 🧑‍🚀, ce qui vous redonne
    une petite réserve d'air.
    
    Pour pouvoir sortir de la station, vous allez devoir déverrouiller
    la porte du hangar. Sur la console de la porte, vous voyez que
    l'ouverture vous réclame un mot de passe.
    
    Vous testez le code '123456' mais rien ne se passe...
    La console bascule et affiche une {JAUNE}question mystère{RESET}.
    """)

  print(f'Il vous reste {vies} vies. ❤️')
  print("Voici la question mystère :")
  question_mystere()
  return

def question_mystere():
  while vies > 0 :
    reponse_myst = input ("⏳Qui a fait le premier pas sur la lune ?\nEcris 'indice' si tu souhaites un indice.\n")
    reponse_myst = normaliser(reponse_myst)
    if reponse_myst == "inventaire":
      afficher_inventaire()
    elif reponse_myst == "indice":
      print("Voici un indice : \nUn petit pas pour l'homme, un grand pas pour l'humanité.\nCeci vous coûte une vie.")
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
    
    print(f"""
    {CYAN}╔══════════════════════════════════════════════════════════════╗
    ║                🚀 NAVETTE DE SECOURS - SAS FINAL             ║
    ╚══════════════════════════════════════════════════════════════╝{RESET}
    
         _________________________________________________________
        |                                                         |
        |     [ HANGAR ] ───► [ PANNEAU DE CONTRÔLE ]             |
        |                            │                            |
        |                            ▼                            |
        |                    {ROUGE}╔═══════════════════╗{RESET}                |
        |                    {ROUGE}║ PORTE DE LA NEF   ║{RESET} 🔒 [ BLOCAGE ] |
        |                    {ROUGE}║   (VERROUILLÉE)   ║{RESET}                |
        |                    {ROUGE}╚═══════════════════╝{RESET}                |
        |                            │                            |
        |                            ▼                            |
        |                     {VERT}▓▒░ ESCAPE POD ░▒▓{RESET}                  |
        |_________________________________________________________|
    
    Vous arrivez enfin devant la {CYAN}navette de secours{RESET}.
    L'alarme résonne dans toute la station... 
    
    {ROUGE}🚨 LA PORTE EST VERROUILLÉE !{RESET}
    
    À l'aide des indices et objets trouvés précédemment dans votre 
    {MAUVE}inventaire{RESET}, calculez ou déduisez le code de déverrouillage final.
    
    💡 {JAUNE}Rappel :{RESET} À tout moment, vous pouvez taper '{JAUNE}inventaire{RESET}' 👜.
    Il vous reste {vies} vies. ❤️
    """)

    while vies > 0 :
      code_navette = input("Code de la navette : \n")
      code_navette = normaliser(code_navette)
      if code_navette == "inventaire":
        afficher_inventaire()
      elif code_navette == CODE_FINAL:
        print(f"""{VERT}
    ╔══════════════════════════════════════════════════════════════╗
    ║        🎉 MISSION ACCOMPLIE - VOUS AVEZ SURVÉCU ! 🎉         ║
    ╚══════════════════════════════════════════════════════════════╝{RESET}
    {CYAN}
           .      .   *   .      .   .   .   *   .   .
        *      .      .   .   .   *   .   .   .   .
           .      .   ________   .   .   .   *
        .      .   .-'      '-._   .   .   .   .   .
           *   .'               '.   .   .
            /                     \\   .   .   *
       .   |    [NEF DE SECOURS]   |   .   .   .   .
        *  |        (ACTIVE)       |   .   .
            \\                     /   .   .   .   .
       .     '.                 .'   .   .   *
        *      '-.__________.坏'   .   .   .   .
                   //     \\\\   .   .   .   .   .
           .      //       \\\\   .   .
                 V          V   .   .   *   .
        _____________________________________________________{RESET}
                     {VERT}▄▄████████▄▄{RESET}
                   {VERT}▄██████████████▄{RESET}    .       *
                  {VERT}██████████████████{RESET}
                 {VERT}▀██████████████████▀{RESET}        .
                   {VERT}▀██████████████▀{RESET}      *
                     {VERT}▀▀████████▀▀{RESET}      {VERT}🌍 [ LA TERRE ]{RESET}
    {VERT}
    La porte de la navette s'ouvre enfin.
    Le décompte de la station se poursuit... Décompression dans 5... 4...
    
    Vous vous jetez à l'intérieur, verrouillez le sas et basculez
    les commandes sur le poste de pilotage. Les propulseurs s'allument
    alors que le hangar de la station commence à se déchirer.
    
    Vous quittez la zone à toute vitesse. Au loin, à travers le hublot,
    vous apercevez la Terre. L'air pur de sa surface n'est plus qu'à 
    quelques heures de vol.
    
    UN GRAND BRAVO, VOUS AVEZ REJOINT LA TERRE SAIN ET SAUF ! 🌍🙌
    {RESET}""")

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