import math
import json
from os import path
from experimentalData import ExperimentalData
import os.path

Buildingkm = 74.07

Building = "Ocean Tower"

AssaultRifle = "DT MDR 7.62x51"

Caliber = "7.62x51mm NATO"

Bullet = "7.62x51mm Ultra Nosler"

BulletSpeed = 822

BulletWeight = 0.021

Gravity = 9.8

# self.Gun = Gun
# self.Calliber = Calliber
# self.Bullet = Bullet
# self.Velocityms = Velocityms
# self.Building = Building
# self.BuildingHeight = Buildingheight_m
# self.gravityms = gravityms

print(f"Calculate the time that the bullet would take from {Building} to the floor")

Time = math.sqrt((int(Buildingkm) * 2) / int(Gravity))

Velocity = (Buildingkm / Time)

delta_x =  (Velocity / Time)


# Gun = "DT MDR 7.62x51"
# Calliber = "7.62x51mm NATO"
# Bullet = "7.62x51mm Ultra Nosler"
# Velocityms = 18.27
# Building = "Ocean Tower"
# Buildingheight_m = 74.07
# gravityms = 9.81

print(f"In the experiment we shot a gun from a building to see it's speed from the top of the building to the floor. The gun we used was the {AssaultRifle} and its caliber was {Caliber} with the bullet {Bullet} and we shot it from the building {Building}.")
print(Velocity)
myDataSet = [
    ExperimentalData("DT MDR 7.62x51", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Ocean Tower", 74.07, 9.81),
    ExperimentalData("DT MDR 7.62x51", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Ocean Tower", 74.07, 9.81),
    ExperimentalData("DT MDR 7.62x51", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Ocean Tower", 74.07, 9.81),
    ExperimentalData("DT MDR 7.62x51", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Ocean Tower", 74.07, 9.81),
    ExperimentalData("DT MDR 7.62x51", "7.62x51mm NATO", "7.62x51mm Ultra Nosler", 822, "Ocean Tower", 74.07, 9.81),
    ]

ProjectileFunction(myDataSet[1])

myOutputPath = path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath,'Experiment.json')

with open (myOutputPath, 'w') as outfile:
    json.dump(myDataSet[1].__dict__, outfile)




