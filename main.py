import time
from datetime import datetime

#стартовая позиция (широта)
position = 66.1233251
#скорость(км/ч)
velocity = 20;
#нормировочный коэффициент скорости
velocity_delimiter = 0.00005;
#рабочий цикл
while True:
    #период: 0.5 секунд
    time.sleep(0.5)
    #вывод текущих даты-времени и широты полета
    print (datetime.now().strftime("%d/%m/%Y %H:%M:%S"), "we fly at: ", position)
    #изменение позиции со временем
    position += velocity * velocity_delimiter
