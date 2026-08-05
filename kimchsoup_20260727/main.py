# 김치찌개 재료 나열하기

bowl = ["가마솥", "스테인리스", "양은", "웍"]
kimchi = ["신김치", "생김치", "익은김치", "무른김치"]
meat = ["목살", "삼겹살", "매머드앞다리살", "참치", "스팸"]
made = ["양파", "두부", "대파", "사과반개"]
madeone = ["소금", "후추", "다진마늘", "멸치액젓", "쌀뜨물"]


#김치찌개 만들 재료를 고르기

print(bowl[1])
print(kimchi[0])
print(meat[3])
print(made)
print(madeone)

# * ---------------------------------------------------

#김치찌개 생성화
#클래스로 규격을 만들기.

# * ---------------------------------------------------

#냄비가 제일 먼저 골라져야 하는 부분이라 끌어옴
class Kimchi_two :
    def __init__(self, bowl) : 
        self.bowl = bowl

    def made_one(self) :
        print(f"{self.bowl}를 골랐습니다.")

kimchi = Kimchi_two(bowl[1])

kimchi.made_one()

# * ---------------------------------------------------

#신김치 고른 내용
class Kimchi_soup :
    def made_one(self) :
            print(f"{self.kimchi}를 골랐습니다.")

    def __init__(self, kimchi) : 
        self.kimchi = kimchi

kimchi = Kimchi_soup("신김치")
kimchi.made_one()

#얼마나 된 김치 인지 묻기
kimchi_date = int(input("몇 년 묵은 김치입니까?"))
if kimchi_date > 1 : #김치 신선도 물어보기
        print("묵은김치 입니다.")
else : 
        print("다른 김치를 사용하세요.")

# * -----------------------------------------------

#고기 고르기
class Kimchi_meat :
    def __init__(self, tuna) : 
        self.meat = tuna

    def made_one(self) :
        print(f"{self.meat}를 골랐습니다.")

kimchi = Kimchi_meat("참치")
kimchi.made_one()

#얼마나 된 고기 인지 묻기
kimchi_date = int(input("참치 캔 유통기한 년도가 언제입니까?"))
if kimchi_date > 20260820 : #참치 캔 유통기한 물어보기
        print("바로 사용해도 됩니다.")
else : 
        print("다른 캔 사용하세요.")

# * -------------------------------------------

#쌀뜨물 넣기
kimchi_rice = int(input("쌀뜨물을 냄비에 몇 L 녛을 예정입니까?"))
if kimchi_rice <= 2 :
        print("정량입니다.")
else : 
        print("싱거워 질 수 있습니다.")

# * -------------------------------------------

#부가재료
class Kimchi_one :
    def __init__(self, one) : 
        self.meat = one

    def made_one(self) :
        print(f"{self.one}를 골랐습니다.")

kimchi = Kimchi_meat(made)
kimchi.made_one()

#재료 기한 인지 묻기
#두부
kimchi_dubu = int(input("두부의 유통기한은 언제까지 입니까?"))
if kimchi_dubu > 20260820 : 
        print("사용해도 됩니다.")
else : 
        print("상했습니다.")

#양파
kimchi_onion = int(input("양파가 단단합니까? 1. 그렇다. 2. 아니다."))
if kimchi_onion == 1 :
        print("사용해도 됩니다.")
else : 
        print("다른 양파 사용하세요.")

#대파
kimchi_greenonion = int(input("대파의 색이 선명합니까? 1. 그렇다. 2. 아니다."))
if kimchi_greenonion == 1 :
        print("사용해도 됩니다.")
else : 
        print("상했습니다. 다른 대파 사용하세요.")

#사과 반개
kimchi_apple = int(input("사과가 색이 선명하고 단단합니까? 1. 그렇다. 2. 아니다."))
if kimchi_apple == 1 :
        print("사용해도 됩니다.")
else : 
        print("상했습니다. 다른 대파 사용하세요.")

# * ---------------------------------------------------

#부가재료2
class Kimchi_two :
    def __init__(self, two) : 
        self.meat = two

    def made_one(self) :
        print(f"{self.two}를 골랐습니다.")

kimchi = Kimchi_meat(madeone)
kimchi.made_one()

#소금 양
kimchi_salt = int(input("소금은 얼마나 g 넣을 예정입니까?"))
if kimchi_salt < 3 :
        print("적절합니다.")
else : 
        print("짤 것 같습니다. 물을 더 추가해주세요.")

#후추 양
kimchi_blackpepper = int(input("후추은 얼마나 g 넣을 예정입니까?"))
if kimchi_blackpepper < 3 :
        print("적절합니다.")
else : 
        print("그만 넣어주세요.")

#액젓 양
kimchi_enchovy = int(input("액젓은 몇 큰술 넣을 예정입니까?"))
if kimchi_enchovy < 3 :
        print("적절합니다.")
else : 
        print("짤 수도 있습니다.")

# * ----------------------------------------------------