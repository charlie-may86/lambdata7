from pdb import set_trace as breakpoint


class Person():
  def __init__(self, name, age, birth_month, home_state):
    self.name = name
    self.age = age
    self.birth_month = birth_month
    self.home_state = home_state

  def greets(self, name):
    print(f'Hello, {name}! My name is {self.name}, nice to meet you!')

  def had_birthday(self):
    self.age = self.age + 1
  
  def my_home(self):
    print(f'Guess where I am from? {self.home_state}!!')


if __name__ == "__main__":

    charlie = Person('Charlie', 34, 'March', 'Nebraska')
    breakpoint()