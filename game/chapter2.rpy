label go_to_room:

    jump maid_hall
    return

label maid_hall:

    menu:
        "Nu-i așa de greu, de aceea da":
            jump maid_hall
        "Singură se discurcă":
            jump find_garden_1
    return

label good_maid:

    jump find_garden_1
    return

label find_garden_1:

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

    call screen two_img_diff
    jump meeting_robin
    return

screen two_img_diff:
    pass

label meeting_robin:

    menu:
        "Desigur":
            jump go_to_the_middle_of_garden
        "Pentru ce?":
            jump bad_end
    return

label go_to_the_middle_of_garden:

    menu:
        "Hai":
            jump robin_and_bush
        "N-are sens, i-o pasăre simplă":
            jump go_back_in_house
    return

label robin_and_bush:

    menu:
        "Lasă. e un tufar simplu":
            jump go_back_in_house
        "Trebuie sa cautam":
            jump find_hidden_garden
    return

label find_hidden_garden:

    return

label go_back_in_house:

    jump bad_end
    return