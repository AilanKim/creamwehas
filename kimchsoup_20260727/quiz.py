#김치찌개를 퀴즈

question = {
    "김치찌개에서 제일 중요한 재료는?" : "김치",
    "돼재목살김치찌개에서 사용되는 돼지고기 부위는?" : "목살",
    "참치김치찌개에서 사용되는 참치는?" : "캔참치",
    "김치찌개에 정량보다 물을 많이 넣으면 싱겁다? 안싱겁다?" : "싱겁다"
}

#점수 셀 수 있게 초기화 시작
score = 0

#for in 문을 사용하여 정답, 틀린거 결정하기

for kimchi, choice in question.items() :
    answer = input(kimchi + ":")

    if answer == choice :
        print("정답!")
        score += 1

    else : 
        print("다시 생각해보세요!")

print(f"총 점수 :{score}/{len(question)}")