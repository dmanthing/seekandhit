# -*- coding: utf-8 -*-
"""
Created on Mon May  8 23:10:49 2017

@author: Pribudic
"""

import random

class Airplane:
    
    #Inicijalizacija
    def __init__(self, aid, pid):
        self.id = aid
        self.pid = pid
        
    #Ispis
    def pprint(self):
        print("Airplane: " + str(self.id) + " Parking: "+ str(self.pid))
        
        
class Parking:
    
    #Inicijalizacija
    def __init__(self, pid, status):
        self.id = pid
        self.status = status
        
    #Ispis
    def pprint(self):
        print("Parking: " + str(self.id) + " Status: "+ str(self.status))
        
#Pronalazak neparkiranih aviona i parkiranje istih        
def park_planes(airplane_list, parking_list):
    for plane in airplane_list:
        if plane.pid == 0:
            assign_parking(plane, parking_list)
    print("Done! All planes are assigned with a parking spot.")

#Dodjela random slobodnog parking mjesta avionu
def assign_parking(plane, parking_list):
    spot = random.randrange(0, 100)
    if(parking_list[spot].status == "Free"):
        plane.pid = parking_list[spot].id
        parking_list[spot].status = "Taken"
    else:
        assign_parking(plane, parking_list)
        

if __name__ == "__main__":
    airplane_list = []
    parking_list = []
    #Popunjavanje liste aviona
    for i in range(0,80):
        air = Airplane(i+1, 0)
        airplane_list.append(air)
    #Popunjavanje liste parkinga
    for i in range(0,100):
        park = Parking(i+1, "Free")
        parking_list.append(park)
    #Parkiranje aviona  
    park_planes(airplane_list, parking_list)
    #Ispis aviona nakon parkiranja
    for plane in airplane_list:
        plane.pprint()
    #Ispis parkinga nakon parkiranja aviona
    for park in parking_list:
        park.pprint()