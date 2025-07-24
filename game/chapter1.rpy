
init python:
    globals()['ceva'] = "ceva"
    import pygame

    class Book(renpy.Displayable):

        def __init__(self, color, book, pos):
            super().__init__(self)
            self.color = color
            self.book = book
            self.pos = pos

label arrival_to_uncles_house:

    scene uncle_house_outside
    
    show fl
    "Penelope a ajuns în casa unchiului"
    hide fl

    jump get_into_uncles_house

label get_into_uncles_house:
    scene uncle_house_inside_door

    "Ușa grea a conacului scrâșni când Penelope o deschise, ca un geamăt de durere. Aerul împuțit de praf și ceară veche o învălui, amestecându-se cu umbra lungă a serii. Pe pereți, portretele strămoșilor păreau să o privească cu milă - o musafiră nedorită în această casă de doliu."

    jump search_through_house


screen find_smth:
    pass

screen find_toys:
    pass

label search_through_house:
    scene uncle_house_inside1
    show screen find_smth

    menu:
        "Este suspicios":
            # call screen find_toys
            jump library
        "Nu ma intereseaza. E ora cinei":
            jump search_through_house
    return

screen book(book, color, pos):
    vbox:
        add book
    

label library:

    scene library1
    
    play sound whispers_library

    "Aud ceva"

    menu:
        "Este suspicios. Ma uit.":
            stop sound
            jump choose_book
        "Daca fac ceva, unchiul se va enerva":
            stop sound
            jump bad_end

    return

label choose_book:

    menu:
        "Aleg cartea verde":
            $ book = "green"
            jump hidden_passage
        "Aleg cartea rosie":
            $ book = "red"
            jump hidden_passage
    
    return

label hidden_passage:

    scene library_hidden_passage
    jump secret_room
    return

label secret_room:

    scene secret_cousin_room
    if book == "green":
        jump wrong_dialog_boy
    else:
        jump right_dialog_boy

    return

label right_dialog_boy:

    menu:
        "Ma plimb.":
            jump good_dialog_boy
        "Am gasit [ceva]. Ce crezi ar putea insemna?":

            jump bad_end
    return

label good_dialog_boy:

    jump go_to_room
    return

label wrong_dialog_boy:

    jump run_to_hall
    return

label run_to_hall:

    scene uncle_house_inside1

    jump bad_end
    return

label bad_end:
    scene uncle_house_outside:
        matrixcolor SaturationMatrix(0)
    "WASTED"
    return