import tkinter as tk  # [내장 모듈] 파이썬 기본 내장 GUI 라이브러리
import sys  # [내장 모듈] 파이썬 프로세스 제어 모듈
from quiz import quiz

# 2. 함수 기본 틀
def say_hello():
    print("안녕하세요! 좋은 하루 되세요💜💜")

game = {
    "name" : "맞추기게임",
    "점수" : 0,
    "greeting" : say_hello, # 기존 함수를 키의 값으로 지정
}
# [객체/딕셔너리 안에 함수 넣기]
# 키(Key)의 값(Value)으로 함수 자체를 넣어서 관리할 수 있습니다.

# * ---------------------------------------------------

#클래스화 하기 전 가져 올 거 미리 위에 세팅

class QuizGame :
    #방문에 대한 라벨
    def __init__(self, root) :
        self.root = root

        #점수 매기고 계산하는 부분
        self.current = 0
        self.score = 0
        self.hint_used = False

        self.hi = tk.Label(root, 
            text="안녕하세요.\n 방문해 주셔서 감사합니다.🙇🏻‍♀️🙇🏻‍♀️", 
            font=("맑은 고딕", 12))
        self.hi.pack(pady=20)

        #설명에 대한 라벨
        self.explain = tk.Label(root, 
            text="아래에 랜덤으로 문제가 나옵니다.\n"
            "글을 읽고 그에 맞는 대사나 제목을 밑에 입력창에 쓰시면 됩니다. 화이팅!!🔥🔥\n"
            "점수 계산은 정답은 +10, 땡 -10, 힌트보기 -5 차감 됩니다."
            ,font=("맑은 고딕", 12))
        self.explain.pack(pady=10)

        #시작하는 부분
        self.start = tk.Label(root, 
            text="도전하기", font=("맑은 고딕", 15))
        self.start.pack(pady=5)

        #질문
        self.first = tk.Label(root, 
            text=quiz[self.current]["question"], 
            font=("맑은 고딕", 15))
        self.first.pack(pady=10)

        #입력
        self.answer = tk.Entry(root, font=("궁서체", 20))
        self.answer.pack(pady=10)

        #프레임작업
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        #정답결과
        self.result = tk.Label(root, text="", font=("맑은 고딕", 15))
        self.result.pack(pady=10)

        #힌트 나오는 라벨
        self.hint = tk.Label(root, text="", font=("맑은 고딕", 15))
        self.hint.pack(pady=10)

        #힌트보기버튼
        self.hint_button = tk.Button(self.button_frame, text="힌트보기", font=("맑은 고딕", 15), command=self.hint_text)
        self.hint_button.pack(side="left", pady=10)

        self.pass_button = tk.Button(self.button_frame, text="PASS", font = ("궁서체", 18), command=self.next_question)
        self.pass_button.pack(side="left", pady=10)

        self.clear_button = tk.Button(self.button_frame, text="지우기",
                font=("맑은 고딕", 15), command=self.clear) #지우는거 넣기
        self.clear_button.pack(side="left", pady=10)

        self.answer.bind("<Return>", self.enter_text) #Enter누르면 넘어가게 하기

# * ------------------------------------------------

#게임 진행
    def enter_text(self, event) :

        text = self.answer.get().strip() #입력창의 글자를 땡겨와서 검사 하는 것.
        print(text) #답 입력 값 출력
        print(quiz[self.current]["answer"]) #여기에 다음 답 넘어가는 걸 입력
    
        if text == quiz[self.current]["answer"]: #다음 답이 계속 되도록 돌리기
            self.result.config(text = "⭕정답!⭕") #정답표시
            self.score += 10
            print(f"총 점수 : {self.score}")

            self.root.after(2000, self.next_question)

        else : 
            self.result.config(text = "❌땡!❌")
            self.score -= 10
            print(f"총 점수 : {self.score}")

    def hint_text(self) :

        if not self.hint_used : #힌트 누르면 깍이게 되는 장치
            self.score -= 5
            self.hint_used = True
            self.hint.config(text=quiz[self.current]["Hint"])

# * --------------------------------------------------------

    def next_question(self) : #점수 메기고 넘어가는 진행 부분
        print("next_question 실행") #안내

        if self.current < len(quiz) -1 : #총 문제에서
            self.current += 1 #다음 문제로 넘어갈 수 있게 하기
            self.hint_used = False #다음문제에서도 힌트 쓰면 점수 깍기.
            print("현제 문제 번호:", self.current)
            print(len(quiz))

            self.first.config(text=quiz[self.current]["question"])
            self.result.config(text="")#지우기
            self.hint.config(text="") #여기에 힌트도 볼 수 있게 집어 넣기
            self.answer.delete(0, tk.END) #입력 후 바로 다 지워지게 한다.
            self.answer.focus_set() #커서 다시 입력창으로 가기

        else :
            self.total_score = len(quiz) * 10 #이렇게 수식해놓으면 퀴즈마다 점수가 총 자동계산.
            print(self.total_score)
            self.result.config(text= f"🎉게임종료!\n 최종점수 : {self.score}/{self.total_score}점")

    def clear(self):
        self.answer.delete(0, tk.END) #입력하고 나면 싹 지우기

#여기서는 지금 실행이 안된다. root mainloop는 main파일로 이동