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

define audio.background_song_0 = "background song 0.mp3"
define audio.background_song_1 = "background song 1.mp3"
define audio.whispers_library = "whispers library.mp3"

define mother = Character("Mama", color = "#ffffff")
define fl = Character("Penelope", color = "#ffffff")
define sheriff = Character("Ofițer", color = "#ffffff")

# The game starts here.

label start:

    queue music background_song_0 volume 0.1

    call prologue

    stop music fadeout 1.0

    queue music background_song_1 volume 0.1

    jump arrival_to_uncles_house
