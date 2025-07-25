default current_room_two = 1
default first_library_entry = True
default carte_rosie = False
default first_book_choice = True

label library:
    scene intro7

    if first_book_choice:

        "Vrei să investighezi sunetul care vine din spatele dulapului?"
        menu:
            "Mergi sa cauti sursa sunetului.":
                Penelope "Grădina nu e doar un loc... e un ecou. Și acum, el vrea să fie auzit."
                "Penelope trecu cu degetele peste cotoarele prăfuite. Lemnul suspina la fiecare atingere, parcă păstrând în el poveștile celor care atinseseră rafturile înaintea ei."
                Penelope "Una dintre ele trebuie să fie cheia. Dar care..."
                menu:
                    "Carte rosie.":
                        $ first_book_choice = False
                        $ carte_rosie = True
                        "Cartea alunecă din mâna ei – ca și cum o forță nevăzută refuza să fie citită."
                        jump handle

                    "Carte albastra.":
                        $ first_book_choice = False
                        "Cartea alunecă din mâna ei – ca și cum o forță nevăzută refuza să fie citită."
                        "Căzu pe podea cu un ecou stins, iar în genunchi, când fata se aplecă să o ridice, observă ceva ce nu văzuse până atunci."
                        "Un mâner de fier, ascuns într-o cavitate sub raft. Rece ca piatra udă."
                        jump handle

            "Nu e treaba ta. Pleaca si intoarce-te mai tarziu.":
                Penelope "Unele uși rămân închise dintr-un motiv. Poate... poate încă nu sunt pregătită."
    else:
        jump colin_room
return

label handle:
    scene intro4

    Penelope "Asta n-are ce căuta aici..."
    "Trage."
    "Un zgomot gutural de metal pe lemn umple biblioteca. Un perete lateral se dă la o parte, scrâșnind din toate încheieturile."
    "În spatele lui – un coridor îngust, care duce spre o cameră slab luminată."
    jump colin
return

label colin:
    scene intro3

    show Colin
    "Camera din spatele dulapului nu era ceea ce Penelope se aștepta să găsească. Nu o cameră de servitori, nu o arhivă uitată. Ci un colț de lume înghețată în timp."
    "Pereții erau palizi, cu dungi de umbră unde soarele nu ajunsese niciodată."
    "În mijloc, lângă o fereastră obturată de iederă, stătea un băiat într-un scaun cu rotile, învelit într-o pătură groasă."
    "Cânta încet, dar melodia s-a oprit brusc când a văzut-o."
    "Ochii lui erau adânci, visători și aproape străvezii."
    Colin "Cine ești? Cum ai ajuns aici?"
    "Vocea lui nu era furioasă. Era precaută. Ca și cum fiecare om pe care îl întâlnea putea să-i fure ceva — liniștea, secretele, sau grădina din vis."
    Penelope "Sunt Penelope. Tocmai am ajuns la conac. Și dacă nu întreb nimic și nu plâng, am voie să rămân. Așa mi s-a spus."
    Penelope "Au zis că sunt nepoata domnului Craven. Dar nimeni nu m-a chemat cu adevărat. Am... găsit o carte. A căzut. Apoi, un mâner."
    Penelope "N-am vrut să intru. Adică… am vrut. Dar n-am știut ce caut. Până acum."

    if carte_rosie:
        "Ochii băiatului se lărgesc. Se uită la cartea din mâna Penelopei ca la o păpușă din copilărie pierdută și regăsită."
        Colin "Cartea aceea... Era a mea. O citea mama când eram bolnav. Nu credeam că cineva o mai găsește. Tu... ai gust bun."
        Colin "Dar... ce cauți aici, de fapt?"
        menu:
            "Spune adevarul":
                "Căut grădina secretă."
                Colin "Și tu o vrei... Grădina. Toți o vor. Toți cred că o pot repara. Dar nu înțeleg nimic."
                Penelope "Eu nu vreau să iau nimic. Doar... să știu."
                Colin "Pleacă. Te rog."
                jump unchiul_library

            "Spune altceva":
                "Doar mă plimbam."
                Penelope "Nu știu... Nu căutam nimic. M-a adus... cartea. Și... poate și cântecul tău."
                Colin "Tu ești prima persoană care mă ascultă. De fapt."
                "Vorbele se preling ușor, ca lumina de amurg: despre păsări care se opresc doar pe un geam anume, despre vise care se repetă și despre secrete care cresc ca florile."
    
    else:
        "Băiatul o fixează. Îi fuge privirea de la fața ei la coperta verde, apoi înapoi."
        Colin "Aia nu... aia n-avea ce să fie scoasă. De ce ai ales tocmai pe ea?"
        Penelope "A căzut singură..."
        Colin "Toate cărțile cad. Nu toate trebuie ridicate."
        "Băiatul se închide. Fruntea i se încrețește. Își trage pătură mai sus."
        Colin "Dacă nu mai vrei nimic, pleacă. Te rog."

        hide Colin
        jump unchiul_library
return

label unchiul_library:
    scene intro1

    show Craven
    Craven "Ai fost acolo?! Ți-am interzis!"
    hide Craven
return

label colin_room:
    scene intro1
    show Colin
    Colin "Salut"
    hide Colin
return

screen explore_hall_two():

    if current_room_two == 1:
        add "intro1.png"

        imagebutton:
            idle "east_idle.png"
            hover "east_hover.png"
            xpos 600
            ypos 100
            action Function(renpy.call_in_new_context, "house1")

    elif current_room_two == 2:
        add "intro2.png"
            
    elif current_room_two == 3:
        add "intro3.png"

    elif current_room_two == 4:
        add "intro3.png"

    elif current_room_two == 5:
        add "intro3.png"

        imagebutton:
            idle "library.png"
            hover "east_hover.png"
            xpos 900
            ypos 300
            action Function(renpy.call_in_new_context, "library")

    if current_room_two < 5:
        imagebutton:
            idle "arrow right.png"
            hover "east_hover.png"
            xpos 1770
            ypos 300
            action SetVariable("current_room_two", current_room_two + 1)

    if current_room_two > 1:
        imagebutton:
            idle "arrow left.png"
            hover "east_hover.png"
            xpos 50
            ypos 300
            action SetVariable("current_room_two", current_room_two - 1)