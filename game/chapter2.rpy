image corridor = im.Scale("corridor.png", 1920, 1080) 
image gradina_veranda = im.Scale("gradina_veranda.png", 1920, 1080) 
image gradina = im.Scale("gradina.png", 1920, 1080) 
image usa_tufis = im.Scale("usa in tufis.png", 1920, 1080) 
image gradina_secreta = im.Scale("gradina secreta.png", 1920, 1080) 
image diferente = im.Scale("diferente/diferente1.png", 1920, 1080) 


label corridor:
    
    scene corridor

    show Penelope img1
    "Penelope nu atinse mâncarea de la micul dejun. Farfuria a rămas neatinsă, dar mâna ei, pe furiș, strecură o bucată de pâine în buzunarul rochiei. Poate pentru mai târziu. Poate pentru cineva care nu avea voie la masă."
    "Coridorul principal era întunecos, luminat doar de reflexele obosite ale soarelui printre draperii groase. Acolo, la cotitură, zări o servitoare — tânără, îngenuncheată, cu un teanc de rufe proaspăt spălate căzute în jurul ei."
    "Țesături albe, pătate ici-colo, se amestecau cu praful de pe podea."
    show Servitoare img1 at right
    Servitoare "Nu, nu, nu, nu, din nou... Domnul Craven o să fie furios..."
    hide Penelope img1
    show Penelope img2 
    "Vrei să o ajuți pe servitoare să adune rufele căzute?"
    menu:
        "Da: o ajuți ":
            hide Penelope img2
            hide Servitoare img1
            jump ajutor
        "NU: treci mai departe ":
            hide Penelope img2
            hide Servitoare img1
            jump nu_ajuti
    return

label ajutor:
    show Servitoare img1 at right
    show Penelope img1 
    "Penelope se aplecă fără cuvinte și adună o batistă căzută. Fata o privește uluită pentru o clipă, apoi roșește. Împreună, termină în tăcere."
    Servitoare "Mulțumesc... n-ai fi avut de ce s-o faci."
    Servitoare "Avea dreptate bătrâna Martha... poate nu ești chiar ca ceilalți."
    Servitoare "(Șoptind, ca un gând spus prea tare)
    Într-o zi, chiar am văzut-o pe Doamna Lily ducând acolo o cheie... către grădină. Dar acum e totul încuiat. O fi pierdută pentru totdeauna."
    hide Penelope img1

    show Penelope img2 
    "Întrebi mai mult despre grădina secretă?"
    menu: 
        "Da, întrebi":
            hide Servitoare img1
            hide Penelope img2
            jump intrebi_servitoarea
        "Nu, taci și pleci mai departe":
            hide Servitoare img1
            hide Penelope img2
            jump nu_intrebi_servitoarea


label nu_ajuti:
    show Servitoare img1 at right
    "Penelope trecu mai departe fără să spună nimic. Tălpile ei tăcură peste podeaua rece.
    În urmă, servitoarea rămase îngenuncheată, cu rușine pe obraz și ochii în podea."
    hide Servitoare img1
    jump corridor 


label intrebi_servitoarea:
    show Penelope img1 
    show Servitoare img1 at right
    Penelope "Și... ai mai auzit pe cineva vorbind despre acea grădină? E chiar atât de... secretă?"
    Servitoare "N-ar fi trebuit să mă fi auzit. Scuzați-mă, domnișoară."
    " Fără alt cuvânt, se întoarce și pleacă în grabă, uitând un ciorap pe jos."
    "Seara, Penelope e chemată de unchiul ei. Ușa biroului troncăne greoi."
    hide Penelope img1
    hide Servitoare img1
    jump bad_end_intrebari
        
label bad_end_intrebari:
    show Craven img2 
    Craven "Se pare că ai urechi prea mari pentru locuri închise. Ți-am spus să nu întrebi."
    Craven "Nu ai ce căuta aici. Mâine vei fi trimisă înapoi."
    hide Craven img2
    jump bad_end

