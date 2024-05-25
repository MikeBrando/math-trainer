import random
from tkinter import *

w = Tk()
w.geometry('600x300')

question = Label(w, text='')
question['font'] = 'Arial 24'
question.pack()

user = Entry(w, width=10)
user.pack()

result_label = Label(w, text='', font='Arial 16')
result_label.pack()

themes = ["Дроби", "Деление", "Умножение", "Проценты"]
subthemes = []

def questionC(quest):
    question.configure(text=quest)

def check_answer():
    answer_user = user.get()  # Получаем ответ пользователя из поля ввода
    if str(answer_user) == str(answer):
        result_label.configure(text='Правильно!', fg='green')
    else:
        result_label.configure(text=f'Неправильно, ответ: {answer}', fg='red')

def generate_question():
    global answer, question_text
    theme = random.choice(themes)
    
    if theme == "Дроби":
        number_l = random.randint(1, 15)
        number_h = random.randint(5, 40)
        subthemes = ["Вычитание", "Изображение"]
        subtheme = random.choice(subthemes)
        
        if subtheme == "Вычитание":
            drobi = []
            drobi.append(number_l)
            
            for i in range(3):
                number_h = random.randint(5, 40)
                drobi.append(number_h)
                
            if drobi[1] <= drobi[2]:
                drobi[1], drobi[2] = drobi[2], drobi[1]
                
            question_text = f'{drobi[0]}/{drobi[1]} - {drobi[0]}/{drobi[2]}'
            answer = drobi[1] - drobi[2]
            
        elif subtheme == "Изображение":
            tip = ''
            
            if number_h <= number_l:
                tip = 'неправильную'
            elif number_h > number_l:
                tip = 'правильную'
                
            picture = random.randint(5, 15)
            
            question_text = f'Изобразите число {picture} как {tip} дробь со знаменателем {number_l}'
            answer = str(picture * number_l) + '/' + str(number_l)
            
    elif theme == 'Умножение':
        first = random.randint(2, 10)
        second = random.randint(2, 10)
        
        question_text = f'{first} * {second} = '
        answer = first * second
        
    elif theme == 'Проценты':
        percent = random.randint(1, 99)
        numb = random.randint(50, 1000)
        
        question_text = f'Найдите {percent}% от {numb}'
        answer = numb * percent // 100
    
    questionC(question_text)  # Отображаем вопрос
    result_label.configure(text='')  # Очищаем результат проверки
    
generate_question()

submit_button = Button(w, text="Проверить ответ", command=check_answer)
submit_button.pack()

next_button = Button(w, text="Следующий вопрос", command=generate_question)
next_button.pack()

w.mainloop()
