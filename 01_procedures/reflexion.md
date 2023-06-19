# Процедурный стиль

В отличие от примера, у меня не используется глобальное состояние.
Каждое состояние робота неизменяемо передаётся как аргумент.


# Плюсы
  - простое проектирование: постепенно уточняем каждую операцию;
  - быстрая разработка: процедуры проще чем АТД;
  - простое тестирование: мои процедуры обладают ссылочной прозрачностью;


# Минусы
  - логика работы с состоянием размазана по нескольким процедурам;
  - процедура должна заботиться о копировании даже тех данных, с которыми не работает
    (сильная связность, плохая масштабируемость);