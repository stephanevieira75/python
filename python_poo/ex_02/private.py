class CoffeeMachine:
    WATER_LEVEL=100

    def _start_machine(self):
        # starts the machine
        if self.WATER_LEVEL > 20:
            return True
        else:
            print("Please add some Water !")
            return False

    def __boil_water(self):
        # boils the water!
        return "boiling..."

    def make_coffee(self):
        #yum, a good coffee!
        if self._start_machine():
            self.WATER_LEVEL -= 20
            print(self.__boil_water())
            print("Coffee is ready my dear!")

machine = CoffeeMachine()
for i in range(0, 5):
    machine.make_coffee()
 
# - print("Make coffee: Public", machine.make_coffee()) # is public 
# - print("Start machine: Protected", machine._start_machine()) # is protected
# - print("Boil Water: Private", machine._CoffeeMachine__boil_water()) # is private