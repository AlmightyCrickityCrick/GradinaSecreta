label house1:

    show screen explore_hall_one
    label explore_loop_one:
    $ renpy.pause(0.1, hard=True)
    jump explore_loop_one

return

label house2:

    show screen explore_hall_two
    label explore_loop_two:
    $ renpy.pause(0.1, hard=True)

    if current_room_two == 5:
        if first_library_entry:
            Penelope "Aerul miroase a pergament vechi și fum stins."
            Penelope "Un sunet."
            Penelope "Nu un suspin. Nu un foșnet."
            Penelope "O melodie."
            Penelope "Fragilă, ca un cântec de leagăn murmurat de cineva ce nu mai știe ce e somnul."
            Penelope "„Cine... cântă? Și de ce din spatele cărților?"
            $ first_library_entry = False

    jump explore_loop_two

return