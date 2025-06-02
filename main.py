#!/usr/bin/env python3

# needs opentrons library version 2.5.2 exactly
from opentrons import robot
from opentrons import containers, instruments

def main():

    print("Starting")

#    robot.connect('Virtual Smoothie')
    robot.connect('/dev/ttyUSB0')    
    robot.home()
    
    tiprack = containers.load(
        'tiprack-200ul',  # container type
        'A1',             # slot
        'tiprack'         # user-defined name
    )

    plate = containers.load('96-flat', 'B1', 'plate')
    
    p200 = instruments.Pipette(
        axis="b",
        max_volume=200
    )

    p200.pick_up_tip(tiprack[0])

    for i in range(95):
        p200.aspirate(100, plate[i])
        p200.dispense(plate[i + 1])

    p200.return_tip()


#    robot.simulate()
    

if __name__ == "__main__":
    main()
