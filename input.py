from python.calculator.add import addition
from python.calculator.sub import subtraction
from python.calculator.mul import multiplication
from python.calculator.div import division

class optionsys:

    def addition(self):
        a = int(input("enter a first number:"))
        b = int(input("enter a second number:"))
        add_ = addition(a,b)
        result = add_.addi()
        print("Result is:",result)

    def subtraction(self):
        a = int(input("enter a first number:"))
        b = int(input("enter a second number"))
        sub_obj = subtraction(a,b)
        result = sub_obj.subt()
        print("Result is:",result)

    def multiplication(self):
        a = int(input("enter a first number:"))
        b = int(input("enter a second number:"))
        mul_obj = multiplication(a,b)
        result = mul_obj.multi()
        print("Result is:",result)

    def division(self):
        a = int(input("enter a first number:"))
        b = int(input("enter a sceond number:"))
        div_obj = division(a,b)
        result = div_obj.div()
        print("Result is:",result)

    def exit(self):
        exit()

    def validateoption(self,option):
        if option == 1:
            self.addition()
        elif option == 2:
            self.subtraction()
        elif option == 3:
            self.multiplication()
        elif option == 4:
            self.division()
        elif option == 5:
            self.exit()
        else:
            print("enter the validate option")

class calculator:

    choice = {1:"addition",2:"subtraction",3:"multiplication",4:"division",5:"exit"}
    optionsys = optionsys()
    @staticmethod
    def welcome():
        print("welcome to the calculator application!")
        for option in calculator.choice:
            print(option,".",calculator.choice[option],end = " ")
        print()
        choice_selc = int(input("enter your option:"))
        calculator.optionsys.validateoption(choice_selc)


calculator.welcome()



