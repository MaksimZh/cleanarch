import pure_robot as pr

state: pr.RobotState

def reset():
    global state
    state = pr.RobotState(0, 0, 0, pr.WATER)

def run(code: list[str]):
    global state
    state = pr.make(pr.transfer_to_cleaner, code, state) #type: ignore

reset()
