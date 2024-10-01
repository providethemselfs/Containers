# Начнём с базового образа ROS (замените humble на желаемую версию, если это необходимо)
FROM osrf/ros:humble-desktop
# Задаём переменную окружения, чтобы пользователь не участвовал в установке (выбор клавиатуры и прочее)
ENV DEBIAN_FRONTEND=noninteractive
# Установим необходимые пакеты
RUN apt update && apt install -y \
    net-tools \
    nano
# Зададим стартовую команду для контейнера
CMD ["bash"]
