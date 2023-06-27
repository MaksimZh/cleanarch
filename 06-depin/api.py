from abc import ABC, abstractmethod
from typing import Any

import pure_robot as pr


class Robot(ABC):

    @abstractmethod
    def get_x(self) -> float:
        assert False

    @abstractmethod
    def get_y(self) -> float:
        assert False

    @abstractmethod
    def get_angle(self) -> float:
        assert False

    @abstractmethod
    def get_state(self) -> Any:
        assert False

    @abstractmethod
    def run_command(self, command: str) -> None:
        assert False


class Driver:
    __robot: Robot

    def __init__(self, robot: Robot) -> None: # раз внедрение
        self.__robot = robot

    def get_x(self) -> float:
        return self.__robot.get_x()

    def get_y(self) -> float:
        return self.__robot.get_y()

    def get_angle(self) -> float:
        return self.__robot.get_angle()

    def get_state(self) -> Any:
        return self.__robot.get_state()

    def run(self, code: list[str]) -> None:
        for command in code:
            self.__robot.run_command(command)


class CleanerRobot(Robot):
    __transfer: pr.Transfer
    __state: pr.RobotState

    def __init__(self, transfer: pr.Transfer) -> None: # два внедрение
        self.__transfer = transfer
        self.__state = pr.RobotState(0, 0, 0, pr.DeviceState.WATER)

    def get_x(self) -> float:
        return self.__state.x

    def get_y(self) -> float:
        return self.__state.y

    def get_angle(self) -> float:
        return self.__state.angle

    def get_state(self) -> Any:
        return self.__state.state

    def run_command(self, command: str) -> None:
        self.__state = pr.make(self.__transfer, [command], self.__state)


def transfer(message: pr.Message) -> None:
    print(*message)


class CleanerApi(Driver):

    def __init__(self) -> None:
        cleaner = CleanerRobot(transfer) # внедрение зависимости
        super().__init__(cleaner) # внедрение зависимости в родительский класс
