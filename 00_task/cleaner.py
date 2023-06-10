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


class Position:
    __coords: tuple[int, int]
    
    def __init__(self, x: int, y: int) -> None:
        self.__coords = (x, y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Position):
            return False
        return self.__coords == other.__coords
    
    def get_x(self) -> int:
        return self.__coords[0]

    def get_y(self) -> int:
        return self.__coords[1]
    
    def shift(self, direction: Angle, distance: Distance) -> "Position":
        angle_radians = radians(int(direction))
        dx = round(int(distance) * cos(angle_radians))
        dy = round(int(distance) * sin(angle_radians))
        return Position(self.get_x() + dx, self.get_y() + dy)


class RobotCleaner:
    __device: Device
    __position: Position
    __angle: Angle
    
    # CONSTRUCTOR
    # POST: created new robot with: device=WATER, position=(0, 0), angle=0
    def __init__(self) -> None:
        self.__device = Device.WATER
        self.__position = Position(0, 0)
        self.__angle = Angle(0)


    # QUERIES

    # Return current device of the robot
    def get_device(self) -> Device:
        return self.__device
    
    # Return current position of the robot
    def get_position(self) -> Position:
        return self.__position

    # Return current angle of the robot
    def get_angle(self) -> Angle:
        return self.__angle
    

    # COMMANDS

    # Move robot to distance
    def move(self, distance: Distance) -> None:
        self.__position = self.__position.shift(self.__angle, distance)

    # Turn robot by angle
    def turn(self, angle_degrees: int) -> None:
        self.__angle = self.__angle.turn(angle_degrees)

    # Set current cleaning device
    def set_device(self, device: Device) -> None:
        self.__device = device


def parse_command(command: str) -> tuple[str, list[str]]:
    words = command.split()
    return words[0], words[1:]


def run(commands: list[str]) -> list[str]:
    robot = RobotCleaner()
    result = list[str]()
    for cmd in commands:
        action, args = parse_command(cmd)
        match action:
            case "move":
                distance = Distance(int(args[0]))
                robot.move(distance)
                position = robot.get_position()
                result.append(f"POS {position.get_x()}, {position.get_y()}")
            case "turn":
                delta = int(args[0])
                robot.turn(delta)
                result.append(f"ANGLE {int(robot.get_angle())}")
            case "set":
                device = Device(args[0])
                robot.set_device(device)
                result.append(f"STATE {robot.get_device().value}")
            case "start":
                result.append(f"START WITH {robot.get_device().value}")
            case "stop":
                result.append(f"STOP")
            case _:
                assert False
    return result
