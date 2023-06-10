# Робот-дворник

## Задача
Входные команды:
  - `move <distance_meters>`;
  - `turn <angle_degrees>`;
  - `set <device>`;
  - `start`;
  - `stop`;

Типы устройств (`<device>`):
  - `water`;
  - `soap`;
  - `brush`;

Вывод:
  - `move` -> текущая позиция `POS <x_meters>, <y_meters>`
    (старт в нуле?);
  - `turn` -> текущее направление (угол поворота) `ANGLE <a_degrees>`
    (старт в нуле?);
  - `set` -> текущее устройство очистки `STATE water/soap/brush`
    (начальное устройство - `none`?, если уже работаем - выключить и заменить?);
  - `start` -> начало работы с текущим устройством `START WITH water/soap/brush`
    (пусть по умолчанию будет `water`, если уже работаем - игнорировать?);
  - `stop` -> прекращение работы `STOP`
    (если работа не начата - ОК)


## АТД

### State
  - `RUNNING`
  - `IDLE`


### Device
  - `none`
  - `water`
  - `soap`
  - `brush`


### Position

#### Запросы
  - `get_x() -> int`
  - `get_y() -> int`
  - `shift(direction: Angle, distance: Distance) -> Position` \
    сдвиг в заданном направлении с округлением


### Angle
Целое от 0 до 359.
  - запрос `turn(delta: int) -> Angle` \
    поворот с возможным переполнением


### Distance
Целое неотрицательное.


### RobotCleaner

#### Запросы
  - `get_state() -> State` \
    Возвращает текущее состояние робота.
  - `get_device() -> Device` \
    Возвращает текущее устройство очистки.
  - `get_position() -> Position` \
    Возвращает текущую позицию робота.
  - `get_angle() -> Angle` \
    Возвращает текущий угол поворота робота.

#### Команды
  - `move(distance: Distance)` \
    смещение в текущем направлении
  - `turn(angle: Angle)` \
    изменение текущего направления
  - `set_device(device: Device)` \
    выбор текущего устройства
  - `start()` \
    начало работы
    - **PRE:** устройство не `none`
    - **POST:** состояние равно `RUNNING`
  - `stop()` \
    конец работы
    - **POST:** состояние равно `IDLE`
