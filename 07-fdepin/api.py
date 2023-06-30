from typing import Callable

import pure_robot as pr

InitFunc = Callable[[], pr.RobotState]
CommandFunc = Callable[[tuple[str, ...], pr.RobotState, pr.TransferFunc], pr.RobotState]
ControlFuncs = dict[str, CommandFunc]

CleanerFuncs: ControlFuncs = {
    "move": lambda args, state, transfer: pr.move(transfer, float(args[0]), state),
    "turn": lambda args, state, transfer: pr.turn(transfer, float(args[0]), state),
    "set": lambda args, state, transfer: pr.set_state(transfer, args[0], state),
    "start": lambda args, state, transfer: pr.start(transfer, state),
    "stop": lambda args, state, transfer: pr.stop(transfer, state),
}

SlowCleanerFuncs: ControlFuncs = {
    "move": lambda args, state, transfer: pr.move(transfer, float(args[0]) / 2, state),
    "turn": CleanerFuncs["turn"],
    "set": CleanerFuncs["set"],
    "start": CleanerFuncs["start"],
    "stop": CleanerFuncs["stop"],
}

def run(
        init: InitFunc,
        commands: list[str],
        robot_funcs: ControlFuncs,
        transfer: pr.TransferFunc
        ) -> None:
    state = init()
    for command in commands:
        words = command.split()
        action = words[0]
        args = tuple(words[1:])
        state = robot_funcs[action](args, state, transfer)
