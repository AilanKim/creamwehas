#여기로 실행하는거 옮기기
import tkinter as tk  # [내장 모듈] 파이썬 기본 내장 GUI 라이브러리
import sys  # [내장 모듈] 파이썬 프로세스 제어 모듈
from quiz import quiz
from hello import QuizGame

# 1. Tkinter 기본 창 생성 (초기화)
# tk.Tk()는 화면에 띄울 메인 창(Window) 객체를 만듭니다.
root = tk.Tk()
root.title("대사, 제목을 맞춰보세요.") #게임제목
root.geometry("700x600") #사이즈 설정하는 것으로 수정 금지

game = QuizGame(root) #실행하는거 끌고 오기

root.mainloop() #실행