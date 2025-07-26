
image casa_parinteasca = im.Scale("casa parinteasca2.jpeg", 1920, 1080) 
image casa unchiului = im.Scale("casa unchiului.jpeg", 1920, 1080) 
image casa parinteasca alb-negru = im.Scale("casa parinteasca alb-negru.png", 1920, 1080) 
image black = im.Scale("black.jpeg", 1920, 1080)
image camera_c_p = im.Scale("camera din casa parinteasca.png", 1920, 1080)
image corridor cu usa = im.Scale("corridor cu usa.png", 1920, 1080)
image camera_ep = im.Scale("camera ep.jpg", 1920, 1080)
image birou = im.Scale("birou.png", 1920, 1080)
image sertar = im.Scale("sertar.png", 1920, 1080)
image dulap = im.Scale("dulap.png", 1920, 1080)
image usa_dulap = im.Scale("usa in dulap(1).png", 1920, 1080)
image camera lui colin = im.Scale("camera lui colin.png", 1920, 1080)
image bad_end = im.Scale("bad end.png", 1920, 1080)
image holl= im.Scale("holl.png", 1920, 1080)
image corridor_spre_colin= im.Scale("corridor spre Colin.png", 1920, 1080)

define audio.usa = "usa.mp3"
define audio.chirp = "chirp.mp3"
define audio.gradina = "gradina.mp3"
define audio.hartia = "hartia.mp3"
define audio.pian = "pian.mp3"
define audio.rain = "rain.mp3"
define audio.sertar = "sertar.mp3"
define audio.sosirea = "sosirea.mp3"
define audio.tufis = "tufis.mp3"
define audio.usa_birou = "usa birou.mp3"




label pre_istorie:
    queue music background_song_0
    scene casa_parinteasca

    "Penelope Lennox nu a fost niciodată un copil dorit."
    "Sub soarele orbitor al Indiei, trăia ca un obiect uitat într-un sertar – văzută, dar niciodată aleasă."
    jump mama

label mama:

    scene intro2
    Mama "Las-o pe Ayah să-i dea de mâncare. Am rochia nouă de la Paris de încercat!"

    jump holera


label holera:
    scene casa parinteasca alb-negru

    "Timp de 48 de ore, tăcerea a înghițit totul."
    "Părinții ei, mumii în eșarfe albe."
    "Aya, o grămadă sub un cearșaf în curtea din spate."
    "Și Penelope..."
    "singură cu un șarpe care îi lingea picioarele goale, așteptând ca cineva..."
    "oricine..."
    "să-și amintească că a existat."

    scene black 
    "Când toți mor, cine rămane să plângă după tine?"
    jump ofiter
label ofiter:
    scene camera_c_p
    Ofiter "Unchiul tău e un om... particular. Nu te aștepta la flori și îmbrățișări."
    Penelope "N-am primit niciodată nici una. De ce aș începe acum?"

    jump casa

#sunet de crasnet si portile se deschid
label casa:
    scene casa unchiului
    play sound usa
    "Ușa grea a conacului scrâșni când Penelope o deschise, ca un geamăt de durere. Aerul împuțit de praf și ceară veche o învălui, amestecându-se cu umbra lungă a serii."

    scene holl
    "Pe pereți, portretele strămoșilor păreau să o privească cu milă - o musafiră nedorită în această casă de doliu."
    jump cip_cip

label cip_cip:
    play sound chirp
    "Cip-cip!"
    "O pasăre roșietică ciugulea un fir de iarbă pe pervaz. Ochii ei negri străluceau curios spre fată."
    show Penelope img1
    Penelope "Ayah spunea că păsările aduc vești... Oare asta e semnul că am ajuns unde trebuie?"
    jump corridor_cu_usa

label corridor_cu_usa:
    scene corridor cu usa
    show Penelope img1
    play sound rain
    show Craven img2 at right
    "Peste geam ploua când Domnul Craven – un văr îndepărtat – o studie fără să coboare jos. "
    "Ai înțeles regulile? - rostogoli el. - Nu deranja. Nu întreba. Nu plânge."
    hide Craven img2
    show Servitoare img1
    Servitoare"El n-a mai vorbit cu nimeni de când Doamna Lily a murit... Nici măcar cu băiatul."
    Servitoare "Aici vei sta de-acum."

