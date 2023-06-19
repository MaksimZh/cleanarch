from motion import Angle, Distance, Location, Position
from devices import Device

class RobotCleaner:
    __position: Position
    __device: Device
    
    # CONSTRUCTOR
    # POST: created new robot with given position and devices
    def __init__(self, location: Location, angle: Angle, *devices: str) -> None:
        self.__position = Position(location, angle)
        self.__device = Device(*devices)


    # QUERIES

    # Return current device of the robot
    def get_device_name(self) -> str:
        return self.__device.get_name()
    
    # Return current position of the robot
    def get_location(self) -> Location:
        return self.__position.get_location()

    # Return current angle of the robot
    def get_angle(self) -> Angle:
        return self.__position.get_angle()
    

    # COMMANDS

    # Move robot to distance
    def move(self, distance: Distance) -> None:
        self.__position.move(distance)

    # Turn robot by angle
    def turn(self, angle_degrees: int) -> None:
        self.__position.turn(angle_degrees)

    # Set current cleaning device
    def select_device(self, name: str) -> None:
        self.__device.select(name)
