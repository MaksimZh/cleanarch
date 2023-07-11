from typing import Callable, Any

import pure_robot as pr


Command = Callable[[pr.RobotState, pr.TransferFunc], pr.RobotState]

class _StateMonad:
    __initial: pr.RobotState
    __transfer: pr.TransferFunc
    __commands: list[Command]
    
    def __init__(self, state: pr.RobotState, transfer: pr.TransferFunc) -> None:
        self.__initial = state
        self.__transfer = transfer
        self.__commands = []

    def bind(self, command: Command) -> "_StateMonad":
        new_monad = _StateMonad(self.__initial, self.__transfer)
        new_monad.__commands = self.__commands + [command]
        return new_monad

    def eval(self) -> pr.RobotState:
        if len(self.__commands) == 0:
            return self.__initial
        new_state = self.__commands[0](self.__initial, self.__transfer)
        tail_monad = _StateMonad(new_state, self.__transfer)
        tail_monad.__commands = self.__commands[1:]
        return tail_monad.eval()


def wrap(func: Callable[..., pr.RobotState], *args: Any) -> Command:
    
    def cmd(state: pr.RobotState, transfer: pr.TransferFunc) -> pr.RobotState:
        new_state = func(transfer, *args, state)
        return new_state
    
    return cmd

def transfer(message: pr.Message):
    print(message)

def new() -> _StateMonad:
    return _StateMonad(pr.RobotState(0, 0, 0, pr.DeviceState.WATER), transfer)

def move(distance: float) -> Command:
    return wrap(pr.move, distance)

def turn(angle: float) -> Command:
    return wrap(pr.turn, angle)

def set_state(state: str) -> Command:
    return wrap(pr.set_state, state)

def start() -> Command:
    return wrap(pr.start)

def stop() -> Command:
    return wrap(pr.stop)
