import random 
import os
import time


while True:

    # 난이도 선택
    while True:
        time.sleep(0.6)
        os.system("cls")
        print("="*30)
        print("1. EASY")
        print("2. NORM")
        print("3. HARD")
        print("="*30)
        level = int(input("난이도 선택 : "))

        if level == 1:
            mi = 1
            ma = 9
        elif level == 2:
            mi = 10
            ma = 99
        elif level == 3:
            mi = 100
            ma = 999
        else:
            print("난이도 입력 오류!")
            continue
        break
    time.sleep(0.6)
    os.system("cls")

    cnt = 0
    # 문제출제
    com = random.randint(mi,ma)

    # 게임하는곳
    while True:
        
        print(mi, ma)
        cnt += 1    
        user = int(input(f"{cnt} th GUESS .... "))
        
        
        # 최소최대 판단 및 세팅
        if mi <= user <= ma:
            if user > com:
                ma = user - 1
            elif com > user:
                mi = user + 1
        else:
            cnt += 1
            print("바보같이 입력해서 cnt + 1")



        # 채점
        if user > com:
            print("DOWN !")
        elif com > user:
            print("UP !")
        else:
            print("Correct !!")
            print(f"{cnt} 번만에 맞춤!!")
            break
    
    time.sleep(0.6)
    os.system("cls")
    while True:
        again = input("계속하시겠습니까? (y/n) ")
        if again == "y" or again == "n":
            break
        else:
            print("입력오류!!")
            time.sleep(0.6)
            os.system("cls")
    if again == "n":
        break
