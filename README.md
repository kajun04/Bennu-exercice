/*[
 * Copyright 1986 - 1993, 1998, 2004   Thomas Williams, Colin Kelley
 *
 * Permission to use, copy, and distribute this software and its
 * documentation for any purpose with or without fee is hereby granted,
 * provided that the above copyright notice appear in all copies and
 * that both that copyright notice and this permission notice appear
 * in supporting documentation.
 *
 * Permission to modify the software is granted, but not the right to
 * distribute the complete modified source code.  Modifications are to
 * be distributed as patches to the released version.  Permission to
 * distribute binaries produced by compiling modified sources is granted,
 * provided you
 *   1. distribute the corresponding source modifications from the
 *    released version in the form of a patch file along with the binaries,
 *   2. add special version identification to distinguish your version
 *    in addition to the base release version number,
 *   3. provide your name and address as the primary contact for the
 *    support of your modified version, and
 *   4. retain our contact information in regard to use of the base
 *    software.
 * Permission to distribute the released version of the source code along
 * with corresponding source modifications in the form of a patch file is
 * granted with same provisions 2 through 4 for binary distributions.
 *
 * This software is provided "as is" without express or implied warranty
 * to the extent permitted by applicable law.
]*/

/*
** Author: DOGBE KOKOU JUNIOR
** Email: kajunscott@gmail.com
**
*/


* stats_printer est un programme affichant des statisques sur des discussions whatsapp ou de n'importe quel réseau social

* ...extensible: stats_printer est un programme extensible. Il vient avec un certain nombre de fonctions permetttant d'afficher des statisques mais si vous êtes développeurs python, en suivant
quelques règles, vous pouvez ajouter le vôtre.


* ...facile à utiliser: Il vient avec un programme en ligne de commande. En gros, vous pouvez l'utiliser comme n'importe quel programme linux. Vous pouvez demandez l'aide avec l'option -h pour voir toutes les fonctionnalités qu'il ofrre.

* ...fortement customisable: Vous pouvez avec quelques options changer son comportement par défaut(par défaut, il est conçu pour n'analyser que des discussions du réseau social whatsapp mais si vous précisez le bon argument en paramètre il pourra analyser d'autres discussion comme par exemple celle du réseau snapchat)


## Comment l'utiliser
Pour l'utiliser, vu qu'il n'est pas installé sur la machine,
1.  Ouvrer un terminal dans le dossier dans lequel se trouve ses fichiers, faites chmod +x stats.py
2.  Saisissez la commande
2.1      ./stats.py pour entrer dans son mode interactif
2.2      ./stats.py file_name pour afficher toutes les statistiques implémentées dans le module
2.2      ./stats.py -h pour voir la liste des commandes possibles. Ce qui vous permetrra aussi de choisir le type de statisque que vous voulez afficher.


### Comment créer un plugin
Le principe de création de plugins utilisé ici est simple. Il est basé sur le pattern dispatcher
La première chose que vous devez savoir c'est comment nous avons organisé en interne l'objet
représentant la discussion
# objet représentant la discussion et l'objet discussion
L'objet contenant la discussion est un dictionnaire qui est sous cette forme 
discuss: dict = { name_of_author(str): messages_list(list) }
messages_list[ { message_element: Message } ]
message{
    'date': str
    'time': str
    'message': str
    
    get_date: function
    get_time: function
    get_message: function
    set_date: function
    set_time: function
    set_message: function
    contains: function
}
Méthodes de la class Discussion
get_discussion(): Renvoie discuss
get_all_messages(): Renvoie la liste de tous les messages
get_authors(): Renvoie la liste de tous les auteurs
get_messages_by_author: Renvoie la liste totale des méssages écrits par author

*** Il y a deux sortes de plugins. 
1.  Les plugins globaux: Ce sont les plugins qui n'ont pas besoin de savoir qui a envoyé tel message
    par exemple, une fonction affichant le nombre total de messages n'a pas besoin de connaitre l'auteur des messages
2.  Les plugins personnalisés: Ce sont les plugins utilisés quand le nom d'un quelconque utilisateur
    est précisé dans la ligne de commande avec l'option --user. Sinon, choisit un user au hasard

Pour notre petit programme, un plugin, c'est juste une fonction prenant en paramètre l'objet discussion
et décorée par soit @GlobalStatPrinter.register('nom_du_plugin') s'il s'agit de plugins globaux ou soit @IndividualStatPrinter.register('nom_du_plugin) s'il s'agit de plugins individuels

#Note
IndividualStatPrinter et GlobalStatPrinter sont deux classes qui se trouvent dans le module stats_printer.py donc avant de décorer votre fonction plugin, assurez-vous de l'avoir importé

#Règle à respecter pour le nom du plugin
Le nom du plugin est une chaine de caractère en notation camel_case

Exemple:
<code>

    from stats_printer import GlobalStatPrinter
    GlobalStatPrinter.register('fuck')
    def fuck_stat_printer(obj_discussion):
        """Méthode permettant de vérifier combien de fois le mot 'fuck' est utilisé dans
        la discussion"""
        all_messages = obj_discussion.get_all_messages()
        fuck_count = 0
        for message in all_messages:
            if message.contains('fuck'):
                fuck_count = fuck_count + 1

        print("[Fuck Stat printer]: {} méssages au total contiennent le mot 'fuck'"
                .format(fuck_count))    

</code>

Dans le cas de IndividualStatPrinter, l'auteur sur lequel les méthodes doivent porter est retenu
dans la variable globale AUTHOR que vous pouvez trouver dans le module utils.py

######## TODO ############
*... Faire de sorte que l'user puisse choisir lui-même la fonction de statistique qu'il veut utiliser
*... Afficher de l'aide accessible depuis le terminal pour toutes les fonctions à afficher les stats
*... Développer le mode interactif
*... Réorganiser le code
*... Gérer le verbose mode
*... Mettre à jour les expressions régulières
