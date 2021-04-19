event = {
    "intro": {
        "script": {
            "intro1": {
                "text": "La salle semble vide ce n'est pas ici que vous trouverez des réponses. En vous dirigeant vers ce qui semble être une porte, celle-ci s'ouvre dans un chuintement sourd. Vous vous retrouvez dans un couloir qui semble aussi ancien que la pièce que vous venez de quitter mis à part sa couleur, vert kaki. Tout semble rappeler une esthétique spartiate, vous donnant l'impression d'être dans un ancien complexe militaire.",
                "actions": {
                    "action1": {
                        "description": "Dans la monotonie du couloir, une pièce dont la porte est peinte en rouge vif attire votre attention. Vous décidez de vous y diriger.",
                        "next_message": "La porte ne s'ouvre pas à votre approche, pas non plus quand vous faites pression dessus. Vous reprenez votre marche.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [
                            [
                                "lab",
                                "random",
                                "porte_rouge1"
                            ],
                            [
                                "lab",
                                "random",
                                "porte_rouge2"
                            ],
                            [
                                "lab",
                                "random",
                                "porte_rouge3"
                            ]
                        ],
                        "remove": [],
                        "script": [
                            "intro2"
                        ],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Sans intérêt.",
                        "next_message": "Vous reprenez votre marche.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [
                            "intro2"
                        ],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "intro2": {
                "text": "Le couloir poussiéreux débouche sur une salle dégageant une faible lumière dont la porte est ouverte. Vous décidez de vous y engager. Un robot, ressemblant étrangement à celui sur lequel vous travailliez au laboratoire git, éventré, au milieu de cette petite salle. Une table recouverte d'un liquide visqueux se trouve au fond de la pièce. Inutile de rebrousser chemin, la porte s'est refermée derrière-vous et ne semble pas s'ouvrir de ce côté.",
                "actions": {
                    "action1": {
                        "description": "Vous investiguez le robot.",
                        "next_message": "\\\"EXPLO_MS#373\\\" C'est bien un des modèles que vous avez contribué a développer. Mais il semble disposer de composants d'on vous n'êtes pas au fait. Son état déplorable ne vous permet pas d'en dire beaucoup plus. Il semble avoir été déchiqueté par une grande mâchoire métallique. Le mystère s'épaissit.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [
                            "intro3"
                        ],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous investiguez la table, vous pensez avoir repéré un objet intéressant, bien que la plupart soit recouverts d'un fluide ressemblant à de l'huile de moteur.",
                        "next_message": "Vous parvenez à en extraire une petite clef orange fluo, cependant il s'avère que le fluide était acide, vous serrez contre vous votre main meurtrie.",
                        "health": -1,
                        "oxygen": 0,
                        "loot": [
                            "clef_orange"
                        ],
                        "add": [],
                        "remove": [],
                        "script": [
                            "intro3"
                        ],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "intro3": {
                "text": "Soudain, dans un fracas retentissant, les murs, en fait des volets métalliques, remontent révélant un magnifique panorama. Dans la salle soudain inondée de lumière, vous apercevez un immense désert de couleur rouge et des montagnes loin à l'horizon. Ce décor vous semble étrangement familier... Soudain la réalité vous frappe en plein cœur : vous êtes sur Mars ! Mais comment cela à-t 'il pu arriver, aucun homme n'est jamais allé sur Mars, qui à construit ce complexe ? Vous comprenez rapidement que vous n'aurez aucune réponse à ces questions en restant dans cette pièce. Comme répondant à votre souhait, une dalle se soulève révélant une combinaison spatiale dernière génération, autosuffisante en nutriments. Vous distinguez une porte dans le fond de la pièce. Il va vous falloir explorer MARS !",
                "actions": {
                    "action1": {
                        "description": "Vous enfilez la combinaison et ouvrez la porte.",
                        "next_message": "Cette porte au contraire des autres de la station est manuelle. En sortant vous êtes frappé par les violents vents faisant un bruit effroyable. Vous êtes dans un désert de sable rouge qui s'étendrait jusqu'à l'horizon si vous ne distinguiez pas d'immenses montagnes au lointain. Tétanisés par l'immensité et la nature des lieux vous vous mettez à marcher au hasard à la recherche de réponses, espérant que celles-ci vous soient dévoilées avant épuisement de vos réserves d'oxygène. ",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": "desert",
                        "require": []
                    }
                }
            }
        },
        "random": {}
    },
    "desert": {
        "script": {
            "desert1": {
                "text": "Tandis que votre regard divague, vous entendez un curieux grincement métallique et vous avez l'impression d'apercevoir une forme miroitant au soleil au sommet d'une dune avoisinante. Puis, plus rien.",
                "actions": {
                    "action1": {
                        "description": "Vous vous aventurez au sommet du monticule et tentez de vous introduire dans le trou.",
                        "next_message": "L'entreprise est assez aisée et vous atterrissez dans une petite cavité ovale creusée dans le sable. L'endroit est vide mis à part une solide caisse en métal.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [
                            "desert2"
                        ],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous vous éclipsez discrètement pris d'un mauvais pressentiment",
                        "next_message": "Vous attendez quelques kilomètres avant de pousser un soupir de soulagement, vous sentez que vous avez échappé à un grand danger.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "desert2": {
                "text": "Des bruits aigus attirent votre attention. Vous tendez l'oreille et discernez des sorts de jappements semblant venir de plus profond dans le sol. Mieux vaudrait ne pas s'y attarder.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez d'ouvrir la caisse en métal.",
                        "next_message": "Après de multiples éraflures vous parvenez à l'ouvrir, elle ne contient, à votre grand désarroi, rien que des pierres et des débris métalliques. Soudain un grognement furieux et très proche se fait entendre. Vous sortez immédiatement par l'ouverture du plafond. Vous attendez quelques kilomètres avant de pousser un soupir de soulagement, vous sentez que vous avez échappé à un grand danger.",
                        "health": -1,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous examinez attentivement la pièce.",
                        "next_message": "Une paroi de la pièce s'avéré être friable, révélant un tunnel qui semble s'enfoncer profondément sous terre. Vous vous y aventurez sans pouvoir réprimer un frison.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [
                            "desert3"
                        ],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "desert3": {
                "text": "Après de longues minutes de descente abrupte, vous arrivez dans une pièce rectangulaire faiblement éclairée par ce qui semble être des pierres luminescentes. Des tas de ferrailles métalliques jonchent le sol parfois arrivant jusqu'au plafond environ 3 mètres de hauteur. Au milieu de celle-ci trône un autel en pierre sur lequel repose une plaque luminescente métallique gravée, iridescente. Cet objet est tellement étrange et beau qu'il semblerait presque d'origine extra-terrestre.",
                "actions": {
                    "action1": {
                        "description": "Vous vous dépêchez d'aller étudier cette plaque de plus près.",
                        "next_message": "Vous distinguez en transparence des circuits électriques dans la plaque. Alors que vous étiez en train de l'examiner un tas s'effondre laissant sortir ce qui semble être un tigre robotique muni d'une désagréablement large mâchoire robotique. Il se jette sur vous dans un grincement d'engrenages et tente de vous déchiqueter. Vous parvenez à vous défaire de son emprise et remontez la pente en courant avant de sortir par l'ouverture du plafond. Vous pensez qu'il n'a pas réussi à vous suivre mais votre combinaison est déchirée. Vous espérez que cette plaque en valait la peine.",
                        "health": -1,
                        "oxygen": -3,
                        "loot": [
                            "plaque_iridescente"
                        ],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous examinez le tas de ferrailles.",
                        "next_message": "C'est un bric à brac d'objets hétéroclites, la plupart en trop mauvais état pour être utilisable. Vous y dénichez tout de même un kit de soin d'urgence. Ca peut toujours servir. Cependant avant que vous n'ayez pu poursuivre vos recherches, un grognement strident retentit et le tas s'effondre sur vous. Vous perdez connaissance... Vous vous réveillez à l'entrée du trou qui est maintenant effondré. Quelque chose ou quelqu'un ou quelqu'un vous en a sorti. Vous ne souffrez que de contusions. Vous vous éloignez et attendez quelques kilomètres avant de pousser un soupir de soulagement, vous sentez que vous avez échappé à un grand danger.",
                        "health": -2,
                        "oxygen": -1,
                        "loot": [
                            "kit_soin1"
                        ],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "desert4": {
                "text": "L'intérieur, poussiéreux, ne révèle qu'une trappe dans le sol.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "Dommage, elle est verrouillée et solide et il n'y a rien d'autre à voir ici, vous repartez dépité.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "C'est sans doute un piège, vous partez immédiatement.",
                        "next_message": "Vous repartez à la recherche d'un endroit plus accueillant.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "desert5": {
                "text": "L'intérieur, poussiéreux, ne révèle qu'une trappe dans le sol.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "Dommage, elle est verrouillée et solide et il n'y a rien d'autre à voir ici, vous repartez dépité.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "C'est sans doute un piège, vous partez immédiatement.",
                        "next_message": "Vous repartez à la recherche d'un endroit plus accueillant.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "desert6": {
                "text": "L'intérieur, poussiéreux, ne révèle qu'une trappe dans le sol.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "La trappe s'ouvre sans difficulté et révèle une petite cache protégeant une curieuse armure de protection qui semble faite pour être portée par-dessus votre combinaison. Voila de quoi vous protéger des dangers à venir.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [
                            "armure"
                        ],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "C'est sans doute un piège, vous partez immédiatement.",
                        "next_message": "Vous repartez à la recherche d'un endroit plus accueillant.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "desert7": {
                "text": "Vous examinez la machine, vous distinguez deux symboles compréhensibles. Le premier est \"N+O2\", le deuxième est \"NO3\".",
                "actions": {
                    "action1": {
                        "description": "Vous branchez le tuyau \"N+O2\" à votre réservoir d'oxygène.",
                        "next_message": "Bon choix, vos réserves d'oxygène sont maintenant au maximum.",
                        "health": 0,
                        "oxygen": 99,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous branchez le tuyau \"NO3\" à votre réservoir d'oxygène.",
                        "next_message": "Vous vous rendez rapidement compte que l'air injecté est irrespirable, quelle erreur ! Et la machine ne semble pas vouloir refonctionner... La purge nécessaire du réservoir vient encore amoindrir vos maigres réserves.",
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
            }
        },
        "random": {
            "random1": {
                "text": "Perdu dans le désert vous errez au hasard. Une tempête de sable semble sur le point de se lever. De fines particules de sable s'infiltrent dans le système respiratoire de la combinaison, vous faisant abondamment tousser.",
                "actions": {
                    "action1": {
                        "description": "Vous endurez, marchant lentement mais surement pour sortir de la zone de danger.",
                        "next_message": "Pendant des minutes qui vous semblent des heures vous luttez contre les vents violents. Puis d'un coup le calme. Vous reprenez votre périple relativement indemne.",
                        "health": 0,
                        "oxygen": -3,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random1"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous cherchez à creuser le sable pour vous fournir un abri temporaire et ainsi attendre la fin de la tempête en relative sécurité.",
                        "next_message": "Vous commencez à creuser avec une relative aisance. Cependant vos espoirs sont rapidement douchés car le sable est en fait très dur dès 15 cm de profondeur. Vous vous allongez sur le sol et attendez de longues heures dans cet ersatz d'abri que les vents se couchent. C'est épuisé et presque asphyxié que vous reprenez ensuite votre péril. Cependant tout n'est pas perdu, vous avez trouvé une petite carte d'accès noire en creusant. Vous en êtes certain, vous êtes sur la bonne piste.",
                        "health": -1,
                        "oxygen": -3,
                        "loot": [
                            "carte_noire"
                        ],
                        "add": [
                            [
                                "lab",
                                "random",
                                "porte_mystérieuse"
                            ]
                        ],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random1"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random2": {
                "text": "Les dunes de sable se suivent et se ressemblent, et vous avez l'impression d'être totalement perdu.",
                "actions": {
                    "action1": {
                        "description": "Vous vous dirigez à tout hasard vers l'est.",
                        "next_message": "Toujours rien, c'est sûr vous êtes perdu...",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous vous dirigez à tout hasard vers l'ouest.",
                        "next_message": "Toujours rien, c'est sûr vous êtes perdu...",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random3": {
                "text": "Dans cette étendue de sable bien monotone vous ne savez plus où aller.",
                "actions": {
                    "action1": {
                        "description": "Vous vous dirigez à tout hasard vers l'est.",
                        "next_message": "Toujours rien, c'est sûr vous êtes perdu...",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random3"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous vous dirigez à tout hasard vers l'ouest.",
                        "next_message": "Vous apercevez un monticule de sable différent des autres. Celui-ci comporte une large excavation visiblement creusée par une machine. ",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random3"
                            ]
                        ],
                        "script": [
                            "desert1"
                        ],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random4": {
                "text": "Vous apercevez ce qui est probablement un drone foncer droit dans votre direction loin au dessus de vous.",
                "actions": {
                    "action1": {
                        "description": "Vous vous mettez à couvert.",
                        "next_message": "Vous plongez derrière une dune. Le drone poursuit son chemin et disparait à l'horizon.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [
                            [
                                "desert",
                                "random",
                                "random_drone"
                            ]
                        ],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random4"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous vous manifestez espérant de l'aide.",
                        "next_message": "Le drone ne vous accorde aucune attentionnais lâche une petite bille noire avant de disparaitre à l'horizon. Vous vous dirigez vers l'objet qui s'avère être... une grenade à fragmentation… qui explose, heureusement à bonne distance, ce qui ne vous empêche pas de recevoir un shrapnel dans le pied. Maudite planète.",
                        "health": -2,
                        "oxygen": -1,
                        "loot": [],
                        "add": [
                            [
                                "desert",
                                "random",
                                "random_drone"
                            ]
                        ],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random4"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random5": {
                "text": "Alors que vous marchez dans ce désert infini. Un événement vient troubler vos divagations. Une petite météorite vient de s'écraser non loin, événement que vous savez pas si rare sur Mars. Vous vous approchez du lieu de l'impact. Vous sentez des vagues d'air brûlant de plus en plus intense quand vous vous approchez du cratère.",
                "actions": {
                    "action1": {
                        "description": "Vous luttez contre la chaleur et vous vous dirigez vers la météorite.",
                        "next_message": "Vous parvenez non sans difficulté jusqu'à la météorite. De petits cristaux d'un blanc très pur parsèment sa surface. Vous en ramassez quelques un avant de battre en retraite. A bonne distance vous reprenez vos esprits et contemplez votre butin en espérant que ces pierres vous seront utiles. Vous avez tout de même pris quelques brulures.",
                        "health": -2,
                        "oxygen": -1,
                        "loot": [
                            "pierres_blanches"
                        ],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random5"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous passez votre chemin, vous n'avez pas envie de finir rôti.",
                        "next_message": "Vous reprenez votre route.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random5"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random6": {
                "text": "Au gré de vos pérégrinations, vous arrivez dans une zone de geyser de gaz, dont les émanations bleutées arrivent très haut dans le ciel.",
                "actions": {
                    "action1": {
                        "description": "Vous la traversez en espérant que le gaz ne soit pas corrosif.",
                        "next_message": "Il n'est pas corrosif mais le terrain est traversée de profondes crevasses qui vous mettent en grande difficulté. Une fois que vous avez réussi à traverser l'endroit le constat n'est pas brillant ; vous avez dépensé beaucoup d'oxygène. Sur une note plus positive, le gaz semble avoir eu sur vous un effet curatif, vous voyez des égratignures se résorber. C'est donc à moitié satisfait que vous reprenez votre périple.",
                        "health": 2,
                        "oxygen": -3,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random6"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous l'évitez, vous ne savez pas où aller de toute façon.",
                        "next_message": "Vous marchez jusqu'à ce que les geyser ne soient plus qu'un point à l'horizon.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random6"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random7": {
                "text": "Au détour d'une dune, vous distinguez un bâtiment en béton muni d'une unique porte branlante à moitié enfoui dans le sable. Elle est tout de même verrouillée. Cela vaut-il le coup de la forcer ?",
                "actions": {
                    "action1": {
                        "description": "Le jeu n'en vaut pas la chandelle.",
                        "next_message": "Vous ignorez le bâtiment et continuez votre chemin.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random7"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous vous jetez contre la porte espérant la forcer.",
                        "next_message": "C'est sans grande difficulté mais au prix d'une épaule endolorie que vous pénétrez dans le bâtiment.",
                        "health": -1,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random7"
                            ]
                        ],
                        "script": [
                            "desert4",
                            "desert5",
                            "desert6"
                        ],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random8": {
                "text": "Alors que vous marchez tranquillement, vous faites une chute malencontreuse. ",
                "actions": {
                    "action1": {
                        "description": "Vous vous relevez immédiatement.",
                        "next_message": "Cependant le mal est fait, votre cheville est maintenant douloureuse. Quel manque de chance.",
                        "health": -1,
                        "oxygen": -1,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random8"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random9": {
                "text": "Alors que vous marchez au hasard, vous tombez sur un autel en pierre, qui ne semble pas à sa place au milieu des dunes. Celui-ci comporte un levier qui ne demande qu'à être activé.",
                "actions": {
                    "action1": {
                        "description": "La tentation est trop forte, vous abaissez le levier.",
                        "next_message": "Aussitôt un tuyau sort de l'autel, il semble fait pour recharger vos réserves d'oxygène. Et effectivement une fois branché sur votre combinaison celles-ci remontent un peu. Ensuite retentit un cliquètement assourdissant qui semble provenir du désert même. Quoique vous ayez déclenché, cela doit être très important.",
                        "health": 0,
                        "oxygen": 3,
                        "loot": [],
                        "add": [
                            [
                                "desert",
                                "random",
                                "random11"
                            ],
                            [
                                "desert",
                                "random",
                                "random12"
                            ],
                            [
                                "desert",
                                "random",
                                "random13"
                            ],
                            [
                                "desert",
                                "random",
                                "random15"
                            ]
                        ],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random9"
                            ],
                            [
                                "desert",
                                "random",
                                "random10"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random10": {
                "text": "Alors que vous marchez au hasard, vous tombez sur un levier qui dépasse à peine du sable.",
                "actions": {
                    "action1": {
                        "description": "Vous abaissez ce levier.",
                        "next_message": "Un cliquètement assourdissant retentit, qui semble provenir du désert même. Quoique vous ayez déclenché, cela doit être très important.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [
                            [
                                "desert",
                                "random",
                                "random11"
                            ],
                            [
                                "desert",
                                "random",
                                "random12"
                            ],
                            [
                                "desert",
                                "random",
                                "random13"
                            ],
                            [
                                "desert",
                                "random",
                                "random15"
                            ]
                        ],
                        "remove": [
                            [
                                "desert",
                                "random",
                                "random9"
                            ],
                            [
                                "desert",
                                "random",
                                "random10"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous résistez à la tentation.",
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
            }
        }
    },
    "lab": {
        "script": {
            "lab1": {
                "text": "Vos yeux mettent quelques secondes à s'habituer à la semi-pénombre, agréable après l'éblouissement du désert. Votre enthousiasme précédent est bien retombé, il vous faut maintenant explorer ce lieu inconnu et les dangers du désert vous bien mis en garde ; vous êtes en zone hostile. Au fond de la pièce deux portes, l'une ouvre sur une ligne verte serpentant le long du mur et s'enfonçant dans les profondeurs du complexe. L'autre est identique à la différence que la ligne est rouge.",
                "actions": {
                    "action1": {
                        "description": "Vous décidez de suivre la ligne verte.",
                        "next_message": "Le couloir dans lequel vous entrez vous paraît tout à fait banal, à l'exception de cette large ligne verte peinte sur le mur. Le couloir à de nombreux embranchements mais leur pénombre vous dissuade de les emprunter, de plus vous préférez continuer à suivre la ligne. Cependant au bout de quelques minutes celle-ci s'arrête abruptement, en fait le couloir a intégralement été repeint en noir, du sol au plafond, sans distinction pour les portes ou les néons. La pénombre est donc encore plus étouffante. Pourtant il vous faut continuer ... Vous décidez de marcher au hasard.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [
                            [
                                "lab",
                                "random",
                                "random_vert_1"
                            ]
                        ],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous décidez de suivre la ligne rouge. [WIP]",
                        "next_message": "Le couloir dans lequel vous entrez vous paraît tout à fait banal, à l'exception de cette large ligne rouge peinte sur le mur. Le couloir s'enfonce tout droit dans les profondeurs du complexe et la ligne s'agrandit progressivement jusqu'à recouvrir l'intégralité du couloir d'un rouge vif. Soudain sans prévenir, la lumière s'éteint et vous entendez un chuintement que vous reconnaissez entre mille ; de l'oxygène c'était trop beau pour durer. Déboussolé par ces événements inattendus il va pourtant falloir continuer ... Vous décidez de marcher au hasard.",
                        "health": 0,
                        "oxygen": -1,
                        "loot": [],
                        "add": [
                            [
                                "lab",
                                "random",
                                "random_rouge_1"
                            ]
                        ],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "lab2": {
                "text": "Il n'y a aucune source de lumière et aucun moyen d'en emporter une, vous commencez à douter de votre idée.",
                "actions": {
                    "action1": {
                        "description": "Vous vous élancez en dehors du sas, tant pis vous ferez à tâtons.",
                        "next_message": "Vous prenez une grande emjambée et sortez du sas .. et heurtez violemment une paroi. Sonné vous tentez de vous remettre sur vos pieds et découvrez qu'il n y a pas de sol. A l'extérieur du sas, il n'y avait en fait qu'un énorme trou. Malheureusement, vu la longueur de votre chute, vous ne saurez jamais ce qu'il y a au fond ...",
                        "health": -99,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous jugez plus prudent d'abandonner votre idée.",
                        "next_message": "Vous avez sans doute pris la bonne décision.",
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
            "lab3": {
                "text": "Après plus ample investigation, cela semble être une plateforme d'analyse d'objets minéraux aux vu des différents pictogrammes. Il est cependant difficile d'en savoir plus.",
                "actions": {
                    "action1": {
                        "description": "Vous insérez les pierres blanches trouvées dans le desert dans le module principal.",
                        "next_message": "Celui-ci commence à tournoyer et à produire un sifflement intense. Après quelques secondes tous les voyants passent au rouge et le sol commence à trembler. Vous commencez à paniquer quand soudain tout s'arrête, le module se calme et le sas s'ouvre libérant vos pierres. Celles-ci sont maintenant parfaitement taillés en forme de gemmes hexagonales. Vous comprenez maintenant le rôle des fentes de la même forme dans le pupitre de commande non-loin de là. Vous vous dépêchez de récupérer les gemmes et de les insérer. Aussitôt un écran  apparait sur le mur opposé, affichant un message énigmatique : \" Bienvenue U4563-P345. Niveaux d'oxygénation et de fertilisant des jardins restaurés.\". Vous avez beau vous creuser la tête vous ne savez pas si ce qui viens de se passer est vraiment une bonne chose. Secoué par tous ces événements vous finissez par quitter la pièce plongé dans vos pensées.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": [
                            "pierres_blanches"
                        ]
                    },
                    "action2": {
                        "description": "Vous ne voyez pas en quoi de telles machines pourraient vous être utiles.",
                        "next_message": "Vous auriez espéré qu'une telle salle vous viendrait en aide, quelle déception. Cependant avant de quitter la salle vous trouvez un petit morceau de métal en forme de roue crantée derrière un amas de câble. Sait-on jamais, vous le fourrez dans votre poche.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [
                            "roue_crantee"
                        ],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "lab4": {
                "text": "Vous arrivez à un cul de sac.",
                "actions": {
                    "action1": {
                        "description": "Vous rebroussez chemin.",
                        "next_message": "Encore du temps perdu …",
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
            "lab5": {
                "text": "Soudain vous entendez les crissements d'une chenille, immédiatement un petit robot d'un blanc immaculé apparaît à l'angle d'un couloir. \"ALERTE INTRUS DETECTE\". Crie-t'il d'une voix stridente.",
                "actions": {
                    "action1": {
                        "description": "Vous détalez sans tarder.",
                        "next_message": "Vous parvenez à le semer sans difficulté et sa petite voix-stridente disparait rapidement.",
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
                        "description": "Vous vous jetez sur le petit robot, histoire de le faire taire une bonne fois pour toutes.",
                        "next_message": "Bien mal vous en a pris, vous commencez à réaliser votre erreur au premier choc électrique, bientôt suivi de nombreux autres. Vous êtes bientôt incapable de bouger. Soudain le robot s'arrête et s'exclame fièrement \"INTRUS NEUTRALISE\", il s'éloigne alors avec le même bruit de chenille qu'il est venu. Au bout de longues minutes vous parvenez à vous lever, ou plutôt à vous trainez et vous reprenez votre route en espérant ne jamais recroiser ce robot.",
                        "health": -2,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            }
        },
        "random": {
            "random1_gar": {
                "text": "Une alarme retentit soudain et tous les néons passent au rouge. Puis, au bout de quelques secondes, l'alarme s'arrête. A part l'éclairage rien ne semble avoir changé. Vous espérez que votre intrusion n'ait aucun lien avec l'événement.",
                "actions": {
                    "action1": {
                        "description": "Vous retenez votre souffle.",
                        "next_message": "Rien ne se passe, mais vous êtes plus que jamais sur vos gardes.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [
                            [
                                "lab",
                                "random",
                                "random_garde"
                            ]
                        ],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random1_gar"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random2_ox": {
                "text": "Au grès d'un couloir, une aspérité du mur accroche votre bonbonne d'oxygène qui commence à fuir. Vous vous apercevez heureusement rapidement. De toute façon ce n'est pas l'oxygène qui manque ici.",
                "actions": {
                    "action1": {
                        "description": "Faire un réparage de fortune.",
                        "next_message": "La fuit est rapidement colmatée et vous vous efforcez de ne plus y penser.",
                        "health": 0,
                        "oxygen": -3,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random2_ox"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "La laisser fuir, de toute façon vous n'en avez plus besoin.",
                        "next_message": "Vous continuez le cœur léger en laissant la bouteille se vider.",
                        "health": 0,
                        "oxygen": -2,
                        "loot": [
                            "bombonne_end"
                        ],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random2_ox"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random3_ded": {
                "text": "Ce complexe est un véritable dédale ! Vous n'êtes pas sûr d'être dans la bonne direction. Et cette maudite ligne qui a disparue …",
                "actions": {
                    "action1": {
                        "description": "Vous vous dirigez à droite.",
                        "next_message": "Encore un couloir identique aux autres ...",
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
                        "description": "Vous vous dirigez à gauche.",
                        "next_message": "Encore un couloir identique aux autres ...",
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
            "random4_ded+": {
                "text": "[WIP]",
                "actions": {
                    "action1": {
                        "description": "",
                        "next_message": "",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random4_ded+"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random5_salle1": {
                "text": "Soudain, vous percevez de la lumière sous une porte du couloir.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "Rien à faire, elle est solide et verrouillée.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [
                            "lab4",
                            "lab5"
                        ],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous n'y prêtez pas attention.",
                        "next_message": "Qui sait ce que vous auriez pu trouver derrière ?",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [],
                        "script": [
                            "lab4",
                            "lab5"
                        ],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random6_salle2": {
                "text": "Soudain, vous percevez de la lumière sous une porte du couloir.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "A votre grande surprise, la porte s'ouvre sans broncher. L'intérieur révèle une salle poussiéreuse, au carrelage seulement partièlement posé et aux murs encore nus. Ceci explique pourquoi elle était ouverte sa construction n'est pas terminé. Pourtant on dirait que cela fait longtemps que le chantier a été abandonné. Pas grand chose d'intéressant à trouver à part des rations de protéines, sans doute destinées aux ouvrier. Ou aux gardes ...",
                        "health": 1,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random6_salle2"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous n'y prêtez pas attention.",
                        "next_message": "Qui sait ce que vous auriez pu trouver derrière ?",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random6_salle2"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random7_salle3": {
                "text": "Soudain, vous percevez de la lumière sous une porte du couloir.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "A votre grande surprise, la porte s'ouvre sans broncher. L'intérieur révèle ce qui semble être une station d'analyse, dont la machinerie avancée et les diodes électroniques clignotantes ne vous évoquent rien de particulier, ce ne semble pas être lié à votre domaine d'expertise.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random7_salle3"
                            ]
                        ],
                        "script": [
                            "lab3"
                        ],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous n'y prêtez pas attention.",
                        "next_message": "Qui sait ce que vous auriez pu trouver derrière ?",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random7_salle3"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random8_salle4": {
                "text": "Une porte entrebaillée attire votre attention à l'autre bout d'un couloir.",
                "actions": {
                    "action1": {
                        "description": "Vous tentez de l'ouvrir.",
                        "next_message": "[WIP]",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random8_salle4"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous n'y prêtez pas attention.",
                        "next_message": "Qui sait ce que vous auriez pu trouver derrière ?",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random8_salle4"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random9_grat": {
                "text": "Un genre de grattement se fait entendre, réverbéré le long du couloir devant vous. Difficile de déterminer son origine. ",
                "actions": {
                    "action1": {
                        "description": "Vous accélérez le pas vers ce qui est peut-être l'origine du grattement.",
                        "next_message": "Il s'arrête au bout de quelques secondes, et ne reprend plus. Dépité vous poursuivez votre exploration.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random9_grat"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous vous faites tout petit, et rebroussez chemin.",
                        "next_message": "Plus de signe du bruit. Vous l'avez sans doute échappé belle.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random9_grat"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random10_gro": {
                "text": "Un grognement fait trembler les murs. Et au bruit qu'il fait, la cause se rapproche de vous !",
                "actions": {
                    "action1": {
                        "description": "Vous détalez.",
                        "next_message": "Après quelques minutes de course, vous n'entendez plus rien. Vous avez sans doute semé la chose responsable du grognement. Vous reprenez diffcilement haleine.",
                        "health": -1,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random10_gro"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vous foncez droit vers le bruit, déterminé à en confronter le responsable.",
                        "next_message": "Plus vous avancez plus le grognement devient ronronnement. Vous arrivez dans une large salle blanche éclairée par des puissants spots. Plissants les yeux vous comprenez que le grognement n'était en fait que le ronronnement rassurant d'une photocopieuse, horriblement déformé par l'écho des longs couloirs. Au pieds de l'imprimante, une marre de feuilles, toutes semble-t-il étant des impressions du même document. Celui-ci est un plan de ce qui semble être un dédale, avec un chemin grossièrement dessiné en rouge. Celui-ci est sobrement appelé \"Plan des jardins\". Malheureusement cela ne vous est d'aucune aide dans l'immédiat. Il ne semble rien n'y avoir d'autre à faire dans cette salle et vous reprenez votre chemin.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [
                            "plan_jardin"
                        ],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random10_gro"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            },
            "random11_sas": {
                "text": "A l'angle d'un couloir anodin, vous vous retrouvez face à un sas étanche. Un petit écran vert à sa gauche ne comporte qu'un seul mot : \"ouvrir ?\". Allez-vous répondre à cet appel ?",
                "actions": {
                    "action1": {
                        "description": "Vous vérifiez votre oxygène, mettez votre combinaison, et ouvrez le sas sans perdre de temps.",
                        "next_message": "Devant vous le noir total, vous êtes sans doute dans une grotte.",
                        "health": 0,
                        "oxygen": -2,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random11_sas"
                            ]
                        ],
                        "script": [
                            "lab2"
                        ],
                        "zone": None,
                        "require": []
                    },
                    "action2": {
                        "description": "Vos réponses sont dans ce complexe, pas dehors !",
                        "next_message": "Vous avez sans doute pris la bonne décision.",
                        "health": 0,
                        "oxygen": 0,
                        "loot": [],
                        "add": [],
                        "remove": [
                            [
                                "lab",
                                "random",
                                "random11_sas"
                            ]
                        ],
                        "script": [],
                        "zone": None,
                        "require": []
                    }
                }
            }
        }
    }
}