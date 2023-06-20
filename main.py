# #
# def myfunc():
#     """
#     bu hisoblab beradi
    
#     """
#     num1 = int(input('son1>>> '))
#     num2 = int(input('son2>>> '))
#     amal = input('amal>>> ')
#     if amal == '+':
#         result = num1 + num2
#         return result 
        
#     elif amal == '-':
#         result = num1 - num2
#         return result 
#     elif amal == '*':
#         result = num1 * num2
#         return result 
#     elif amal == '/':
#         result = num1 / num2

        
#         return result

# books = []

# def addBooks(*args):
#     for i in args:
#         books.append(i)
    
        
# 91 145 33 15 zikirillo

# addBooks('salom', 'salom2')
# print(books)
import random 
while True:
    quiz = ['is 2 + 2 = 4?','is 2 + 2 = 5?']
    x = random.choice(quiz)
    
    quizInput = input(f"{x} your answer>>> ").lower()
    def myfunc():
        tugri = 'true'
        notugri = 'false'
        
        if x == 'is 2 + 2 = 4?' and quizInput == 'ha' or quizInput == 'true':
            return tugri
        elif x == 'is 2 + 2 = 5?' and quizInput == 'yuq' or quizInput == 'false':
            return tugri
        else:
            return notugri
    
    print(myfunc())
        
    

    