label camera_ep:
    scene camera_ep
    "Penelope deschise ușa încet. Lumina de pe fereastră curgea peste podeaua de lemn, iar perdelele albe fâlfâiau în adiere. "
    "Camera părea suspendată în timp. Pe pereți, fluturii din rame stăteau nemișcați, ca niște amintiri uitate."
    "Se apropie de noptieră, fără să știe ce caută. Sertarul cedă cu un scârțâit blând. Înăuntru, un jurnal legat în piele șifonată strălucea slab în lumina lunii. "

    $ setup_puzzle()
    $ finished_pieces = 0

    call screen reassemble_puzzle
    
    play audio hartia
    "Pe copertă, inițialele L.C. erau gravate cu cerneală roșie - ca sângele uscat. "
    "10 Iulie... Grădina noastră secretă a înflorit azi. Arhid spune că e periculos să o păzim, dar eu... - restul paginii era smulsă. "
    "Degetele i se înfiorară. Ce ascundea acest loc? "
    stop audio

    "Vrei să cauți toate obiectele și să afli ce legătură are jurnalul cu grădina secretă?"
    menu:
        "Da – Continuă căutarea.":
            jump ce_inseamna
        "Nu – Închide jurnalul și așteaptă dimineața.":
            jump nu_intereseaza

label nu_intereseaza:
    Penelope "E doar un vis. Un vis scris pe hârtie veche. N-are rost să mă agăț de umbre..."
    jump casa

label ce_inseamna:
    Penelope "Grădina secretă?... interesant... Trebuie să găsesc mai multă informație."
    jump birou

label birou:
    scene birou
    play audio usa_birou
    "Ușa bine-uleiată a biroului alunecă în cadru cu un șuierat abia auzit. Aerul miroase a pergament vechi și fum stins. Cărțile aliniază pereții ca niște martori tăcuți. În colțul opus, un dulap masiv, din lemn înnegrit, înghite lumina. "
    "Apropiindu-se cu grijă de unul dintre numeroasele sertare, ea a tras de mâner."
    "Balamalele scârțâiau ușor, ca și cum ar fi încercat să-și ascundă secretul."
    jump sertar

label sunet:
    scene birou
    stop music fadeout 1.0
    queue music pian
    "Și... acolo. Un sunet."
    "Nu un suspin. Nu un foșnet."
    "O melodie"
    "Fragilă, ca un cântec de leagăn murmurat de cineva ce nu mai știe ce e somnul."
    Penelope "Cine... cântă? Și de ce din spatele cărților?"

    "Vrei să investighezi sunetul care vine din spatele dulapului?"
    menu:
        "Da - Mergi să cauți sursa sunetului.":
            jump dulap
        "Nu e treaba ta. Pleacă și întoarce-te mai târziu.":
            jump nu_ea_treaba_ta

    jump dulap

label sertar:
    scene sertar
    play audio sertar
    call screen search_game

    if is_over2 == True:
        if is_win2 == True:
            "Ai gasit toate lucrurile!"
        else:
            "Timpul a expirat!"

    jump sunet

label dulap:
    scene dulap
    "Penelope trecu cu degetele peste cotoarele prăfuite. Lemnul suspina la fiecare atingere, parcă păstrând în el poveștile celor care atinseseră rafturile înaintea ei."
    "Apoi le văzu"
    "O carte roșie, groasă, legată în piele, cu titlul șters de vreme – parcă bătută de ploi și sânge."
    "Una albastră, subțire, de un albastru aprins, cu broderie aurie și miros de frunze uscate."
    Penelope "Una dintre ele trebuie să fie cheia. Dar care..."
    menu:
        "Cartea roșie": # + points
            jump carte_rosie 
        "Cartea albastră":
            jump carte_albastra

label nu_ea_treaba_ta:
    scene birou
    "Unele uși rămân închise dintr-un motiv. Poate... poate încă nu sunt pregătită."
    jump casa 

label carte_rosie:
    "Cartea alunecă din mâna ei – ca și cum o forță nevăzută refuza să fie citită."
    "Căzu pe podea cu un ecou stins, iar în genunchi, când fata se aplecă să o ridice, observă ceva ce nu văzuse până atunci."
    "Un mâner de fier, ascuns într-o cavitate sub raft. Rece ca piatra udă."
    Penelope "Asta n-are ce căuta aici..."

    scene usa_dulap
    "Trage. Un zgomot gutural de metal pe lemn umple biblioteca. Un perete lateral se dă la o parte, scrâșnind din toate încheieturile."
    scene corridor_spre_colin
    "În spatele lui – un coridor îngust, care duce spre o cameră slab luminată."
    jump camera_lui_Colin_rosu

