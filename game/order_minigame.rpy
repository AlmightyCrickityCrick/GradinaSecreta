default is_win = False
default is_over = False

init python:
    import pygame

    def get_order(n):
        return range(0,n)

    class ClickableEl(renpy.Displayable):
        def __init__(self, elements):
            super().__init__(self)
            self.elements = elements
            self.order = get_order(len(elements))
            self.n = 0
            self.j = 0

            self.width = 1920
            self.height = 1080

            self.shown = False
            self.start_time = 0

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)

            time = st - self.start_time

            for i, el in enumerate(self.elements):
                element = renpy.render(el[0], el[1], el[2], st, at)
                if time // 1 % len(self.order) == i and i > self.n:
                    self.shown = True
                if time // 1 % len(self.order) == i and not self.shown and i <= self.n:
                    r.blit(element,(el[3] + 20, el[4]))
                else:
                    r.blit(element,(el[3],el[4]))
            renpy.redraw(self,0)
            return r

        def event(self, ev, x, y, st):
            is_over = False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.elements[self.order[self.j]][3] < x \
                    and self.elements[self.order[self.j]][4] < y \
                    and self.elements[self.order[self.j]][1] + self.elements[self.order[self.j]][3] > x \
                    and self.elements[self.order[self.j]][4] + self.elements[self.order[self.j]][2] > y:
                    if self.j == self.n:
                        self.j = 0
                        self.n += 1
                        self.shown = False
                        self.start_time = st
                        if self.n == len(self.order):
                            globals() ['is_win'] = True
                            is_over = True
                    else:
                        self.j += 1
                else:
                    is_over = True

            
            if is_over:
                globals() ['is_over'] = True
                return is_over
            else:
                raise renpy.IgnoreEvent()

screen order_game:
    
    default clickableEl = ClickableEl([ \
        [im.Scale("teddy bear.png",100,100),100,100,100,100], \
        [im.Scale("teddy bear.png",100,100),100,100,200,300], \
        [im.Scale("teddy bear.png",100,100),100,100,300,400], \
        [im.Scale("teddy bear.png",100,100),100,100,400,500], \
        [im.Scale("teddy bear.png",100,100),100,100,500,600] \
        ])

    add "uncle_house_inside1"
    add clickableEl

label order_minigame:
    call screen order_game

    if is_over == True:
        if is_win == True:
            "Ai castigat"
        else:
            "Ai pierdut"