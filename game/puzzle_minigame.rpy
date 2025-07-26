default full_page_size = (640, 871)

default page_pieces = [
    [im.Scale("pieces/piece_1.png", 288, 218), (352, 0)], \
    [im.Scale("pieces/piece_2.png", 406, 193), (0, 0)], \
    [im.Scale("pieces/piece_3.png", 206, 392), (0, 94)], \
    [im.Scale("pieces/piece_4.png", 240, 286), (0, 446)], \
    [im.Scale("pieces/piece_5.png", 316, 290), (162, 111)], \
    [im.Scale("pieces/piece_6.png", 324, 174), (315, 178)], \
    [im.Scale("pieces/piece_7.png", 442, 329), (198, 208)], \
    [im.Scale("pieces/piece_8.png", 346, 397), (294, 474)], \
    [im.Scale("pieces/piece_9.png", 308, 339), (224, 532)], \
    [im.Scale("pieces/piece_10.png", 277, 209), (163, 662)], \
    [im.Scale("pieces/piece_11.png", 198, 154), (0, 717)], \
]

default initial_piece_positions = []
default finished_pieces = 0

init python:
    def setup_puzzle():
        global initial_piece_positions
        initial_piece_positions = []
        for _ in page_pieces:
            rand_x = renpy.random.randint(1200, 1700)
            rand_y = renpy.random.randint(200, 800)
            initial_piece_positions.append((rand_x, rand_y))

    def piece_drop(dropped_on, dragged_piece):
        # Extract the piece number from the drag names
        piece_num = dragged_piece[0].drag_name.replace("piece_", "")
        target_num = dropped_on.drag_name.replace("target_", "")
        
        # Debug output to see what's happening
        renpy.notify("Dropped piece {} on target {}".format(piece_num, target_num))
        
        if piece_num == target_num:
            renpy.notify("Match! Placing piece {}".format(piece_num))
            # Snap to the target's position
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            global finished_pieces
            finished_pieces += 1
            renpy.restart_interaction()  # Refresh the screen to update the counter
            if finished_pieces == len(page_pieces):
                renpy.end_interaction("complete")
        else:
            renpy.notify("No match: {} vs {}".format(piece_num, target_num))


label puzzle_minigame:
    jump camera_ep

screen reassemble_puzzle:
    # Show progress counter
    text "Pieces placed: [finished_pieces]/[len(page_pieces)]" xpos 50 ypos 50 size 30 color "#ffffff"

    frame:
        background "pieces/pieces_frame.png"
        xysize full_page_size
        anchor (0, 0)
        pos (330, 100)  # Direct top-left positioning

    draggroup:
        # Draggable pieces
        for i, piece in enumerate(page_pieces):
            drag:
                drag_name "piece_" + str(i)
                pos initial_piece_positions[i]
                anchor (0, 0)
                focus_mask True
                drag_raise True
                image piece[0]

        # Drop targets - now much simpler positioning
        for i, piece in enumerate(page_pieces):
            drag:
                drag_name "target_" + str(i)
                draggable False
                droppable True
                dropped piece_drop
                pos (330 + piece[1][0], 100 + piece[1][1])  # Frame position + piece offset
                anchor (0, 0)
                focus_mask True
                image piece[0] alpha 0.2  # Make slightly visible for debugging



label reassemble_complete:
    return