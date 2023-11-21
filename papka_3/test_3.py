# Задание 1
class CreateMixin:
    def create(self, todo, key):
        if not key in self.todos.keys():
            self.todos[key] = todo
            return self.todos
        return "Задача под таким ключом уже существует"

class DeleteMixin:
    def delete(self, key):
        if key in self.todos.keys():
            a = self.todos.pop(key)
            return a

class UpdateMixin:
    def update(self, key, new_value):
        self.todos[key] = new_value
        return self.todos

class ReadMixin:
    def read(self):
        a = [x for x in self.todos.items()]
        return a
    
import datetime
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}
    def set_deadline(self, dedline):
        new_date = datetime.datetime.now().strftime('%d/%m/%Y')
        dedline = dedline.split('/')
        new_date = new_date.split('/')
        dedline = list(map(int, dedline))
        new_date = list(map(int, new_date))
        new_date = sum((new_date[0], new_date[1]*30, new_date[2]*365))
        dedline = datetime.date(dedline[2], dedline[1], dedline[0])
        new_date = datetime.date.today()
        return (dedline - new_date).days

task = ToDo()
print(task.create(1, 'Do housework'))
print(task.create(1, 'Do housework'))
print(task.create(2, 'Go for a walk'))
print(task.update(1, 'Do homework'))
print(task.delete(2))
print(task.read())
print(task.set_deadline('31/12/2021'))
print(task.todos)

import datetime
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}
    def set_deadline(self, dedline):
        new_date = datetime.datetime.now().strftime('%d/%m/%Y')
        dedline = dedline.split('/')
        new_date = new_date.split('/')
        dedline = list(map(int, dedline))
        new_date = list(map(int, new_date))
        new_date = sum((new_date[0], new_date[1]*30, new_date[2]*365))
        dedline = datetime.date(dedline[2], dedline[1], dedline[0])
        new_date = datetime.date.today()
        return (dedline - new_date).days
    




# Задание 2
class Person:
    def __init__(self, name=None, last_name=None,age=None, email=None):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__email = email
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_last_name):
        self.__name = new_last_name
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, new_last_name):
        self.__last_name = new_last_name
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        self.__age = new_age
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, new_email):
        self.__email = new_email


john = Person()
print(john.name) # None
print(john.last_name) # None
print(john.age) # None
print(john.email) # None
john.name = 'John'
john.last_name = 'Snow'
john.age = 30
john.email = 'johnsnow@gmail.com'
print(john.name) # John
print(john.last_name) # Snow
print(john.age) # 30
print(john.email)  # johnsnow@gmail.com





# Задание 3
class Dog:
    def voice(self):
        print("Гав")

class Cat:
    def voice(self):
        print("Мяу")

def to_pet(a):
    a.voice()

barsik = Cat()
rex = Dog()
to_pet(barsik)
to_pet(rex) 