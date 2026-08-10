
# * -------------------

# fish_bread basic tool
class Fish_bread :
    def __init__(self,name) :
        self.name = name

    def speak(self) :
        print(f"{self.name} 만듭니다.")

# * --------------------

class Ingredient(Fish_bread) :
    def speak(self) :
        print(f"{self.name} 넣습니다.")

# 슈크림

class Kinds(Fish_bread) :
    def speak(self) :
        print(f"{self.name} 붕어빵 입니다.")


# 크림치즈
class Cream(Fish_bread) :
    def speak(self) :
        print(f"{self.name} 붕어빵 입니다.")


#팥
class Ang(Fish_bread) :
    def speak(self) :
        print(f"{self.name} 붕어빵 입니다.")


#아이스크림
class Icecream(Fish_bread) :
    def speak(self) :
        print(f"{self.name} 붕어빵 입니다.")

# * ----------------------

ingredient = Ingredient("골라서")
kinds = Kinds("슈크림")
cream = Cream("크림치즈")
ang = Ang("팥")
icecream = Icecream("아이스크림")

ingredient.speak()
kinds.speak()
cream.speak()
ang.speak()
icecream.speak()

