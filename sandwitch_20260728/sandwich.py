import random

#샌드위치 만드는 가게를 만들어 봅시다.
# * ------------------------------------------
#샌드위치를 주문 하는 곳 #기본
        #키오스크
        #주문대
        #썹픽어플주문

class Iam_sandwich() :
    def __init__(self): #우선 속성 초기화 시켜주기 None을 사용해서
        self.vending = None
        self.person = None
        self.app = None
        self.where = None #밑에 값을 설정해주기 위해서 만들어준 목록

    def order(self):
        print("1. 키오스크 | 2. 대면 | 3. 앱")
        self.where = int(input("어디에서 주문하시겠습니까? (숫자): "))
        #이 입력을 쓰기 위해서 새로 또 설정해주기.

        if self.where == 1: #이 값 설정을 해서 판단하게 만들기
            self.vending = "키오스크 주문 완료"
            print("주문표를 받아주세요.")
        elif self.where == 2:
            self.person = "주문대 주문 완료"
            print("자리에서 기다려주세요.")
        elif self.where == 3:
            self.app = "앱 주문 완료"
            print("주문이 완료 되었습니다.")
        else:
            print("잘못된 입력입니다.")

sandwich_order = Iam_sandwich() # 따로 지정
sandwich_order.order() #판단문이 들어간 함수 order 설정

# * -------------------------------------------------

    # 구성원 
    #일하는 사람의 구성원. 점주를 비롯해 정규직 직원 그리고 비정규직 직원
    # 점주 #전체적인 관리
    # 직원 #홀담당 주방담당
    # 알바 #알바의 경우에는 시급제, 평일근무, 주말근무

#사장은 지정된 사람이기에 이름만 지정
class Staff : 
    def sajang() :
        master_name = "Kim"
        print(master_name)

name = Staff
name.sajang()

#직원들의 겹치는 출근 날을 뽑기

#정규직원
regular_staff = [
    {
        "이름" : "홍길등",
        "출근" : ["월", "화", "수", "목", "금"],
        "쉬는날" : ["토", "일"],
    },
    {
        "이름" : "신윤복",
        "출근" : ["화", "수", "목", "금", "토"],
        "쉬는날" : ["일, 월"]
    }
]

#시간제직원
part_time = [
    {

    "이름" : "허난설현",
    "출근" : ["월", "수", "토"],
    },
    {
    "이름" : "신사임당",
    "출근" : ["일", "화", "목"],
    }
]

#근무시간 겹치는거 추출
#정규직과 시간제 합치기

