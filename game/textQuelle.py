import random

setupCharacter = [["dario",[":crown: [rgb(255,140,20)]  Dario:[/rgb(255,140,20)]", "rgb(255,150,100)"]],
                  ["erek",[":shield: [rgb(50,200,190)]   Erek:[/rgb(50,200,190)]", "rgb(150,255,255)"]],
                  ["pilgrim",[":hammer_and_pick: [rgb(70,220,50)] Pilgrim:[/rgb(70,220,50)]", "rgb(200,255,150)"]],
                  ["game",["", "rgb(200,200,255)"]],
                  ]
setupVars = [
             ["seed","r",random.randint(1585411,994599399),[""]],
             ["jahr","rw",1,""],
             ["day","rw",1,""],

             ["gold","rw",3465,"[rgb(255,210,0)]Gold:[/rgb(255,210,0)] !oldVal! -> !change! -> !newVal!"],
             ["bewohner","rw",72,"[rgb(200,160,255)]Bewohner:[/rgb(200,160,255)] !oldVal! -> !change! -> !newVal!"],
             ["essen","rw",100,"[rgb(50,180,50)]Essen:[/rgb(50,180,50)] !oldVal! -> !change! -> !newVal!"],
             ["holz","rw",50,"[rgb(160,110,50)]Holz:[/rgb(160,110,50)] !oldVal! -> !change! -> !newVal!"],
             ["stein","rw",20,"[rgb(160,160,140)]Stein:[/rgb(160,160,140)] !oldVal! -> !change! -> !newVal!"],

             ["bewohnerGefallen","rw",50,"Das [rgb(255,200,150)]Ansehen[/rgb(255,200,150)] Darios hat sich um !change! geändert und ist nun !newVal!"],
             ["erekGefallen","rw",75,"[rgb(50,200,190)]Ereks[/rgb(50,200,190)] meinung gegenüber Dario hat sich um !change! geändert und ist jetzt !newVal!"],
             ["pilgrimGefallen","rw",75,f"[rgb(70,220,50)]Pilgrims[/rgb(70,220,50)] meinung gegenüber Dario hat sich um !change! geändert und ist jetzt !newVal!"],

             
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
                   ["newTask",5,"Erek: ressourcen sammeln",[["say","erek","ich habe fertig gesammelt"],["set","holz",50],["set","stein",30]]]],
                [["say","erek","Wir haben aber keine Kaserne"],["retry"],["wait"]]]
              ]],
        ["runTasks"],
           

        ]

             

teststr = [    ["set","erekGefallen", 15],
               ["set","pilgrimGefallen", -15],
               ["set","bewohnerGefallen",12],
               ["set","gold",-200],
               ["set","bewohner",80],
               ["set","essen",-25],
               ["set","holz",70],
               ["set","stein",-2],]