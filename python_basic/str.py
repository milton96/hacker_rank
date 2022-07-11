class Car:
    def __init__(self, max_speed, speed_unit) -> None:
        self.max_speed = max_speed
        self.speed_unit = speed_unit
    
    def __str__(self) -> str:
        return f'Car with the maximum speed of {self.max_speed} {self.speed_unit}'

class Boat:
    def __init__(self, max_speed) -> None:
        self.max_speed = max_speed
    
    def __str__(self) -> str:
        return f'Boar with the maximum of {self.max_speed} knots'

if __name__ == '__main__':
    car = Car(123, 'hola')
    print(car)