label arrival_to_uncles_house:

    jump search_through_house
    return

screen find_smth:

    return

screen find_toys:

    return

label search_through_house:
    show screen find_smth

    menu:
        "Este suspicios":
            call screen find_toys
            jump library
        "Nu ma intereseaza. E ora cinei":
            jump search_through_house
    return

label library:

    menu:
        "Este suspicios. Ma uit.":
            jump
        "Daca fac ceva, unchiul se va enerva":
            jump bad_end

    return

label choose_book:

    menu:
        "Aleg cartea verde":
            jump hidden_passage
        "Aleg cartea rosie":
            jump hidden_passage
    
    return

label hidden_passage:

    jump secret_room
    return

label secret_room:

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

    jump bad_end
    return

label bad_end:

    return