from tello import Tello
import sys
from datetime import datetime
import time
import TelloPro

tello = Tello()

command_lst = []
command_lst.append(TelloPro.get_instance('takeoff',3))
command_lst.append(TelloPro.get_instance('up',40))
command_lst.append(TelloPro.get_instance('down',40))
command_lst.append(TelloPro.get_instance('left',40))
command_lst.append(TelloPro.get_instance('right',40))
command_lst.append(TelloPro.get_instance('forward',40))
command_lst.append(TelloPro.get_instance('back',40))
command_lst.append(TelloPro.get_instance('cw',40))
command_lst.append(TelloPro.get_instance('ccw',40))
command_lst.append(TelloPro.get_instance('land',3))


for command in command_lst:
	tello.send_command_instance(command)
