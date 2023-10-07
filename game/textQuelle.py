import random

setupCharacter = [["dario",[":crown: [rgb(255,140,20)]  Dario:[/rgb(255,140,20)]", "rgb(255,150,100)"]],
                  ["erek",[":shield: [rgb(50,200,190)]   Erek:[/rgb(50,200,190)]", "rgb(150,255,255)"]],
                  ["pilgrim",[":hammer_and_pick: [rgb(70,220,50)] Pilgrim:[/rgb(70,220,50)]", "rgb(200,255,150)"]],
                  ["game",["", "rgb(200,200,255)"]],
                  ]
setupVars = [
             ["seed","r",random.randint(1585411,994599399),[""]],
             ["jahr","rw",1,""],
             ["day","rw",0,""],

             ["gold","rw",3465,"[rgb(255,210,0)]Gold:[/rgb(255,210,0)] !oldVal! -> !change! -> !newVal!"],
             ["bewohner","rw",72,"[rgb(200,160,255)]Bewohner:[/rgb(200,160,255)] !oldVal! -> !change! -> !newVal!"],
             ["essen","rw",100,"[rgb(50,180,50)]Essen:[/rgb(50,180,50)] !oldVal! -> !change! -> !newVal!"],
             ["holz","rw",50,"[rgb(160,110,50)]Holz:[/rgb(160,110,50)] !oldVal! -> !change! -> !newVal!"],
             ["stein","rw",20,"[rgb(160,160,140)]Stein:[/rgb(160,160,140)] !oldVal! -> !change! -> !newVal!"],

             ["bewohnerGefallen","rw",50,"Das [rgb(255,200,150)]Ansehen[/rgb(255,200,150)] Darios hat sich um !change! geändert und ist nun !newVal!"],
             ["erekGefallen","rw",75,"[rgb(50,200,190)]Ereks[/rgb(50,200,190)] meinung gegenüber Dario hat sich um !change! geändert und ist jetzt !newVal!"],
             ["pilgrimGefallen","rw",75,f"[rgb(70,220,50)]Pilgrims[/rgb(70,220,50)] meinung gegenüber Dario hat sich um !change! geändert und ist jetzt !newVal!"],

             ["def","rw",50,"[rgb(50,100,255)]Verteidigung:[/rgb(50,100,255)] !oldVal! -> !change! -> !newVal!"],
             ["att","rw",10,"[rgb(255,100,50)]Angriff:[/rgb(255,100,50)] !oldVal! -> !change! -> !newVal!"],
             ]

intro = [
        ["clear"],
        ["newTask",10,"Laden...",[]],
        ["runTasks"],
        ["clear"],
        ["say","game"," Die Schlacht gegen das Böse"],
        ["say","game"," In einer fernen Welt,"],
        ["say","game"," geprägt von Königreichen,"],
        ["say","game"," Rivalitäten und Eroberungen,"],
        ["say","game"," übernimmst du die Rolle von unserem König Dario.",0.1],
        ["say","game"," Deine Aufgabe ist es,"],
        ["say","game"," das Schicksal unseres Königreichs zu lenken.",0.1],
        ["say","game"," Unser Königreich wird von Kerberos Truppen bedroht.",0.1],
        ["say","game"," Deine Aufgabe ist es die Verteidigung zu organisieren",0.1],
        ["say","game"," und strategische Entscheidungen zu treffen,"],
        ["say","game"," um das Überleben deines Volkes zu sichern."],
        ["say","game"," Deine strategischen Entscheidungen"],
        ["say","game"," werden den Verlauf der Geschichte"],
        ["say","game"," und das Schicksal des Königreichs bestimmen.",0.1],
        ["poll",["Bist du bereit? [drücke 1 oder 2]",
            ["Ja","Nein"],
            [[["clear"]],[["say","game","auf Wieder sehen"],["exit"]]]
            ]],
        ["clear"],
        ["say","erek","Hallo Dario mein Freund"],
        ["say","dario","Hallo Erek was gibt es"],
        ["say","erek","man munkelt das Kerberos Truppen sich vielleicht in unseren Wäldern aufhalten",5],
        ["say","dario","Das hat mir gerade noch gefehlt"],
        ["say","erek","ich habe aber auch gute Nachrichten"],
        ["say","erek","das ist Pilgrim unser neuer Baumeister er ist sehr talentiert",4],
        ["say","pilgrim","Euer Ehren zu euren diensten"],
        ["say","pilgrim","eure Majestät hattet ihr einen Bauvorschlag"],
        ["poll",["Was soll Pilgrim bauen?",
              ["Eine Kathedrale",
               "Ein Markt",
               "Eine Mühle",
               "Eine Schmiede"],
               [[["say","pilgrim","dafür fehlen uns die Ressourcen "],["retry"]],
                [["say","erek","wir haben schon einen"],["retry"]],
                [["say","erek","das ist eine gute Idee"], ["newTask",7,"Pilgrim: Mühle bauen:",[["clear"],["say","game","Die Mühle ist fertig"],["set","bewohnerGefallen",12]]]],
                [["say","erek","wir haben doch letztes Jahr eine neue gebaut"],["retry"],["wait"]]]
              ]],
        ["clear"],
        ["say","pilgrim","ich werde mich sofort an die Arbeit machen"],
        ["say","erek","Was soll ich noch für dich machen?"],
        ["poll",["Was soll Erek machen?",
              ["Ressourcen sammeln",
               "Truppen ausbilden"],
               [[["say","erek","Das ist eine gute Idee"],
                   ["newTask",5,"Erek: ressourcen sammeln",[["say","erek","ich habe fertig gesammelt"],["set","holz",50],["set","stein",30],["time",5],["wait",4]]]],
                [["say","erek","Wir haben aber keine Kaserne"],["retry"],["wait"]]]
              ]],
        ["runTasks"],
        ["clear"]
           

        ]

