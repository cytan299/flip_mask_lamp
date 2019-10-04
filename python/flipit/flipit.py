"""
    flipit.py is the python script for controlling flip_mask and flip_lamp
    Copyright (C) 2017  C.Y. Tan
    Contact: cytan299@yahoo.com

    This file is part of flipit.py

    flipit.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    flipit.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with derot.  If not, see <http://www.gnu.org/licenses/>.
"""
__author__ = "C.Y. Tan"
__copyright__ = "Copyright 2017, C.Y. Tan"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "C.Y. Tan"
__email__ = "cytan299@yahoo.com"
__status__ = "alpha"

import time;

import os;
import platform;

import argparse;

from maestro import Controller;
import serial; # import again to get exceptions

#######################################################
# Initialization code
#######################################################

if (platform.uname()[0] == "Darwin"):
  SERIAL_PORT="/dev/cu.usbmodem00183281";
  # define the clear screen command depending on OS
  CLEAR_SCREEN = "clear";

if(platform.uname()[0] == "Windows"):  
  SERIAL_PORT="COM3";
  # define the clear screen command depending on OS
  CLEAR_SCREEN = "cls";

# constants

FLIP_MASK=0; # servo channel of flip mask
FLIP_LAMP=1; # servo channel of flip lamp

CH_MASK_ON = 2; # Hall probe channel that indicates mask is on
CH_MASK_OFF = 3; # interlock channel for the mask when it is off

CH_LAMP_ON = 4; # Hall probe channel that indicates lamp is on
CH_LAMP_OFF = 5; # interlock channel for the lamp when it is off

# set the speed of the servo so that the mask and lamp doesn't
# flip too quickly
MASK_SERVO_SPEED = 40; # 40*0.25us/10 ms= 10 us change per 10 ms. OR 1 ms/s.
LAMP_SERVO_SPEED = 40;

# set the acceleration of the servos. 0 unrestricted. 1 is slowest. 
# Range is 0 to 255
MASK_SERVO_ACCEL = 2;
LAMP_SERVO_ACCEL = 1;

# flip mask target values
FLIP_MASK_ON=500; # us
FLIP_MASK_NEUTRAL=1500;
FLIP_MASK_OFF=3200;

# flip lamp target values
FLIP_LAMP_ON=2400; #us
FLIP_LAMP_NEUTRAL=1500;
FLIP_LAMP_OFF=400;

# do nothing value is negative
DO_NOTHING=-1;

########################################################
# menu() - prints out the menu options for the user to select
########################################################
def menu():
    print("Flip options:");
    print("\tMask\t\tLamp");
    print("\t 1: OFF\t\t 7: OFF");
    print("\t 2: ON\t\t 8: ON");
    print("\t 3: Neutral\t 9: Neutral");
    print("\t 0: exit");
    print("=> ", end="");
    return int(input());

########################################################
# is_mask_on(): returns true if mask is in "on" position
########################################################
def is_mask_on(servo):
  if servo.getPosition(CH_MASK_ON) < 128:
    return True;
  else:
    return False;
  

########################################################
# is_mask_off(): returns true if mask is "off" position
########################################################

def is_mask_off(servo):
  if servo.getPosition(CH_MASK_OFF) > 512:
    return True;
  else:
    return False;

########################################################
# is_lamp_on(servo): returns true if lamp is in "on" position
########################################################
def is_lamp_on(servo):
  if servo.getPosition(CH_LAMP_ON) < 128:
    return True;
  else:
    return False;

########################################################
# is_lamp_off(): returns true if lamp is in "off" position
########################################################

def is_lamp_off(servo):
  if servo.getPosition(CH_LAMP_OFF) > 512:
    return True;
  else:
    return False;

########################################################
# print_state() - prints out the current state of the flip mask and lamp
########################################################
def print_state(servo):
  print("**************************");
  print("Mask: ", end="");
  if is_mask_on(servo):
    print("ON", end="");
  elif is_mask_off(servo):
    print("OFF", end="");
  else:
    print("?", end="");

  print("\t Lamp: ", end="");
  if is_lamp_on(servo):
    print("ON", end="");
  elif is_lamp_off(servo):
    print("OFF", end="");
  else:
    print("?", end="");

  print("");
  print("**************************");  
    

########################################################
# main entry point
########################################################

# parse any commandline arguments
parser = argparse.ArgumentParser(description="flip mask and lamp control programme");

if (platform.uname()[0] == "Darwin"):
  parser.add_argument("serial_port", type=str, nargs='?', default=SERIAL_PORT, help='serial port name. Default: '+ SERIAL_PORT);

if(platform.uname()[0] == "Windows"):  
  parser.add_argument("serial_port", type=str, nargs='?', default=SERIAL_PORT, help='serial port name. Default: ' + SERIAL_PORT);
args = parser.parse_args();

# completed parsing the commandline arguments and let's open the serial port etc.
try:
  servo = Controller(args.serial_port);
except serial.SerialException:
  print("flipit.py: cannot open ", args.serial_port);
  exit();

servo.setSpeed(FLIP_MASK, MASK_SERVO_SPEED);
servo.setAccel(FLIP_MASK, MASK_SERVO_ACCEL);
servo.setSpeed(FLIP_LAMP, LAMP_SERVO_SPEED);
servo.setAccel(FLIP_LAMP, LAMP_SERVO_ACCEL);

# for some stupid reason the above speeds and accelerations
# don't seem to be executed until the first command is sent
servo.setTarget(FLIP_MASK, FLIP_MASK_OFF*4);
servo.setTarget(FLIP_LAMP, FLIP_LAMP_OFF*4);

# Print out the current state of the flip mask and lamp
_=os.system(CLEAR_SCREEN);
print_state(servo);

# Now we can process the user inputs
while 1:
  choice = menu();

  print("Working ...");

  if choice == 0:
    servo.close();
    _=os.system(CLEAR_SCREEN);
    exit();
  if choice == 1:
    target = FLIP_MASK_OFF;
  elif choice == 2:
    # check that the lamp is already on. If so, do nothing
    if is_lamp_on(servo):
      choice = DO_NOTHING;
    target = FLIP_MASK_ON;
  elif choice == 3:
    target = FLIP_MASK_NEUTRAL;
  elif choice == 7:
    target = FLIP_LAMP_OFF;
  elif choice == 8:
    # check that the mask is already on. If so, do nothing
    if is_mask_on(servo): 
      choice = DO_NOTHING;  
    target = FLIP_LAMP_ON;
  elif choice == 9:
    target = FLIP_LAMP_NEUTRAL;

  if choice < 0:
    if target == FLIP_MASK_ON:
       print("!!!! Error: FLIP LAMP is still on !!!!");
    if target == FLIP_LAMP_ON:
       print("!!!! Error: FLIP MASK is still on !!!!");
  else:  
    if 1<= choice <= 3: 
      servo.setTarget(FLIP_MASK, target*4);
    if 7<= choice <=9:
      servo.setTarget(FLIP_LAMP, target*4);

    time.sleep(5.0);
    _=os.system(CLEAR_SCREEN);
    print_state(servo);

          

