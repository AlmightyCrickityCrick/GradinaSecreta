image corridor = "corridor.png"


label go_to_room:

    jump maid_hall
    return

label corridor:
    scene corridor

    "Penelope nu atinse mâncarea de la micul dejun. Farfuria a rămas neatinsă, dar mâna ei, pe furiș, strecură o bucată de pâine în buzunarul rochiei. Poate pentru mai târziu. Poate pentru cineva care nu avea voie la masă."
    "Coridorul principal era întunecos, luminat doar de reflexele obosite ale soarelui printre draperii groase. Acolo, la cotitură, zări o servitoare — tânără, îngenuncheată, cu un teanc de rufe proaspăt spălate căzute în jurul ei."
    "Țesături albe, pătate ici-colo, se amestecau cu praful de pe podea."
    Servitoarea "Nu, nu, nu, nu, din nou... Domnul Craven o să fie furios..."
    
    "Vrei să o ajuți pe servitoare să adune rufele căzute?"
    menu:
        "Da: o ajuți ":
            jump ajutor
        "NU: treci mai departe ":
            jump nu_ajuti
    return

label ajutor:
    "Penelope se aplecă fără cuvinte și adună o batistă căzută. Fata o privește uluită pentru o clipă, apoi roșește. Împreună, termină în tăcere."
    Servitoarea "Mulțumesc... n-ai fi avut de ce s-o faci."
    Servitoarea "Avea dreptate bătrâna Martha... poate nu ești chiar ca ceilalți."
    Servitoarea "(Șoptind, ca un gând spus prea tare)
    Într-o zi, chiar am văzut-o pe Doamna Lily ducând acolo o cheie... către grădină. Dar acum e totul încuiat. O fi pierdută pentru totdeauna."

    "Întrebi mai mult despre grădina secretă?"
    menu: 
        "Da, întrebi":
            jump intrebi_servitoarea
        "Nu, taci și pleci mai departe":
            jump nu_intrebi_servitoarea


label nu_ajuti:
    "Penelope trecu mai departe fără să spună nimic. Tălpile ei tăcură peste podeaua rece.
În urmă, servitoarea rămase îngenuncheată, cu rușine pe obraz și ochii în podea."
    jump corridor 


label intrebi_servitoarea:
    Penelope "Și... ai mai auzit pe cineva vorbind despre acea grădină? E chiar atât de... secretă?"
    Servitoarea "N-ar fi trebuit să mă fi auzit. Scuzați-mă, domnișoară."
    " Fără alt cuvânt, se întoarce și pleacă în grabă, uitând un ciorap pe jos."
    "Seara, Penelope e chemată de unchiul ei. Ușa biroului troncăne greoi."
        jump bad_end
        
label bad_end:
    Craven "Se pare că ai urechi prea mari pentru locuri închise. Ți-am spus să nu întrebi."
    Craven "Nu ai ce căuta aici. Mâine vei fi trimisă înapoi."

label nu_intrebi_servitoarea:
    "Penelope o privește pe fată cum se îndepărtează cu grijă. În mâna ei, una dintre rufe se mișcă ușor, ca o floare pe timp de vânt."
    Penelope "(în gând)
    Deci cheia a existat. Și dacă există o cheie… există și o încuietoare."














label good_maid:

    jump find_garden_1
    return

label find_garden_1:
    scene uncle_simple_garden

    menu:
        "Intreaba":
            jump maid_uncle
        "Nu intreaba":
            jump go_out_of_garden
    return

label maid_uncle:

    jump bad_end
    return

label go_out_of_garden:

    # call screen two_img_diff
    jump meeting_robin
    return

screen two_img_diff:
    pass

label meeting_robin:
    scene uncle_simple_garden

    menu:
        "Desigur":
            jump go_to_the_middle_of_garden
        "Pentru ce?":
            jump bad_end
    return

label go_to_the_middle_of_garden:
    scene uncle_simple_garden_middle

    menu:
        "Hai":
            jump robin_and_bush
        "N-are sens, i-o pasăre simplă":
            jump go_back_in_house
    return

label robin_and_bush:
    scene bush

    menu:
        "Lasă. e un tufar simplu":
            jump go_back_in_house
        "Trebuie sa cautam":
            jump find_hidden_garden
    return

label find_hidden_garden:
    scene secret_garden
    "Ai gasit gradina secreta"
    return

label go_back_in_house:
    scene uncle_house_inside1
    "Esti iarasi in casa"
    jump bad_end
    return