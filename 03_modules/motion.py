from math import sin, cos, radians


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


class Position:
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