label camera_lui_Colin_rosu:
    scene camera lui colin
    "Penelope rămase cu respirația tăiată. "
    "În spatele dulapului, nu o simplă încăpere, ci o lume pierdută: pereți albi pătați de umbre, o fereastră înțesată de iederă. "
    "Și acolo, în scaunul cu rotile, un băiat palid cu ochi ca gheața sub lumina lunii."

    stop music fadeout 1.0

    "Cânta încet, dar melodia s-a oprit brusc când a văzut-o."
    Colin "Cine ești? Cum ai ajuns aici?"
    "Vocea lui nu era furioasă. Era precaută. Ca și cum fiecare om pe care îl întâlnea putea să-i fure ceva — liniștea, secretele, sau grădina din vis."
    Penelope "Sunt Penelope. Tocmai am ajuns la conac. Și dacă nu întreb nimic și nu plâng, am voie să rămân. Așa mi s-a spus."
    Penelope "Au zis că sunt nepoata domnului Craven. Dar nimeni nu m-a chemat cu adevărat. Am... găsit o carte. A căzut. Apoi, un mâner."
    Penelope "N-am vrut să intru. Adică… am vrut. Dar n-am știut ce caut. Până acum."
  
    queue music background_song_0
    "Ochii băiatului se lărgesc. Se uită la cartea din mâna Penelopei ca la o păpușă din copilărie pierdută și regăsită."
    Colin "Cartea aceea... Era a mea. O citea mama când eram bolnav. Nu credeam că cineva o mai găsește. Tu... ai gust bun."
    jump rosu

label rosu:
    Colin "Dar... ce cauți aici, de fapt?"
    menu:
        "Spune adevărul":
            jump adevar 
        "Spune altceva":
            jump alt_ceva
label adevar:
    Colin "Și tu o vrei... Grădina. Toți o vor. Toți cred că o pot repara. Dar nu înțeleg nimic."
    Penelope "Eu nu vreau să iau nimic. Doar... să știu."
    Colin "Pleacă. Te rog."
    jump albastru

label alt_ceva:
    Penelope "Nu știu... Nu căutam nimic. M-a adus... cartea. Și... poate și cântecul tău."
    Colin "Tu ești prima persoană care mă ascultă. De fapt."
    "Vorbele se preling ușor, ca lumina de amurg: despre păsări care se opresc doar pe un geam anume, despre vise care se repetă și despre secrete care cresc ca florile."
    jump corridor


label carte_albastra:
    "Cartea alunecă din mâna ei – ca și cum o forță nevăzută refuza să fie citită."
    "Căzu pe podea cu un ecou stins, iar în genunchi, când fata se aplecă să o ridice, observă ceva ce nu văzuse până atunci."
    "Un mâner de fier, ascuns într-o cavitate sub raft. Rece ca piatra udă."
    Penelope "Asta n-are ce căuta aici..."

    scene usa_dulap
    "Trage. Un zgomot gutural de metal pe lemn umple biblioteca. Un perete lateral se dă la o parte, scrâșnind din toate încheieturile."
    "În spatele lui – un coridor îngust, care duce spre o cameră slab luminată."
    jump camera_lui_Colin_albastru

label camera_lui_Colin_albastru:
    scene camera lui colin
    "Penelope rămase cu respirația tăiată. "
    "În spatele dulapului, nu o simplă încăpere, ci o lume pierdută: pereți albi pătați de umbre, o fereastră înțesată de iederă. "
    "Și acolo, în scaunul cu rotile, un băiat palid cu ochi ca gheața sub lumina lunii."
    "Cânta încet, dar melodia s-a oprit brusc când a văzut-o."
    Colin "Cine ești? Cum ai ajuns aici?"
    "Vocea lui nu era furioasă. Era precaută. Ca și cum fiecare om pe care îl întâlnea putea să-i fure ceva — liniștea, secretele, sau grădina din vis."
    Penelope "Sunt Penelope. Tocmai am ajuns la conac. Și dacă nu întreb nimic și nu plâng, am voie să rămân. Așa mi s-a spus."
    Penelope "Au zis că sunt nepoata domnului Craven. Dar nimeni nu m-a chemat cu adevărat. Am... găsit o carte. A căzut. Apoi, un mâner."
    Penelope "N-am vrut să intru. Adică… am vrut. Dar n-am știut ce caut. Până acum."

    "Băiatul o fixează. Îi fuge privirea de la fața ei la coperta albastră, apoi înapoi."
    Colin "Aia nu... aia n-avea ce să fie scoasă. De ce ai ales tocmai pe ea?"
    Penelope "A căzut singură..."
    Colin "Toate cărțile cad. Nu toate trebuiau ridicate."
    "Băiatul se închide. Fruntea i se încrețește. Își trage pătură mai sus."
    Colin "Dacă nu mai vrei nimic, pleacă. Te rog."
    jump albastru

label albastru:
    scene corridor
    "Penelope pleacă. Ușa rămâne deschisă. Pe hol – unchiul."
    Craven "Ai fost acolo?! Ți-am interzis!"

label bad_end:
    scene bad_end
    "Gradina secretă rămâne pierdută... Dar poveștile au întotdeauna o a doua șansă."

    #buton incepe din nou
    jump ofiter





