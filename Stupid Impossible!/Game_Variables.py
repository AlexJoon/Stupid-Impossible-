from graphics import *
import random
import time
import sys


#Window Variables for the First Level.
def Window_Variables():

    Window_Name = "Stupid Impossible!"
    Window_x = 800
    Window_y = 400

    return Window_Name , Window_x , Window_y

Window_Variables()


#Window Variables for the Second Level.
def Window_Variables_2():

    Window_Name_2 = "Stupid Impossible!"
    Window_x_2 = 500
    Window_y_2 = 600

    return Window_Name_2 , Window_x_2 , Window_y_2

Window_Variables_2()


#Window Variables for the Third Level.
def Window_Variables_3():

    Window_Name_3 = "Stupid Impossible!"
    Window_x_3 = 600
    Window_y_3 = 600

    return Window_Name_3 , Window_x_3 , Window_y_3

Window_Variables_3()


#Window Variables for the Fourth Level.
def Window_Variables_4():

    Window_Name_4 = "Stupid Impossible!"
    Window_x_4 = 600
    Window_y_4 = 600

    return Window_Name_4 , Window_x_4 , Window_y_4


Window_Variables_4()


#Window Variables for the Fifth Level.
def Window_Variables_5():

    Window_Name_5 = "Stupid Impossible!"
    Window_x_5 = 800
    Window_y_5 = 500

    return Window_Name_5 , Window_x_5 , Window_y_5

Window_Variables_5()

    
#Window Variables for the Sixth Level.
def Window_Variables_6():

    Window_Name_6 = "Stupid Impossible!"
    Window_x_6 = 700
    Window_y_6 = 600

    return Window_Name_6 , Window_x_6 , Window_y_6

Window_Variables_6()


#Window Variables for the Final Level.
def Window_Variables_7():

    Window_Name_7 = "Stupid Impossible!"
    Window_x_7 = 600
    Window_y_7 = 600

    return Window_Name_7 , Window_x_7 , Window_y_7

Window_Variables_7()


#Movement for the First Level.
def Movement_Variables():

    X2 = 0
    Y2 = 0
    F2 = 0
    F3 = 4
    V2 = 0
    V3 = -4

    return X2 , Y2 , F2 , F3 , V2 , V3

Movement_Variables()


#Movement for the Second Level.
def Movement_Variables_2():

    X2 = 0
    Y2 = 0
    F2 = -3
    F3 = 0
    V2 = 3
    V3 = 0

    O1 = 0
    O2 = -4

    return X2 , Y2 , F2 , F3 , V2 , V3 , O1 , O2

Movement_Variables_2()


#Movement for the Third Level.
def Movement_Variables_3():

    X2 = 0
    Y2 = 0
    F2 = 3
    F3 = 0
    V2 = -3
    V3 = 0

    return X2 , Y2 , F2 , F3 , V2 , V3

Movement_Variables_3()


#Movement for the Fourth Level.
def Movement_Variables_4():

    X2 = 0
    Y2 = 0
    F2 = 0
    F3 = 3
    V2 = 0
    V3 = -3

    D0 = -3
    D1 = 0
    D2 = 3
    D3 = 0 

   
    return X2 , Y2 , F2 , F3 , V2 , V3 , D0 , D1 , D2 , D3

Movement_Variables_4()


#Movement for the Fifth Level.
def Movement_Variables_5():

    X2 = 0
    Y2 = 0
    F2 = 0
    F3 = -10
    V2 = 10
    V3 = 0

    return X2 , Y2 , F2 , F3 , V2 , V3

Movement_Variables_5()


#Movement for the Sixth Level.
def Movement_Variables_6():

    X2 = 0
    Y2 = 0

    F1 = -6
    F2 = 0

    F3 = 6
    F4 = 0

    V1 = 0
    V2 = 5

    V3 = 5
    V4 = 0

    V5 = -5
    V6 = 0

    V7 = 5
    V8 = 0
    
    return X2 , Y2 , F1, F2 , F3 , F4 , V1 , V2 , V3 , V4 , V5 , V6 , V7 , V8

Movement_Variables_6()


#Movement for the Final Level.
def Movement_Variables_7():

    X2 = 0
    Y2 = 0
    F2 = 5
    F3 = 0
    V2 = 0
    V3 = 4

    return X2 , Y2 , F2 , F3 , V2 , V3

Movement_Variables_7()


#Interface accessories.
def Level_Display():

    Size = 11
    Fill = "blue"
    Font = "courier"
    Style = "italic"

    return Size , Fill , Font , Style

Level_Display()


