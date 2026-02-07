

class Light:
    def turn_on(self):
        print("Свет включен")


class Music:
    def turn_on(self):
        print("Музыка включена")


class SmartHome(Light, Music):
    def start(self):
        print("Умный дом активен")
        self.turn_on()


home = SmartHome()
home.start()
print(SmartHome.mro())
