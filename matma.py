import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QIcon,QPixmap
import random

class App(QWidget):


    def __init__(self):
        super().__init__()
        self.title='SORRRRYYY YOU ARE WRONG!!!'
        self.left= 70
        self.top= 80
        self.width= 640
        self.height= 602
        self.initUI()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)
        label=QLabel(self)
        pixmap=QPixmap('fota.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        self.show()


class Calculation():

    def add(self, a, b):
        result = a + b
        return result

    def substract(self, a, b):
        result = a - b
        return result

    def multiply(self, a, b):
        result = a * b
        return result

    def division(self, a, b):
        result = a / b
        return result


if __name__ == '__main__':

    while True:

        calc = Calculation()
        a = random.randint(0, 10)
        b = random.randint(0, 10)
        action_dict = {calc.add(a, b): "+",
                       calc.substract(a, b): "-",
         #             calc.multiply(a,b): "*",
         #             calc.division(a,b): "/"
                    }
        action = random.choice(list(action_dict))

        print('do you want to play? y= YES, n= NO')
        check = input()
        if check == "n":
            print('Game over')
            break

        elif check != "n" and check != "y":
            print('please, make a right decision')
        else:

            for i in range(3):

                result = action
                mark = action_dict[action]
                print(f" {a} {mark} {b} =")
                print("podaj wynik")
                man_result = int(input())
                if man_result == result:
                    print("goog job!")
                    break
                else:
                    print ('try again, you have 2 more chanches')
                    app = QApplication(sys.argv)
                    ex = App()
                    i += 1
