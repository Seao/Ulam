#-*-coding:utf-8-*-
from PIL import Image
from sympy import *
import math

# Définition des couleurs utilisées
WHITE = (0xff, 0xff, 0xff, 0xff)
BLACK = (0x00, 0x00, 0x00, 0xff)

def spiral(largeur, hauteur, img):
    # Initialisation des variables nécessaires
    x = y = 0
    # Variables de déplacement
    pos_x = 0
    pos_y = -1
    # Nombre a tester
    n = 0
    for i in range(largeur*hauteur):
        if (-largeur/2 < x <= largeur/2) and (-hauteur/2 < y <= hauteur/2):

            n += 1
            cx = (largeur/2)-x
            cy = (hauteur/2)-y

            # Test de primalité : on test si n n'est pas un nombre premier
            if isprime(n) :
                img.putpixel((cy,cx), tuple(BLACK))

        # Détermine l'orientation du déplacement à effectuer
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            pos_x, pos_y = -pos_y, pos_x
        x, y = x+pos_x, y+pos_y

# Propriétés graphique de l'image résultante
largeur = hauteur = 500
graphique = Image.new('RGBA',(largeur,hauteur),color=(WHITE))

# Appel de la fonction pour dessiner la spirale
spiral(largeur, hauteur, graphique)
graphique.show(command = 'eog')