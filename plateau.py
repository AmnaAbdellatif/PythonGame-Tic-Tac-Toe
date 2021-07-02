__authors__ = "Ben Zouari Safa et Abdellatif Amna"
__date__ = "31/12/2019"


from case import Case
from random import randrange

class Plateau:
    
    def __init__(self):

        # Dictionnaire de cases.
        # La clé est une position (ligne, colonne), et la valeur est une instance de la classe Case.
        self.cases = {}

        # Appel d'une méthode qui initialise un plateau contenant des cases vides.
        self.initialiser()

    def initialiser(self):
        
        # Vider le dictionnaire (pratique si on veut recommencer le jeu).
        self.cases.clear()
        # Parcourir le dictionnaire et mettre des objets de la classe Case.
        # dont l'attribut "contenu" serait un espace (" ").
        for i in range(0, 3):
            for j in range(0, 3):
                self.cases[i,j] = Case(" ")

    def __str__(self):
    
        s = " +-0-+-1-+-2-+\n"
        for i in range(0, 3):
            s += str(i)+ "| "
            for j in range(0, 3):
                s += self.cases[(i,j)].contenu + " | "
            if i<=1:
                s += "\n +---+---+---+\n"
            else:
                s += "\n +---+---+---+"
        return s

    def non_plein(self):
        s=0 #declarer une variable pour compter le nombre de cases pleines
        for i in range(0, 3):
            for j in range(0, 3):
                if (Case.est_vide(self.cases[i,j])==True):#s'il trouve une case non pleine alors il retourne true c-a-d plateau non plein
                    return True
                else:
                    s=s+1
        if (s==9):#si les 9 cases du plateau sont pleines alors il retourne false.
            return False
    def position_valide(self, ligne, colonne):
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        
        z= (self.cases[ligne,colonne]).est_vide()
        if (z==False): #si une case donnée identifiée par sa ligne et sa colonne est vide alors sa position est valide le programme retourne true sinon false.
            return False
        else:
            return True

    def selectionner_case(self, ligne, colonne, pion):
        assert isinstance(ligne, int), "Plateau: ligne doit être un entier."
        assert isinstance(colonne, int), "Plateau: colonne doit être un entier."
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        self.cases[ligne,colonne]= Case(pion)#affecter le pion choisi dans la case identifiée par sa ligne et sa colonne appriopriée.
        
    def est_gagnant(self, pion):

        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."#verifier tous le lignes,colonnes et diagonales
        if ((self.cases[(0,0)].contenu==pion) and (self.cases[(0,1)].contenu==pion) and (self.cases[(0,2)].contenu==pion)) or((self.cases[(1,0)].contenu==pion) and (self.cases[(1,1)].contenu==pion) and (self.cases[(1,2)].contenu==pion)) or ((self.cases[(2,0)].contenu==pion) and (self.cases[(2,1)].contenu==pion) and (self.cases[(2,2)].contenu==pion)) or ((self.cases[(0,0)].contenu==pion) and (self.cases[(1,0)].contenu==pion) and (self.cases[(2,0)].contenu==pion)) or ((self.cases[(0,1)].contenu==pion) and (self.cases[(1,1)].contenu==pion) and (self.cases[(2,1)].contenu==pion)) or  ((self.cases[(0,2)].contenu==pion) and (self.cases[(1,2)].contenu==pion) and (self.cases[(2,2)].contenu==pion)) or  ((self.cases[(0,0)].contenu==pion) and (self.cases[(1,1)].contenu==pion) and (self.cases[(2,2)].contenu==pion)) or  ((self.cases[(0,2)].contenu==pion) and (self.cases[(1,1)].contenu==pion) and (self.cases[(2,0)].contenu==pion)): 
            return True
        else:
            return False

    def choisir_prochaine_case(self, pion):
        
        assert isinstance(pion, str), "Plateau: pion doit être une chaîne de caractères."
        assert pion in ["O", "X"], "Plateau: pion doit être 'O' ou 'X'."
        
        def recherche_X(): #creation d'une fct qui verifie l'existence de la pion X dans tout le plateau
            global to #declaration d'une variable globale de type booleen qui controle la possibilité de l'ajout de pion
            for i in range(0, 3):
                  a=0 #nbre de x dans la colonne
                  b=0 #nbre de cases vides dans la colonne
                  y=0 #nbre de x dans la ligne
                  t=0 #nbre de cases vides dans la ligne.
                  for j in range(0, 3):
                      if self.cases[j,i].est_X()== True: #si le contenu de la case dans la colonne est x,incrementation de a
                          a=a+1
                      if self.cases[j,i].est_vide()== True: #si le contenu de la case dans la colonne est x,incrementation de b et sauvegarde des coordonnées de cette case dans variables ligne et colonne
                          b=b+1
                          ligne=j
                          colone=i
                      if self.cases[i,j].est_X()== True: #si le contenu de la case dans la ligne est x,incrementation de y
                          y=y+1
                      if self.cases[i,j].est_vide()== True: #si le contenu de la case dans la ligne est x,incrementation de t et sauvegarde des coordonnées de cette case dans variables li et co 
                          t=t+1
                          li=i
                          co=j
                  if a==2 and b==1: #si une colonne contient deux cases contenant x et une case vide, retourner les coordonnées de cette case 
                      to=True
                      return ligne,colone
                  elif y==2 and t==1:#si une ligne contient deux cases contenant x et une case vide, retourner les coordonnées de cette case
                      to=True
                      return li,co
                  else:
                     a=0
                     b=0
                     y=0
                     t=0
                     to=False #sinon il n'ya pas d'ajout
                 
            #recherche de x dans le diagonale de droite à gauche
            if ((self.cases[0,2]).est_X()== True )and ((self.cases[1,1]).est_X()==True) and (self.position_valide(2,0)== True):
                to=True
                return int(2),int(0)
            elif ((self.cases[0,2]).est_X()== True )and ((self.cases[2,0]).est_X()== True) and (self.position_valide(1,1)==True):
                to=True
                return int(1),int(1)
            elif ((self.cases[1,1]).est_X()== True )and ((self.cases[2,0]).est_X()== True) and (self.position_valide(0,2)== True):
                to=True
                return int (0),int (2)
            else:
                to=False #sinon il n'ya pas d'ajout
             #recherche de x dans le diagonale de droite à gauche
                      
            if ((self.cases[0,0]).est_X()==True) and ((self.cases[1,1]).est_X()==True) and (self.position_valide(2,2)==True):
                to=True
                return int(2),int (2)
            elif ((self.cases[0,0]).est_X()==True) and ((self.cases[2,2]).est_X()==True) and (self.position_valide(1,1)==True):
                to=True
                return int (1) , int(1)
            elif ((self.cases[1,1]).est_X()==True) and ((self.cases[2,2]).est_X()== True) and (self.position_valide(0,0)==True):
                to=True
                return int(0),int(0)
            else:
                to=False #sinon il n'ya pas d'ajout
        def recherche_O(): #meme principe pour la recherche de o
            global bo
           
            for i in range(0, 3):
                s=0
                v=0
                h=0
                m=0
                for j in range(0, 3):
                    if self.cases[j,i].est_O()== True:
                        s=s+1
                    if self.cases[j,i].est_vide()== True:
                        v=v+1
                        l=j
                        c=i
                    if self.cases[i,j].est_O()== True:
                        h=h+1
                    if self.cases[i,j].est_vide()== True:
                        m=m+1
                        lig=i
                        col=j
                if s==2 and v==1:
                    bo=True
                    return l,c
                elif h==2 and m==1:
                    bo=True
                    return lig,col
                else:
                    v=0
                    s=0
                    h=0
                    m=0
                    bo=False
                    
                 
            #recherche de x dans le diagonale de droite à gauche
            if ((self.cases[0,2]).est_O()== True )and ((self.cases[1,1]).est_O()==True) and (self.position_valide(2,0)== True):
                bo=True
                return int(2),int(0)
            elif ((self.cases[0,2]).est_O()== True )and ((self.cases[2,0]).est_O()== True) and (self.position_valide(1,1)==True):
                bo=True
                return int(1),int(1)
            elif ((self.cases[1,1]).est_O()== True )and ((self.cases[2,0]).est_O()== True) and (self.position_valide(0,2)== True):
                bo=True
                return int (0),int (2)
            else:
                  bo=False
           #recherche de x dans le diagonale de gauche à droite          
            if ((self.cases[0,0]).est_O()==True) and ((self.cases[1,1]).est_O()==True) and (self.position_valide(2,2)==True):
                bo=True
                return int(2),int (2)
            elif ((self.cases[0,0]).est_O()==True) and ((self.cases[2,2]).est_O()==True) and (self.position_valide(1,1)==True):
                bo=True
                return int (1) , int(1)
            elif ((self.cases[1,1]).est_O()==True) and ((self.cases[2,2]).est_O()== True) and (self.position_valide(0,0)==True):
                bo=True
                return int(0),int(0)
            else:
                bo=False
                
        if pion=="O":  #si le pion de l'ordinateur est o           
            recherche_O() #appeler la fct recherche_O() pour savoir s'il y'a possibilté de gain           
            if bo==True:
                (l,c)=recherche_O()
                return l,c
            recherche_X() #appeler la fct recherche_X() pour savoir s'il y'a possibilté de bloquer l'adversaire              
            if to ==True:
                (li,col)=recherche_X()
                return li,col
            if bo==False and to==False: #sinon jouer la premiére fois de façon aleatoire
                 x=randrange(0,3)
                 y=randrange(0,3)
                 while(self.position_valide(x,y)==False): #la position aleatoire doit etre valide
                     x=randrange(0,3)
                     y=randrange(0,3)
                 return x,y

        if pion=="X": #méme principe pour jouer avec X
            recherche_X()
                        
            if to ==True:
                (l,c)=recherche_X()
                return l,c
            recherche_O()
            if bo ==True :
                (li,col)=recherche_O()
                return li,col
            if bo==False and to==False:            
                 x=randrange(0,3)
                 y=randrange(0,3)
                 while(self.position_valide(x,y)==False):
                     x=randrange(0,3)
                     y=randrange(0,3)
                 return x,y 
                
        
        
            

            
        
                        
                        
                    
                                                                 
                    
            

            
            
                                                                                                               
                           

        
