"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jess Thuer.
"""
###############################################################################
# DONE
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg
window = rg.TurtleWindow

ben = rg.SimpleTurtle('turtle')
ben.pen = rg.Pen('grey',1)
ben.speed = 100

jerry = rg.SimpleTurtle('turtle')
jerry.pen = rg.Pen('maroon',1)
jerry.speed = 100

size1 = 5
size2 = 3

for k in range(50):
    ben.draw_circle(size1)
    ben.pen_up()
    ben.right(45)
    ben.forward(5)
    ben.left(45)
    ben.pen_down()
    size1 = size1 + 5

for k in range (50):

    jerry.draw_square(size2)
    jerry.pen_up()
    jerry.left(30)
    jerry.backward(2.5)
    jerry.right(70)
    jerry.pen_down()
    size2 = size2 + 5

window.close_on_mouse_click()
