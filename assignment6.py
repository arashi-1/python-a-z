from abc import ABC, abstractmethod


class SmartDevice(ABC):
    def __init__(self, name):
        self._name = name
        self.__is_on = False  

    @abstractmethod
    def operate(self):
        pass

    def show_status(self):
        print(f"{self._name} is {'ON' if self.__is_on else 'OFF'}")

    
    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def is_on(self):
        return self.__is_on



class SmartLight(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__brightness = 70  

    def operate(self):
        self.turn_on()
        print(f"{self._name} light turned on with brightness {self.__brightness}%")

    def get_brightness(self):
        return self.__brightness

    def set_brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
        else:
            print("Invalid brightness value. Must be between 0 and 100.")


class SmartFan(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__speed = "Medium"  

    def operate(self):
        self.turn_on()
        print(f"{self._name} fan turned on at {self.__speed} speed")

    def get_speed(self):
        return self.__speed

    def set_speed(self, value):
        if value in ["Low", "Medium", "High"]:
            self.__speed = value
        else:
            print("Invalid speed. Choose from Low, Medium, or High.")



class SmartAC(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.__temperature = 24  

    def operate(self):
        self.turn_on()
        print(f"{self._name} AC turned on at {self.__temperature}°C")

    def get_temperature(self):
        return self.__temperature

    def set_temperature(self, value):
        if 16 <= value <= 30:
            self.__temperature = value
        else:
            print("Invalid temperature. Must be between 16°C and 30°C.")



light = SmartLight("Living Room Light")
fan = SmartFan("Bedroom Fan")
ac = SmartAC("Office AC")

light.operate()
light.show_status()

fan.operate()
fan.show_status()

ac.operate()
ac.show_status()

print("\nAttempting to access private variables directly:")
try:
    print(light.__brightness)
except AttributeError as e:
    print("Error:", e)

try:
    print(fan.__speed)
except AttributeError as e:
    print("Error:", e)

try:
    print(ac.__temperature)
except AttributeError as e:
    print("Error:", e)

print("\nUsing setters to change values:")
light.set_brightness(90)
fan.set_speed("High")
ac.set_temperature(22)

print(f"Updated brightness: {light.get_brightness()}%")
print(f"Updated fan speed: {fan.get_speed()}")
print(f"Updated AC temperature: {ac.get_temperature()}°C")
