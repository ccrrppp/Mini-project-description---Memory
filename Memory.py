import simplegui
import random

state = 0
WIDTH = 863
HEIGHT = 150

mouse_pos = [-1, -1]
card_list = []
view = [[-1, -1],[-1, -1]]
number = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6 ,6]
turns = 0
h = ""
def new_game():
    global state,card_list,mouse_pos,card_list,view,turns
    mouse_pos = [-1, -1]
    state = 0
    card_list = []
    view = [[-1, -1],[-1, -1]]
    turns = 0
    random.shuffle(number)
    for i in range(12):
        card_list.append ( [35 + i * 72 , str(number[i]), False])
    

    
def click(pos):
    global state,mouse_pos,turns,h
    mouse_pos = list(pos)

    for card in card_list:
        if card[2] != True:
            if mouse_pos[0] - card[0] <=35 and mouse_pos[0] - card[0] >=-35:
                if state == 0:
                    state = 1
                    view[0][0] = card[0]
                    view[0][1] = card_list.index(card)
                elif state == 1:
                    turns += 1
                    state = 2
                    view[1][0] = card[0]
                    view[1][1] = card_list.index(card)
                    if card_list[view[0][1]][1] == card_list[view[1][1]][1] :
                        card_list[view[0][1]][2] = True
                        card_list[view[1][1]][2] = True
                else: 
                    state = 1
                    view[0][0] = card[0]
                    view[0][1] = card_list.index(card)
                    view[1][0] = -1
    h = "Turns = " + str(turns)
    label.set_text(h)
                  
def draw(canvas):
    for card in card_list:
        canvas.draw_text(card[1] , [card[0]-10, 75], 50, "White" )
        if card[2] != True:
            if card[0] != view[0][0] and card[0] != view[1][0]:
                canvas.draw_polyline([(card[0],0), (card[0], 150 )], 70, 'Blue')



    
frame = simplegui.create_frame("Memory states", WIDTH, HEIGHT)
frame.set_canvas_background("Black")
frame.add_button("Restart", new_game, 200)
frame.set_mouseclick_handler(click)
frame.set_draw_handler(draw)
label = frame.add_label("Turns = 0", 200)

new_game()
frame.start()