class Workday() : #클래스에 합쳐도 답이 나오는 걸 확인
    monday_set = {"월"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & monday_set :
            print(f"근무날 {staffs['이름']}월요일")
    
        tuesday_set = {"화"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & tuesday_set :
            print(f"근무날 {staffs['이름']}화요일")

        wednseday_set = {"수"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & wednseday_set :
            print(f"근무날 {staffs['이름']}수요일")

            thursday_set = {"목"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & thursday_set :
            print(f"근무날 {staffs['이름']}목요일")

            friday_set = {"금"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & friday_set :
            print(f"근무날 {staffs['이름']}금요일")

    saturaday_set = {"토"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & saturaday_set :
            print(f"근무날 {staffs['이름']}토요일")

    sunday_set = {"일"}
    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & sunday_set :
            print(f"근무날 {staffs['이름']}일요일")

    monday_workers = {"월"}
    monday_list = []

    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & monday_workers :
            monday_list.append(staffs['이름'])

    print("월요일 근무자 :", monday_list)

    friday_workers = {"금"}
    friday_list = []

    for staffs in regular_staff + part_time :
        if set(staffs["출근"]) & friday_workers :
            friday_list.append(staffs['이름'])

    print("금요일 근무자 :", friday_list)

# * ----------------------------------------------

    #샌드위치 종류들
    #이벤트 샌드위치 메뉴
    #이벤트성으로 한정판 핸드위치 및 조합이 되어 있는 샌드위치
        #이벤트샌드위치
            #아기맹수
            #로부스터
            #오이샌드위치
            #터키샌드위치

class Event_sandwich :
    print("이벤트 샌드위치")
    def __init__(self, 이름, 사이즈) :
        self.event = 이름
        self.size = 사이즈

#밑에서 값을 정해주기
    def event_menu(self) :
        print(f"이름 : {self.event}")
        print(f"사이즈: {self.size}")

#종류 리스트
#이벤트 샌드위치 리스트
    event_name = ([
        {"이름" : "아기맹수",
        "사이즈" : "15cm"},

        {"이름" : "로부스터",
        "사이즈" : "15cm"},

        {"이름" : "오이",
        "사이즈" : "15cm"},

        {"이름" : "터키",
        "사이즈" : "15cm"},
        ])

#객체로 생성하는 법

names = []

for this in Event_sandwich.event_name :
    event = Event_sandwich(
        this["이름"],
        this["사이즈"]
    )

    names.append(event)
#더 해서 쫘르르 리스트가 나오도록 만들기

for event in names : 
    event.event_menu()

# * -------------------------------------

#만들 수 있는 샌드위치 메뉴들
#용량은 g으로 통일해서 주기 
        #샌드위치종류 
            #클럽샌드위치
            #스파이시쉬림프
            #쉬림프
            #비프머시룸
            #피자썹
            #에그마요
            #잠봉뵈르
            #스테이크
            #로티세리
            #이탈리안BMT
            #폴드포크바비큐
            #로스트치킨
            #데리야끼
            #치킨베이컨아보카도
            #참치
            #에그슬라이스 #이건 슬라이스 종류라서 슬라이스 갯수로 주기
            #배지
            #랜덤 #결정을 못하는 사람들을 위한 랜덤으로 추천

class Sandwich :
    def __init__(self, names) :
        self.name  = names

#메뉴 이름이 나올 수 있게 print해서 값 설정

    def sandwich_menu(self) :
        print(f"{self.name}")


#순서대로 메뉴가 나오게 정해줌

menus = Sandwich("클럽샌드위치")
menus2 = Sandwich("스파이시쉬림프")
menus3 = Sandwich("쉬림프")
menus4 = Sandwich("비프머시룸")
menus5 = Sandwich("피자썹")
menus6 = Sandwich("에그마요")
menus7 = Sandwich("잠봉뵈르")
menus8 = Sandwich("스테이크")
menus9 = Sandwich("로티세리")
menus10 = Sandwich("이탈리안BMT")
menus11 = Sandwich("폴드포크바비큐")
menus12 = Sandwich("로스트치킨")
menus13 = Sandwich("데리야끼")
menus14 = Sandwich("치킨베이컨아보카도")
menus15 = Sandwich("참치")
menus16 = Sandwich("에그슬라이스")
menus17 = Sandwich("배지")
menus18 = Sandwich("랜덤")

#순서대로 출력 되게 나오는 것

menus.sandwich_menu()
menus2.sandwich_menu()
menus3.sandwich_menu()
menus4.sandwich_menu()
menus5.sandwich_menu()
menus6.sandwich_menu()
menus7.sandwich_menu()
menus8.sandwich_menu()
menus9.sandwich_menu()
menus10.sandwich_menu()
menus11.sandwich_menu()
menus12.sandwich_menu()
menus13.sandwich_menu()
menus14.sandwich_menu()
menus15.sandwich_menu()
menus16.sandwich_menu()
menus17.sandwich_menu()
menus18.sandwich_menu()

# * ------------------------------------------

#랜덤 돌리기 무작위로 정할 수 있게 한번 넣어보기

all = ["클럽", "쉬림프", "잠봉뵈르", "참치", "에그마요"]
print(random.choice(all))

# * ------------------------------------------

#빵을 고르는 문
def sandwich_question() : 
    ask = input("목록을 보고 샌드위치를 입력해주세요.> ")
    print(ask)

sandwich_question()

#고를 수 있는 세부적인 종류들을 추가
#주문이 들어와서 빵을 고른 후 반을 가르기. 그 전에는 긴 빵 모양을 유지
            #기본구성
                #빵
                    #플랫브레드
                    #그레인
                    #오트밀
                    #화이트
                    #위트
                    #파마산오레가노
                    #허니오트

#판단문으로 정확한 메뉴를 골랐으면 다음으로
#아니면 다시 고르기

#빵을 고르는 문
def bread_question() : 
    qusetion = input("빵을 고르시겠습니끼?")
    return qusetion

#클래스로 빵 타입 정해주고 판단문 집어 넣기

class Bread :
    def __init__(self, bread) : 
        self.breadtype = bread

    def choice_bread(self) :
        print(f"{self.breadtype}를 골랐습니다.")

        all_bread = ["플랫브레드", "그레인", "오트밀", "화이트", "위트", "파마산오레가노", "허니오트"]
        #여러 빵을 골라야 하므로 안에 리스트를 집어 넣음

        if self.breadtype in all_bread :
            print(f"{self.breadtype} 다음으로")
        else :
            print(f"{self.breadtype} 목록에 없습니다. 다시 골라주세요.")


bread_choice = bread_question() #우선 고르는 빵의 값의 출력을 설정
bread_pick = Bread(bread_choice) #그것을 받고 유저가 선택한 타입을 넣음
bread_pick.choice_bread() #총 그것에 대한 판단문을 하고 나서 결정하는 출력

# * ----------------------------------------------------------------------

                #치즈 #용량은 g으로 통일해서 주기
                    #아메리칸치즈
                    #슈레드

def chesses_question() :
    chesses_ask = input("치즈 종류를 골라주세요.")
    return chesses_ask

class Add_chesses : 
    def __init__(self, chesses) :
        self.chesses = chesses

    def chesses_choice(self) :
        print(f"{self.chesses} 골랐습니다.")

        chesses = ["아메리칸치즈", "슈레드"]

        if self.chesses in chesses : 
            print(f"{self.chesses} 다음으로")
        else : 
            print(f"{self.chesses} 다시 골라주세요.")

chesses_recipe = chesses_question()
chesses_pick = Add_chesses(chesses_recipe)
chesses_pick.chesses_choice()

# * ----------------------------------------------------------------------

                #채소 #용량은 갯수로 통일해서 주기
                    #토마토
                    #피망
                    #양파
                    #양상추 #이건 g으로 설정

def vege_question() :
    vege_ask = input("채소 종류를 골라주세요.")
    return vege_ask

class vege_chesses : 
    def __init__(self, vege) :
        self.vege = vege

    def vege_choice(self) :
        print(f"{self.vege} 골랐습니다.")

        vege = ["토마토", "피망", "양파", "양상추"]

        if self.vege in vege : 
            print(f"{self.vege} 다음으로")
        else : 
            print(f"{self.vege} 다시 골라주세요.")

vege_recipe = vege_question()
vege_pick = vege_chesses(chesses_recipe)
vege_pick.vege_choice()

# * ----------------------------------------------------------------------

#용량은 g으로 통일
#가미 할 것
            #페스토
                #에그마요
                #아보카도
                #메쉬포테이토
                #고구마
                #바질페스토

def cream_question() :
    cream_ask = input("페스트 종류를 골라주세요.")
    return cream_ask

class Add_recipe : 
    def __init__(self, cream) :
        self.cream = cream

    def cream_choice(self) :
        print(f"{self.cream} 골랐습니다.")

        cream = ["에그마요", "아보카도", "메쉬포테이토", "고구마", "바질페스토"]

        if self.cream in cream : 
            print(f"{self.cream} 다음으로")
        else : 
            print(f"{self.cream} 다시 골라주세요.")

cream_recipe = cream_question()
cream_pick = Add_recipe(cream_recipe)
cream_pick.cream_choice()

# * -------------------------------------------------------------
#소스 목록들
# 한번 짤 때 한바퀴 돌리기
            #소스
                #렌치
                #마요네즈
                #칠리
                #스위트칠리
                #홀리그레인
                #홀래디쉬
                #올리브
                #후추
                #소금

class Source_recipe :
    def __init__(self, powder=None) :
        self.powder = powder

    def select_powder(self) :
        self.powder = input("첨가 재료를 골라주세요: ")
        print(f"{self.powder} 골랐습니다.")

        source = ["렌치", "마요네즈", "스위트칠리", "홀리그레인", "홀래디쉬", "올리브", "후추", "소금"]

        if self.powder in source :
            print(f"{self.powder} 다음으로")
        else : 
            print(f"{self.powder} 다시 골라주세요.")

source_pick = Source_recipe()
source_pick.select_powder()

# * -------------------------------------------------
#샐러드 종류 이건 기본으로 재료 조합이 되어 있는 것
        #샐러드
            #스테이크머쉬룸샐러드
            #쉬림프아보카도샐러드
            #로티세리치킨샐러드
            #타코샐러드
            #폴트포크샐러드
            #에그마요샐러드
            #참치아보카도샐러드
            #그린샐러드
            #미니치킨샐러드


class Salad:
    def __init__(self, salad=None):
        self.salad = salad
        self.price = 0

    def select_salad(self):
        self.salad = input("샐러드를 골라주세요: ")
        print(f"'{self.salad}'(을)를 골랐습니다.")

        # 샐러드 메뉴 목록 (이름과 가격)
        salad_menu = [
            {"이름": "스테이크머쉬룸샐러드", "가격": 14000},
            {"이름": "쉬림프아보카도샐러드", "가격": 10000},
            {"이름": "로티세리치킨샐러드", "가격": 10000},
            {"이름": "타코샐러드", "가격": 15000},
            {"이름": "폴드포크샐러드", "가격": 10000},
            {"이름": "에그마요샐러드", "가격": 10000},
            {"이름": "참치아보카도샐러드", "가격": 11000},
            {"이름": "그린샐러드", "가격": 8000},
            {"이름": "미니치킨샐러드", "가격": 9000},
            {"이름": "선택안함", "가격": 0},
        ]

        # 메뉴를 찾았는지 확인할 스위치(기깃값)
        found = False

        # 샐러드 목록을 하나씩 확인합니다.
        for item in salad_menu:
            # 사용자가 입력한 이름과 메뉴의 '이름'이 같은지 비교
            if self.salad == item["이름"]:
                self.price = item["가격"]
                found = True
                break  # 메뉴를 찾았으니 반복문을 종료합니다.

        # 판단 결과 출력
        if found:
            print(f"[{self.salad}] 가격은 {self.price:,}원입니다.")
            print("준비하겠습니다. 잠시만 기다려 주세요.\n")
        else:
            print(f"[{self.salad}]는 목록에 없는 메뉴입니다. 다시 골라주세요.\n")


salad_pick = Salad()
salad_pick.select_salad()

# * ----------------------------------------------------------

#간편식으로 먹을 수 있는 것
        #랩
            #쉬림프에그마요랩
            #치킨베이컨미니랩
            #스테이크치즈아보카도랩

class Lap:
    def __init__(self, lap=None):
        self.lap = lap
        self.price = 0

    def select_lap(self):
        self.lap = input("랩을 골라주세요: ")
        print(f"'{self.lap}'(을)를 골랐습니다.")

        # 샐러드 메뉴 목록 (이름과 가격)
        lap_menu = [
            {"이름": "쉬림프에그마요랩", "가격": 3900},
            {"이름": "치킨베이컨미니랩", "가격": 3900},
            {"이름": "스테이크치즈아보카도랩", "가격": 3900},
        ]

        found = False

        for item in lap_menu:
            if self.lap == item["이름"]:
                self.price = item["가격"]
                found = True
                break

        # 판단 결과 출력
        if found:
            print(f"[{self.lap}] 가격은 {self.price:,}원입니다.")
            print("준비하겠습니다. 잠시만 기다려 주세요.\n")
        else:
            print(f"[{self.lap}]는 목록에 없는 메뉴입니다. 다시 골라주세요.\n")


lap_pick = Lap()
lap_pick.select_lap()

# * ----------------------------------------------------------
        #수프 #수프종류
        #오늘의수프 #오늘의 수프는 매일 랜덤
        #양송이수프
        #브로콜리수프
        #어니언수프
        #포테이토수프

class Soup : 
        def __init__(self, soup=None):
            self.soup = soup
            self.price = 0

        def select_soup(self):
            self.soup = input("랩을 골라주세요: ")
            print(f"'{self.soup}'(을)를 골랐습니다.")

        # 샐러드 메뉴 목록 (이름과 가격)
        soup_menu = [
            {"이름": "쉬림프에그마요랩", "가격": 3900},
            {"이름": "치킨베이컨미니랩", "가격": 3900},
            {"이름": "스테이크치즈아보카도랩", "가격": 3900},
        ]

        found = False

        for item in soup_menu:
            if self.soup == item["이름"]:
                self.price = item["가격"]
                found = True
                break

        # 판단 결과 출력
        if found:
            print(f"[{self.soup}] 가격은 {self.price:,}원입니다.")
            print("준비하겠습니다. 잠시만 기다려 주세요.\n")
        else:
            print(f"[{self.soup}]는 목록에 없는 메뉴입니다. 다시 골라주세요.\n")


soup_pick = Soup()
soup_pick.select_soup()