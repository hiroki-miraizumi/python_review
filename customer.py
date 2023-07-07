class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if 4 <= self.age <= 20:
            return 1000
        elif 20 <= self.age < 65:
            return 1500
        elif 3 >= self.age:
            return 0
        elif self.age <= 75:
            return 500
        else:
            return 1200
    
    def info_csv(self):
        return self.full_name(), self.age, self.entry_fee()
        

# ken = Customer(first_name="Ken", family_name="Tanaka")
# print(ken.full_name()) 

# tom = Customer(first_name="Tom", family_name="Ford")
# print(tom.full_name())



ken = Customer(first_name="Ken", family_name="Tanaka", age=3)
print(ken.age)  # 15 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.age) # 57 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.age) # 73 という値を返す

ken = Customer(first_name="Ken", family_name="Tanaka", age=3)
print(ken.entry_fee())  # 1000 という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.entry_fee()) # 1500 という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.entry_fee()) # 1200 という値を返す

ken = Customer(first_name="Ken", family_name="Tanaka", age=3)
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す

tom = Customer(first_name="Tom", family_name="Ford", age= 57)
print(tom.info_csv())  # "Tom Ford,57,1500" という値を返す

ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を返す