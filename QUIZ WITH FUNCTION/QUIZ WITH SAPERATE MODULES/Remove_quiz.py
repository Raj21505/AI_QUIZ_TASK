from Continue_quiz import *
from Json_quiz import *
from Read_quiz import show

def remove():
    show()
    print("\nConsider the above list and Enter the number that you want to delete")
    while True:
        del_que = int(input("Enter the number: "))
        if 1 <= del_que <= len(Quetions):
            del Quetions[del_que - 1]
            save_questions()
            print("Question removed")
            cont("remove")
            break
        else:
            print("Enter valid number")