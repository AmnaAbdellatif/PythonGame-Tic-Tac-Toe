__author__ = 'M. Bouden'
__date__ = "Déc. 2019"

"""Ce fichier permet de définir la classe Joueur permettant de jouer au jeu Tic-Tac-Toe"""

class Joueur:
   

    def __init__(self, nom, type, pion):
        """
        Méthode spéciale initialisant un nouveau joueur.
        Args:
            nom (string): Le nom du joueur.
            type (string): Le type du joueur ("Personne", "Ordinateur")
            pion (string): La forme du pion choisi (ou affecté) par le joueur ("O" ou "X")
        """

        assert isinstance(nom, str), "Joeur: nom doit être une chaîne de caractères."
        assert isinstance(type, str), "Joeur: type doit être une chaîne de caractères."
        assert type in ["Personne", "Ordinateur"], "Joueur: type doit être 'Personne' ou 'Ordinateur'."
        assert isinstance(pion, str), "Joueur: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Joueur: pion doit être 'O' ou 'X'."

        self.nom = nom      # Nom du joueur.
        self.type = type    # Type du joueur ("Personne" ou "Ordinateur").
        self.pion = pion    # Forme du pion affecté au joueur.
        self.nb_parties_gagnees = 0 # Nombre de parties gagnées par le joueur.
