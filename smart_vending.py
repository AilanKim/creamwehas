
#김치찌개, 커피 자판기 구현
#가게이름 설정
#자판기 이름
# 위치
#관리자 연락처

# * --------------------------------------------------
#기본 가게 정보
store_name = {
    "store": {
        "machine_title": "대전 김치먹을래? 커피마실래?",
        "place": "대전광역시 신탄진동",
        "manager_contact": "010-1234-5678"
    },

# * -------------------------------------------------

#김치찌개 메뉴
    "menus": [
        {
            "code": "K1",
            "name": "참치김치찌개",
            "price": 11000,
            "count": 5,
            "group": "kimchi",
            "options": ["순한맛", "보통맛", "매운맛"]
        },
        {
            "code": "K2",
            "name": "돼지김치찌개",
            "price": 12000,
            "count": 10,
            "group": "kimchi",
            "options": ["순한맛", "보통맛", "매운맛"]
        },
        {
                    "code": "K3",
                    "name": "스팸김치찌개",
                    "price": 12000,
                    "count": 4,
                    "group": "kimchi",
                    "options": ["순한맛", "보통맛", "매운맛"]
                },
        {
                    "code": "K4",
                    "name": "파김치김치찌개",
                    "price": 13000,
                    "count": 4,
                    "group": "kimchi",
                    "options": ["순한맛", "보통맛", "매운맛"]
        },
        {
                            "code": "K5",
                            "name": "묵은지김치찌개",
                            "price": 13000,
                            "count": 8,
                            "group": "kimchi",
                            "options": ["순한맛", "보통맛", "매운맛"]
                },

#커피메뉴
        {
            "code": "C1",
            "label": "아메리카노",
            "price": 4500,
            "count": 30,
            "group": "coffee",
            "options": ["hot", "ice", "double shot"]
        },
        {
            "code": "C2",
            "label": "카페라떼",
            "price": 5500,
            "count": 20,
            "group": "coffee",
            "options": ["hot", "ice", "extra shot"]
        },
        {
            "code": "C3",
            "label": "바닐라라떼",
            "price": 6000,
            "count": 10,
            "group": "coffee",
            "options": ["hot", "ice", "extra shot"]
        },
        {
            "code": "C4",
            "label": "아이스티",
            "price": 5000,
            "count": 10,
            "group": "drink",
            "options": ["hot", "ice",]
        },
        {
            "code": "C5",
            "label": "카모마일티",
            "price": 5500,
            "count": 10,
            "group": "drink",
            "options": ["hot", "ice",]
        },
    ]
}

# * --------------------------------------------------

# 2. 메뉴 객체 클래스
class Kimch_coffee:
    def __init__(self, items):
        self.item_code = items.get("code")
        self.name = items.get("name") or items.get("label")
        self.price = items.get("price")
        self.stock = items.get("count")
        self.group = items.get("group")
        self.choice = items.get("options")

    def __repr__(self):
        return f"< Menu : {self.name} ({self.price}원) - 재고 : {self.stock}개 >"

# * --------------------------------------------------

# 3. 자판기 클래스 (기능들은 모두 이 안에 집어 넣기)
class Vending_kimchicoffee:
    def __init__(self, vending_name, place, admin_phone):
        self.name = vending_name
        self.location = place
        self.admin_phone = admin_phone
        self.box = {}
        self.cash = 0
        self.sales_history = []

    def pick_menus(self, config_date):
        menu_list = config_date.get("menus", [])
        for menus in menu_list:
            menu_object = Kimch_coffee(menus)
            self.box[menu_object.item_code] = menu_object

    def get_code(self, code):
        return self.box.get(code, "해당메뉴는 없습니다.")

#결제에 대한 부분
    def insert_cash(self, money):
        if money <= 0:
            print("금액을 투입해 주세요.")
            return

        self.cash += money
        print(f"{money}원이 투입되었습니다. (현재 잔액: {self.cash}원)")

    def order_menu(self, code):
        order_pick = self.box.get(code)

        # 메뉴가 있는지 없는지 확인
        if not order_pick:
            print("없는 메뉴 입니다.")
            return

        # 재고 확인 하기
        if order_pick.stock <= 0:
            print(f"[{order_pick.name}] 남은 재료가 부족합니다.")
            return

        # 남은 잔액 확인 하기
        if self.cash < order_pick.price:
            print(f"금액이 부족합니다. (현재잔액 : {self.cash}원 / 필요금액 : {order_pick.price}원)")
            return

        # 결제 처리 (계산 및 차감 동시에 이루어지기)
        self.cash -= order_pick.price
        order_pick.stock -= 1

        # 판매 기록 추가
        self.sales_history.append({
            "code": code,
            "name": order_pick.name,
            "price": order_pick.price
        })

        # 구매 완료 출력
        print(f"[{order_pick.name}] 구매완료! (남은 잔액: {self.cash}원, 남은 재고: {order_pick.stock}개)")

# * --------------------------------------------------

# 가게 정보 불러오기 & 자판기 객체 생성
store_info = store_name["store"]
vending_info = Vending_kimchicoffee(
    store_info["machine_title"],
    store_info["place"],
    store_info["manager_contact"]
)

# * --------------------------------------------------

# 메뉴 불러오는 작업 (자판기에 메뉴 등록)
vending_info.pick_menus(store_name)

# * --------------------------------------------------

# 메뉴 출력해보기
print("메뉴")
for code, item in vending_info.box.items():
    print(f"코드[{code}] : {item}")

print("결과")
print(vending_info.get_code("K1"))

print("구매해주셔서 감사합니다.")
vending_info.insert_cash(11000)   # 15,000원 투입
vending_info.order_menu("K1")     # 참치김치찌개(11,000원) 주문 -> 성공! (잔액 4,000원)
vending_info.order_menu("C1")     # 아메리카노(4,500원) 주문 -> 잔액 부족 메세지 출력!

# * ----------------------------------------------------------------------------

#5번 반복 구매 요청을 받아 실행
print("주문합니다.")
#출력에 나올 문구

#위에 남은 잔액이 있으면 여기에 합쳐저서 계산이 된다. 
vending_info.insert_cash(100000) #넉넉하게 현금을 넣고 시작

# 구매할 김치랑 커피를 리스트로 바꿔서 여기에 표기 하고
#for in문으로 끌어오기

target_menus = ["C1", "C3", "K1", "K4", "K5"]

for i, code in enumerate(target_menus, 1):
    print(f"[{i}번째 구매 시도]")
    vending_info.order_menu(code)

