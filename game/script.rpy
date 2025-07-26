image india_bungalow = im.Scale("india bungalow.png",1920,1080)
image india_bungalow_back_yard = im.Scale("india bungalow back yard.png",1920,1080)

image uncle_house_outside = im.Scale("uncle house outside.png",1920,1080)
image uncle_house_inside1 = im.Scale("uncle house inside 1.png",1920,1080)
image uncle_house_inside2 = im.Scale("uncle house inside 2.png",1920,1080)
image uncle_house_inside3 = im.Scale("uncle house inside 3.png",1920,1080)
image uncle_house_inside4 = im.Scale("uncle house inside 4.png",1920,1080)
image uncle_house_inside_door = im.Scale("uncle house inside door.png",1920,1080)
image library1 = im.Scale("library 1.png",1920,1080)
image uncle_simple_garden = im.Scale("uncle simple garden.png",1920,1080)
image uncle_simple_garden_middle = im.Scale("uncle simple garden middle.png",1920,1080)
image library_hidden_passage = im.Scale("library hidden passage.png",1920,1080)
image secret_cousin_room = im.Scale("secret cousin room.png",1920,1080)
image bush = im.Scale("bush.png",1920,1080)
image secret_garden = im.Scale("secret garden.png",1920,1080)

image green_boook = im.Scale("green book.png",200,400)
image red_boook = im.Scale("red book.png",200,400)

#HOLDERS
image intro1 = "intro1.png"
image intro2 = "intro2.png"
image intro3 = "intro3.png"
image intro4 = "intro4.png"
image intro5 = "intro5.png"
image intro6 = "intro6.png"
image intro7 = "intro7.png"
image intro8 = "intro8.png"

define audio.background_song_0 = "background song 0.mp3"
define audio.background_song_1 = "background song 1.mp3"
define audio.whispers_library = "whispers library.mp3"

define Penelope = Character(name = "Penelope", color = "ffffff")
define Mama = Character(name = "Mama", color = "ffffff")
define Ofiter = Character(name = "Ofiter", color = "ffffff")
define Servitoare = Character(name = "Servitoare", color = "ffffff")
define Robin = Character(name = "Robin", color = "ffffff")
define Craven = Character(name = "Domnul Craven", color = "ffffff")
define Colin = Character(name = "Colin", color = "ffffff")

image Craven img1 = im.Scale('characters/craven.png',1050,1000)
image Craven img2 = im.Scale('characters/craven1.png',1050,1000)
image Colin img1 = im.Scale('characters/colin.png',1050,1000)
image Colin img2 = im.Scale('characters/colin book.png',1050,1000)
image Penelope img1 = im.Scale('characters/penelope.png',1050,1000)
image Penelope img2 = im.Scale('characters/penelope q.png',1050,1000)
image Robin = im.Scale('characters/robin.png',1050,1000)
image Servitoare img1 = im.Scale('characters/serv.png',1050,1000)

# The game starts here.

label start:
    jump pre_istorie

    hide Craven img1
