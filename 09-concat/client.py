import api

r = api.RobotAPI()
code = [
    "100",
    "move",
    "-90",
    "turn",
    "soap",
    "set",
    "start",
    "50",
    "move",
    "stop",
]
for command in code:
    r.send(command)
