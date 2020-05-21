#!/usr/bin/env python3
#-*-coding:utf-8 -*-


import argparse
import sys
from stats_printer import *
#from utilis import *



#TODO Implémenter un mode interactif qui permettra de faire les choses décrites dans le README.md

def check_user_is_present(user, obj_discussion):
    for author in obj_discussion.get_authors():
        if user.lower() == author.lower():
            return True

    return False        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Affiche des statistiques sur une discussion whatsapp" + 
                                    " importée au format txt")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="Affiche des informations sur" + 
                        " l'execution du programme")
    group.add_argument("-q", "--quiet", action="store_true", help="Rend le programme verbeux")                    
    parser.add_argument("file_name", type=str, help="Le nom du fichier à analyser")
    parser.add_argument("user", type=str, nargs='?', help="Le nom de l'utilisateur dont vous voulez la satistique",
                        default=None)

    # On récupère la liste totale des arguments
    args = parser.parse_args()
    file_name = args.file_name
    user = args.user

    # On crée un objet de type discussion
    try:
        w_discussion = Discussion(file_name)
    except FileNotFoundException:
        print("[Stats printer]: Le chemin de fichier spécifié n'est pas valide")
        print("[Stats printer]: Veuillez relancer le script en reprécisant un chemin valide")
        sys.exit(0)

    if user:
        # On vérifie si le user fait partir du dialogue
        if (check_user_is_present(user, w_discussion)):
            AUTHOR = user
        else:
            print("[Stats printer]: L'user précisé ne fait pas partir du dialogue")
            sys.exit(0)

    # On affiche les statistiques globaux
    print("################ GLOBAL STATS #######################\n")
    for key, functions in GlobalStatPrinter().dispatcher.items():
        # On exécute la fonction
        if key == 'emoji_finder':
            continue
        functions(w_discussion)
        print("\n")

    print("################ INDIVIDUAL STATS * {} #######################\n".)

    messages_number_author(obj_discussion,AUTHOR)
        
    print("\n")
    # # On affiche les statistiques personnalisées
    # for function in IndividualStatPrinter.dispatcher.values():
    #     # On exécute la fonction
    #     function()
    #     print("\n"*2)

    print("Merci d'avoir utilisé ce programme. Good bye")          


