import pygame
from dialogue import Dialogue, Replique

texte = [
    [ # LEVEL 1
        [
            "Cobaye : Ma ... ma tête ...",
            "Qu’est ce que je fais ici ?"
        ],
        [
            "??? : Vous vous demandez ce que vous faites là ?"
        ],
        [
            "Cobaye : Oui je viens de le dire",
            "et vous êtes qui d’abord ?!"
        ],
        [
            "??? : Qui je suis n’est pas important,",
            "toi en revanche t’as une mission.",
            "Va au bout de ce labyrinthe."
        ],
        [
            "Cobaye : Et si je refuse ?"
        ],
        [
            "??? : Est-ce que tu as le choix ?",
            "Peux tu au moins me dire ton nom ?"
        ],
        [
            "Cobaye : Vous marquez un point et euh …",
            "C’est bizarre pourquoi je me souviens de rien"
        ],
        [
            "et vous aurez des réponses",
        ],
        [
            "??? : Une dernière chose, votre énergie se tarit vite",
            "récupérez les fruits sur votre chemin",
            "sinon vous ne sortirez pas d’ici vivant !"
        ],
        [
            "??? : Fin de transmission"
        ],
        [
            "Cobaye : Allo ???!!"
        ]
    ],
    [ # LEVEL2
        [
            "??? : Splendide ! Vous avez passé la",
            "première étape, votre question?"
        ],
        [
            "Cobaye : Pourquoi je fais tout ça !"
        ],
        [
            "??? : Vous êtes l’espoir de l’humanité !"
        ],
        [
            "Cobaye : Comment ça ?",
            "Et pourquoi je mange des fruits ?",
            "Et pourquoi il m’attaque la nuit ?"
        ],
        [
            "??? : Qu’est ce que vous racontez ?!"
        ],
        [
            "Cobaye : Rien j’ai du rêver ..."
        ],
        [
            "??? : Bon, j’espère que ce n’est rien de grave !"
        ]
    ],
    [ # LEVEL3
        [
            "Cobaye : Dites moi qui je suis !"
        ],
        [
            "??? : Je vous le révèle, vous",
            "êtes le premier prototype humain qui ne",
            "consomme que des fruits et des légumes"
        ],
        [
            "??? : Vous êtes notre meilleur espoir",
            "notre élément, et je suis le scientifique",
            "qui vous  a conçu ."
        ],
        [
            "Scientifique : Finissez le niveau et",
            "venez avec moi écrire une nouvelle",
            "page de l’humanité !"
        ],
        [
            "Cobaye : J’aimerais mieux en effet !"
        ],
        [
            "Scientifique : Allez courage !"
        ]
    ]
]


dial = []

for D in texte:
    dial.append(Dialogue())
    for R in D:
        dial[len(dial) - 1].addReplique()
        for L in R:
            dial[len(dial) - 1].addLigne(L)

def draw(i):
    if not dial[i].done:
        dial[i].draw()
