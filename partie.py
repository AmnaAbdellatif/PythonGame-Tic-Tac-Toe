-__authors__ = "Ben Zouari Safa et Abdellatif Amna"
__date__ = "31/12/2019"

from plateau import Plateau
from joueur import Joueur
import random
class Partie:

    def __init__(self):
        
        self.plateau = Plateau()    # Le plateau du jeu contenant les 9 cases.
        self.joueurs = []       # La liste des deux joueurs (initialement une liste vide).
                                # Au début du jeu, il faut ajouter les deux joueurs à cette liste.
        self.joueur_courant = None  # Le joueur courant (initialisé à une valeur nulle: None)
                                    # Pendant le jeu et à chaque tour d'un joueur,
                                    # il faut affecter à cet attribut ce joueur courant.
        self.nb_parties_nulles = 0  # Le nombre de parties nulles (aucun joueur n'a gagné).

    def jouer(self):
        print("Bienvenue au jeu Tic Tac Toe\n----------------Menu---------------\n1- Jouer avec l'ordinateur.\n2- Jouer avec une autre persone.\n0- Quitter\n-----------------------------------")
        x=self.saisir_nombre(0,2) #en prmier lieu on va appeller la fonction saisir nombre qui doit vérifier la saisie de l'entier par l'utilisateur
        if(x=="0"):               # si l'utilisateur va quitter c'est à dire va choisir 0 donc on affiche ce message  
         print("***Merci et au revoir !***")    
        elif(x =="1"):            # choisir le mode de jouer avec l'ordinateur
            y=str(input("Entrez s.v.p votre nom:?"))# déclarer une variable "y" qui va prendre le nom de joueur de type personne 
            z=self.demander_forme_pion()  #appeler la fonction demander_forme_pion pour que le joueur choisir son pion en verfiant cette pion
            player1=Joueur(y,"Personne",z)# déclarer le player1 objet de class joueur et affecter ces attribut (nom,type,pion)
            if(z=="X"):                   # si le player1 a choisi de jouer avec X
                ordi=Joueur("Colosse","Ordinateur","O") # alors ordinateur va étre jouer avec O
            elif(z=="O"):                 # si le player1 a choisi de jouer avec O
                ordi=Joueur("Colosse","Ordinateur","X")# alors ordinateur va étre jouer avec X
            self.joueurs.append(player1) #ajouter le player1 à la liste de joueurs
            self.joueurs.append(ordi)    #ajouter le ordinateur à la liste de joueurs
            self.joueur_courant= player1 # Player1 est le joueur courant c'est à dire c'est lui qui va jouer le premier
            k=0 #nombre de fois de gain pour player1
            p=0 #nombre de fois de gain pour ordinateur
            while True or (s=="O"):#boucle pour répeter le partie lorsque on choisie O = Oui et pour la prémiere fois (True)
                self.plateau.initialiser() #initilaiser le plateau pour nouvelle partie
                while ((( self.plateau.est_gagnant(self.joueurs[1].pion)== False) and (self.plateau.est_gagnant(self.joueurs[0].pion)== False))and
                       (self.plateau.non_plein()==True)): #tant qu'aucun joueur n'a gangné et le plateau n'est pas encore plein
                    self.tour(int(x))
                    if (self.joueur_courant == player1):#alterner entre Player1 et ordinateur
                        self.joueur_courant=ordi
                    else:
                        self.joueur_courant=player1

                    if (self.plateau.est_gagnant(self.joueurs[1].pion)== True):#affichage de statistique de partie si l'ordinateur a gagné
                        print(self.plateau)
                        print("------------------------------------------------------")
                        print("Partie terminée! Le joueur gagnant est:",self.joueurs[1].nom)
                        p=p+1
                        print("Parties gagnées par",self.joueurs[0].nom,":",k)
                        print("Parties gagnées par",self.joueurs[1].nom,":",p)
                        print("Parties nulles: ",self.nb_parties_nulles)
                
                    elif(self.plateau.est_gagnant(self.joueurs[0].pion)== True):#affichage de statistique de partie si Player1 est gagner
                        print(self.plateau)
                        print("------------------------------------------------------")
                        print("Partie terminée! Le joueur gagnant est:",self.joueurs[0].nom)
                        k=k+1
                        print("Parties gagnées par",self.joueurs[0].nom,":",k)
                        print("Parties gagnées par",self.joueurs[1].nom,":",p)
                        print("Parties nulles: ",self.nb_parties_nulles)
                
                    elif(self.plateau.non_plein()==False): #affichage de statistique de partie si la partie est nulle
                        print(self.plateau)
                        print("------------------------------------------------------")                       
                        print("Partie terminée! Aucun joueuer n'a gagné!")
                        self.nb_parties_nulles=self.nb_parties_nulles+1
                        print("Parties gagnées par",self.joueurs[0].nom,":",k)
                        print("Parties gagnées par",self.joueurs[1].nom,":",p)
                        print("Parties nulles: ",self.nb_parties_nulles)
                
                s=input("Voulez-vous recommencer (O,N)?") #demander au joueur si il va jouer autre fois si O repter while au début si non affichier un message
                s=s.upper()
                if(s=="N"):
                    print("***Merci et au revoir !***")
                    break
    
        elif(x =="2"):  # choisir le mode de jouer avec un autre joueur
            y=str(input("Entrez s.v.p votre nom:?"))# déclarer une variable "y" qui va prend le nom de joueur1 de type personne
            z=self.demander_forme_pion() #appeler la fonction demander_forme_pion pour que le joueur choisir son pion en verfiant cette pion
            player1=Joueur(y,"Personne",z) # déclarer le player1 objet de class joueur et affecter ces attribut (nom,type,pion)
            a=str(input("Entrez s.v.p le nom de l'autre joueur:?"))# déclarer une variable "a" qui va prend le nom de joueur2 de type personne
            if(z=="X"): # si le player1 a choisi de jouer avec X
                player2=Joueur(a,"Personne","O")# alors Player2 va étre jouer avec O
            elif(z=="O"):
                player2=Joueur(a,"Personne","X")
            self.joueurs.append(player1)#ajouter Player1 et player2 à la liste de joueurs
            self.joueurs.append(player2)
            self.joueur_courant=random.choice(self.joueurs)#choisir de façon aléatoire qui va jouer le premier
            k=0
            p=0
            while True or (s=="O"):
                self.plateau.initialiser()
                while ((( self.plateau.est_gagnant(self.joueurs[1].pion)== False) and (self.plateau.est_gagnant(self.joueurs[0].pion)== False))and(self.plateau.non_plein()==True)):
                    self.tour(int(x))
                    if (self.joueur_courant == player1):
                        self.joueur_courant=player2
                    else:
                        self.joueur_courant=player1

                    if (self.plateau.est_gagnant(self.joueurs[1].pion)== True):
                        print(self.plateau)
                        print("------------------------------------------------------")
                        print("Partie terminée! Le joueur gagnant est:",self.joueurs[1].nom)
                        p=p+1
                        print("Parties gagnées par",self.joueurs[0].nom,":",k)
                        print("Parties gagnées par",self.joueurs[1].nom,":",p)
                        print("Parties nulles: ",self.nb_parties_nulles)
                
                    elif(self.plateau.est_gagnant(self.joueurs[0].pion)== True):
                        print(self.plateau)
                        print("------------------------------------------------------")
                        print("Partie terminée! Le joueur gagnant est:",self.joueurs[0].nom)
                        k=k+1
                        print("Parties gagnées par",self.joueurs[0].nom,":",k)
                        print("Parties gagnées par",self.joueurs[1].nom,":",p)
                        print("Parties nulles: ",self.nb_parties_nulles)
                
                    elif(self.plateau.non_plein()==False):
                        print(self.plateau)
                        print("------------------------------------------------------")
                        print("Partie terminée! Aucun joueuer n'a gagné!")
                        self.nb_parties_nulles=self.nb_parties_nulles+1
                        print("Parties gagnées par",self.joueurs[0].nom,":",k)
                        print("Parties gagnées par",self.joueurs[1].nom,":",p)
                        print("Parties nulles: ",self.nb_parties_nulles)
                s=input("Voulez-vous recommencer (O,N)?")
                s=s.upper()
                if (s=="N"):
                    print("***Merci et au revoir !***")
                    break                
                
    def saisir_nombre(self, nb_min, nb_max):
        assert isinstance(nb_min, int), "Partie: nb_min doit être un entier."
        assert isinstance(nb_max, int), "Partie: nb_max doit être un entier."
        x=(input("entrez s.v.p un nombre entre 0 et 2:?")) #demander au joueur de choisir un nombre entre 0 et 2
        while(isinstance(x, str) and (x.isnumeric()== False)or (int(x)<nb_min)or(int(x)>nb_max)): #la condition pour verifier que l'input ne doit pas etre une chaine
                                                                                                  #et dont l'intervalle de nb ne doit pas etre inferieur à nb_min ou superieur à nb_max
            print("***Valeur incorrecte!***")
            x=(input("entrez s.v.p un nombre entre 0 et 2:?"))
        return x
            
    def demander_forme_pion(self):
       z=str(input("sélectionnez s.v.p la forme de pion (X,O) :?"))#demander à l'utilisateur de choisir un pion
       z=z.upper() #le pion peut etre entrée en majuscule ou miniscule
       while (z not in ["X","O"]):#tant que le choix n'est pas un pion
           print("erreur")#cet message va etre afficher
           z=str(input("sélectionnez s.v.p la forme de pion (X,O) :?"))#demander au joueur de repeter une autre fois
           z=z.upper()
       return z
    
    def tour(self, choix):
       
        assert isinstance(choix, int), "Partie: choix doit être un entier."
        assert choix in [1, 2], "Partie: choix doit être 1 ou 2."
        print(self.plateau)#afficher le plateau
        if ( choix==1):#si le joueur a choisi de joueur avec l'ordinateur
            j=self.joueur_courant
            if(j==self.joueurs[1]):
                #si le joueur actuel est l'ordinateur
                print("c’est le tour de l’ordinateur Colosse!") 
                (l,c)=self.plateau.choisir_prochaine_case(self.joueurs[1].pion)#appeler la fct choisir prochaine case de class plateau pour que l'ordinateur choisi la meilleure position
                self.plateau.selectionner_case(l,c,self.joueurs[1].pion)#appeler la fct selectionner case pour afficher le pion choisi par l'ordinateur dans cette case
            elif(j==self.joueurs[0]):#si le joueur actuel est player1
                (l,c)=self.demander_postion()#appeler la fct demander position de class partie pour que player1 choisi sa position
                self.plateau.selectionner_case(l,c,self.joueurs[0].pion)#appeler la fct selectionner case pour afficher le pion choisi par player1 dans cette case
        elif (choix==2):#si le joueur a choisi de joueur avec un autre joueur
            j=self.joueur_courant
            if(j==self.joueurs[0]):#si le joueur actuel est player1
                (l,c)=self.demander_postion()#appeler la fct demander position de class partie pour que player1 choisi sa position
                self.plateau.selectionner_case(l,c,self.joueurs[0].pion)#appeler la fct selectionner case pour afficher le pion choisi par player1 dans cette case
            elif(j==self.joueurs[1]):#si le joueur actuel est player2
                (l,c)=self.demander_postion()#appeler la fct demander position de class partie pour que player2 choisi sa position
                self.plateau.selectionner_case(l,c,self.joueurs[1].pion)#appeler la fct selectionner case pour afficher le pion choisi par player2 dans cette case
    def demander_postion(self):

        print(self.joueur_courant.nom,":Entrez s.v.p les coordonnées de la case à utiliser")#informer le joueur courant d'entrer les coordonnées de la case
        print("Numéro de la ligne:",end='')#demander au joueur d'entrer le numero de la ligne et l'utilisation de "end" permet d'eviter le retour à la ligne
        l=(self.saisir_nombre(0,2))#appeler la fct saisir_nombre
        print("Numéro de la colonne:",end='')
        c=(self.saisir_nombre(0,2))
        while (self.plateau.position_valide(int(l),int(c))==False):#tant que la position entrée par le joueur n'est pas valide
            print("position invalide")

            print("Numéro de la ligne:",end='')#demander d'entrer les coordonnées de la case une autre fois
            l=(self.saisir_nombre(0,2))
            print("Numéro de la colonne:",end='')
            c=(self.saisir_nombre(0,2))
        return int(l),int(c)

if __name__ == "__main__":
    # Point d'entrée du programme.
    # On initialise une nouvelle partie, et on appelle la méthode jouer().
    partie = Partie()
    partie.jouer()

