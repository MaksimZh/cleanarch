from enum import Enum, auto
from math import sin, cos, radians


class State(Enum):
    IDLE = auto()
    RUNNING = auto()


class Device(Enum):
    NONE = "none"
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
    __state: State
    __device: Device
    __position: Position
    __angle: Angle
    
    # CONSTRUCTOR
    # POST: created new robot with:
    #       state=IDLE, device=none, position=(0, 0), angle=0
    def __init__(self) -> None:
        self.__state = State.IDLE
        self.__device = Device.NONE
        self.__position = Position(0, 0)
        self.__angle = Angle(0)


    # QUERIES

    # Return current state of the robot
    def get_state(self) -> State:
        return self.__state

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

    # Turn robot by anble
    def turn(self, angle_degrees: int) -> None:
        self.__angle = self.__angle.turn(angle_degrees)
