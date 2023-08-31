from tkinter import *
import math
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background='white')
root.resizable(width=False, height=False)
root.geometry("480x568+450+90")
calc = Frame(root)
calc.grid()


class Calc:
    def __init__(self):
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    def numberEnter(self, num):
        self.result = False
        firstNum = txtDisplay.get()
        secondNum = str(num)
        if self.input_value:
            self.current = secondNum
            self.input_value = False
        else:
            if secondNum == '.':
                if secondNum in firstNum:
                    return
            self.current = firstNum + secondNum
        self.display(self.current)

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    def clear_entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    def all_clear_entry(self):
        self.clear_entry()
        self.total = 0

    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def tanh(self):
        self.result = False
        self.current = math.tanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def exp(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    def expm1(self):
        self.result = False
        self.current = math.expm1(float(txtDisplay.get()))
        self.display(self.current)

    def lgamma(self):
        self.result = False
        self.current = math.lgamma(float(txtDisplay.get()))
        self.display(self.current)

    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    def log2(self):
        self.result = False
        self.current = math.log2(float(txtDisplay.get()))
        self.display(self.current)

    def log10(self):
        self.result = False
        self.current = math.log10(float(txtDisplay.get()))
        self.display(self.current)

    def log1p(self):
        self.result = False
        self.current = math.log1p(float(txtDisplay.get()))
        self.display(self.current)


added_value = Calc()
txtDisplay = Entry(calc, font=('Helvetica', 20, 'bold'), bg='black', fg='white', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4, pady=1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='black', fg='white', font=('Helvetica', 20, 'bold'), bd=4,
                          text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpad[i]: added_value.numberEnter(x)
        i += 1


def button_generator(txt, comd, bg="powder blue", fg="black"):
    return Button(calc, text=txt, width=6, height=2, bg=bg, fg=fg, font=('Helvetica', 20, 'bold'), bd=4,
                  command=comd)


button_generator(chr(67), added_value.clear_entry).grid(row=1, column=0, pady=1)
button_generator(chr(67)+chr(69), added_value.all_clear_entry).grid(row=1, column=1, pady=1)
button_generator("\u221A", added_value.squared).grid(row=1, column=2, pady=1)
button_generator("+", lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)
button_generator("-", lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)
button_generator("x", lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)
button_generator("/", lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)
button_generator(txt="0", bg="black", fg="white", comd=lambda: added_value.numberEnter(0)).grid(row=5, column=0, pady=1)
button_generator(".", lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)
button_generator(chr(177), added_value.mathPM).grid(row=5, column=2, pady=1)
button_generator("=", added_value.sum_of_total).grid(row=5, column=3, pady=1)
button_generator("pi", added_value.pi, "black", "white").grid(row=1, column=4, pady=1)
button_generator("cos", added_value.cos, "black", "white").grid(row=1, column=5, pady=1)
button_generator("tan", added_value.tan, "black", "white").grid(row=1, column=6, pady=1)
button_generator("sin", added_value.sin, "black", "white").grid(row=1, column=7, pady=1)
button_generator("2pi", added_value.tau, "black", "white").grid(row=2, column=4, pady=1)
button_generator("Cosh", added_value.cosh, "black", "white").grid(row=2, column=5, pady=1)
button_generator("tanh", added_value.tanh, "black", "white").grid(row=2, column=6, pady=1)
button_generator("sinh", added_value.sinh, "black", "white").grid(row=2, column=7, pady=1)
button_generator("log", added_value.log, "black", "white").grid(row=3, column=4, pady=1)
button_generator("exp", added_value.exp, "black", "white").grid(row=3, column=5, pady=1)
button_generator("Mod", lambda: added_value.operation("mod"), "black", "white").grid(row=3, column=6, pady=1)
button_generator("e", added_value.e, "black", "white").grid(row=3, column=7, pady=1)
button_generator("log10", added_value.log10, "black", "white").grid(row=4, column=4, pady=1)
button_generator("log1p", added_value.log1p, "black", "white").grid(row=4, column=5, pady=1)
button_generator("expm1", added_value.expm1, "black", "white").grid(row=4, column=6, pady=1)
button_generator("gamma", added_value.lgamma, "black", "white").grid(row=4, column=7, pady=1)
button_generator("log2", added_value.log2, "black", "white").grid(row=5, column=4, pady=1)
button_generator("deg", added_value.degrees, "black", "white").grid(row=5, column=5, pady=1)
button_generator("acosh", added_value.acosh, "black", "white").grid(row=5, column=6, pady=1)
button_generator("asinh", added_value.asinh, "black", "white").grid(row=5, column=7, pady=1)

Label(calc, text="Scientific Calculator", font=("Helvetica", 30, "bold"), bg="black", fg="white", justify=CENTER)\
    .grid(row=0, column=4, columnspan=4)

root.mainloop()
