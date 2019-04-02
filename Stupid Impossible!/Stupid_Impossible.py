from graphics import *
import time
import sys
import winsound
import Game_Variables


#The interface variables (Windows & Movement) regarding Levels 1-7 were imported from my Game_Variables module that I made.
#I called all the functions from that module file to this one to trim the main game file and separate some functionality between 2 py files.


#First Level Function.
def Main():


    #First interface of the First Level.
    X2 , Y2 , F2 , F3 , V2 , V3 = Game_Variables.Movement_Variables()
    
    Window_Name , Window_x , Window_y = Game_Variables.Window_Variables()

    Size , Fill , Font , Style = Game_Variables.Level_Display()
    
    Window=GraphWin( Window_Name , Window_x , Window_y )
    Window.setBackground("white")

    winsound.PlaySound('SI.wav', winsound.SND_LOOP + winsound.SND_ASYNC)

    
    MSG=Text(Point(400,200)," Welcome to Stupid Impossible! Grab the coin to advance to the next levels.")
    MSG.setSize(Size)
    MSG.setFace(Font)
    MSG.setStyle(Style)
    MSG_2=Text(Point(400,250),"Can you make it to the end? Hit a key to start!")
    MSG_2.setSize(Size)
    MSG_2.setFace(Font)
    MSG_2.setStyle(Style)
    Title = Image(Point( Window_x / 2 , Window_y / 4),"titlepage.png")
   

    MSG.draw(Window)
    MSG_2.draw(Window)
    Title.draw(Window)
    
    Window.getKey()
    
    MSG.undraw()
    MSG_2.undraw()
    Title.undraw()

    Background_1 = Image(Point( Window_x / 2 , Window_y / 2 ),"First Level.png")
    Background_1.draw(Window)

    One = Text(Point(47,300),"Level 1/7")
    One.setSize(Size)
    One.setFill(Fill)
    One.setFace(Font)
    One.setStyle(Style)
    One.draw(Window)

    Coin = Image(Point(750,200),"Coin.png")
    Coin.draw(Window)

    for j in range(sys.maxsize):

        #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(50,210),10)
        Player.setFill("blue")
        Player.draw(Window)

        Projectile_0 = Image(Point(150,200),"projectile.png")
        Projectile_1 = Image(Point(200,200),"projectile.png")
        Projectile_2 = Image(Point(250,200),"projectile.png")
        Projectile_3 = Image(Point(300,200),"projectile.png")
        Projectile_4 = Image(Point(350,200),"projectile.png")
        Projectile_5 = Image(Point(400,200),"projectile.png")
        Projectile_6 = Image(Point(450,200),"projectile.png")
        Projectile_7 = Image(Point(500,200),"projectile.png")
        Projectile_8 = Image(Point(550,200),"projectile.png")
        Projectile_9 = Image(Point(600,200),"projectile.png")
        Projectile_10 = Image(Point(650,200),"projectile.png")


        Projectile_0.draw(Window)
        Projectile_1.draw(Window)
        Projectile_2.draw(Window)
        Projectile_3.draw(Window)
        Projectile_4.draw(Window)
        Projectile_5.draw(Window)
        Projectile_6.draw(Window)
        Projectile_7.draw(Window)
        Projectile_8.draw(Window)
        Projectile_9.draw(Window)
        Projectile_10.draw(Window)


        #Movement, Collision, and Boundaries in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            Projectile_0.move( F2 , F3 )
            Projectile_1.move( V2 , V3 )
            Projectile_2.move( F2 , F3 )
            Projectile_3.move( V2 , V3 )
            Projectile_4.move( F2 , F3 )
            Projectile_5.move( V2 , V3 )
            Projectile_6.move( F2 , F3 )
            Projectile_7.move( V2 , V3 )
            Projectile_8.move( F2 , F3 )
            Projectile_9.move( V2 , V3 )
            Projectile_10.move( F2 , F3 )
            time.sleep(0.01)
            First_Check = Window.checkKey()

            #Player Movement Keys.
            if First_Check=="Left":
                X2=-4
                Y2=0
            if First_Check=="Right":
                X2=4
                Y2=0
            if First_Check=="Down":
                X2=0
                Y2=4
            if First_Check=="Up":
                X2=0
                Y2=-4
            if First_Check=="x":
                X2 = 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.    
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin.getAnchor()
            P3X = P3.getX()

            P4 = Coin.getAnchor()
            P4X = P4.getY()
            
            M0 = Projectile_0.getAnchor()
            M0X = M0.getX()
            MA = Projectile_0.getAnchor()
            MAX = MA.getY()

            M1 = Projectile_1.getAnchor()
            M1X = M1.getX()
            M2 = Projectile_1.getAnchor()
            M2X = M2.getY()

            M3 = Projectile_2.getAnchor()
            M3X = M3.getX()
            M4 = Projectile_2.getAnchor()
            M4X = M4.getY()

            M5 = Projectile_3.getAnchor()
            M5X = M5.getX()
            M6 = Projectile_3.getAnchor()
            M6X = M6.getY()

            M7 = Projectile_4.getAnchor()
            M7X = M7.getX()
            M8 = Projectile_4.getAnchor()
            M8X = M8.getY()

            M9 = Projectile_5.getAnchor()
            M9X = M9.getX()
            M10 = Projectile_5.getAnchor()
            M10X = M10.getY()

            M11 = Projectile_6.getAnchor()
            M11X = M11.getX()
            M12 = Projectile_6.getAnchor()
            M12X = M12.getY()

            M13 = Projectile_7.getAnchor()
            M13X = M13.getX()
            M14 = Projectile_7.getAnchor()
            M14X = M14.getY()

            M15 = Projectile_8.getAnchor()
            M15X = M15.getX()
            M16 = Projectile_8.getAnchor()
            M16X = M16.getY()

            M17 = Projectile_9.getAnchor()
            M17X = M17.getX()
            M18 = Projectile_9.getAnchor()
            M18X = M18.getY()

            M19 = Projectile_10.getAnchor()
            M19X = M19.getX()
            M20 = Projectile_10.getAnchor()
            M20X = M20.getY()


            #Collision Boundary for the Projectiles to move back and forth.
            if Projectile_0.getAnchor().getY() > 345:
                F2 = 0
                F3 = -4
            if Projectile_0.getAnchor().getY() < 50:
                F2 = 0
                F3 = 4
            if Projectile_1.getAnchor().getY() > 345:
                V2 = 0
                V3 = -4
            if Projectile_1.getAnchor().getY() < 50:
                V2 = 0
                V3 = 4
            if Projectile_2.getAnchor().getY() > 345:
                F2 = 0
                F3 = -4
            if Projectile_2.getAnchor().getY() < 50:
                F2 = 0
                F3 = 4
            if Projectile_3.getAnchor().getY() > 345:
                V2 = 0
                V3 = -4
            if Projectile_3.getAnchor().getY() < 50:
                V2 = 0
                V3 = 4
            if Projectile_4.getAnchor().getY() > 345:
                F2 = 0
                F3 = -4
            if Projectile_4.getAnchor().getY() < 50:
                F2 = 0
                F3 = 4
            if Projectile_5.getAnchor().getY() > 345:
                V2 = 0
                V3 = -4
            if Projectile_5.getAnchor().getY() < 50:
                V2 = 0
                V3 = 4    
            if Projectile_6.getAnchor().getY() > 345:
                F2 = 0
                F3 = -4
            if Projectile_6.getAnchor().getY() < 50:
                F2 = 0
                F3 = 4
            if Projectile_7.getAnchor().getY() > 345:
                V2 = 0
                V3 = -4
            if Projectile_7.getAnchor().getY() < 50:
                V2 = 0
                V3 = 4


            #Collision Boundaries for the walls.
            if Player.getCenter().getX() < 1:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() < 195 and Player.getCenter().getX() < 100:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() < 190 and Player.getCenter().getX() < 101:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() < 35:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 220 and Player.getCenter().getX() < 100:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() > 225 and Player.getCenter().getX() < 101:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 355:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 765:
                X2 = -1
                Y2 = 0
                pass


            #Coin Collision.
            elif (abs(P1X-P3X)) < 25 and (abs(P2X-P4X)) < 25:
                Window.close()
                Second_Level()
                
            #Projectile 0 Collision.   
            elif (abs(P1X-M0X)) < 30 and (abs(P2X-MAX)) < 30:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 1 Collision.
            elif (abs(P1X-M1X)) < 20 and (abs(P2X-M2X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 2 Collision.
            elif (abs(P1X-M3X)) < 20 and (abs(P2X-M4X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 3 Collision.
            elif (abs(P1X-M5X)) < 20 and (abs(P2X-M6X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 4 Collision.
            elif (abs(P1X-M7X)) < 20 and (abs(P2X-M8X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 5 Collision.
            elif (abs(P1X-M9X)) < 20 and (abs(P2X-M10X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 6 Collision.
            elif (abs(P1X-M11X)) < 20 and (abs(P2X-M12X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 7 Collision.
            elif (abs(P1X-M13X)) < 20 and (abs(P2X-M14X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 9 Collision.
            elif (abs(P1X-M15X)) < 20 and (abs(P2X-M16X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 10 Collision.
            elif (abs(P1X-M17X)) < 20 and (abs(P2X-M18X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break
            
            #Projectile 11 Collision.
            elif (abs(P1X-M19X)) < 20 and (abs(P2X-M20X)) < 20:
                Player.undraw()
                Projectile_0.undraw()
                Projectile_1.undraw()
                Projectile_2.undraw()
                Projectile_3.undraw()
                Projectile_4.undraw()
                Projectile_5.undraw()
                Projectile_6.undraw()
                Projectile_7.undraw()
                Projectile_8.undraw()
                Projectile_9.undraw()
                Projectile_10.undraw()
                break


#Second Level Function.
def Second_Level():

    #Second interface of the Second Level.
    X2 , Y2 , F2 , F3 , V2 , V3 , O1 , O2 = Game_Variables.Movement_Variables_2()

    Window_2_Name , Window_2_x , Window_2_y = Game_Variables.Window_Variables_2()

    Size , Fill , Font , Style = Game_Variables.Level_Display()
    
    Window_2=GraphWin( Window_2_Name, Window_2_x , Window_2_y )
    Window_2.setBackground("white")

    Background_2 = Image(Point( Window_2_x / 2 , Window_2_y / 1.75 ),"Second Level.png")
    Background_2.draw( Window_2 )

    Two = Text(Point(100,475),"Level 2/7")
    Two.setSize(Size)
    Two.setFill(Fill)
    Two.setFace(Font)
    Two.setStyle(Style)
    Two.draw(Window_2)

    Coin_2 = Image(Point( 260 , 450 ),"Coin.png")
    Coin_2.draw(Window_2)

   
    for j in range(sys.maxsize):

       #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(260,30),10)
        Player.setFill("blue")
        Player.draw(Window_2)

        S_Projectile_0 = Image(Point(250,75),"projectile.png")
        S_Projectile_1 = Image(Point(250,110),"projectile.png")
        S_Projectile_2 = Image(Point(250,320),"projectile.png")
        S_Projectile_3 = Image(Point(250,280),"projectile.png")
        S_Projectile_4 = Image(Point(250,240),"projectile.png")
        S_Projectile_5 = Image(Point(260,400),"projectile.png")
        S_Projectile_6 = Image(Point(250,360),"projectile.png")

        
        S_Projectile_0.draw( Window_2 ) 
        S_Projectile_1.draw( Window_2 )
        S_Projectile_2.draw( Window_2 )
        S_Projectile_3.draw( Window_2 )
        S_Projectile_4.draw( Window_2 )
        S_Projectile_5.draw( Window_2 )
        S_Projectile_6.draw( Window_2 )
    

        #Movement, Collision, and Boundaries in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            time.sleep(0.01)
            S_Projectile_0.move( F2 , F3 )
            S_Projectile_1.move( V2 , V3 )
            S_Projectile_2.move( F2 , F3 )
            S_Projectile_3.move( V2 , V3 )
            S_Projectile_4.move( F2 , F3 )
            S_Projectile_5.move( O1 , O2 )
            S_Projectile_6.move( V2 , V3 )
            Second_Check = Window_2.checkKey()

            #Player Movement Keys.
            if Second_Check=="Left":
                X2=-3
                Y2=0
            if Second_Check=="Right":
                X2=3
                Y2=0
            if Second_Check=="Down":
                X2=0
                Y2=3
            if Second_Check=="Up":
                X2=0
                Y2=-3
            if Second_Check=="x":
                X2 = 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin_2.getAnchor()
            P3X = P3.getX()

            P4 = Coin_2.getAnchor()
            P4X = P4.getY()
            
            S0 = S_Projectile_0.getAnchor()
            S0X = S0.getX()
            SA = S_Projectile_0.getAnchor()
            SAX = SA.getY()

            S1 = S_Projectile_1.getAnchor()
            S1X = S1.getX()
            S2 = S_Projectile_1.getAnchor()
            S2X = S2.getY()

            S3 = S_Projectile_2.getAnchor()
            S3X = S3.getX()
            S4 = S_Projectile_2.getAnchor()
            S4X = S4.getY()

            S5 = S_Projectile_3.getAnchor()
            S5X = S5.getX()
            S6 = S_Projectile_3.getAnchor()
            S6X = S6.getY()

            S7 = S_Projectile_4.getAnchor()
            S7X = S7.getX()
            S8 = S_Projectile_4.getAnchor()
            S8X = S8.getY()

            S9 = S_Projectile_5.getAnchor()
            S9X = S9.getX()
            S10 = S_Projectile_5.getAnchor()
            S10X = S10.getY()

            S11 = S_Projectile_6.getAnchor()
            S11X = S11.getX()
            S12 = S_Projectile_6.getAnchor()
            S12X = S12.getY()

            #Collision Boundary for the Projectiles to move back and forth.
            if S_Projectile_0.getAnchor().getX() < 110:
                F2 = 3
                F3 = 0
            if S_Projectile_0.getAnchor().getX() > 415:
                F2 = -3
                F3 = 0
            if S_Projectile_1.getAnchor().getX() < 110:
                V2 = 3
                V3 = 0
            if S_Projectile_1.getAnchor().getX() > 415:
                V2 = -3
                V3 = 0
            if S_Projectile_2.getAnchor().getX() < 110:
                V2 = 3
                V3 = 0
            if S_Projectile_2.getAnchor().getX() > 415:
                V2 = -3
                V3 = 0
            if S_Projectile_3.getAnchor().getX() < 110:
                V2 = 3
                V3 = 0
            if S_Projectile_3.getAnchor().getX() > 415:
                V2 = -3
                V3 = 0
            if S_Projectile_4.getAnchor().getX() < 110:
                F2 = 3
                V3 = 0
            if S_Projectile_4.getAnchor().getX() > 415:
                F2 = -3
                V3 = 0
            if S_Projectile_5.getAnchor().getY() > 415:
                O1 = 0
                O2 = -4
            if S_Projectile_5.getAnchor().getY() < 65:
                O1 = 0
                O2 = 4
            if S_Projectile_6.getAnchor().getX() < 110:
                V2 = 3
                V3 = 0
            if S_Projectile_6.getAnchor().getX() > 415:
                V2 = -3
                V3 = 0

            #Collision Boundaries for the walls.
            if Player.getCenter().getX() > 250 and Player.getCenter().getY() <0:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() < 255 and Player.getCenter().getY() < 40:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 265 and Player.getCenter().getY() < 40:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 250 and Player.getCenter().getY() < 41:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 270 and Player.getCenter().getY() < 41:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() >= 150 and Player.getCenter().getY() <= 200 and Player.getCenter().getX() <= 250:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() >= 150 and Player.getCenter().getY() <= 200 and Player.getCenter().getX() >= 270:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() >= 150 and Player.getCenter().getY() <= 220 and Player.getCenter().getX() <= 252 and Player.getCenter().getX() >= 251:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() >= 150 and Player.getCenter().getY() <= 220 and Player.getCenter().getX() >= 268 and Player.getCenter().getX() <= 269:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() >= 221 and Player.getCenter().getY() <= 223 and Player.getCenter().getX() >= 270:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() >= 221 and Player.getCenter().getY() <= 223 and Player.getCenter().getX() <= 250:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() >= 390 and Player.getCenter().getY() <= 392 and Player.getCenter().getX() >= 270:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() >= 390 and Player.getCenter().getY() <= 392 and Player.getCenter().getX() <= 250:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 420:
                X2 = -1
                Y2 = 0
                pass    
            if Player.getCenter().getX() < 100:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 465:
                X2 = 0
                Y2 = -1
                pass

            #Coin Collision.
            elif (abs(P1X-P3X)) < 20 and (abs(P2X-P4X)) < 20:
                Window_2.close()
                Third_Level()
                
            #Projectile 0 Collision.
            elif (abs(P1X-S0X)) < 20 and (abs(P2X-SAX)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
            
            #Projectile 1 Collision.
            elif (abs(P1X-S1X)) < 20 and (abs(P2X-S2X)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
            
            #Projectile 2 Collision.
            elif (abs(P1X-S3X)) < 20 and (abs(P2X-S4X)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
            
            #Projectile 3 Collision.
            elif (abs(P1X-S5X)) < 20 and (abs(P2X-S6X)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
            
            #Projectile 4 Collision.
            elif (abs(P1X-S7X)) < 20 and (abs(P2X-S8X)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
            
            #Projectile 5 Collision.
            elif (abs(P1X-S9X)) < 20 and (abs(P2X-S10X)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
            
            #Projectile 6 Collision.
            elif (abs(P1X-S11X)) < 20 and (abs(P2X-S12X)) < 20:
                Player.undraw()
                S_Projectile_0.undraw()
                S_Projectile_1.undraw()
                S_Projectile_2.undraw()
                S_Projectile_3.undraw()
                S_Projectile_4.undraw()
                S_Projectile_5.undraw()
                S_Projectile_6.undraw()
                break
           

#Third Level Function.
def Third_Level():

    #Third interface of the Third Level.
    X2 , Y2 , F2 , F3 , V2 , V3 = Game_Variables.Movement_Variables_3()

    Window_3_Name , Window_3_x , Window_3_y = Game_Variables.Window_Variables_3()

    Size , Fill , Font , Style = Game_Variables.Level_Display()
    
    Window_3=GraphWin( Window_3_Name, Window_3_x , Window_3_y )
    Window_3.setBackground("white")

    Background_3 = Image(Point( Window_3_x / 2 , Window_3_y / 2),"Third Level.png")
    Background_3.draw(Window_3)

    Coin_3 = Image(Point(455,520),"Coin.png")
    Coin_3.draw(Window_3)

    Three = Text(Point(200,540),"Level 3/7")
    Three.setSize(Size)
    Three.setFill(Fill)
    Three.setFace(Font)
    Three.setStyle(Style)
    Three.draw(Window_3)

    for j in range(sys.maxsize):

        #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(440,30),10)
        Player.setFill("blue")
        Player.draw(Window_3)

        T_Projectile_0 = Image(Point(40,60),"projectile.png")
        T_Projectile_1 = Image(Point(550,195),"projectile.png")
        T_Projectile_2 = Image(Point(40,335),"projectile.png")
        T_Projectile_3 = Image(Point(550,460),"projectile.png")
        
        T_Projectile_0.draw(Window_3)
        T_Projectile_1.draw(Window_3)
        T_Projectile_2.draw(Window_3)
        T_Projectile_3.draw(Window_3)


        #Movement, Collision and Boundaries in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            time.sleep(0.01)
            T_Projectile_0.move( F2 , F3 )
            T_Projectile_1.move( V2 , V3 )
            T_Projectile_2.move( F2 , F3 )
            T_Projectile_3.move( V2 , V3 )
            Third_Check = Window_3.checkKey()

            #Player Movement Keys.
            if Third_Check=="Left":
                X2=-3
                Y2=0
            if Third_Check=="Right":
                X2=3
                Y2=0
            if Third_Check=="Down":
                X2=0
                Y2=3
            if Third_Check=="Up":
                X2=0
                Y2=-3
            if Third_Check=="x":
                X2 = 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin_3.getAnchor()
            P3X = P3.getX()

            P4 = Coin_3.getAnchor()
            P4X = P4.getY()
            
            T0 = T_Projectile_0.getAnchor()
            T0X = T0.getX()
            TA = T_Projectile_0.getAnchor()
            TAX = TA.getY()

            T1 = T_Projectile_1.getAnchor()
            T1X = T1.getX()
            T2 = T_Projectile_1.getAnchor()
            T2X = T2.getY()

            T3 = T_Projectile_2.getAnchor()
            T3X = T3.getX()
            T4 = T_Projectile_2.getAnchor()
            T4X = T4.getY()

            T5 = T_Projectile_3.getAnchor()
            T5X = T5.getX()
            T6 = T_Projectile_3.getAnchor()
            T6X = T6.getY()

            #Collision Boundary for the Projectiles to move back and forth.
            if T_Projectile_0.getAnchor().getX() > 550:
                F2 = -3
                F3 = 0
            if T_Projectile_0.getAnchor().getX() < 40:
                F2 = 3
                F3 = 0
            if T_Projectile_1.getAnchor().getX() < 40:
                V2 = 3
                V3 = 0
            if T_Projectile_1.getAnchor().getX() > 550:
                V2 = -3
                V3 = 0


            #Collision Boundaries for the walls.
            if Player.getCenter().getX() < 455 and Player.getCenter().getY() < 0:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 450 and Player.getCenter().getY() < 40:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 435 and Player.getCenter().getY() < 40:
                X2 = 1
                Y2 = 0
                pass  
            if Player.getCenter().getX() > 455 and Player.getCenter().getY() < 42:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 560:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 560:
                X2= 0
                Y2 = -1
                pass
            if Player.getCenter().getX() < 25:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 430 and Player.getCenter().getY() < 42:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 115 and Player.getCenter().getX() < 118 and Player.getCenter().getY() > 70 and Player.getCenter().getY() < 165:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 168 and Player.getCenter().getY() > 70 and Player.getCenter().getY() < 165:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 115 and Player.getCenter().getY() > 70 and Player.getCenter().getY() < 75:
                 X2 = 0
                 Y2 = -1
                 pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 580 and Player.getCenter().getY() > 70 and Player.getCenter().getY() < 75:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 580 and Player.getCenter().getY() >  165 and Player.getCenter().getY() < 170:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() < 115 and  Player.getCenter().getY() > 165  and Player.getCenter().getY() < 170:
                 X2 = 0
                 Y2 = 1
                 pass
            if Player.getCenter().getX() > 435 and Player.getCenter().getX() < 438 and Player.getCenter().getY() > 210 and Player.getCenter().getY() < 310:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 465 and Player.getCenter().getX() < 470 and Player.getCenter().getY() > 210 and Player.getCenter().getY() < 310:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 25 and Player.getCenter().getX() < 435  and  Player.getCenter().getY() > 205  and Player.getCenter().getY() < 210:
                 X2 = 0
                 Y2 = -1
                 pass
            if Player.getCenter().getX() > 475 and Player.getCenter().getX() < 600 and Player.getCenter().getY() > 205 and Player.getCenter().getY() < 210:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 25 and Player.getCenter().getX() < 435  and  Player.getCenter().getY() > 305  and Player.getCenter().getY() < 310:
                 X2 = 0
                 Y2 = 1
                 pass
            if Player.getCenter().getX() > 475 and Player.getCenter().getX() < 600 and Player.getCenter().getY() > 305 and Player.getCenter().getY() < 310:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 580 and Player.getCenter().getY() >  365 and Player.getCenter().getY() < 370:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() < 125 and  Player.getCenter().getY() > 365  and Player.getCenter().getY() < 370:
                 X2 = 0
                 Y2 = -1
                 pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 580 and Player.getCenter().getY() >  430 and Player.getCenter().getY() < 435:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 130 and Player.getCenter().getX() < 135 and Player.getCenter().getY() > 370 and Player.getCenter().getY() < 430:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 175 and Player.getCenter().getX() < 180 and Player.getCenter().getY() > 370 and Player.getCenter().getY() < 430:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 125 and  Player.getCenter().getY() > 430  and Player.getCenter().getY() < 435:
                 X2 = 0
                 Y2 = 1
                 pass
            if Player.getCenter().getX() > 25 and Player.getCenter().getX() < 435  and  Player.getCenter().getY() > 475  and Player.getCenter().getY() < 480:
                 X2 = 0
                 Y2 = -1
                 pass
            if Player.getCenter().getX() > 475 and Player.getCenter().getX() < 600 and Player.getCenter().getY() > 475 and Player.getCenter().getY() < 480:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 430 and Player.getCenter().getX() < 435 and Player.getCenter().getY() > 475 and Player.getCenter().getY() < 550:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 465 and Player.getCenter().getX() < 470 and Player.getCenter().getY() > 475 and Player.getCenter().getY() < 550:
                X2 = -1
                Y2 = 0
                pass
            

            #Coin Collision.
            elif (abs(P1X-P3X)) < 20 and (abs(P2X-P4X)) < 20:
                Window_3.close()
                Fourth_Level()
                
            #Projectile 0 Collision.
            elif (abs(P1X-T0X)) < 30 and (abs(P2X-TAX)) < 30:
                Player.undraw()
                T_Projectile_0.undraw()
                T_Projectile_1.undraw()
                T_Projectile_2.undraw()
                T_Projectile_3.undraw()
                break
            
            #Projectile 1 Collision.
            elif (abs(P1X-T1X)) < 30 and (abs(P2X-T2X)) < 30:
                Player.undraw()
                T_Projectile_0.undraw()
                T_Projectile_1.undraw()
                T_Projectile_2.undraw()
                T_Projectile_3.undraw()
                break
            
            #Projectile 2 Collision.
            elif (abs(P1X-T3X)) < 30 and (abs(P2X-T4X)) < 30:
                Player.undraw()
                T_Projectile_0.undraw()
                T_Projectile_1.undraw()
                T_Projectile_2.undraw()
                T_Projectile_3.undraw()
                break
            
            #Projectile 3 Collision.
            elif (abs(P1X-T5X)) < 30 and (abs(P2X-T6X)) < 30:
                Player.undraw()
                T_Projectile_0.undraw()
                T_Projectile_1.undraw()
                T_Projectile_2.undraw()
                T_Projectile_3.undraw()
                break
      

#Fourth Level Function.       
def Fourth_Level():

    #Fourth interface of the Fourth Level.
    X2 , Y2 , F2 , F3 , V2 , V3 , D0 , D1 , D2 , D3 = Game_Variables.Movement_Variables_4()

    Window_4_Name , Window_4_x , Window_4_y = Game_Variables.Window_Variables_4()

    Size , Fill , Font , Style = Game_Variables.Level_Display()
    
    Window_4=GraphWin( Window_4_Name, Window_4_x , Window_4_y )
    Window_4.setBackground("white")

    background_4 = Image(Point( Window_4_x / 2 , Window_4_y / 2 ),"Fourth Level.png")
    background_4.draw( Window_4 )

    Coin_4 = Image(Point(50,460),"Coin.png")
    Coin_4.draw(Window_4)

    Four = Text(Point(250,315),"Level 4/7")
    Four.setSize(Size)
    Four.setFill(Fill)
    Four.setFace(Font)
    Four.setStyle(Style)
    Four.draw(Window_4)

    for y in range (sys.maxsize):


        #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(150,30),10)
        Player.setFill("blue")
        Player.draw(Window_4)

        F_Projectile_0 = Image(Point(75,175),"projectile.png")
        F_Projectile_1 = Image(Point(125,175),"projectile.png")
        F_Projectile_2 = Image(Point(175,175),"projectile.png")
        F_Projectile_3 = Image(Point(225,175),"projectile.png")
        F_Projectile_4 = Image(Point(275,175),"projectile.png")
        F_Projectile_5 = Image(Point(325,175),"projectile.png")
        F_Projectile_6 = Image(Point(375,175),"projectile.png")
        F_Projectile_7 = Image(Point(275,460),"projectile.png")
        F_Projectile_8 = Image(Point(325,460),"projectile.png")
        F_Projectile_9 = Image(Point(375,460),"projectile.png")
        F_Projectile_10 = Image(Point(425,460),"projectile.png")
        F_Projectile_11 = Image(Point(175,460),"projectile.png")
        F_Projectile_12 = Image(Point(225,460),"projectile.png")
        F_Projectile_13 = Image(Point(300,510),"projectile.png")
        F_Projectile_14 = Image(Point(300,385),"projectile.png")
        F_Projectile_15 = Image(Point(300,125),"projectile.png")
        F_Projectile_16 = Image(Point(425,175),"projectile.png")
        F_Projectile_17 = Image(Point(475,175),"projectile.png")
        F_Projectile_18 = Image(Point(300,230),"projectile.png")
        F_Projectile_19 = Image(Point(125,460),"projectile.png")
        F_Projectile_20 = Image(Point(475,460),"projectile.png")


        F_Projectile_0.draw( Window_4 ) 
        F_Projectile_1.draw( Window_4 )
        F_Projectile_2.draw( Window_4 )
        F_Projectile_3.draw( Window_4 )
        F_Projectile_4.draw( Window_4 )
        F_Projectile_5.draw( Window_4 )
        F_Projectile_6.draw( Window_4 )
        F_Projectile_7.draw( Window_4 )
        F_Projectile_8.draw( Window_4 )
        F_Projectile_9.draw( Window_4 )
        F_Projectile_10.draw( Window_4 )
        F_Projectile_11.draw( Window_4 )
        F_Projectile_12.draw( Window_4 )
        F_Projectile_13.draw( Window_4 )
        F_Projectile_14.draw( Window_4 )
        F_Projectile_15.draw( Window_4 )
        F_Projectile_16.draw( Window_4 )
        F_Projectile_17.draw( Window_4 )
        F_Projectile_18.draw( Window_4 )
        F_Projectile_19.draw( Window_4 )
        F_Projectile_20.draw( Window_4 )
        
        
        #Movement, Collision, and Boundaries in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            time.sleep(0.01)
            F_Projectile_0.move( F2 , F3 )
            F_Projectile_1.move( V2 , V3 )
            F_Projectile_2.move( F2 , F3 )
            F_Projectile_3.move( V2 , V3 )
            F_Projectile_4.move( F2 , F3 )
            F_Projectile_5.move( V2 , V3 )
            F_Projectile_6.move( F2 , F3 )
            F_Projectile_7.move( F2 , F3 )
            F_Projectile_8.move( V2, V3 )
            F_Projectile_9.move( F2, F3 )
            F_Projectile_10.move(V2,V3)
            F_Projectile_11.move(F2,F3)
            F_Projectile_12.move(V2,V3)
            F_Projectile_13.move(D2,D3)
            F_Projectile_14.move(D0,D1)
            F_Projectile_15.move(D2,D3)
            F_Projectile_16.move(V2,V3)
            F_Projectile_17.move(F2,F3)
            F_Projectile_18.move(D0,D1)
            F_Projectile_19.move(V2,V3)
            F_Projectile_20.move(F2,F3)
            Fourth_Check= Window_4.checkKey()

            #Player Movement Keys.
            if Fourth_Check=="Left":
                X2=-5
                Y2=0
            if Fourth_Check=="Right":
                X2=5
                Y2=0
            if Fourth_Check=="Down":
                X2=0
                Y2=5
            if Fourth_Check == "Up":
                X2=0
                Y2=-5
            if Fourth_Check =="x":
                X2 = 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin_4.getAnchor()
            P3X = P3.getX()

            P4 = Coin_4.getAnchor()
            P4X = P4.getY()

            Z0 = F_Projectile_0.getAnchor()
            Z0X = Z0.getX()
            ZA = F_Projectile_0.getAnchor()
            ZAX = ZA.getY()

            Z1 = F_Projectile_1.getAnchor()
            Z1X = Z1.getX()
            Z2 = F_Projectile_1.getAnchor()
            Z2X = Z2.getY()

            Z3 = F_Projectile_2.getAnchor()
            Z3X = Z3.getX()
            Z4 = F_Projectile_2.getAnchor()
            Z4X = Z4.getY()

            Z5 = F_Projectile_3.getAnchor()
            Z5X = Z5.getX()
            Z6 = F_Projectile_3.getAnchor()
            Z6X = Z6.getY()

            Z7 = F_Projectile_4.getAnchor()
            Z7X = Z7.getX()
            Z8 = F_Projectile_4.getAnchor()
            Z8X = Z8.getY()

            Z9 = F_Projectile_5.getAnchor()
            Z9X = Z9.getX()
            Z10 = F_Projectile_5.getAnchor()
            Z10X = Z10.getY()

            Z11 = F_Projectile_6.getAnchor()
            Z11X = Z11.getX()
            Z12 = F_Projectile_6.getAnchor()
            Z12X = Z12.getY()

            Z13 = F_Projectile_7.getAnchor()
            Z13X = Z13.getX()
            Z14 = F_Projectile_7.getAnchor()
            Z14X = Z14.getY()

            Z15 = F_Projectile_8.getAnchor()
            Z15X = Z15.getX()
            Z16 = F_Projectile_8.getAnchor()
            Z16X = Z16.getY()

            Z17 = F_Projectile_9.getAnchor()
            Z17X = Z17.getX()
            Z18 = F_Projectile_9.getAnchor()
            Z18X = Z18.getY()

            Z19 = F_Projectile_10.getAnchor()
            Z19X = Z19.getX()
            Z20 = F_Projectile_10.getAnchor()
            Z20X = Z20.getY()

            Z21 = F_Projectile_11.getAnchor()
            Z21X = Z21.getX()
            Z22 = F_Projectile_11.getAnchor()
            Z22X = Z22.getY()

            Z23 = F_Projectile_12.getAnchor()
            Z23X = Z23.getX()
            Z24 = F_Projectile_12.getAnchor()
            Z24X = Z24.getY()

            Z25 = F_Projectile_13.getAnchor()
            Z25X = Z25.getX()
            Z26 = F_Projectile_13.getAnchor()
            Z26X = Z26.getY()

            Z27 = F_Projectile_14.getAnchor()
            Z27X = Z27.getX()
            Z28 = F_Projectile_14.getAnchor()
            Z28X = Z28.getY()

            Z29 = F_Projectile_15.getAnchor()
            Z29X = Z29.getX()
            Z30 = F_Projectile_15.getAnchor()
            Z30X = Z30.getY()

            Z31 = F_Projectile_16.getAnchor()
            Z31X = Z31.getX()
            Z32 = F_Projectile_16.getAnchor()
            Z32X = Z32.getY()

            Z33 = F_Projectile_17.getAnchor()
            Z33X = Z33.getX()
            Z34 = F_Projectile_17.getAnchor()
            Z34X = Z34.getY()

            Z35 = F_Projectile_18.getAnchor()
            Z35X = Z35.getX()
            Z36 = F_Projectile_18.getAnchor()
            Z36X = Z36.getY()

            Z37 = F_Projectile_19.getAnchor()
            Z37X = Z37.getX()
            Z38 = F_Projectile_19.getAnchor()
            Z38X = Z38.getY()

            Z39 = F_Projectile_20.getAnchor()
            Z39X = Z39.getX()
            Z40 = F_Projectile_20.getAnchor()
            Z40X = Z40.getY()


            #Collision Boundary for the Projectiles to move back and forth.
            if F_Projectile_0.getAnchor().getY() > 245 :
                F2 = 0
                F3 = -3
            if F_Projectile_0.getAnchor().getY() < 120:
                F2 = 0
                F3 = 3
            if F_Projectile_1.getAnchor().getY() > 245:
                V2 = 0
                V3 = -3
            if F_Projectile_1.getAnchor().getY() < 120:
                V2 = 0
                V3 = 3
            if F_Projectile_2.getAnchor().getY() > 245 :
                F2 = 0
                F3 = -3
            if F_Projectile_2.getAnchor().getY() < 120:
                F2 = 0
                F3 = 3
            if F_Projectile_3.getAnchor().getY() > 245:
                V2 = 0
                V3 = -3
            if F_Projectile_3.getAnchor().getY() < 120:
                V2 = 0
                V3 = 3
            if F_Projectile_4.getAnchor().getY() > 245 :
                F2 = 0
                F3 = -3
            if F_Projectile_4.getAnchor().getY() < 120:
                F2 = 0
                F3 = 3
            if F_Projectile_5.getAnchor().getY() > 245:
                V2 = 0
                V3 = -3
            if F_Projectile_5.getAnchor().getY() < 120:
                V2 = 0
                V3 = 3
            if F_Projectile_6.getAnchor().getY() > 245 :
                F2 = 0
                F3 = -3
            if F_Projectile_6.getAnchor().getY() < 120:
                F2 = 0
                F3 = 3
            if F_Projectile_7.getAnchor().getY() > 530 :
                V2 = 0
                V3 = -3
            if F_Projectile_7.getAnchor().getY() < 275:
                V2 = 0
                V3 = 3
            if F_Projectile_8.getAnchor().getY() > 530 :
                F2 = 0
                F3 = -3
            if F_Projectile_8.getAnchor().getY() < 275:
                F2 = 0
                F3 = 3
            if F_Projectile_9.getAnchor().getY() > 540 :
                V2 = 0
                V3 = -3
            if F_Projectile_9.getAnchor().getY() < 275:
                V2 = 0
                V3 = 3
            if F_Projectile_10.getAnchor().getY() > 530 :
                F2 = 0
                F3 = -3
            if F_Projectile_10.getAnchor().getY() < 275:
                F2 = 0
                F3 = 3
            if F_Projectile_11.getAnchor().getY() > 530 :
                V2 = 0
                V3 = -3
            if F_Projectile_11.getAnchor().getY() < 275:
                V2 = 0
                V3 = 3
            if F_Projectile_12.getAnchor().getY() > 530 :
                F2 = 0
                F3 = -3
            if F_Projectile_12.getAnchor().getY() < 275:
                F2 = 0
                F3 = 3
            if F_Projectile_13.getAnchor().getX() > 510:
                D2 = -3
                D3 = 0
            if F_Projectile_13.getAnchor().getX() < 60:
                D2 = 3
                D3 = 0
            if F_Projectile_14.getAnchor().getX() > 510:
                D2 = -3
                D3 = 0
            if F_Projectile_14.getAnchor().getX() < 60:
                D2 = 3
                D3 = 0
            if F_Projectile_15.getAnchor().getX() > 510:
                D2 = -3
                D3 = 0
            if F_Projectile_15.getAnchor().getX() < 60:
                D2 = 3
                D3 = 0
            if F_Projectile_16.getAnchor().getX() > 510:
                D0 = -3
                D1 = 0
            if F_Projectile_16.getAnchor().getX() < 60:
                D0 = 3
                D1 = 0
            if F_Projectile_17.getAnchor().getX() > 510:
                D0 = -3
                D1 = 0
            if F_Projectile_17.getAnchor().getX() < 60:
                D0 = 3
                D1 = 0   
            if F_Projectile_18.getAnchor().getX() > 510:
                D0 = -3
                D1 = 0
            if F_Projectile_18.getAnchor().getX() < 60:
                D0 = 3
                D1 = 0           
            if F_Projectile_19.getAnchor().getX() > 510:
                D0 = -3
                D1 = 0
            if F_Projectile_19.getAnchor().getX() < 60:
                D0 = 3
                D1 = 0
            if F_Projectile_20.getAnchor().getX() > 510:
                D0 = -3
                D1 = 0
            if F_Projectile_20.getAnchor().getX() < 60:
                D0 = 3
                D1 = 0

            #Collision Boundaries for the walls.
            if Player.getCenter().getY() < 1:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() < 40:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 520:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 540:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 160 and Player.getCenter().getY() < 100:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 140 and Player.getCenter().getY() < 100:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 170 and Player.getCenter().getX() < 530 and  Player.getCenter().getY() < 105:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 50 and Player.getCenter().getX() < 135 and Player.getCenter().getY() < 105:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 50 and Player.getCenter().getX() < 475 and Player.getCenter().getY() > 255 and Player.getCenter().getY() < 270:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 50 and Player.getCenter().getX() < 475 and Player.getCenter().getY() > 350 and Player.getCenter().getY() < 370:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 255 and Player.getCenter().getY() < 350 and Player.getCenter().getX() > 450 and Player.getCenter().getX() < 475:
                X2 = 1
                Y2 = 0    
                pass

            #Coin Collision.
            elif (abs(P1X-P3X)) < 20 and (abs(P2X-P4X)) < 20:
                Window_4.close()
                Fifth_Level()

            #Projectile 0 Collision.
            elif (abs(P1X-Z0X)) < 25 and (abs(P2X-ZAX)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 1 Collision.
            elif (abs(P1X-Z1X)) < 25 and (abs(P2X-Z2X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 2 Collision.
            elif (abs(P1X-Z3X)) < 25 and (abs(P2X-Z4X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 3 Collision.
            elif (abs(P1X-Z5X)) < 25 and (abs(P2X-Z6X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 4 Collision.
            elif (abs(P1X-Z7X)) < 25 and (abs(P2X-Z8X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 5 Collision.
            elif (abs(P1X-Z9X)) < 25 and (abs(P2X-Z10X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 6 Collision.
            elif (abs(P1X-Z11X)) < 25 and (abs(P2X-Z12X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 7 Collision.
            elif (abs(P1X-Z13X)) < 25 and (abs(P2X-Z14X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 8 Collision.
            elif (abs(P1X-Z15X)) < 25 and (abs(P2X-Z16X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 9 Collision.
            elif (abs(P1X-Z17X)) < 25 and (abs(P2X-Z18X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 10 Collision.
            elif (abs(P1X-Z19X)) < 25 and (abs(P2X-Z20X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 11 Collision.
            elif (abs(P1X-Z21X)) < 25 and (abs(P2X-Z22X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 12 Collision.
            elif (abs(P1X-Z23X)) < 25 and (abs(P2X-Z24X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 13 Collision.
            elif (abs(P1X-Z25X)) < 25 and (abs(P2X-Z26X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 14 Collision.
            elif (abs(P1X-Z27X)) < 25 and (abs(P2X-Z28X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 15 Collision.
            elif (abs(P1X-Z29X)) < 25 and (abs(P2X-Z30X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 16 Collision.
            elif (abs(P1X-Z31X)) < 25 and (abs(P2X-Z32X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 17 Collision.
            elif (abs(P1X-Z33X)) < 25 and (abs(P2X-Z34X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 18 Collision.
            elif (abs(P1X-Z35X)) < 25 and (abs(P2X-Z36X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 19 Collision.
            elif (abs(P1X-Z37X)) < 25 and (abs(P2X-Z38X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break
            
            #Projectile 20 Collision.
            elif (abs(P1X-Z39X)) < 25 and (abs(P2X-Z40X)) < 25:
                Player.undraw()
                F_Projectile_0.undraw()
                F_Projectile_1.undraw()
                F_Projectile_2.undraw()
                F_Projectile_3.undraw()
                F_Projectile_4.undraw()
                F_Projectile_5.undraw()
                F_Projectile_6.undraw()
                F_Projectile_7.undraw()
                F_Projectile_8.undraw()
                F_Projectile_9.undraw()
                F_Projectile_10.undraw()
                F_Projectile_11.undraw()
                F_Projectile_12.undraw()
                F_Projectile_13.undraw()
                F_Projectile_14.undraw()
                F_Projectile_15.undraw()
                F_Projectile_16.undraw()
                F_Projectile_17.undraw()
                F_Projectile_18.undraw()
                F_Projectile_19.undraw()
                F_Projectile_20.undraw()
                break

                
#Fifth Level Function.
def Fifth_Level():


    #Fifth interface of the Fifth Level.
    X2 , Y2 , F2 , F3 , V2 , V3 = Game_Variables.Movement_Variables_5()

    Window_5_Name , Window_5_x , Window_5_y = Game_Variables.Window_Variables_5()

    Size , Fill , Font , Style = Game_Variables.Level_Display()
    
    Window_5=GraphWin( Window_5_Name, Window_5_x , Window_5_y )
    Window_5.setBackground("white")

    Background_5 = Image(Point( Window_5_x / 2 , Window_5_y / 2),"Fifth level.png")
    Background_5.draw( Window_5 )

    Five = Text(Point(100,325),"Level 5/7")
    Five.setSize(Size)
    Five.setFill(Fill)
    Five.setFace(Font)
    Five.setStyle(Style)
    Five.draw(Window_5)

    Coin_5 = Image(Point(660,240),"Coin.png")
    Coin_5.draw( Window_5 )
       
    for j in range(sys.maxsize):

        #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(50,240),10)
        Player.setFill("blue")
        Player.draw(Window_5)

        F_Projectile_0 = Image(Point(350,240),"projectile.png")
        F_Projectile_0.draw( Window_5 )
        

        #Movement, Collision, and Boundaries  in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            time.sleep(0.02)
            F_Projectile_0.move(V2,V3)
            Fifth_Check = Window_5.checkKey()

            #Player Movement Keys.
            if Fifth_Check=="Left":
                    X2=-5
                    Y2=0
            if Fifth_Check=="Right":
                    X2=5
                    Y2=0
            if Fifth_Check=="Down":
                    X2=0
                    Y2=5
            if Fifth_Check=="Up":
                    X2=0
                    Y2=-5
            if Fifth_Check =="x":
                X2= 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin_5.getAnchor()
            P3X = P3.getX()

            P4 = Coin_5.getAnchor()
            P4X = P4.getY()

            R0 = F_Projectile_0.getAnchor()
            R0X = R0.getX()
            
            RA = F_Projectile_0.getAnchor()
            RAX = RA.getY()


            #Collision Boundary for the projectile to move back and forth.
            if F_Projectile_0.getAnchor().getX() < 125:
                V2 = 10
                V3 = 0
            if F_Projectile_0.getAnchor().getX() > 600:
                V2 = -10
                V3 = 0

            #Collision Boundaries for the walls.
            if Player.getCenter().getX() < 1:
                X2 =1
                Y2 =0
                pass
            if Player.getCenter().getX() > 680:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() < 160:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 320:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() < 220 and Player.getCenter().getX() < 155:
                X2 =0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 260 and Player.getCenter().getX() < 285:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() > 150 and Player.getCenter().getY() < 220 and Player.getCenter().getX() > 155 and Player.getCenter().getX() < 165:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 150 and Player.getCenter().getY() < 220 and Player.getCenter().getX() > 215 and Player.getCenter().getX() < 230:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 150 and Player.getCenter().getY() < 220 and Player.getCenter().getX() > 430 and Player.getCenter().getX() < 440:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 150 and Player.getCenter().getY() < 220 and Player.getCenter().getX() > 490 and Player.getCenter().getX() < 500:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 230 and Player.getCenter().getX() < 430 and Player.getCenter().getY() > 210 and Player.getCenter().getY() < 220:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 490 and Player.getCenter().getX() < 680 and Player.getCenter().getY() > 210 and Player.getCenter().getY() < 220:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 260 and Player.getCenter().getY() < 320 and Player.getCenter().getX() > 285 and Player.getCenter().getX() < 295:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 260 and Player.getCenter().getY() < 320 and Player.getCenter().getX() > 350 and Player.getCenter().getX() < 360:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 360 and Player.getCenter().getX() < 680 and Player.getCenter().getY() > 260 and Player.getCenter().getY() < 270:
                X2 = 0
                Y2 = -1
                pass

            #Coin Collision.
            if (abs(P1X-P3X)) < 30 and (abs(P2X-P4X)) < 30:
                Coin_5.undraw()
                Sixth_Level()

            #Projectile Collision.
            elif (abs(P1X-R0X)) < 30 and (abs(P2X-RAX)) < 30:
                Player.undraw()
                F_Projectile_0.undraw()
                break


#Sixth Level Function.
def Sixth_Level():

   #Sixth interface of the Sixth Level.
    X2 , Y2 , F1 , F2 , F3 , F4 , V1 , V2 , V3 , V4 , V5 , V6 , V7 , V8 = Game_Variables.Movement_Variables_6()
    
    Window_Name_6 , Window_x_6 , Window_y_6 = Game_Variables.Window_Variables_6()

    Size , Fill , Font , Style = Game_Variables.Level_Display()
    
    Window_6 = GraphWin( Window_Name_6 , Window_x_6 , Window_y_6 )
    Window_6.setBackground("white")

    background_6 = Image(Point( Window_x_6 / 2 , Window_y_6 / 2 ),"Sixth Level.png")
    background_6.draw( Window_6 )

    Six = Text(Point(250,45),"Level 6/7")
    Six.setSize(Size)
    Six.setFill(Fill)
    Six.setFace(Font)
    Six.setStyle(Style)
    Six.draw(Window_6)

    Coin_6 = Image(Point(645,455),"Coin.png")
    Coin_6.draw( Window_6 )

    Fake_Coin = Image(Point(355,550),"Coin.png")
    Fake_Coin.draw (Window_6)

    Message = Text(Point(500,45),"Which one is the real coin?")
    Message.setSize(Size)
    Message.setFill(Fill)
    Message.setFace(Font)
    Message.setStyle(Style)
    Message.draw(Window_6)


    for j in range(sys.maxsize):

       #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(150,580),10)
        Player.setFill("blue")
        Player.draw(Window_6)

        Se_Projectile_0 = Image(Point(355,300),"projectile.png")
        Se_Projectile_1 = Image(Point(150,200),"projectile.png")
        Se_Projectile_2 = Image(Point(150,280),"projectile.png")
        Se_Projectile_3 = Image(Point(150,320),"projectile.png")
        Se_Projectile_4 = Image(Point(150,400),"projectile.png")
        Se_Projectile_5 = Image(Point(150,440),"projectile.png")
        Se_Projectile_6 = Image(Point(150,520),"projectile.png")
        Se_Projectile_7 = Image(Point(585,300),"projectile.png")
        Se_Projectile_8 = Image(Point(585,340),"projectile.png")
        Se_Projectile_9 = Image(Point(585,380),"projectile.png")
        Se_Projectile_10 = Image(Point(585,420),"projectile.png")
        Se_Projectile_11 = Image(Point(355,105),"projectile.png")
       

        Se_Projectile_0.draw( Window_6 )
        Se_Projectile_1.draw( Window_6 )
        Se_Projectile_2.draw( Window_6 )
        Se_Projectile_3.draw( Window_6 )
        Se_Projectile_4.draw( Window_6 )
        Se_Projectile_5.draw( Window_6 )
        Se_Projectile_6.draw( Window_6 )
        Se_Projectile_7.draw( Window_6 )
        Se_Projectile_8.draw( Window_6 )
        Se_Projectile_9.draw( Window_6 )
        Se_Projectile_10.draw( Window_6 )
        Se_Projectile_11.draw( Window_6 )

        #Movement, Collision, and Boundaries in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            time.sleep(0.01)
            Se_Projectile_0.move( V1 , V2 )
            Se_Projectile_1.move( F3 , F4 )
            Se_Projectile_2.move( F1 , F2 )
            Se_Projectile_3.move( F3 , F4 )
            Se_Projectile_4.move( F1 , F2 )
            Se_Projectile_5.move( F3 , F4 )
            Se_Projectile_6.move( F1 , F2 )
            Se_Projectile_7.move( V3 , V4 )
            Se_Projectile_8.move( V5 , V6 )
            Se_Projectile_9.move( V3 , V4 )
            Se_Projectile_10.move( V5 , V6 )
            Se_Projectile_11.move( V7 , V8 )
            Sixth_Check = Window_6.checkKey()

            #Player Movement Keys.
            if Sixth_Check=="Left":
                X2=-5
                Y2=0
            if Sixth_Check=="Right":
                X2=5
                Y2=0
            if Sixth_Check=="Down":
                X2=0
                Y2=5
            if Sixth_Check=="Up":
                X2=0
                Y2=-5
            if Sixth_Check =="x":
                X2= 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin_6.getAnchor()
            P3X = P3.getX()

            P4 = Coin_6.getAnchor()
            P4X = P4.getY()

            P5 = Fake_Coin.getAnchor()
            P5X = P5.getX()

            P6 = Fake_Coin.getAnchor()
            P6X = P6.getY()

            F0 = Se_Projectile_0.getAnchor()
            F0X = F0.getX()
            FA = Se_Projectile_0.getAnchor()
            FAX = FA.getY()

            Se1 = Se_Projectile_1.getAnchor()
            Se1X = Se1.getX()
            Se2 = Se_Projectile_1.getAnchor()
            Se2X = Se2.getY()

            Se3 = Se_Projectile_2.getAnchor()
            Se3X = Se3.getX()
            Se4 = Se_Projectile_2.getAnchor()
            Se4X = Se4.getY()

            Se5 = Se_Projectile_3.getAnchor()
            Se5X = Se5.getX()
            Se6 = Se_Projectile_3.getAnchor()
            Se6X = Se6.getY()

            Se7 = Se_Projectile_4.getAnchor()
            Se7X = Se7.getX()
            Se8 = Se_Projectile_4.getAnchor()
            Se8X = Se8.getY()

            Se9 = Se_Projectile_5.getAnchor()
            Se9X = Se9.getX()
            Se10 = Se_Projectile_5.getAnchor()
            Se10X = Se10.getY()

            Se11 = Se_Projectile_6.getAnchor()
            Se11X = Se11.getX()
            Se12 = Se_Projectile_6.getAnchor()
            Se12X = Se12.getY()

            Se13 = Se_Projectile_7.getAnchor()
            Se13X = Se13.getX()
            Se14 = Se_Projectile_7.getAnchor()
            Se14X = Se14.getY()

            Se15 = Se_Projectile_8.getAnchor()
            Se15X = Se15.getX()
            Se16 = Se_Projectile_8.getAnchor()
            Se16X = Se16.getY()
            
            Se17 = Se_Projectile_9.getAnchor()
            Se17X = Se17.getX()
            Se18 = Se_Projectile_9.getAnchor()
            Se18X = Se18.getY()

            Se19 = Se_Projectile_10.getAnchor()
            Se19X = Se19.getX()
            Se20 = Se_Projectile_10.getAnchor()
            Se20X = Se20.getY()

            Se21 = Se_Projectile_11.getAnchor()
            Se21X = Se21.getX()
            Se22 = Se_Projectile_11.getAnchor()
            Se22X = Se22.getY()


            #Collision Boundary for the Projectiles to move back and forth.
            if Se_Projectile_0.getAnchor().getY() < 140:
                V1 = 0
                V2 = 5
            if Se_Projectile_0.getAnchor().getY() > 500:
                V1 = 0
                V2 = -5
            if Se_Projectile_1.getAnchor().getX() < 80:
                F3 = 6
                F4 = 0
            if Se_Projectile_1.getAnchor().getX() > 230:
                F3 = -6
                F4 = 0
            if Se_Projectile_2.getAnchor().getX() < 80:
                F1 = 6
                F2 = 0
            if Se_Projectile_2.getAnchor().getX() > 230:
                F1 = -6
                F2 = 0
            if Se_Projectile_3.getAnchor().getX() < 80:
                F3 = 6
                F4 = 0
            if Se_Projectile_3.getAnchor().getX() > 230:
                F3 = -6
                F4 = 0
            if Se_Projectile_4.getAnchor().getX() < 80:
                F1 = 6
                F2 = 0
            if Se_Projectile_4.getAnchor().getX() > 230:
                F1 = -6
                F2 = 0
            if Se_Projectile_5.getAnchor().getX() < 80:
                F3 = 6
                F4 = 0
            if Se_Projectile_5.getAnchor().getX() > 230:
                F3 = -6
                F4 = 0
            if Se_Projectile_6.getAnchor().getX() < 80:
                F1 = 6
                F2 = 0
            if Se_Projectile_6.getAnchor().getX() > 230:
                F1 = -6
                F2 = 0
            if Se_Projectile_7.getAnchor().getX() > 650:
                V3 = -5
                V4 = 0
            if Se_Projectile_7.getAnchor().getX() < 520:
                V3 = 5
                V4 = 0
            if Se_Projectile_8.getAnchor().getX() > 650:
                V5 = -5
                V6 = 0
            if Se_Projectile_8.getAnchor().getX() < 520:
                V5 = 5
                V6 = 0
            if Se_Projectile_9.getAnchor().getX() > 650:
                V3 = -5
                V4 = 0
            if Se_Projectile_9.getAnchor().getX() < 520:
                V3 = 5
                V4 = 0
            if Se_Projectile_10.getAnchor().getX() > 650:
                V5 = -5
                V6 = 0
            if Se_Projectile_10.getAnchor().getX() < 520:
                V5 = 5
                V6 = 0
            if Se_Projectile_11.getAnchor().getX() > 520:
                V7 = -5
                V8 = 0
            if Se_Projectile_11.getAnchor().getX() < 155:
                V7 = 5
                V8 = 0

            #Collision Boundaries for the walls.   
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 175 and Player.getCenter().getY() > 540:
                X2 = -1
                Y2 = 0
                pass
            if  Player.getCenter().getX() < 135 and Player.getCenter().getY() > 540:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 250 and Player.getCenter().getY() > 530 and Player.getCenter().getY() < 550:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 60 and Player.getCenter().getX() < 135 and Player.getCenter().getY() > 530 and Player.getCenter().getY() < 550:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() > 135 and Player.getCenter().getY() < 530 and Player.getCenter().getX() > 250 and Player.getCenter().getX() < 260:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 60 and Player.getCenter().getX() < 135 and Player.getCenter().getY() > 160 and Player.getCenter().getY() < 170:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 250 and Player.getCenter().getY() > 160 and Player.getCenter().getY() < 170:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 85 and Player.getCenter().getY() < 160  and Player.getCenter().getX() > 125 and Player.getCenter().getX() < 135:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 125 and Player.getCenter().getY() < 170  and Player.getCenter().getX() > 165 and Player.getCenter().getX() < 175:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 165 and Player.getCenter().getX() < 335 and Player.getCenter().getY() > 120 and Player.getCenter().getY() < 130:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 365 and Player.getCenter().getX() < 500 and Player.getCenter().getY() > 120 and Player.getCenter().getY() < 130:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 505 and Player.getCenter().getX() < 515 and Player.getCenter().getY() > 130 and Player.getCenter().getY() < 465:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 505 and Player.getCenter().getX() < 650 and Player.getCenter().getY() > 465 and Player.getCenter().getY() < 475:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() > 90 and Player.getCenter().getY() < 265 and Player.getCenter().getX() > 540 and Player.getCenter().getX() < 550 :
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 540 and Player.getCenter().getX() < 660 and Player.getCenter().getY() > 265 and Player.getCenter().getY() < 275:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 365 and Player.getCenter().getX() < 375 and Player.getCenter().getY() > 120 and Player.getCenter().getY() < 270:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 330 and Player.getCenter().getX() < 340 and Player.getCenter().getY() > 120 and Player.getCenter().getY() < 385:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 370 and Player.getCenter().getX() < 430 and Player.getCenter().getY() > 270 and Player.getCenter().getY() < 280:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 370 and Player.getCenter().getX() < 430 and Player.getCenter().getY() > 310 and Player.getCenter().getY() < 320:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() > 410 and Player.getCenter().getX() < 420 and Player.getCenter().getY() > 270 and Player.getCenter().getY() < 320:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 365 and Player.getCenter().getX() < 375 and Player.getCenter().getY() > 320 and Player.getCenter().getY() < 600:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 385 and Player.getCenter().getY() < 395 and Player.getCenter().getX() > 300 and Player.getCenter().getX() < 340:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 290 and Player.getCenter().getX() < 300 and Player.getCenter().getY() > 385 and Player.getCenter().getY() < 600:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 300 and Player.getCenter().getX() < 340 and Player.getCenter().getY() > 420 and Player.getCenter().getY() < 430:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() > 420 and Player.getCenter().getY() < 600 and Player.getCenter().getX() > 330 and Player.getCenter().getX() < 340:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 600:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getX() < 60:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getX() > 655:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getY() < 95:
                X2 = 0
                Y2 = 1
                pass
          

            #Coin Collision
            if (abs(P1X-P3X)) < 25 and (abs(P2X-P4X)) < 25:
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                Final_Level()
                
            #Fake Coin Collision.
            elif (abs(P1X-P5X)) < 25 and (abs(P2X-P6X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                Fake_Coin.undraw()
                break
            
            #Projectile 0 Collision.
            elif (abs(P1X-F0X)) < 25 and (abs(P2X-FAX)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
            #Projectile 1 Collision.
            elif (abs(P1X-Se1X)) < 25 and (abs(P2X-Se2X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 2 Collision.
            elif (abs(P1X-Se3X)) < 25 and (abs(P2X-Se4X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 3 Collision.
            elif (abs(P1X-Se5X)) < 25 and (abs(P2X-Se6X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 4 Collision.
            elif (abs(P1X-Se7X)) < 25 and (abs(P2X-Se8X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 5 Collision.
            elif (abs(P1X-Se9X)) < 25 and (abs(P2X-Se10X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 6 Collision.
            elif (abs(P1X-Se11X)) < 25 and (abs(P2X- Se12X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 7 Collision.
            elif (abs(P1X-Se13X)) < 25 and (abs(P2X-Se14X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 8 Collision.
            elif (abs(P1X-Se15X)) < 25 and (abs(P2X-Se16X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 9 Collision.
            elif (abs(P1X-Se17X)) < 25 and (abs(P2X-Se18X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
           #Projectile 10 Collision.
            elif (abs(P1X-Se19X)) < 25 and (abs(P2X-Se20X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break
            
            #Projectile 11 Collision.
            elif (abs(P1X-Se21X)) < 25 and (abs(P2X-Se22X)) < 25:
                Player.undraw()
                Se_Projectile_0.undraw()
                Se_Projectile_1.undraw()
                Se_Projectile_2.undraw()
                Se_Projectile_3.undraw()
                Se_Projectile_4.undraw()
                Se_Projectile_5.undraw()
                Se_Projectile_6.undraw()
                Se_Projectile_7.undraw()
                Se_Projectile_8.undraw()
                Se_Projectile_9.undraw()
                Se_Projectile_10.undraw()
                Se_Projectile_11.undraw()
                break


#Final Level Function.                
def Final_Level():

    #Final interface of the Final Level.
    X2 , Y2 , F2 , F3 , V2 , V3  = Game_Variables.Movement_Variables_7()
    
    Window_Name_7 , Window_x_7 , Window_y_7 = Game_Variables.Window_Variables_7()

    Size , Fill , Font , Style = Game_Variables.Level_Display() 
    
    Window_7 = GraphWin( Window_Name_7 , Window_x_7 , Window_y_7 )
    Window_7.setBackground("white")

    background_7 = Image(Point( Window_x_7 / 2 , Window_y_7 / 2 ),"Final Level.png")
    background_7.draw( Window_7 )

    Seventh = Text(Point(150,35),"Level 7/7")
    Seventh.setSize(Size)
    Seventh.setFill(Fill)
    Seventh.setFace(Font)
    Seventh.setStyle(Style)
    Seventh.draw(Window_7)

    Coin_7 = Image(Point(500,470),"Coin.png")
    Coin_7.draw( Window_7 )

    Coin_8 = Image(Point(100,100),"Coin.png")
    Coin_8.draw(Window_7)

    Coin_9 = Image(Point(500,100),"Coin.png")
    Coin_9.draw(Window_7)

    Final_Coin = Image(Point(100,470),"Coin.png")
    Final_Coin.draw(Window_7)

    Congrats = Text(Point ( Window_x_7 / 2 , Window_y_7 / 2),"You've won the game! Congrats!")
    Congrats.setSize(20)
    Congrats.setFill("blue")
    Congrats.setFace(Font)
    Congrats.setStyle(Style)

    Message_2 = Text(Point(463,35),"Three fake coins. One real coin.")
    Message_2.setSize(10)
    Message_2.setFill(Fill)
    Message_2.setFace(Font)
    Message_2.setStyle(Style)
    Message_2.draw(Window_7)
    ##

    for y in range (sys.maxsize):

        #Drawing the Player and Projectiles in this for loop.
        Player = Circle(Point(300,30),10)
        Player.setFill("blue")
        Player.draw(Window_7)

        
        FI_Projectile_0 = Image(Point(85,300),"projectile.png")
        FI_Projectile_1 = Image(Point(145,300),"projectile.png")
        FI_Projectile_2 = Image(Point(205,300),"projectile.png")
        FI_Projectile_3 = Image(Point(265,300),"projectile.png")
        FI_Projectile_4 = Image(Point(325,300),"projectile.png")
        FI_Projectile_5 = Image(Point(385,300),"projectile.png")
        FI_Projectile_6 = Image(Point(445,300),"projectile.png")
        FI_Projectile_7 = Image(Point(505,300),"projectile.png")
        FI_Projectile_8 = Image(Point(500,85),"projectile.png")
        FI_Projectile_9 = Image(Point(500,145),"projectile.png")
        FI_Projectile_10 = Image(Point(500,205),"projectile.png")
        FI_Projectile_11 = Image(Point(500,265),"projectile.png")
        FI_Projectile_12 = Image(Point(500,325),"projectile.png")
        FI_Projectile_13 = Image(Point(500,385),"projectile.png")
        FI_Projectile_14 = Image(Point(500,445),"projectile.png")
     
        
        FI_Projectile_0.draw( Window_7 ) 
        FI_Projectile_1.draw( Window_7 )
        FI_Projectile_2.draw( Window_7 )
        FI_Projectile_3.draw( Window_7 )
        FI_Projectile_4.draw( Window_7 )
        FI_Projectile_5.draw( Window_7 )
        FI_Projectile_6.draw( Window_7 )
        FI_Projectile_7.draw( Window_7 )
        FI_Projectile_8.draw( Window_7 ) 
        FI_Projectile_9.draw( Window_7 )
        FI_Projectile_10.draw( Window_7 )
        FI_Projectile_11.draw( Window_7 )
        FI_Projectile_12.draw( Window_7 )
        FI_Projectile_13.draw( Window_7 )
        FI_Projectile_14.draw( Window_7 )
        ##
      
        #Movement, Collision, and Boundaries in this nested for loop.
        for k in range(sys.maxsize):
            Player.move( X2 , Y2 )
            FI_Projectile_0.move( V2 , V3 )
            FI_Projectile_1.move( V2 , V3 )
            FI_Projectile_2.move( V2 , V3 )
            FI_Projectile_3.move( V2 , V3 )
            FI_Projectile_4.move( V2 , V3 )
            FI_Projectile_5.move( V2 , V3 )
            FI_Projectile_6.move( V2 , V3 )
            FI_Projectile_7.move( V2 , V3 )
            FI_Projectile_8.move( F2 , F3 )
            FI_Projectile_9.move( F2 , F3 )
            FI_Projectile_10.move( F2 , F3 )
            FI_Projectile_11.move( F2 , F3 )
            FI_Projectile_12.move( F2 , F3 )
            FI_Projectile_13.move( F2 , F3 )
            FI_Projectile_14.move( F2 , F3 )
            time.sleep(0.01)
            Final_Check = Window_7.checkKey()

            #Player Movement Keys.
            if Final_Check=="Left":
                X2=-2
                Y2=0
            if Final_Check=="Right":
                X2=2
                Y2=0
            if Final_Check=="Down":
                X2=0
                Y2=2
            if Final_Check=="Up":
                X2=0
                Y2=-2
            if Final_Check =="x":
                X2= 0
                Y2 = 0

            #Getting the X and Y's of the Projectiles and Player for collisions.
            P1 = Player.getCenter()
            P1X = P1.getX()

            P2 = Player.getCenter()
            P2X = P2.getY()

            P3 = Coin_7.getAnchor()
            P3X = P3.getX()

            P4 = Coin_7.getAnchor()
            P4X = P4.getY()

            P5 = Coin_8.getAnchor()
            P5X = P5.getX()

            P6 = Coin_8.getAnchor()
            P6X = P6.getY()

            P7 = Coin_9.getAnchor()
            P7X = P7.getX()

            P8 = Coin_9.getAnchor()
            P8X = P8.getY()

            P9 = Final_Coin.getAnchor()
            P9X = P9.getX()

            P10 = Final_Coin.getAnchor()
            P10X = P10.getY()

            F0 = FI_Projectile_0.getAnchor()
            F0X = F0.getX()
            FA = FI_Projectile_0.getAnchor()
            FAX = FA.getY()

            FI1 = FI_Projectile_1.getAnchor()
            FI1X = FI1.getX()
            FI2 = FI_Projectile_1.getAnchor()
            FI2X = FI2.getY()

            FI3 = FI_Projectile_2.getAnchor()
            FI3X = FI3.getX()
            FI4 = FI_Projectile_2.getAnchor()
            FI4X = FI4.getY()

            FI5 = FI_Projectile_3.getAnchor()
            FI5X = FI5.getX()
            FI6 = FI_Projectile_3.getAnchor()
            FI6X = FI6.getY()

            FI7 = FI_Projectile_4.getAnchor()
            FI7X = FI7.getX()
            FI8 = FI_Projectile_4.getAnchor()
            FI8X = FI8.getY()

            FI9 = FI_Projectile_5.getAnchor()
            FI9X = FI9.getX()
            FI10 = FI_Projectile_5.getAnchor()
            FI10X = FI10.getY()

            FI11 = FI_Projectile_6.getAnchor()
            FI11X = FI11.getX()
            FI12 = FI_Projectile_6.getAnchor()
            FI12X = FI12.getY()

            FI13 = FI_Projectile_7.getAnchor()
            FI13X = FI13.getX()
            FI14 = FI_Projectile_7.getAnchor()
            FI14X = FI14.getY()
            
            FI15 = FI_Projectile_8.getAnchor()
            FI15X = FI15.getX()
            FI16 = FI_Projectile_8.getAnchor()
            FI16X = FI16.getY()
            
            FI17 = FI_Projectile_9.getAnchor()
            FI17X = FI17.getX()
            FI18 = FI_Projectile_9.getAnchor()
            FI18X = FI18.getY()
            
            FI19 = FI_Projectile_10.getAnchor()
            FI19X = FI19.getX()
            FI20 = FI_Projectile_10.getAnchor()
            FI20X = FI20.getY()
            
            FI21 = FI_Projectile_11.getAnchor()
            FI21X = FI21.getX()
            FI22 = FI_Projectile_11.getAnchor()
            FI22X = FI22.getY()

            FI23 = FI_Projectile_12.getAnchor()
            FI23X = FI23.getX()
            FI24 = FI_Projectile_12.getAnchor()
            FI24X = FI24.getY()

            FI25 = FI_Projectile_13.getAnchor()
            FI25X = FI25.getX()
            FI26 = FI_Projectile_13.getAnchor()
            FI26X = FI26.getY()

            FI27 = FI_Projectile_14.getAnchor()
            FI27X = FI27.getX()
            FI28 = FI_Projectile_14.getAnchor()
            FI28X = FI28.getY()

            #Collision Boundary for the Projectiles to move back and forth.
            if FI_Projectile_0.getAnchor().getY() < 100:
                V2 = 0
                V3 = 4
            if FI_Projectile_0.getAnchor().getY() > 450:
                V2 = 0
                V3 = -4
            if FI_Projectile_8.getAnchor().getX() < 100:
                F2 = 5
                F3 = 0
            if FI_Projectile_8.getAnchor().getX() > 520:
                F2 = -5
                F3 = 0

            
            #Collision Boundaries for the walls.        
            if Player.getCenter().getX() > 535:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 60:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 490:
                X2 = 0
                Y2 = -1
                pass
            if Player.getCenter().getY() < 0:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getX() > 310 and Player.getCenter().getY() < 80:
                X2 = -1
                Y2 = 0
                pass
            if Player.getCenter().getX() < 290 and Player.getCenter().getY() < 80:
                X2 = 1
                Y2 = 0
                pass
            if Player.getCenter().getY() > 70 and Player.getCenter().getY() < 80 and Player.getCenter().getX() > 310 and Player.getCenter().getX() < 535:
                X2 = 0
                Y2 = 1
                pass
            if Player.getCenter().getY() > 70 and Player.getCenter().getY() < 80 and Player.getCenter().getX() > 60 and Player.getCenter().getX() < 290:
                X2 = 0
                Y2 = 1
                pass

            #Coin 7 Collision
            if (abs(P1X-P3X)) < 25 and (abs(P2X-P4X)) < 25:
                Player.undraw()
                Coin_7.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
            #Coin 8 Collision.
            elif (abs(P1X-P5X)) < 25 and (abs(P2X-P6X)) < 25:
                Player.undraw()
                Coin_8.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
            #Coin 9 Collision.
            elif (abs(P1X-P7X)) < 25 and (abs(P2X-P8X)) < 25:
                Player.undraw()
                Coin_9.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
            #Final Coin Collision.
            elif (abs(P1X-P9X)) < 25 and (abs(P2X-P10X)) < 25:
                Player.undraw()
                Final_Coin.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                Congrats.draw(Window_7)
                
            #Projectile 0 Collision.
            elif (abs(P1X-F0X)) < 25 and (abs(P2X-FAX)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
          #Projectile 1 Collision.
            elif (abs(P1X-FI1X)) < 25 and (abs(P2X-FI2X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 2 Collision.
            elif (abs(P1X-FI3X)) < 25 and (abs(P2X-FI4X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 3 Collision.
            elif (abs(P1X-FI5X)) < 25 and (abs(P2X-FI6X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 4 Collision.
            elif (abs(P1X-FI7X)) < 25 and (abs(P2X-FI8X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 5 Collision.
            elif (abs(P1X-FI9X)) < 25 and (abs(P2X-FI10X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 6 Collision.
            elif (abs(P1X-FI11X)) < 25 and (abs(P2X-FI12X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 7 Collision.
            elif (abs(P1X-FI13X)) < 25 and (abs(P2X-FI14X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 8 Collision.
            elif (abs(P1X-FI15X)) < 25 and (abs(P2X-FI16X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 9 Collision.
            elif (abs(P1X-FI17X)) < 25 and (abs(P2X-FI18X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 10 Collision.
            elif (abs(P1X-FI19X)) < 25 and (abs(P2X-FI20X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 11 Collision.
            elif (abs(P1X-FI21X)) < 25 and (abs(P2X-FI22X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 12 Collision.
            elif (abs(P1X-FI23X)) < 25 and (abs(P2X-FI24X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 13 Collision.
            elif (abs(P1X-FI25X)) < 25 and (abs(P2X-FI26X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
            
             #Projectile 14 Collision.
            elif (abs(P1X-FI27X)) < 25 and (abs(P2X-FI28X)) < 25:
                Player.undraw()
                FI_Projectile_0.undraw()
                FI_Projectile_1.undraw()
                FI_Projectile_2.undraw()
                FI_Projectile_3.undraw()
                FI_Projectile_4.undraw()
                FI_Projectile_5.undraw()
                FI_Projectile_6.undraw()
                FI_Projectile_7.undraw()
                FI_Projectile_8.undraw()
                FI_Projectile_9.undraw()
                FI_Projectile_10.undraw()
                FI_Projectile_11.undraw()
                FI_Projectile_12.undraw()
                FI_Projectile_13.undraw()
                FI_Projectile_14.undraw()
                break
                 
Main()
