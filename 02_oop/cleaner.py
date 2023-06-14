from enum import Enum
from math import sin, cos, radians


class Device(Enum):
    WATER = "water"
    SOAP = "soap"
    BRUSH = "brush"


class Angle:
    __value: int
    
    def __init__(self, value: int) -> None:
        self.__value = value % 360

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Angle):
            return False
        return self.__value == other.__value
    
    def __int__(self) -> int:
        return self.__value
    
    def turn(self, delta: int) -> "Angle":
        return Angle(self.__value + delta)


class Distance:
    __value: int

    def __init__(self, value: int) -> None:
        assert value >= 0
        self.__value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Distance):
            return False
        return self.__value == other.__value
    
    def __int__(self) -> int:
        return self.__value


class Location:
    __coords: tuple[int, int]
    
    def __init__(self, x: int, y: int) -> None:
        self.__coords = (x, y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Location):
            return False
        return self.__coords == other.__coords
    
    def get_x(self) -> int:
        return self.__coords[0]

    def get_y(self) -> int:
        return self.__coords[1]
    
    def shift(self, direction: Angle, distance: Distance) -> "Location":
        angle_radians = radians(int(direction))
        dx = round(int(distance) * cos(angle_radians))
        dy = round(int(distance) * sin(angle_radians))
        return Location(self.get_x() + dx, self.get_y() + dy)
    

class RobotPosition:
    __location: Location
    __angle: Angle

    # CONSTRUCTOR
    # POST: created new robot position
    def __init__(self, location: Location, angle: Angle) -> None:
        self.__location = location
        self.__angle = angle


    # QUERIES

    # Return current position of the robot
    def get_location(self) -> Location:
        return self.__location

    # Return current angle of the robot
    def get_angle(self) -> Angle:
        return self.__angle
    

    # COMMANDS
        
    # Move robot to distance
    def move(self, distance: Distance) -> None:
        self.__location = self.__location.shift(self.__angle, distance)

    # Turn robot by angle
    def turn(self, angle_degrees: int) -> None:
        self.__angle = self.__angle.turn(angle_degrees)


class RobotCleaner:
    __position: RobotPosition
    __device: Device
    
    # CONSTRUCTOR
    # POST: created new robot with given position and device state
    def __init__(self, location: Location, angle: Angle, device: Device) -> None:
        self.__position = RobotPosition(location, angle)
        self.__device = device


    # QUERIES

    # Return current device of the robot
    def get_device(self) -> Device:
        return self.__device
    
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
    def set_device(self, device: Device) -> None:
        self.__device = device


class RobotCleanerDriver:
    __robot: RobotCleaner
    __last_action: str

    # CONSTRUCTOR
    # POST: created new driver for robot
    def __init__(self, robot: RobotCleaner) -> None:
        self.__robot = robot
        self.__last_action = ""


    # QUERIES

    # Return last action
    def get_last_action(self) -> str:
        return self.__last_action
    

    # COMMANDS

    # Run command
    def run(self, command: str) -> None:
        action, args = self.__parse_command(command)
        match action:
            case "move":
                assert len(args) == 1
                return self.__move(int(args[0]))
            case "turn":
                assert len(args) == 1
                return self.__turn(int(args[0]))
            case "set":
                assert len(args) == 1
                return self.__set_state(Device(args[0]))
            case "start":
                assert len(args) == 0
                return self.__start()
            case "stop":
                assert len(args) == 0
                return self.__stop()
            case _:
                assert False

    @staticmethod
    def __parse_command(command: str) -> tuple[str, list[str]]:
        words = command.split()
        return words[0], words[1:]


    def __move(self, distance: int) -> None:
        self.__robot.move(Distance(distance))
        loc = self.__robot.get_location()
        self.__last_action = f"POS {loc.get_x()}, {loc.get_y()}"

    def __turn(self, delta: int) -> None:
        self.__robot.turn(delta)
        angle_degrees = int(self.__robot.get_angle())
        self.__last_action = f"ANGLE {angle_degrees}"

    def __set_state(self, device: Device) -> None:
        self.__robot.set_device(device)
        self.__last_action = f"STATE {device.value}"

    def __start(self) -> None:
        device = self.__robot.get_device()
        self.__last_action = f"START WITH {device.value}"

    def __stop(self) -> None:
        self.__last_action = f"STOP"


def run_cleaner(commands: list[str]) -> list[str]:
    robot = RobotCleaner(Location(0, 0), Angle(0), Device.WATER)
    driver = RobotCleanerDriver(robot)
    output = list[str]()
    for command in commands:
        driver.run(command)
        output.append(driver.get_last_action())
    return output
