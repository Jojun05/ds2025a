import random #랜덤 숫자 생성하기 위한 random

answer = random.randint(1, 100) #answer(정답) 1부터 100사이
win = False #초기값을 false로 설정해 사용자가 정답을 맞췄는지 확인하기 위한 변수임

for guesses in range(7): #7번 돌아가게 만들기
    print(f"{10-guesses}번의 기회가 남았습니다. 숫자 입력 : ", end='') # 남은 기회 출력
    guess = int(input()) #숫자를 입력하고 이걸 정수로 바꿔 저장 

    if answer == guess: #만약 정답이 같다면 true하고 break
        print("정답입니다!")
        win = True
        break
        
    elif answer > guess: #f랜덤한 값이 작다 입력값보다
        print("입력하신 수는 정답보다 작은 수 입니다. LOW")
    else: #그것도 아니면 입력값이 랜덤값이 크다
        print("입력하신 수는 정답보다 큰 수 입니다. HIGH")

if win: #정답을 맞추면 win
    print("You win!")
else: #아니면 lose
    print(f"You lose. The answer is {answer}.")
