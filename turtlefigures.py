from turtle import *
import math



 
# -------------------- binary tree (0) ------------------------
def tree(n, l, pen):
     if n==0 or l<2 :
          return
     #endif
     pen.forward(l)
     pen.left(45)
     tree(n-1, l/2, pen)
     pen.right(90)
     tree(n-1, l/2, pen)
     pen.left(45)
     pen.backward(l)


 
#end binary tree



     
 
# ---------------------- quad tree () -------------------------
 
def tree4(n, l, pen):
     # termination
     if n==0 or l<2: return
 
     # recursive contruction
     pen.forward(l)
     pen.left(90)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.right(60)
     tree4(n-1, l/2, pen)
     pen.left(90)
     pen.backward(l)
     
#end quad tree 



     

# ----------------------- fern fractal (3) --------------------
def fern(n, l, pen):
     # termination
     if n==0 or l<2: return

     # recursive contruction
     pen.forward(0.3*l)
     pen.left(55)
     fern(n-1, l/2, pen)
     pen.right(55)
     pen.forward(0.7*l)
     pen.right(40)
     fern(n-1, l/2, pen)
     pen.left(40)
     pen.forward(l)
     pen.left(10)
     fern(n-1, 0.8*l, pen)
     pen.right(10)
     pen.backward(2*l)

#end fern






# ---------------------- serpinsky (4) ------------------

def s(n, l, pen):
     # termination
     if n==0 or l<2:
          # draw an equilateral triangle
          for i in range(3):
               pen.forward(l)
               pen.left(120)
          #end for
          return
     #end if

     #recursive definition
     for i in range(3):
          s(n-1, l/2, pen)
          pen.forward(l/2)
          pen.left(120)
     #end for
          
# end serpinky






# ------------------------- koch snowflake (5) -------------------

def koch(n, l, pen):
    if n==0 or l<2:
        pen.forward(l)
        return
     
    koch(n-1, l/3, pen)
    pen.left(60)
    koch(n-1, l/3, pen)
    pen.right(120)
    koch(n-1, l/3, pen)
    pen.left(60)
    koch(n-1, l/3, pen)
         
def kochsnow(n, l, pen):
     for i in range(3):
          koch(n, l, pen)
          pen.right(120)

    
#end koch



    
# ------------------------ anti-snowflake (6) ----------------------

def koch2(n, l, pen):
    if n==0 or l<2:
        pen.forward(l)
        return
     
    koch2(n-1, l/3, pen)
    pen.left(60)
    koch2(n-1, l/3, pen)
    pen.right(120)
    koch2(n-1, l/3, pen)
    pen.left(60)
    koch2(n-1, l/3, pen)
         
def anti(n, l, pen):
     for i in range(3):
          koch2(n, l, pen)
          pen.left(120)

    
#end koch


    
# ------------------------- square gasket (7) ----------------------


def gasket(n, l, pen):
    if n==0 or l<2:
        for i in range(4):
            pen.forward(l)
            pen.left(90)
        return

    for i in range (4):
        gasket(n-1, l/3, pen)
        pen.forward(l/3)
        pen.left(90)


# ------------------------- circle (8) ----------------------------------

def circle(n, l, pen):
    if n==0 or l<2:
        for i in range (1):
             for colours in ["red", "cyan", "yellow"]:
                  pen.color(colours)
                  pen.circle(l)
                  pen.left(10)
        return

    for i in range (4):
         circle(n-1, l, pen)




   


#----------------------------peoni (9)-----------------------------------

def peoni(n, l, pen):
    if n==0 or l<2:
        pen.forward(l)
        for i in range(5):
             pen.forward(l)
             pen.left(90)
             pen.right(10)
        return
     
     
    for i in range(2):
        pen.color("pink")
        peoni(n-1, l-3, pen)

#----------------------------sunflower (10)-------------------------------


def sunflower(n, l, pen):
     if n==0 or l<2:
          pen.forward(l)
          for i in range(100):
              pen.forward(math.sqrt(i)*50)
              pen.left(170)

     for i in range(2):
        pen.color("orange")
        sunflower(n-1, l, pen)





























    


