import math

OceanTower = 74.07

AssaultRifle = "DT MDR 7.62x51"

Bullet = "7.62x51mm Ultra Nosler"

BulletSpeed = 822

BulletWeight = 0.021

Gravity = 9.8

print("Calculate the time that the bullet would take from OceanTower to the floor")

Time = math.sqrt((int(OceanTower) * 2) / int(Gravity))

Velocity = (OceanTower / Time)

delta_x =  (Velocity / Time)