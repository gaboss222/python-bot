======================
    Tic-Tac-Toe bot
======================

Par Gabriel Griesser
et Florian Fasmeyer


----------------
   Introduction
----------------

Ce bot permet de jouer une partie de Tic-Tac-Toe sur Discord.

Le joueur peut s�lectionner la case qu'il veut cocher en entrant
sa position sur la grille, exemple: "a1"

Le fichier TTTBot.py g�re la connexion avec le serveur, le fichier ticTacToe.py
g�re la partie de ticTacToe.

Le code est absolument ignoble mais il fonctionne. Il est temps d'apprendre le zen
de python!

Une version avec AI pourrait-�tre impl�menter  pourrait �tre imagin�e
(un peu trop nul pour le faire..)

L'AI calculerait, � chaque coup (dans la m�thode botPlay()).
Il prendrait une copy du board, puis testerais chaque case.
Si deux cases c�te-�-c�te sont identiques ('X' ou 'O'), il pose son 'O' dans la case.
Puis il appellerait winCondition() pour checker si le bot � gagn� (3 rond d'affil�).
Si c'est le cas, il applique le changement sur le vrai board, et gagne la partie.
Sinon, il check si il a une autre possibilit� de gagner (2 'O' c�te-�-c�te) et essaie dans une autre case si une possibilit� est trouv�e.
Si il n'y a plus de possibilit�, il check si il y a 2 'X' et poserait son 'O' pour contrer le coup adverse.
