default is_over3 = False
default is_win3 = False

init python:
    import pygame

    class DifEl(renpy.Displayable):
        def __init__(self, elements):
            super().__init__(self)
            self.width = 1920
            self.height = 1080

            self.mistakes = 0
            self.elements = elements
            self.circles = []

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)

            st_p = 50

            text_element = renpy.render(Text(f"Time remaining: {5 - st}"), 1000, 50, st, at)
            r.blit(text_element,(20,20))

            text_element = renpy.render(Text(f"Mistakes left: {5 - self.mistakes}"), 1000, 50, st, at)
            r.blit(text_element,(20,100))

            for i, el in enumerate(self.circles):
                element = renpy.render(im.Scale("circle.png",el[0],el[1]), el[0], el[1], st, at)
                r.blit(element,(el[2],el[3]))
            
            if st >= 5 or self.mistakes >= 5:
                globals() ['is_over3'] = True
                renpy.timeout(0)

            renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            at_least_once = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for el in self.elements:
                    if el[2] < x and el[3] < y and el[0] + el[2] > x and el[3] + el[1] > y:
                        self.circles.append(el)
                        self.elements.remove(el)
                        at_least_once = True
                        if len(self.elements) == 0:
                            globals() ['is_over3'] = True
                            globals() ['is_win3'] = True
                if not at_least_once:
                    self.mistakes += 1


            if globals()['is_over3']:
                return globals()['is_over3']
            else:
                raise renpy.IgnoreEvent()

screen dif_game:
    add "uncle_house_outside"

    default difEL = DifEl([ \
        [100,100,100,100], \
        [100,100,200,300], \
        [100,100,300,400], \
        [100,100,400,500], \
        [100,100,500,600] \
    ])

    add difEL


label dif_minigame:
    call screen dif_game

    if is_over3 == True:
        if is_win3 == True:
            "Ai gasit toate diferentele!"
        else:
            "Timpul a expirat!/Ai facut 5 greseli!"