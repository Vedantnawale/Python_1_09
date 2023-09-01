class Person:
    # name = "Harry"
    # occupation = "Software Developer" or we used constructor
    def __init__(self,n,o):
        print("hey i am a person")
        self.name = n
        self.occupation = o
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
        
a = Person("Harry","Developer")
b = Person("Divya","HR")
# print(a.name)
# a.name = "Divya"
# a.occupation = "HR"
a.info()
b.info()