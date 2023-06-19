from typing import Callable

from motion import Location, Angle, Distance
from cleaner import RobotCleaner

class RobotCleanerDriver:
    __robot: RobotCleaner
    __process: Callable[[str], None]

    # CONSTRUCTOR
    # POST: created new driver for robot
    def __init__(self, process: Callable[[str], None]) -> None:
        self.__robot = RobotCleaner(
            Location(0, 0), Angle(0), 
            "water", "soap", "brush")
        self.__process = process


    # COMMANDS

    # Run command
    def run(self, command: str) -> None:
        action, args = self.__parse_command(command)
        match action:
            case "move":
                assert len(args) == 1
                self.__move(int(args[0]))
            case "turn":
                assert len(args) == 1
                self.__turn(int(args[0]))
            case "set":
                assert len(args) == 1
                self.__select_device(args[0])
            case "start":
                assert len(args) == 0
                self.__start()
            case "stop":
                assert len(args) == 0
                self.__stop()
            case _:
                assert False

    @staticmethod
    def __parse_command(command: str) -> tuple[str, list[str]]:
        words = command.split()
        return words[0], words[1:]


    def __move(self, distance: int) -> None:
        self.__robot.move(Distance(distance))
        loc = self.__robot.get_location()
        self.__process(f"POS {loc.get_x()}, {loc.get_y()}")

    def __turn(self, delta: int) -> None:
        self.__robot.turn(delta)
        angle_degrees = int(self.__robot.get_angle())
        self.__process(f"ANGLE {angle_degrees}")

    def __select_device(self, name: str) -> None:
        self.__robot.select_device(name)
        self.__process(f"STATE {name}")

    def __start(self) -> None:
        device = self.__robot.get_device_name()
        self.__process(f"START WITH {device}")

    def __stop(self) -> None:
        self.__process(f"STOP")
