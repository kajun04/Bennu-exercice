from utils import *
from stats import AUTHOR
import argparse
import sys
import re


class GlobalStatPrinter(Dispatcher):
    """Classe définissant l'ensemble des méthodes pouvant être utilisées pour afficher
        les statistiques d'une discussion donnée
        Elle est abstraite.
    """

    @staticmethod
    @Dispatcher.register('messages_number')
    def messages_number(obj_discussion):
        """Renvoie la liste totale des méssages affichés sous forme de statisques"""
        all_messages = obj_discussion.get_all_messages()
        print("[Messages number Stats]")
        print("\tNombre total de méssages trouvés: {}".format(len(all_messages)))

    @staticmethod
    @Dispatcher.register('authors')
    def messages_author_names(obj_discussion):
        """Renvoie les noms des personnes ayant écrit les méssages"""
        
        authors_names = obj_discussion.get_authors()
        print(authors_names)
        print("[Messages author names Stats]")
        print("\tNombre total de participants: {}".format(len(authors_names)))
        print("\tNoms des auteurs des méssages:")
        for author in authors_names:
            print("\t\t**{}**".format(author))

    @staticmethod
    @Dispatcher.register('discussion_begin_end')
    def discussion_begin_end(obj_discussion):
        """Renvoie la date à laquelle la discussion a commencé et celle à laquelle elle a pris fin"""
        all_messages = obj_discussion.get_all_messages()
        print("[Discussion begin Stats]")
        print("\tDate de début de la discussion: {}"
                .format(all_messages[0].get_date()))    
        print("\tDate de fin de la discussion: {}"
                .format(all_messages[-1].get_date()))            


    @staticmethod
    @Dispatcher.register('names_authors')
    def names_of_authors(obj_discussion):
        pass

    @staticmethod
    @Dispatcher.register('emoji_finder')
    def emoji_finder(obj_discussion, emoji_code):
        pass

    @staticmethod
    @Dispatcher.register('media_counts')
    def media_counts(obj_discussion):
        """Affiche le nombre total de médias que les interlocuteurs se sont échangés entre eux"""
        all_messages = obj_discussion.get_all_messages()
        counts = 0
        for message in all_messages:
            # print(message)
            if message.get_message().strip() == "<Media omitted>":
                counts = counts + 1
        print("[Media counts Stat printer]: {} médias sont trouvés dans cette discussion".format(counts))    

### ################ INDIVIDUAL STATS ####################### ####

    ##print("################ INDIVIDUAL STATS #######################\n")
    @staticmethod
    @Dispatcher.register('messages_number_author')
    def messages_number_author(obj_discussion,):
        """Renvoie la liste totale des méssages d'un auteur affichés sous forme de statisques"""
        all_messages = obj_discussion.get_messages_by_author(AUTHOR)
        print("[Messages number Stats]")
        print("\tNombre total de méssages envoyé cet auteur: {}".format(len(all_messages)))

    @staticmethod
    @Dispatcher.register('word_counts')
    def fuck_stat_printer(obj_discussion):
        """Méthode permettant de vérifier combien de fois le mot 'fuck' est utilisé dans
        la discussion"""
        all_messages = obj_discussion.get_all_messages()
        merci_count = 0
        for message in all_messages:
            if message.contains('merci'):
                merci_count = merci_count + 1

        akpe_count = 0
        for message in all_messages:
            if message.contains('akpe'):
                akpe_count = akpe_count + 1

        nagode_count = 0
        for message in all_messages:
            if message.contains('nagode'):
                nagode_count = nagode_count + 1

        alhamdulillah_count = 0
        for message in all_messages:
            if message.contains('alhamdulillah'):
                alhamdulillah_count = alhamdulillah_count + 1

        shukran_count = 0
        for message in all_messages:
            if message.contains('shukran'):
                shukran_count = shukran_count + 1

        amen_count = 0
        for message in all_messages:
            if message.contains('amen'):
                amen_count = amen_count + 1

        shukran_count = 0
        for message in all_messages:
            if message.contains('shukran'):
                shukran_count = shukran_count + 1

        thanks_count = 0
        for message in all_messages:
            if message.contains('thanks'):
                thanks_count = thanks_count + 1

        thanks_you_count = 0
        for message in all_messages:
            if message.contains('thanks_you'):
                thanks_you_count = thanks_you_count + 1

        imela_count = 0
        for message in all_messages:
            if message.contains('imela'):
                imela_count = imela_count + 1

        print("[Merci Stat printer]: {} méssages au total contiennent le mot 'Merci'"
                .format(merci_count))
        print("[Akpe Stat printer]: {} méssages au total contiennent le mot 'Akpe'"
                .format(akpe_count))
        print("[Imela Stat printer]: {} méssages au total contiennent le mot 'Imela'"
                .format(imela_count))
        print("[Shukran Stat printer]: {} méssages au total contiennent le mot 'Shukran'"
                .format(shukran_count))
        print("[Alhamdulillah Stat printer]: {} méssages au total contiennent le mot 'Alhamdulillah'"
                .format(alhamdulillah_count))
        print("[Nagode Stat printer]: {} méssages au total contiennent le mot 'Nagode'"
                .format(nagode_count))


