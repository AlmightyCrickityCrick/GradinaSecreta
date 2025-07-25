default current_room_one = 1
default first_maid_click = True
default first_room_exit = True
default first_drawer_search = True
default first_journal_search = True
default first_birou_entry = True

label bird:
    scene intro7

    Robin "Cip-cip!"
    Penelope "Ayah spunea că păsările aduc vești..."
    Penelope "Oare asta e semnul că am ajuns unde trebuie?"
return

label uncle_first_encounter:
    scene intro7

    show Craven
    Craven "Ai inteles regulile?"
    Craven "Nu deranja. Nu întreba. Nu plânge"
    hide Craven

    $ first_room_exit = False
return

label maid_about_uncle:
    scene intro7
    
    show Maid at Position(xpos = 300, ypos = 1500)
    Maid "Domnul Craven n-a mai vorbit cu nimeni de când Doamna Lily a murit... Nici măcar cu băiatul."
    hide Maid

    $ first_maid_click = False
return

label journal:
    scene intro1
    "Coperta L.C."
    jump journal_open
return

label journal_open:
    scene intro2
    "10 Iulie... Grădina noastră secretă a înflorit azi. Arhid spune că e periculos să o păzim, dar eu..."
    "Restul paginii era smulsă."
    if first_journal_search:
        "Degetele i se înfiorară."
        Penelope "Ce ascundea acest loc?"
        "Vrei să cauți toate obiectele și să afli ce legătură are jurnalul cu grădina secretă?"
        menu:
            "Continua cautarea.":
                $ first_journal_search = False
                "Grădina secretă?... interesant... Trebuie să găsesc mai multă informație."
        
            "Inchide jurnalul si asteapta dimineata.":
                Penelope "E doar un vis. Un vis scris pe hârtie veche. N-are rost să mă agăț de umbre..."
                jump restart
    else:
        "Grădina secretă?... interesant... Trebuie să găsesc mai multă informație."
return

label drawer:
    scene intro4

    if first_drawer_search:
        "Apropiindu-se cu grijă de unul dintre numeroasele sertare, ea a tras de mâner. Balamalele scârțâiau ușor, ca și cum ar fi încercat să-și ascundă secretul."
        "Ai descoperit un fragment misterios în jurnal."
        "Pentru a înțelege mesajul, trebuie să aduni toate indiciile ascunse în cameră înainte ca lumânarea să se stingă."
        "Ai 30 de secunde. Fiecare obiect te apropie de înțelegerea misterului. Dacă nu reușești, indiciile vor rămâne pierdute în întuneric."
        $ first_drawer_search = False
#MINIGAME

return


screen explore_hall_one():
    
    #Display the background image depending on current_room
    if current_room_one == 1:
        add "intro1.png"

        imagebutton:
            idle "robin.png"
            hover "east_hover.png"
            xpos 300
            ypos 300
            action Function(renpy.call_in_new_context, "bird")

        imagebutton:
            idle "robin.png"
            hover "east_hover.png"
            xpos 600
            ypos 300
            action Function(renpy.call_in_new_context, "journal")

    elif current_room_one == 2:
        add "intro2.png"
        imagebutton:
            idle "house door.png"
            hover "east_hover.png"
            xpos 600
            ypos 300
            action Function(renpy.call_in_new_context, "house2")

        if first_maid_click:
            imagebutton:
                idle "maid.png"
                hover "east_hover.png"
                xpos 900
                ypos 300
                action Function(renpy.call_in_new_context, "maid_about_uncle")
        else:
            imagebutton:
                idle "east_idle.png"
                hover "east_hover.png"
                xpos 900
                ypos 300
                action Function(renpy.call_in_new_context, "bird")
            
    elif current_room_one == 3:
        add "intro3.png"

        imagebutton:
            idle "drawer.png"
            xpos 900
            ypos 300
            action Function(renpy.call_in_new_context, "drawer")

    #If we're NOT in the last room, show the right arrow
    if current_room_one < 3:

        if first_room_exit:
            imagebutton:
                idle "arrow right.png"
                hover "east_hover.png"
                xpos 1770
                ypos 300
                action Function(renpy.call_in_new_context, "uncle_first_encounter")

        else:
            imagebutton:
                idle "arrow right.png"
                hover "east_hover.png"
                xpos 1770
                ypos 300
                action SetVariable("current_room_one", current_room_one + 1)

    #If we're NOT in the first room, show the left arrow
    if current_room_one > 1:
        imagebutton:
            idle "arrow left.png"
            hover "east_hover.png"
            xpos 50
            ypos 300
            action SetVariable("current_room_one", current_room_one - 1)