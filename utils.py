#-*-coding:utf-8 -*-

from collections import ChainMap


FILE_OPEN = 0
FILE_CLOSE = 1
AUTHOR = None

class DispatcherMeta(type):
    def __new__(mcs, name, bases, attrs):
        # Juste avant que la classe ne soit définie par Python

        # On construit le dictionnaire de callbacks en héritant ceux des
        # classes mères
        callbacks = ChainMap()
        maps = callbacks.maps
        for base in bases:
            if isinstance(base, DispatcherMeta):
                maps.extend(base.__callbacks__.maps)

        # On ajoute le dictionnaire de callbacks
        # la property "dispatcher" pour y accéder
        attrs['__callbacks__'] = callbacks
        attrs['dispatcher'] = property(lambda obj: callbacks)
        cls = super().__new__(mcs, name, bases, attrs)
        return cls

    def set_callback(cls, key, callback):
        cls.__callbacks__[key] = callback
        return callback

    def register(cls, key):
        def wrapper(callback):
            return cls.set_callback(key, callback)
        return wrapper


class Dispatcher(metaclass=DispatcherMeta):
    def dispatch(self, key, default=None):
        return self.dispatcher.get(key, default)



class FileNotFoundException(Exception):
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message

    def __str__(self):
        """On renvoie le message"""
        return self.message


class NotNewMessageException(Exception):
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message

    def __str__(self):
        """On renvoie le message"""
        return self.message
        
class AuthorNotFoundException(Exception):
    def __init__(self, message):
        """On se contente de stocker le message d'erreur"""
        self.message = message

    def __str__(self):
        """On renvoie le message"""
        return self.message

class OrganizeDict:
    """Notre dictionnaire ordonné. L'ordre des données est maintenu
    et il peut donc, contrairement aux dictionnaires usuels, être trié
    ou voir l'ordre de ses données inversées"""

    def __init__(self, base={}, **data):
        """Constructeur de notre objet. Il peut ne prendre aucun paramètre
        (dans ce cas, le dictionnaire sera vide) ou construire un dictionnaire remplis
        grâce : 
        - au dictionnaire 'base' passé en premier paramètre ;
        - aux valeurs que l'on retrouve dans 'data'. """

        self._keys = [] # Liste contenant nos clés
        self._values = []   # Liste contenant les valeurs correspondant à nos clés
        # On vérifie que 'base' est un dictionnaire exploitable
        if type(base) not in (dict, OrganizeDict):
            raise TypeError(\
                "Le type attendu est un dictionnaire (usuel ou ordonne)")
        # On récupère les données de 'base'
        for key in base:
            self[key] = base[key]

        # On récupère les données de 'data'
        for key in data:
            self[key] = data[key]       

    def __repr__(self):
        """Représentation de notre objet. C'est cette chaine qui sera affichée
        quand on saisit directement le dictionnaire dans l'interpréteur, ou en utilisant
        la fonction 'repr'"""

        string = "("
        first_round = True
        for key, value in self.item():
            if not first_round:
                string += ", " # On ajoute la virgule comme séparateur
            else:
                first_round = False
            string += repr(key) + ": " + repr(value)     
        string += ")"
        return string


    def __str__(self):
        """Fonction appelée quand on souhaite afficher le dictionnaire grâce à la
        fonction 'print' ou le convertir en chaîne grâce au constructeur 'str'.
        On redirige sur __repr__"""
        return repr(self)

    def __len__(self):
        """Renvoie la taille du dictionnaire"""
        return len(self.keys)    

    def __contains__(self, key):
        """Renvoie True si la clé est dans la liste des clés, False sinon"""
        return key in self._keys

    def __getitem__(self, key):
        """Renvoie la valeur correspondant à la clé si elle existe, lève
        une exception KeyError sinon"""

        if key not in self._keys:
            raise KeyError(\
                "La clé {} ne se trouve pas dans le dictionnaire".format(key))

    def __setitem__(self, key, value):
        """Méthode spéciale appelée quand on cherche à modifier une clé
        présente dans le dictionnaire. Si la clé n'est pas présente, on l'ajoute à
        la fin du dictionnaire"""
        if key in self._keys:
            index = self._keys.index(key)
            self._values[index] = value
        else:
            self._keys.append(key)
            self._values.append(value)

    def __delitem__(self, key):
        """Méthode appelé quand on souhaite supprimer une clé"""
        if key not in self._keys:
            raise KeyError(\
                "La clé {} ne se trouve pas dans le dictionnaire".format(key))
        else:
            index = self._keys.index(key)
            del self._keys[index]
            del self._values[index]


    def __iter__(self):
        """Méthode de parcours de l'objet. On renvoie l'itérateur des clés"""
        return iter(self._keys)

    def __add__(self, other):
        """On renvoie un nouveau dictionnaire contenant les deux dictionnaire mis bout à bout
        (d'abor self puis autre_objet)"""    
        #TODO Méthode à améliorer de sorte que ça puisse gérer les conflits
        if type(other) is not type(self):
            raise TypeError(\
                "Impossible de concaténer {} et {}".format(type(self), type(other)))
        else:
            new = OrganizeDict()

            # On commence par copier self dans le dictionnaire
            for key, value in self.items():
                new[key] = value   

            for key, value in other.items():
                new[key] = value

        return new


    def items(self):
        """Renvoie un générateur contenant les couples (key, value)"""
        for i, key in enumerate(self._keys):
            value = self._values[i]
            yield(key, value)

    def keys(self):
        """Cette méthode renvoie la liste des clés"""
        return list(self._keys)

    def values(self):
        """Cette méthode renvoie la liste des valeurs"""
        return list(self._values)

    def reverse(self):
        """Inversion du dictionnaire"""
        # On crée deux listes vides qui contiendront le nouvel ordre des clés
        # et valeurs
        keys = []
        values = []
        for key, value in self.items():
            # On ajoute les clés et valeurs au début de la liste
            keys.insert(0, key)
            values.insert(0, value)
        # On met ensuite à jour nos liste
        self._keys = keys
        self._values = values

    def sort(self):
        """Méthode permettant de trier le dictionnaire en fonction de ses clés"""
        # On trie les clés
        sorted_keys = sorted(self._keys)
        # On crée un liste de valeurs, encore vide
        values = []
        # On parcours ensuite la liste des clés triées
        for key in keys:
            value = self[key]
            values.append(value)
        # Enfin, on met à jour notre liste de clés et de valeurs
        self._keys = sorted_keys
        self.values = values            


