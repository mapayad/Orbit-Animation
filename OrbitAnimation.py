# Marie Payad
# ASWF 2022
# OrbitAnimation.py
# A python script used in Maya to simulate an object orbiting around another object.

import math
import maya.cmds as cmds

# Object must be selected before running the script.
planets = cmds.ls(selection = True)
cmds.cutKey(planets)
planet = planets[0]

# Position of the selected object and how many frames it will create.
positionX = 0
positionY = 0
radius = 5
frame = 0
frames = 100

# Sets the minimum frames and radius parameters.
if frames <= 0:
    frames = 50
if radius <= 0:
    radius = 4

# Creates the object movement and animation.
for i in range(0, frames):
    frame = i;
    positionX = math.cos(math.radians(360.0 / frames * i)) * radius
    positionZ = math.sin(math.radians(360.0 / frames * i)) * radius

    # Sets the key frame of the object.
    cmds.setKeyframe(planet + ".translateX", value = positionX, time = frame, inTangentType = "linear", outTangentType = "linear")
    cmds.setKeyframe(planet + ".translateZ", value = positionZ, time = frame, inTangentType = "linear", outTangentType = "linear")