import random

newVal = 0
oldval = 0
change = 0


setupCharacter = [["dario",[":crown: [rgb(255,140,20)] Dario:[/rgb(255,140,20)]", "rgb(255,150,100)"]],
                  ["erek",[":shield: [rgb(50,200,190)] Dario:[/rgb(50,200,190)]", "rgb(150,255,255)"]],
                  ["pilgrim",[":hammer_and_pick: [rgb(70,220,50)] Dario:[/rgb(70,220,50)]", "rgb(200,255,150)"]],
                  ["game",["", "rgb(200,200,255)"]],
                  ]
setupVars = [
             ["seed","r",random.randint(1585411,994599399),""],
             ["jahr","rw",1,""],
             ["day","rw",1,""],

             ["gold","rw",3465,f"[rgb(255,210,0)]Gold[/rgb(255,210,0)]: {oldval} -> {change} -> {newVal}"],
             ["bewohner","rw",72,""],
             ["essen","rw",100,""],
             ["holz","rw",50,""],
             ["stein","rw",20,""],

             ["bewohnerGefallen","rw",50,f"Das [rgb(255,200,150)]Ansehen[/rgb(255,200,150)] Darios hat sich um {change} geändert und ist nun {newVal}"],
             ["erekGefallen","rw",75,f"[rgb(50,200,190)]Ereks[/rgb(50,200,190)] meinung gegenüber Dario hat sich um {change} geändert und ist jetzt {newVal}"],
             ["pilgrimGefallen","rw",75,f"[rgb(70,220,50)]Pilgrims[/rgb(70,220,50)] meinung gegenüber Dario hat sich um {change} geändert und ist jetzt {newVal}"],

             
             ]

intro = [["say","game"," Die Schlacht gegen das Böse"],
            ["say","game"," In einer fernen Welt,"],
            ["say","game"," geprägt von Königreichen,"],
            ["say","game"," Rivalitäten und Eroberungen,"],
            ["say","game"," übernimmst du die Rolle von unserem König Dario.",3],
            ["say","game"," Deine Aufgabe ist es,"],
            ["say","game"," das Schicksal unseres Königreichs zu lenken.",3],
            ["say","game"," Unser Königreich wird von Kerberos Truppen bedroht.",3],
            ["say","game"," Deine Aufgabe ist es die Verteidigung zu organisieren",3],
            ["say","game"," und strategische Entscheidungen zu treffen,"],
            ["say","game"," um das Überleben deines Volkes zu sichern."],
            ["say","game"," Deine strategischen Entscheidungen"],
            ["say","game"," werden den Verlauf der Geschichte"],
            ["say","game"," und das Schicksal des Königreichs bestimmen.",3],
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
                    [["say","erek","das ist eine gute Idee"], ["newTask",7,"Pilgrim: Mühle bauen:",[["say","game","Die Mühle ist fertig"],["set","bewohnerGefallen",12]]]],
                    [["say","erek","wir haben doch letztes Jahr eine neue gebaut"],["retry"],["wait"]]]
                  ]],
            ["clear"],
            ["say","pilgrim","ich werde mich sofort an die Arbeit machen"],
            ["say","erek","Was soll ich noch für dich machen?"],
            ["poll",["Was soll Erek machen?",
                  ["Ressourcen sammeln",
                   "Truppen ausbilden"],
                   [[["say","erek","Das ist eine gute Idee"],
                       ["newTask",7,"Erek: ressourcen sammeln",[["erek","ich habe fertig gesammelt"],["set","holz",50],["set","stein",30]]]],
                    [["say","erek","Wir haben aber keine Kaserne"],["retry"],["wait"]]]
                  ]],
            ["runTasks"],
            ["set","holz",50],["set","gold",30],["set","erekGefallen", 15],
               ["set","pilgrimGefallen", -15],["set","bewohnerGefallen",12]

            ]

             

teststr = [    ["set","erekGefallen", 15],
               ["set","pilgrimGefallen", -15],
               ["set","bewohnerGefallen",12],
               ["set","gold",-200],
               ["set","bewohner",80],
               ["set","essen",-25],
               ["set","holz",70],
               ["set","stein",-2],]