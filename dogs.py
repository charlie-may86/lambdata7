from pdb import set_trace as breakpoint


class Dog():
    def __init__(self, name, age, housebroke=True):
        self.name = name
        self.age = age
        self.housebroke = housebroke

    # if the @property is used, you don't have to have a trailing
    # parenteses, it makes it a property instead of a class
    @property
    def bark(self):
        print(f'{self.name} likes to go "roof!"')

class Beagle(Dog):
    def __init__(self, name, age, housebroke=True, barks_alot=True):
        super().__init__(name, age, housebroke=True)
        self.barks_alot = barks_alot

    @property
    def bark(self):
        print(f'{self.name} goes "roof!" too much...')


if __name__ == "__main__":

    lucky = Dog('lucky', 3, "R. Ridgeback")
    Georgie = Dog('Georgie', 7, 'Boxer')
    Foust = Beagle('Foust', 6, barks_alot=False)
    breakpoint()

    # Type dir(lucky) to see all things we could do

    # run function with lucky.bark() if @property not live
