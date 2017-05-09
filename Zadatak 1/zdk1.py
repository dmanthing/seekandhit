# -*- coding: utf-8 -*-
"""
Created on Mon May  8 22:24:53 2017

@author: Pribudic
"""

class Robot:
    
    #Inicijalizacija
    def __init__(self):
        self.x = 0
        self.y = 0
        self.status = "Waiting"
        self.direction = "NORTH"
        
    #Naredba za postavljanje robota unutar polja
    def place(self, x, y, direction):
        if(self.status == "Waiting"):
            self.x = x
            self.y = y
            self.direction = direction
            if(self.check_move() == False):
                print("Invalid placement!")
            else:
                self.status = "Placed"
        else:
            print("Robot is already placed!")
            
    #Resetiranje robota za novi set naredbi
    def reset(self):
        self.x = 0
        self.y = 0
        self.status = "Waiting"
        self.direction = "NORTH"
        
    #Naredba za pomicanje robota unutar polja
    def move(self):
        if(self.status == "Placed"):
            if(self.direction == "NORTH"):
                self.y += 1
                if(self.check_move() == False):
                    self.y -= 1
                    print("Invalid move!")
            elif(self.direction == "SOUTH"):
                self.y -= 1
                if(self.check_move() == False):
                    self.y += 1
                    print("Invalid move!")
            elif(self.direction == "EAST"):
                self.x += 1
                if(self.check_move() == False):
                    self.x -= 1
                    print("Invalid move!")
            elif(self.direction == "WEST"):
                self.x -= 1
                if(self.check_move() == False):
                    self.x += 1
                    print("Invalid move!")
                    
    #Naredba za okretanje robota u lijevu stranu s obzirom na trenutnu orjentaciju
    def left(self):
        if(self.status == "Placed"):
            if(self.direction == "NORTH"):
                self.direction = "WEST"
            elif(self.direction == "WEST"):
                self.direction = "SOUTH"
            elif(self.direction == "SOUTH"):
                self.direction = "EAST"
            elif(self.direction == "EAST"):
                self.direction = "NORTH"
                
    #Naredba za okretanje robota u desnu stranu s obzirom na trenutnu orjentaciju
    def right(self):
        if(self.status == "Placed"):
            if(self.direction == "NORTH"):
                self.direction = "EAST"
            elif(self.direction == "EAST"):
                self.direction = "SOUTH"
            elif(self.direction == "SOUTH"):
                self.direction = "WEST"
            elif(self.direction == "WEST"):
                self.direction = "NORTH"
                
    #Naredba za ispis stanja robota
    def report(self):
        if(self.status == "Placed"):
            print(str(self.x) + "," + str(self.y) + "," + self.direction)
            
    #Pomocna naredba za provjeru valjanosti pokreta
    def check_move(self):
        if(self.x < 0 or self.x > 4 or self.y < 0 or self.y > 4):
            return False
        else:
            return True
        
    #Metoda pomocu koje se pozivaju odgovarajuce narebe u odnosu na korisnicki input
    def parse_command(self, commands):
        if(commands.startswith("PLACE")):
            sub_commands = commands.split(" ")
            if len(sub_commands) > 1:
                place_params = sub_commands[1].split(",")
                if len(place_params) == 3:
                    robot.place(int(place_params[0]), int(place_params[1]), place_params[2])
                sub_commands.pop(0)
                sub_commands.pop(0)
            for command in sub_commands:
                if(command == "MOVE"):
                    self.move()
                elif(command == "LEFT"):
                    self.left()
                elif(command == "RIGHT"):
                    self.right()
                elif(command == "REPORT"):
                    self.report()
                    
                    
if __name__ == "__main__":
    #Testovi iz zadatka (za dani input ispisati oputput)
    robot = Robot()
    command = "PLACE 0,0,NORTH MOVE REPORT"
    robot.parse_command(command)
    robot.reset()
    command = "PLACE 0,0,NORTH LEFT REPORT"
    robot.parse_command(command)
    robot.reset()
    command = "PLACE 1,2,EAST MOVE MOVE LEFT MOVE REPORT"
    robot.parse_command(command)