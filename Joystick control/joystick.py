import pygame
import time

dev = []
pygame.joystick.quit()
pygame.joystick.init()
names = []
nbrOfInputs = pygame.joystick.get_count()
for i in range(0,nbrOfInputs):
 j = pygame.joystick.Joystick(i)
 name = j.get_name()
 if names.count(name) > 0:
  name = "{0} #{1}".format(name, names.count(name) + 1)
 dev.append({"id":i, "name" : name})
 names.append(name)
 print(dev)
