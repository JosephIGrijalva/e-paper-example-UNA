# Author: Steven Puckett
# Section: CIS 225 01
# Date: 09/11/2019
# File: una_lions.py
#
# A simple program to draw UNA LIONS using Graphics

from graphics import *

def main():
    print("This program draws out UNA LIONS in a graphics window")

    win = GraphWin("UNA",800,480) 
    win.setBackground("purple") 
  
    y_bottom = 230
    y_top = 170
    
    # Draw a Circle for the bottom half of the U  
    u = Circle(Point(120,205), 25)
    u.setFill("purple")
    u.setWidth(3)
    u.setOutline("white")
    u.draw(win)
    
    # Draw a block to hide the top half of the circle
    block = Rectangle(Point(90,y_top),Point(150,210))
    block.setFill("purple")
    block.setOutline("purple")
    block.draw(win)

    # Draw a line for the left side of the "U"
    u_line_left = Line(Point(95,212),Point(95,y_top))
    u_line_left.setWidth(3)
    u_line_left.setOutline("white")
    u_line_left.draw(win)
    
    # Draw a line for the right side of the "U"
    u_line_rigtht = Line(Point(145,y_bottom), Point(145,y_top))
    u_line_rigtht.setWidth(3)
    u_line_rigtht.setOutline("white")
    u_line_rigtht.draw(win)
          
    # Draw the N
    n_line_left = Line(Point(173,y_bottom), Point(173,y_top))
    n_line_left.setWidth(3)
    n_line_left.setOutline("white")
    n_line_left.draw(win)    
    
    n_line_right = n_line_left.clone()
    n_line_right.move(46,0)
    n_line_right.draw(win)
    
    n_line_diag = Line(Point(173,y_top), Point(219,y_bottom))
    n_line_diag.setWidth(3)
    n_line_diag.setOutline("white")
    n_line_diag.draw(win) 

    # Draw the A
    a_line_left = Line(Point(270,y_top),Point(247,y_bottom))
    a_line_left.setWidth(3)
    a_line_left.setOutline("white")
    a_line_left.draw(win) 
    
    a_line_right = Line(Point(270,y_top),Point(290,y_bottom))
    a_line_right.setWidth(3)
    a_line_right.setOutline("white")
    a_line_right.draw(win)
    
    a_cross_bar = Line(Point(260,200),Point(280,200))
    a_cross_bar.setWidth(3)
    a_cross_bar.setOutline("white")
    a_cross_bar.draw(win)


    # Draw a Tick Mark for the letters
    tick = Line(Point(10,10),Point(20,10))
    tick.setWidth(3)
    tick.setOutline("white")
    tick.move(130,220)
    tick.draw(win)
    
    # Clone the tick mark for each end of the lines
    tick_1 = tick.clone()
    tick_1.move(0,-60)
    tick_1.draw(win)
    
    tick_2 = tick_1.clone()
    tick_2.move(-50,0)
    tick_2.draw(win)   
    
    tick_3 = tick.clone()
    tick_3.move(28,0)
    tick_3.draw(win)
    
    tick_4 = tick_3.clone()
    tick_4.move(46,0)
    tick_4.draw(win)

    tick_5 = tick_3.clone()
    tick_5.move(0,-60)
    tick_5.draw(win)
    
    tick_6 = tick_4.clone()
    tick_6.move(0,-60)
    tick_6.draw(win)
    
    tick_7 = tick_6.clone()
    tick_7.move(51,0)
    tick_7.draw(win)    
    
    tick_8 = tick_4.clone()
    tick_8.move(29,0)
    tick_8.draw(win)
    
    tick_9 = tick_8.clone()
    tick_9.move(42,0)
    tick_9.draw(win)
    
    # Write out Lions
    # Write the O
    o_lion = Circle(Point(190, 300),15)
    o_lion.setWidth(2)
    o_lion.setOutline("white")
    o_lion.draw(win)
    
    # Write the I
    i_lion = Line(Point(160,315),Point(160,285))
    i_lion.setWidth(2)
    i_lion.setOutline("white")
    i_lion.draw(win)
    
    # Write the L
    l_lion = Line(Point(145,315),Point(130,315))
    l_lion.setWidth(2)
    l_lion.setOutline("white")
    l_lion.draw(win)
    
    l2_lion=i_lion.clone()
    l2_lion.move(-30,0)
    l2_lion.draw(win)
    
    # Write the N
    n_left_lion = i_lion.clone()
    n_left_lion.move(60,0)
    n_left_lion.draw(win)
    
    n_right_lion = n_left_lion.clone()
    n_right_lion.move(20,0)
    n_right_lion.draw(win)
    
    n_diag_lion = Line(Point(220,285),Point(240,315))
    n_diag_lion.setWidth(2)
    n_diag_lion.setOutline("white")
    n_diag_lion.draw(win)
    
    # Write the S
    s_top = Circle(Point(265,293),8)
    s_top.setWidth(2)
    s_top.setOutline("white")
    s_top.draw(win)
    
    s_bottom = s_top.clone()
    s_bottom.move(0,15)
    s_bottom.draw(win)

    # Draw out boxes to hide the parts of the circles we want to hide in the 'S'
    box_1 = Rectangle(Point(266,290),Point(275,300))
    box_1.setFill("purple")
    box_1.setOutline("purple")
    box_1.draw(win)
    
    box_2 = box_1.clone()
    box_2.move(-13,11)
    box_2.draw(win)
    
    input("Hit enter to close the window")
    
main()