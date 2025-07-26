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
        [im.Scale("robin_2.png",250,250),250,250,100,400], \
        [im.Scale("robin_2.png",250,250),250,250,350,150], \
        [im.Scale("robin_2.png",250,250),250,250,650,225], \
        [im.Scale("robin_2.png",250,250),250,250,900,300], \
        [im.Scale("robin_2.png",250,250),250,250,500,600], \
        [im.Scale("robin_2.png",250,250),250,250,1050,700], \
        [im.Scale("robin_2.png",250,250),250,250,1500,300], \
        [im.Scale("robin_2.png",250,250),250,250,1300,580], \
        [im.Scale("robin_2.png",250,250),250,250,150,700]
        ])

    add clickableEl

label order_minigame:
    jump gradina