from read_excel import read_excel
import random

dataset = input("file to be opened:")
sheet = input(f'sheet inside {dataset+".xlsx"} to be opened:')

dirt, max_q = read_excel(dataset+".xlsx", sheet)

q_num = input(f'There are {max_q} words, how many words you want to challenge? ')

score = 0
while(True):
    ran_int = random.randint(0,int(q_num)-1)
    print(ran_int)
    print(f'what is the hiragana of... {dirt[ran_int][0]}')
    answer = input('Answer: ')
    if answer == dirt[ran_int][1]:
        print("Correct!")
        score += 1
    else:
        print(f'Correct answer is {dirt[ran_int][1]}')

    # task to do:
    # 1. no repeat question
    # 2. program end when gone through all the questions.