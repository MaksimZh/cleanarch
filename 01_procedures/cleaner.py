from enum import Enum
from dataclasses import dataclass
from math import sin, cos, radians


class Device(Enum):
    WATER = "water"
    SOAP = "soap"
    BRUSH = "brush"


@dataclass
class Robot:
    x: int
    y: int
    angle: int
    device: Device


def run_cleaner(commands: list[str]) -> list[str]:
    robot = Robot(0, 0, 0, Device.WATER)
    output = list[str]()
    for command in commands:
        robot, out = run_command(robot, command)
        output.append(out)
    return output

def run_command(robot: Robot, command: str) -> tuple[Robot, str]:
    action, args = parse_command(command)
    match action:
        case "move":
            assert len(args) == 1
            return move(robot, int(args[0]))
        case "turn":
            assert len(args) == 1
            return turn(robot, int(args[0]))
        case "set":
            assert len(args) == 1
            return set_state(robot, Device(args[0]))
        case "start":
            assert len(args) == 0
            return start(robot)
        case "stop":
            assert len(args) == 0
            return stop(robot)
        case _:
            assert False

def parse_command(command: str) -> tuple[str, list[str]]:
    words = command.split()
    return words[0], words[1:]

def move(robot: Robot, distance: int) -> tuple[Robot, str]:
    angle_radians = radians(robot.angle)
    new_robot = Robot(
        round(robot.x + distance * cos(angle_radians)),
        round(robot.y + distance * sin(angle_radians)),
        robot.angle,
        robot.device,
    )
    return new_robot, f"POS {new_robot.x}, {new_robot.y}"

def turn(robot: Robot, delta: int) -> tuple[Robot, str]:
    new_robot = Robot(
        robot.x,
        robot.y,
        (robot.angle + delta) % 360,
        robot.device,
    )
    return new_robot, f"ANGLE {new_robot.angle}"

def set_state(robot: Robot, device: Device) -> tuple[Robot, str]:
    new_robot = Robot(
        robot.x,
        robot.y,
        robot.angle,
        device,
    )
    return new_robot, f"STATE {new_robot.device.value}"

def start(robot: Robot) -> tuple[Robot, str]:
    return robot, f"START WITH {robot.device.value}"

def stop(robot: Robot) -> tuple[Robot, str]:
    return robot, f"STOP"
