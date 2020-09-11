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


class Worker(Person):
    def __init__(self, name, age, birth_month, home_state,
                 company, job_title, personal_title,
                 college_grad=False, high_school_grad=True):
        super().__init__(name, age, birth_month, home_state)
        self.company = company
        self.job_title = job_title
        self.personal_title = personal_title
        self.college_grad = college_grad
        self.high_school_grad = high_school_grad

    def greets(self, some_person):
        print(f'Hello, {some_person}! My name is {self.personal_title}. {self.name}, I work for {self.company}.')

    def graduate_college(self):
        if self.college_grad is False:
            self.college_grad = True
            print(f'{self.name} has graduated college!')
        else:
            print(f'{self.name} already graduated, duh :)')

if __name__ == "__main__":

    charlie = Person('Charlie', 34, 'March', 'Nebraska')
    ryan = Worker('Ryan', 33, 'March', 'Nebraska', 'Buildertrend',
                  'Project Dude', 'Mr')
    breakpoint()
