class Device:
    __devices: set[str]
    __selected_device: str

    def __init__(self, *devices: str) -> None:
        assert len(devices) > 0
        self.__devices = set(devices)
        self.__selected_device = devices[0]

    def get(self) -> str:
        return self.__selected_device
    
    def select(self, name: str) -> None:
        assert name in self.__devices
        self.__selected_device = name
