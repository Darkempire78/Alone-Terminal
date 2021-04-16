addEvent = {
    "porte_rouge1": {
        "text": "Vous apercevez une porte dont la couleur rouge vif ne vous est pas inconnue. Va-t'elle s'ouvrir cette fois ?",
        "actions": {
            "action1": {
                "description": "Vous vous dirigez vers la porte.",
                "next_message": "Vous n'avez pas plus de chance cette fois ; porte verrouillée.",
                "health": 0,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": None,
                "require": []
            },
            "action2": {
                "description": "Ça ne sert à rien, elle est probablement encore verrouillée, vous l'ignorez.",
                "next_message": "Vous reprenez votre marche.",
                "health": 0,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "porte_rouge2": {
        "text": "Vous apercevez une porte dont la couleur rouge vif ne vous est pas inconnue. Va-t'elle s'ouvrir cette fois ?",
        "actions": {
            "action1": {
                "description": "Vous vous dirigez vers la porte.",
                "next_message": "A votre approche, la port cliquète, avant de libérer un nuage de gaz aussi rouge que la porte. Vous vous éloignez en courant et en toussant abondamment. Maudite porte ! ",
                "health": -3,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [
                    "porte_rouge1",
                    "porte_rouge2",
                    "porte_rouge3"
                ],
                "script": [],
                "zone": None,
                "require": []
            },
            "action2": {
                "description": "Ça ne sert à rien, elle est probablement encore verrouillée, vous l'ignorez.",
                "next_message": "Vous reprenez votre marche.",
                "health": 0,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "porte_rouge3": {
        "text": "Vous apercevez une porte dont la couleur rouge vif ne vous est pas inconnue. Va-t'elle s'ouvrir cette fois ?",
        "actions": {
            "action1": {
                "description": "Vous vous dirigez vers la porte.",
                "next_message": "A votre étonnement, la porte s'ouvre sans faire d'histoire à votre approche. La salle toujours rouge vive comporte une unique table blanche immaculée sur laquelle repose une bonbonne de grande taille. Vous reprenez le chemin ragaillardi après vous en être saisi.",
                "health": 0,
                "oxygen": 0,
                "loot": [
                    "bonbonne5"
                ],
                "add": [],
                "remove": [
                    "porte_rouge1",
                    "porte_rouge2",
                    "porte_rouge3"
                ],
                "script": [],
                "zone": None,
                "require": []
            },
            "action2": {
                "description": "Ça ne sert à rien, elle est probablement encore verrouillée, vous l'ignorez.",
                "next_message": "Vous reprenez votre marche.",
                "health": 0,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [
                    "porte_rouge3"
                ],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "porte_mystérieuse": {
        "text": "Une porte noir mat d'un étrange éclat attire votre attention. Elle est faite d'un métal que vous ne connaissez pas et est de très bonne facture, tranchant avec l'état de délabrement général. Elle dispose d'un lecteur de carte.",
        "actions": {
            "action1": {
                "description": "Vous introduisez la carte magnétique noire dans le lecteur.",
                "next_message": "La porte s'ouvre sans un seul bruit. Celle-ci protégeait en fait un bureau en acier trempé sur lequel repose un ordinateur qui sort de sa veille dès votre entrée dans la pièce. Celui-ci ne vous laisse accéder qu'à une unique note.  Rapport-XX/XX/XX\\  :  Le sujet s'est échappé du secteur 4. Comment est-ce possible avec le renforcement de la sécurité ? Envoyez une équipe sur place et ordonnez au personnel sans combi d'évitez la zone de h-s (à gauche à l'entrée du centre), il faudra certainement encore drainer l'oxygène pour en venir à bout. Tandis que vous méditez cette lecture vous apercevez derriere le bureau une station de soin personnel, un matériel qui coûte une fortune, en effet dès utilisation l'effet est immédiat, vous vous sentez rajeuni de 10 ans.",
                "health": 99,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    "lab",
                    "script",
                    "porte_mystérieuse"
                ],
                "script": [],
                "zone": None,
                "require": [
                    "carte_noire"
                ]
            },
            "action2": {
                "description": "Rien à faire, la porte refuse de s'ouvrir.",
                "next_message": "Vous reprenez votre marche.",
                "health": 0,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [
                    "porte_mystérieuse"
                ],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "random_drone": {
        "text": "Le drone que vous aviez aperçu précedemment s'est crashé non loin ; vous voyez sa carcasse métallique dans un petit cratère. Il est entouré de petites billes noires.",
        "actions": {
            "action1": {
                "description": "Vous passez votre chemin.",
                "next_message": "Vous reprenez votre marche.",
                "health": 0,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random_drone"
                    ]
                ],
                "script": [],
                "zone": None,
                "require": []
            },
            "action2": {
                "description": "Vous allez investiguer le crash.",
                "next_message": "A votre approche les petites billes explosent en une pluie de shrapnels ; vous en recevez deux dans les jambes. Passablement énérvé, vous reprenez votre route en maudissant cette planete.",
                "health": -3,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random_drone"
                    ]
                ],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "random11": {
        "text": "Alors que vous venez de monter au sommet d'une énième dune, vous percevez en contrebas de petits monticules de pierre qui semblent avoir surgi des sables. Plus loin derrière, sur une grande plateforme de pierre noire, repose une machierie complexe dont les tuyaux reflétent l'éclat du soleil.",
        "actions": {
            "action1": {
                "description": "Vous traversez la zone de monticules pour arriver jusqu'à la machine.",
                "next_message": "Alors que vous n'êtes qu'à mi-chemin, de petites billes noires commencent à sortir en nombre des monticules puis soudainement à exploser, couvrant l'air de shrapnels. Vous courrez aussi vite que vos jambes vous le permettent. Arrivé à la machine vous êtes hors de danger, mais vous avez malheureusement reçu plusieurs éclats vous faisant douloureusement souffrir.",
                "health": -3,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random11"
                    ]
                ],
                "script": [
                    "desert7"
                ],
                "zone": None,
                "require": []
            },
            "action2": {
                "description": "Tout cela ne laisse rien présager de bon.",
                "next_message": "Vous passez votre chemin.",
                "health": 0,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random11"
                    ]
                ],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "random12": {
        "text": "Non loin de là où vous êtes, des carcasses métalliques gisent au soleil. En les observant de plus près, elles ressemblent à des sortes de félins mécaniques. Des tigres peut-être ?",
        "actions": {
            "action1": {
                "description": "Intrigué vous allez les observer de plus près.",
                "next_message": "Bien  mal vous en a pris, ce que vous preniez pour des carcasses inertes se sont réveillés et près à en découdre. Ce sont bien des tigres à la mâchoire métallique démesurée. Vous prenez vos jambes à votre coup et les tigre probablement rouillés ne parviennent heureusement pas à vous suivre. Une fois semés vous vous apercevez que votre jambe saigne abondamment ; un tigre a du réussir à vous griffer sans que vous vous en aperceviez dans le feu de l'action. Vous reprenez votre recherche en grimaçant.",
                "health": -3,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random12"
                    ]
                ],
                "script": [],
                "zone": None,
                "require": []
            },
            "action2": {
                "description": "Mieux vaut éviter la zone.",
                "next_message": "Vous faites un détour.",
                "health": 0,
                "oxygen": -1,
                "loot": [],
                "add": [],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random12"
                    ]
                ],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "random13": {
        "text": "Alors que vous marchez seul avec vos pensées, votre réservoir semble dysfonctionner. ",
        "actions": {
            "action1": {
                "description": "Vous utilisez un des kits de réparation fourni avec la combinaison.",
                "next_message": "La réparation fonctionne mais vous avez perdu un peu d'oxygène. Très étrange incident…",
                "health": 0,
                "oxygen": -4,
                "loot": [],
                "add": [
                    [
                        "desert",
                        "random",
                        "random14"
                    ]
                ],
                "remove": [
                    [
                        "desert",
                        "random",
                        "random13"
                    ]
                ],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "random14": {
        "text": "Mauvaise nouvelle, votre réservoir semble à nouveau dysfonctionner. ",
        "actions": {
            "action1": {
                "description": "Vous utilisez un autre des kits de réparation fourni avec la combinaison.",
                "next_message": "La réparation fonctionne mais vous avez perdu un peu d'oxygène. Comment ce fait-il que pareil incident se reproduise ?!",
                "health": 0,
                "oxygen": -2,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": None,
                "require": []
            }
        }
    },
    "random15": {
        "text": "Vous arrivez devant une très grande porte en métal qui semble avoir émergé du sable. Vous sentez que dans cet endroit vous trouverez enfin des réponses.",
        "actions": {
            "action1": {
                "description": "Il y a un emplacement correspondant à celui de votre plaque iridescente, Vous l'insérez dans le mécanisme.",
                "next_message": "Avec un grognement sinistre, la porte s'ouvre révélant une grande salle peinte intégralement en blanc. Vous sentez que vous êtes plus près du but que jamais. Un tuyau sort du mur adjacent et vous permet de recharger votre oxygène. De même un kit de soin est à votre disposition sur une table du même blanc. L'air du bâtiment est de plus respirable.",
                "health": 5,
                "oxygen": 99,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": "lab",
                "require": [
                    "plaque_iridescente"
                ]
            },
            "action2": {
                "description": "Vous tentez de pousser la lourde porte.",
                "next_message": "Au prix d'immenses efforts, vous parvenez à ouvrir assez la porte pour pouvoir la traverser révélant une grande salle peinte intégralement en blanc. Vous sentez que vous êtes plus près du but que jamais. Un tuyau sort du mur adjacent et vous permet de recharger votre oxygène. Cependant cet effort vous a proprement épuisé.",
                "health": -3,
                "oxygen": 99,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": "lab",
                "require": []
            }
        }
    },
    "random_vert_1": {
        "text": "",
        "actions": {
            "action1": {
                "description": "",
                "next_message": "",
                "health": 0,
                "oxygen": 0,
                "loot": [],
                "add": [],
                "remove": [],
                "script": [],
                "zone": "",
                "require": []
            }
        }
    }
}