questBurgBauen = [["say","game"," Burg"],        
                  ]
questMaterialSammeln = [["say","game"," Material"],    
                  ]
questGeheimnissRuinen = [     ["say","erek","Hallo Dario."],
                              ["poll",["Deine Antwort:",
                                    ["Hallo Erek","Habe gerade keine Zeit"],
                                    [[  ["clear"],
                                        ["say","dario","Hallo Erek"],
                                        ["say","erek","Heute ist ja ein wundervolles Wetter."],
                                        ["poll",["Deine Antwort:",
                                                ["Ja finde ich auch","Ja das Wetter ist fast so schön wie deine Mutter"],
                                                [[["clear"],["say","dario","Ja finde ich auch"]],
                                                [     ["clear"],
                                                      ["say","dario","Ja das Wetter ist fast so schön wie deine Mutter"],
                                                      ["say","erek","meine Mutter?"],
                                                      ["wait",3],
                                                      ["say","erek","ist auch egal"],
                                     ]]]]],[["clear"],["say","dario","Habe gerade keine Zeit"],["set","erekGefallen",-15]]]]],
                              ["say","erek","ich bin hier um etwas mitzuteilen"],
                              ["say","dario","was gibt es?"],
                              ["say","erek","du weißt ja wenn du am See durch die Schlucht gehst"],
                              ["say","erek","kommst du ja zu dem Wald da."],
                              ["say","erek","in diesem Wald haben ein paar Bauern alte Ruinen gefunden."],
                              ["poll",["Deine Antwort:",
                                    ["Immer diese Bauern","Ok was ist mit diesen Ruinen?"],
                                    [[["clear"],
                                      ["say","dario","Immer diese Bauern"],["set","bewohnerGefallen",-10],
                                      ["say","erek","Ok wenn du nicht wissen möchtest was sie gefunden haben"],
                                      ["say","erek","ist auch ok."],["say","erek","Schönen Tag dir noch!"],
                                      ["say","dario","Dir auch"],],
                                     [    ["clear"],
                                          ["say","dario","Ok was ist mit diesen Ruinen?"],
                                          ["set","bewohnerGefallen",+5],
                                          ["say","erek","Diese Ruinen machen einen sehr stabilen eindruck."],
                                          ["say","dario","Meinst du Pilgrim sollte sich die mal ansehen?"],
                                          ["say","erek","Ja genau, ich glaube er kann da noch was lernen"],
                                          ["say","erek","Ich gebe ihm gleich bescheid"],
                                          ["newTask",5,"Pilgrim: Alte Mauern begutachten",[["wait",1]]],
                                          ["runTasks"],
                                          ["clear"],
                                          ["time",1],
                                          ["say","pilgrim","Die Mauern waren sehr interessand."],
                                          ["say","pilgrim","Ich konnte viel lernen"],
                                          ["say","pilgrim","Mit dieser Technologie"],
                                          ["say","pilgrim","können unsere Mauern dem Feind viel besser wiederstehen"],
                                          ["set","def",10],
                                          
                                    ]]]],
                              ]



game = [["sideQuest",5,[["!gold! >= 5",questBurgBauen],["!gold! >= 50",questMaterialSammeln,True],["1",questGeheimnissRuinen],]]]  


