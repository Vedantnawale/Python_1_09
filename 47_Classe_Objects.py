class Person:
    name = "Harry"
    occupation = "Software Developer"
    netWorth = 10
    def info(self):
        print(f"{self.name} is a {self.occupation}")
 
a = Person()
# a.name = "Shubham"
# a.occupation = "Accountant"
# print(a.name,a.occupation)
a.info()

# self --> wo object jiske liye method call kiya ja raha hai