label nu_intrebi_servitoarea:
    show Penelope img1
    show Servitoare img1 at right
    "Penelope o privește pe fată cum se îndepărtează cu grijă. În mâna ei, una dintre rufe se mișcă ușor, ca o floare pe timp de vânt."
    Penelope "(în gând)
    Deci cheia a existat. Și dacă există o cheie… există și o încuietoare."
    hide Penelope img1
    hide Servitoare img1


label veranda:
    scene gradina_veranda
    "În prima zi, Penelope o zărise doar cu coada ochiului — O grădină mare, ca din poveste. Astăzi însă... era altfel."

# jocul - gaseste 7 diferente 
    scene diferente

    call screen dif_game

    if is_over3 == True:
        if is_win3 == True:
            "Ai gasit toate diferentele!"
        else:
            "Timpul a expirat!/Ai facut 5 greseli!"

    scene gradina_veranda

# a doua fotografie cu diferente se numeste "gradina veranda joc"

    show Robin at right
    "Un fâlfâit scurt. Un tril vesel, aproape ironic."
    "Pe balustrade, în bătaia soarelui, stă același robin roșu pe care Penelope îl văzuse în prima zi."
    "O pasăre mică, cu pieptul aprins ca o brichetă vie."
    show Penelope img1
    Penelope "Tu din nou? Sau poate ai fost aici tot timpul…"
    hide Penelope img1
    show Penelope img2

    "Hrănești pasărea cu bucata de pâine?"
    menu: 
        "Da - îi dai pâinea":
            hide Penelope img2
            jump zbor 
        "Nu - păstrezi pâinea":
            hide Penelope img2
            jump zbor

label zbor:
    show Robin at right
    "Robin își înclină capul, părând să o studieze pe Penelope o clipă. Apoi, cu un „cip-cip” răsunător, își deschide aripile – un fulger roșu pe cerul palid – și se înălță în văzduh. Penele îi străluceau în lumina slabă"

    show Penelope img2
    "Mergi după pasăre?"
    menu:
        "Da – o urmărești":
            hide Robin
            hide Penelope img2
            jump gradina
        "Nu – te întorci înapoi":
            hide Robin
            hide Penelope img2
            jump nu_mergi

label nu_mergi:
    "Penelope se întoarce cu pași rari spre casă. Pe drum, simte privirea."
    "Pe terasa dinspre est, unchiul Craven o privește fix."
    show Craven img2
    Craven "Ai timp de hoinărit? Sau ai de gând să încalci reguli neștiute încă?"
    hide Craven img2
    jump bad_end


label gradina:
    scene gradina
    show Robin
    "Robinul zboară scurt, apoi se așază. Zboară din nou. Se oprește. De parcă ar cunoaște drumul mai bine decât oricine."
    hide Robin

    call screen order_game

    if is_over == True:
        if is_win == False:
            jump gradina
    
    show Robin at right
    "În cele din urmă, se oprește lângă un tufiș mare și des, cu frunze care se mișcă fără vânt."
    show Penelope img2
    "Cauți ceva în tufiș?"
    menu:
        "Da – cauți":
            hide Robin
            hide Penelope img2
            jump usa_tufis
        "Nu – ignori și te întorci":
            hide Robin
            hide Penelope img2
            jump nu_cauti

label nu_cauti:
    show Penelope img2
    "Penelope privește tufișul, dar nu îndrăznește."
    "Se întoarce."
    show Craven at right
    "Unchiul e în lângă ușă."
    "Așteaptă. Privește."
    hide Penelope img2
    hide Craven
    jump bad_end


label usa_tufis:
    scene usa_tufis
    "Frunzele se lasă la o parte cu un foșnet moale. Înăuntru — mușchi, pietre și... metal rece."
    "O ușă veche, rotundă, învelită de rădăcini. Cu un lacăt ruginit."
    Penelope "E adevărată... Grădina chiar există..."
    jump gradina_secreta

label gradina_secreta:
    scene gradina_secreta
    "Grădina secretă a tresărit la atingerea ta... 
Și-și dezvăluie acum tainele, pâclă de pâclă,
în vântul ce șoptește numele tău printre trandafiri."