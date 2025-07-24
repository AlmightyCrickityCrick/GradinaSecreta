image uncle_house_outside = im.Scale("uncle house outside.png",1920,1080)
image uncle_house_inside1 = im.Scale("uncle house inside 1.png",1920,1080)
image library1 = im.Scale("library 1.png",1920,1080)
image uncle_simple_garden = im.Scale("uncle simple garden.png",1920,1080)
image library_hidden_passage = im.Scale("library hidden passage.png",1920,1080)
image secret_cousin_room = im.Scale("secret cousin room.png",1920,1080)

image green_boook = im.Scale("green book.png",200,400)
image red_boook = im.Scale("red book.png",200,400)

define audio.background_song_1 = "background song 1.mp3"
define audio.whispers_library = "whispers library.mp3"

# The game starts here.

label start:

    play music background_song_1 volume 0.1
    jump arrival_to_uncles_house

    return
