import pure_robot as pr

class Cleaner:
    def __init__(self):
        self.__state = pr.RobotState(0, 0, 0, pr.WATER)

    def transfer_to_cleaner(self, message):
        print(message)

    def get_x(self):
        return self.__state.x

    def get_y(self):
        return self.__state.y

    def get_angle(self):
        return self.__state.angle

    def get_state(self):
        return self.__state.state
    
    def run(self, code):
        new_cleaner = Cleaner()
        new_cleaner.__state = pr.make(self.transfer_to_cleaner, code, self.__state)
        return new_cleaner
