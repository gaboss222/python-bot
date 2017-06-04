======================
    Tic-Tac-Toe bot
======================

Par Gabriel Griesser
et Florian Fasmeyer


----------------
   Introduction
----------------

Ce bot permet de jouer une partie de Tic-Tac-Toe sur Discord.

Le joueur peut sélectionner la case qu'il veut cocher en entrant
sa position sur la grille, exemple: "a1"

Le fichier TTTBot.py gère la connexion avec le serveur, le fichier ticTacToe.py
gère la partie de ticTacToe.

Le code est absolument ignoble mais il fonctionne. Il est temps d'apprendre le zen
de python!

Une version avec AI pourrait-être implémenter  pourrait être imaginée
(un peu trop nul pour le faire..)

L'AI calculerait, à chaque coup (dans la méthode botPlay()).
Il prendrait une copy du board, puis testerais chaque case.
Si deux cases côte-à-côte sont identiques ('X' ou 'O'), il pose son 'O' dans la case.
Puis il appellerait winCondition() pour checker si le bot à gagné (3 rond d'affilé).
Si c'est le cas, il applique le changement sur le vrai board, et gagne la partie.
Sinon, il check si il a une autre possibilité de gagner (2 'O' côte-à-côte) et essaie dans une autre case si une possibilité est trouvée.
Si il n'y a plus de possibilité, il check si il y a 2 'X' et poserait son 'O' pour contrer le coup adverse.
