import sys
sys.path.append('C:/Users/Joseph H. Hendrickso/AppData/Local/Programs/Python/Python37/Tools')
sys.path.append('C:/Users/Joseph H. Hendrickso/Documents/python')
import pdb
from joe_turtle_utilities import *
from joe_utilities import *
from graphics import *
from turtle import *
from random import randint
import math
from turtle import TurtleScreen, RawTurtle, TK

def find_in_list(a,l):
    out = []
    for i in range(len(l)):
        if a == l[i]: 
            out = out +[i]
    return out

def process_hit(guess,word,start_letters_pt):
    spots = find_in_list(guess,word)
    for spot in spots:
        pt = add(start_letters_pt,[spot*35,0])
        #if guess in "ilt":
            #pt = add(pt,[15,0])
        up()
        goto(pt[0],pt[1])
        clr=color()
        color("white")
        write(guess,font=("Courier", 40, "normal"))
        #color(clr)
        

def process_miss():
    head_pt  = draw_head(height,start_pt)
    
    leg_pt   = draw_body(height,head_pt)
    draw_leg(height,leg_pt,-65)  #right leg
    draw_leg(height,leg_pt,-115)  #right leg
    
    
    draw_arm (height, head_pt, leg_pt, -65)  #right arm
    draw_arm (height, head_pt, leg_pt, -115)  #right arm




def mkscreen(win,bottom_left_point=[-500,-500],top_right_point=[500,500]):
    lx = bottom_left_point[0] 
    ly = bottom_left_point[1] 
    ux = top_right_point[0] 
    uy = top_right_point[1] 
    setworldcoordinates(lx, ly, ux, uy)

   

def make_scaffold_base(height):
    base_len = height
    base_height = height/4
    color("black")
    up()
    start_pt = [-base_len/4, -height/2]
    goto(start_pt)
    seth(0)
    down()
    begin_fill()
    fd(base_len)
    seth(-90)
    fd(base_height)
    seth(180)
    fd(base_len)
    seth(90)
    fd(base_height)
    end_fill()
    beam_start_point = [0,-height/2]
    return (beam_start_point)
    

def draw_hangman_beam(height,start_pt):
    up()
    color("brown")
    width(10)
    goto (start_pt)
    seth(90)
    down()
    fd(height)
    seth(0)
    fd(height/4)
    seth(-90)
    width(4)
    color("gray")
    fd(height/5)
    start_pt = [xcor(), ycor()]
    return( start_pt )



    
                    
def draw_scaffold(height):
    # draw base
    width(5)
    start_pt = make_scaffold_base(height)
    # draw support beam
    end_of_rope_pt = draw_hangman_beam(height, start_pt)
    # return location to start head
    return ( [xcor(), ycor()] )

def draw_head(height,pt):
    up()
    goto (pt)
    seth(180)
    down()
    color("red")
    radius = height/15
    circle(radius,540)    
    return ( [xcor(),ycor()] )

def draw_leg(height,pt,angle):
    up()
    goto(pt)
    seth(angle)
    down()
    fd(height/10)
    return ( [xcor(),ycor()] )

def draw_foot(height,pt,angle):
    up()
    goto(pt)
    seth(angle)
    down()
    fd(height/60)

    
def draw_body(height,pt):
    up()
    goto (pt)
    seth(-90)
    down()
    fd(height/5)
    return([xcor(),ycor()])





    
def draw_arm (height, head_pt, leg_pt, angle):
    up()
    goto(head_pt)
    seth(-90)
    fd( 0.25 * (dist(head_pt,leg_pt) ) )
    seth(angle)
    down()
    fd(height/10)
    
   
    

  
       
def play_game(word_list,height):

    
    # choose word
    word = word_list[randint(1, len(word_list)-1)]
    wlen = len(word)
    start_pt = draw_scaffold(height)    # print spaces for letters
    start_letters_pt = mult(height,[-0.25,-0.75])
    start_input_pt   = sub(start_letters_pt,[0,50])
    start_letters_pt = add(start_letters_pt,[5,8])

    # clean up from previous game
    up()
    goto(start_input_pt)
    width(50)
    down()
    color("white")
    goto(add(start_input_pt,[300,0]))
    
    # draw spaces
    width(5)
    down()
    l_pt = start_letters_pt
    color("white")
    for i in range(wlen):
        up()
        goto(l_pt)
        down()
        l_pt = add(l_pt,[30,0])
        goto(l_pt)
        l_pt = add(l_pt,[5,0])
    
    up()
    
    done = False
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    remaining_letters = set(word)
    misses = 0
    while not done:
        color("red")
        goto(start_input_pt)
        write("Guess a letter:",font=("Arial", 18, "normal"))
        guess = ""
        while not((guess in lowercase) and (len(guess)== 1)):
            guess = input()
        if guess in remaining_letters:
            remaining_letters = remaining_letters - set(guess)
            process_hit(guess,word,start_letters_pt)
            if len(remaining_letters) == 0:
               done = True
               continue
        else:
            misses = misses+1
            #print("misses=",misses)
            if misses == 1:            
                head_pt  = draw_head(height,start_pt)
            elif misses == 2:
                leg_pt   = draw_body(height,head_pt)
            elif misses == 3:
                foot_pt = draw_leg(height,leg_pt,-65)  #right leg
            elif misses == 4:
                draw_foot(height,foot_pt,0)
            elif misses == 5:
                foot_pt = draw_leg(height,leg_pt,-115)  #right leg
            elif misses == 6:
                draw_arm (height, head_pt, leg_pt, -65)  #right arm
            elif misses == 7:
                draw_foot(height,foot_pt,180)
            elif misses == 8:
                draw_arm (height, head_pt, leg_pt, -115)  #right arm
                done = True
            up()
    if len(remaining_letters) == 0:
        msg = "Congratulations - You win"
    else:
        msg = "Sorry - You lose. The word was '" + word + "'"
    goto(start_input_pt)
    width(50)
    down()
    color("white")
    goto(add(start_input_pt,[300,0]))
    up()
    color("blue")
    goto(start_input_pt)
    write(msg,font=("Arial", 18, "normal"))
        
    

def main(height=300):
    
    ht()
    word_list = read_word_list (4,7,10)
    playing = True
    
    print("\n\nWelcome to Hangman!\n\n")
    
    
    
    while playing:
        clear()
        play_game(word_list, height)
        again = input("Play Agian (y/n)? ")
        playing = again == 'y'
    
    return "EVENTLOOP"

main(300)

#pdb.run("main()")

#if __name__ == '__main__':
#    main()
#    mainloop()  # keep window open until user closes it
   
    

    
    

    

