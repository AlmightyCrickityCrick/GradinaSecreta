default is_over2 = False
default is_win2 = False
default inventory = []

init python:
    import pygame

    def get_scaled_image(name, width, height):
        return Transform(name, size=(width, height))

    class SearchEl(renpy.Displayable):
        def __init__(self, elements):
            super().__init__(self)
            self.width = 1920
            self.height = 1080

            self.elements = elements

        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)

            st_p = 50

            text_element = renpy.render(Text(f"Time remaining: {5 - st}"), 1000, 50, st, at)
            r.blit(text_element,(20,20))

            for i, el in enumerate(self.elements):
                element = renpy.render(get_scaled_image(el[0][0], el[0][1], el[0][2]), el[1], el[2], st, at)
                r.blit(element,(el[3],el[4]))
            
            for i, el in enumerate(globals() ['inventory']):
                element = renpy.render(get_scaled_image(el[0][0], el[0][1], el[0][2]), el[1], el[2], st, at)
                r.blit(element,(st_p, 100))
                st_p += 50 + el[1]
            
            if st >= 5:
                globals() ['is_over2'] = True
                renpy.timeout(0)

            renpy.redraw(self, 0)

            return r

        def event(self, ev, x, y, st):
            if ev.type == pygame.MOUSEBUTTONDOWN:
                for el in self.elements:
                    if el[3] < x and el[4] < y and el[1] + el[3] > x and el[4] + el[2] > y:
                        globals()['inventory'].append(el)
                        self.elements.remove(el)
                        if len(self.elements) == 0:
                            globals() ['is_over2'] = True
                            globals() ['is_win2'] = True
            
            if globals() ['is_over2']:
                return globals() ['is_over2']
            else:
                raise renpy.IgnoreEvent()



screen search_game:
    
    $ globals()['inventory'] = []
    default searchEl = SearchEl([ \
        [("sertar/carte.png",100,100),100,100,100,100], \
        [("sertar/cerneala.png",100,100),100,100,200,300], \
        [("sertar/fotografie.png",100,100),100,100,300,400], \
        [("sertar/harta.png",100,100),100,100,400,500], \
        [("sertar/lenta.png",100,100),100,100,400,500], \
        [("sertar/pana.png",100,100),100,100,400,500], \
        [("sertar/scrisori.png",100,100),100,100,400,500], \
        [("sertar/timbru.png",100,100),100,100,500,600] \
        ])

    add searchEl


label search_minigame:

    jump sertar
    # call screen search_game

    # if is_over2 == True:
    #     if is_win2 == True:
    #         "Ai gasit toate lucrurile!"
    #     else:
    #         "Timpul a expirat!"