class IndividualStatPrinter(GlobalStatPrinter):
    """Statistisques personnalisées pour un individu"""

    def messages_number_author(obj_discussion,user):
        """Renvoie la liste totale des méssages d'un auteur affichés sous forme de statisques"""
        all_messages = obj_discussion.get_messages_by_author(user)
        print("[Messages number Stats]")
        print("\tNombre total de méssages envoyé cet auteur: {}".format(len(all_messages)))
    pass

class Message:
    """Class définissant un nouveau message"""
    # J'ai été obligé de l'implémenter parce que j'ai constaté un petit bug survenu dans mon
    # implémentation précédente
    
    def __init__(self, date, time, message):
        self.date = date
        self.time = time
        self.message = message

    def get_date(self):
        return self.date

    def get_time(self):
        return self.time

    def get_message(self):
        return self.message

    def set_message(self, message):
        self.message = message

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time

    def contains(self, pattern):
        return self.message.find(pattern)     

class Discussion:
    """Classe définissant un objet de type Discussion.
        - sa variable d'instance file_name contient le nom du fichier à partir
            duquel il est initialisé
        - sa variable discuss autre contient la discussion; les différents participants,
        la date à laquelle un tel méssage est envoyé et le message enboyé
    """

    def __init__(self, file_name=None):
        """
        self.discuss: dict = { name_of_author(str): messages_list(list) }
        self.file_name: str                    
        """
        self.file_name = file_name
        self.discuss = {}
        self.load_discussion()

    def load_discussion(self):
        """ Méthode permettant d'extraire une discussion à partir d'un fichier """
        # On vérifie si la variable file_name pointe éffectivement vers un fichier
        # Pour ce faire, on importe path du module os
        from os import path
        if path.isfile(self.file_name) is False:
            # On soulève une exception
            raise FileNotFoundException('Fichier non trouvé')

        # On ouvre le fichier
        obj_file = None
        error_type = None
        discussion_lines = []
        try:
            error_type = FILE_OPEN
            obj_file = open(self.file_name, 'r')
            # On récupère les lignes nétoyées
            discussion_lines = self.read_file_and_clean(obj_file)
            error_type = FILE_CLOSE
            obj_file.close()
        except IOError:
            # Impossible d'ouvrir le ficher
            # On affiche un méssage d'erreur et on quitte le programme
            if error_type == FILE_OPEN:
                print("[Stats printer]: Impossible d'ouvrir le fichier en mode lecture")
                print("[Stats printer]: peut-être devriez-vous changer les droits d'accès au fichier")

                # On importe sys
                import sys
                sys.exit(0)  # On quitte le programme    
            else:
                print("\t[Stats printer]: Impossible de fermer le fichier")
                print("\t[Stats printer]: toutefois nous réessayerons\n_n")      

        # On construit le dict self.discuss
        self.load_discuss(discussion_lines)

    def read_file_and_clean(self, obj_file):
        """Méthode se chargeant de lire le fichier et de le nétoyer pour eviter
            d'éventuelles erreurs plus tard
        """
        discussion_lines = []
        # On récupère les lignes de discussion
        discussion_lines = obj_file.readlines()
        # Il se pourrait qu'au début du ficher, whatsapp mette un méssage
        # du genre que la discussion est cryptée de bout en bout du coup
        # on va skipper ce type de messages
        probably_whatsapp_message = discussion_lines[0].split('PM - ')[1].strip()
        # Si c'est un message whatsapp
        if probably_whatsapp_message.startswith("Messages"):
            # Peut-être que l'utilisateur a pour nom Messages (on ne sait jamais)
            if probably_whatsapp_message.endswith("Tap for more info."):
                # On éfface le méssage
                del discussion_lines[0]

        # On enlève le caractère '\n' de la fin des lignes
        for i in range(len(discussion_lines)):
            discussion_lines[i] = discussion_lines[i][:-1]
        # On renvoie la discussion
        return discussion_lines  
                    
    def load_discuss(self, discussion_lines):
        """"Charge la discussion dans la variable self.discuss conformement 
            à son modèle de données
        """
        # TODO étendre load_dicussion de sorte que ça puissse supporter n'importe quel pattern
        # et éventuellement générer des exceptions

        # On parcours chaque ligne de la liste des messages envoyés et
        # on construit le self.discuss 
        next_i, i = 0, 0
        discuss_len = len(discussion_lines)
        expression = r"^[1-9]{1,2}/[0-9]{1,2}/[0-9]{1,2},"

        message = ""
        date_time_message = {}  # Placeholder du dict qui contiendra les infos sur la date ...
        name = ""
        be_continued = True
        while i < discuss_len:
            # Connaissant le pattern selon lequel whatsapp exporte ces discussions
            # on extrait les infos voulus en fonction de celui-ci
            # On se sert des méthodes de class list pour extraire les infos
            # On vérifie qu'il s'agit bien d'un nouveau méssage
            # Pour se faire on utilise les exceptions de python
            item = discussion_lines[i]
            try:
                if not re.match(expression, item):
                    raise NotNewMessageException('Pas un nouveau méssage')
            except NotNewMessageException:
                while (i < discuss_len and not re.match(expression, discussion_lines[i])):
                    #print("m", message)
                    message += "\n" + discussion_lines[i]
                    i += 1
                self.discuss[name][-1].set_message(message)
                be_continued = False
                
            else:
                if not be_continued:
                    item = discussion_lines[i]
                # On sait que la date est séparée de l'heure par une virgule
                # donc on cherche la position de cette virgule
                coma_pos = item.find(',')
                # On fait un slice
                date = item[:coma_pos].strip() # On extrait la date
                # On sait que l'heure est séparée du nom de la personne qui a envoyé le méssage
                # par '-'
                tiret_pos = item.find('-')
                # On fait un slice
                time = item[coma_pos+1:tiret_pos].strip() # On extrait l'heure à laquelle le message est envoyé
                # On sait que tout juste après le nom du user, il y a un ':'
                colon_pos = item[tiret_pos+1:].find(':') + tiret_pos + 1
                # On fait un slice
                name = item[tiret_pos+1:colon_pos].strip() # On extrait le nom de l'auteur du message
                # On extrait le méssage
                message = item[colon_pos+2:]
            
            # print(i, "d",date, "t", time, "n", name, "m", message)
            
            
            if name in self.discuss.keys():
                # Si nous avons enregistré des informations de la
                # part de l'utilisateur courant
                # on ajoute juste des messages à sa liste de messages.
                self.discuss[name].append(Message(date, time, message))
            else:
                
                # On crée une nouvelle entrée dans notre map
                # print("I have right")
                self.discuss[name] = list()
                # On y ajoute le premier message envoyé par l'user de nom name
                self.discuss[name].append(Message(date, time, message))
            i+=1
                

    def get_authors(self):
        """Retourne la liste totale des auteurs"""
        return list(self.discuss.keys())

    def get_messages_by_author(self, author):
        """Renvoie la liste totale des messages envoyés par personne"""
        # Si l'auteur précisé en paramètre n'existe pas, levé une exception
        if not author in self.discuss.keys():
            raise AuthorNotFoundException("L'auteur spécifié n'existe pas")
        # Sinon envoyé la liste des messages envoyés par l'auteur
        return self.discuss[author]

    def get_all_messages(self):
        """Renvoie la liste totale des messages envoyés"""
        # J'avoue que cette méthode est un peu lente surtout s'il s'agit d'une
        # discussion de groupe mais bon vu que je voulais utiliser le code précédent
        # je ne pu que faire comme ça 
        all_messages = []
        for author in self.discuss:
            # print(author)
            all_messages = all_messages + self.get_messages_by_author(author)
        return all_messages

    def get_discussion(self):
        """Renvoie le disctionnaire représentant la discussion"""
        return self.discuss            

