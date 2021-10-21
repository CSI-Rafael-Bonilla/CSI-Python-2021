import math
import json

OceanTowerkm = 74.07

Building = "Ocean Tower"

AssaultRifle = "DT MDR 7.62x51"

Bullet = "7.62x51mm Ultra Nosler"

BulletSpeed = 822

BulletWeight = 0.021

Gravity = 9.8

print("Calculate the time that the bullet would take from OceanTower to the floor")

Time = math.sqrt((int(OceanTowerkm) * 2) / int(Gravity))

Velocity = (OceanTowerkm / Time)

delta_x =  (Velocity / Time)

print(f"This experiment is about shooting a gun from a building. The gun will be {AssaultRifle} with the bullet called {Bullet} and we will be use the building {Building}.")