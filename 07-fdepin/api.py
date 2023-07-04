from typing import Callable

import pure_robot as pr

InitFunc = Callable[[], pr.RobotState]
CommandFunc = Callable[[tuple[str, ...], pr.RobotState, pr.TransferFunc], pr.RobotState]

def CleanerFunc(
        command: tuple[str, ...],
        state: pr.RobotState,
        transfer: pr.TransferFunc
        ) -> pr.RobotState:
    action = command[0]
    args = command[1:]
    match action:
        case "move":
            return pr.move(transfer, float(args[0]), state)
        case "turn":
            return pr.turn(transfer, float(args[0]), state)
        case "set":
            return pr.set_state(transfer, args[0], state)
        case "start":
            return pr.start(transfer, state)
        case "stop":
            return pr.stop(transfer, state)
        case _:
            assert False

def SlowCleanerFunc(
        command: tuple[str, ...],
        state: pr.RobotState,
        transfer: pr.TransferFunc
        ) -> pr.RobotState:
    action = command[0]
    args = command[1:]
    match action:
        case "move":
            return pr.move(transfer, float(args[0]) / 2, state)
        case "turn":
            return pr.turn(transfer, float(args[0]), state)
        case "set":
            return pr.set_state(transfer, args[0], state)
        case "start":
            return pr.start(transfer, state)
        case "stop":
            return pr.stop(transfer, state)
        case _:
            assert False

def run(
        init: InitFunc,
        commands: list[str],
        robot_func: CommandFunc,
        transfer: pr.TransferFunc
        ) -> None:
    state = init()
    for command in commands:
        words = tuple(command.split())
        state = robot_func(words, state, transfer)
