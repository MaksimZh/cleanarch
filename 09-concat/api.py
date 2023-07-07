from typing import Any
import pure_robot as pr

def transfer(message: pr.Message):
    print(message)

class RobotAPI:
    __state: pr.RobotState
    __stack: list[str]

    def __init__(self) -> None:
        self.__state = pr.RobotState(0, 0, 0, pr.DeviceState.WATER)
        self.__stack = []

    def send(self, command: str) -> None:
        match command:
            case "move":
                arg = self.__stack.pop()
                self.__state = pr.move(transfer, float(arg), self.__state)
            case "turn":
                arg = self.__stack.pop()
                self.__state = pr.turn(transfer, float(arg), self.__state)
            case "set":
                arg = self.__stack.pop()
                self.__state = pr.set_state(transfer, arg, self.__state)
            case "start":
                self.__state = pr.start(transfer, self.__state)
            case "stop":
                self.__state = pr.stop(transfer, self.__state)
            case _:
                self.__stack.append(command)

    def get_x(self) -> float:
        return self.__state.x

    def get_y(self) -> float:
        return self.__state.y

    def get_angle(self) -> float:
        return self.__state.angle

    def get_state(self) -> Any:
        return self.__state.state
