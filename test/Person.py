class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    p1 = Person("John", 40)
    print(p1.name)
    print(p1.age)