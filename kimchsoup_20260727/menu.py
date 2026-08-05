#김치찌개 종류에 대한 메뉴 관리

class Kimchi_soup : 
    def __init__(self, kind) :
        self.kind = kind

    def info(self) :
        return f"{self.kind} 김치찌개" #이거 김치찌개 단어 고정

kimchi_stew = Kimchi_soup("북엇국")
kimchi_stew1 = Kimchi_soup("스팸")
kimchi_stew2 = Kimchi_soup("참치")
kimchi_stew3 = Kimchi_soup("목살")
kimchi_stew4 = Kimchi_soup("매머드앞다리살")
kimchi_stew5 = Kimchi_soup("소시지") #하고 싶은 정류 다 입력

print(kimchi_stew.info()) #그만킁믜 답 이렇게 하면 쫙 나온다.
print(kimchi_stew1.info())
print(kimchi_stew2.info())
print(kimchi_stew3.info())
print(kimchi_stew4.info())
print(kimchi_stew5.info())


#샌드위치도 이런식으로 메뉴를 할 수 있다. 

class Sandwich : 
    def __init__(self, kind) :
        self.kind = kind

    def info(self) :
        return f"{self.kind} 샌드위치" #이거 샌드위치 단어 고정


subway_sandwich = Sandwich("스파이시쉬림프")
subway_sandwich1 = Sandwich("에그마요")
subway_sandwich2 = Sandwich("랍스타")
subway_sandwich3 = Sandwich("이탈리안BMT")
subway_sandwich4 = Sandwich("로티세리")

print(subway_sandwich.info())
print(subway_sandwich1.info())
print(subway_sandwich2.info())
print(subway_sandwich3.info())
print(subway_sandwich4.info())
