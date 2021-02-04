import tkinter as tk


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def btnClearDisplay():
    global operator
    operator = ''
    text_input.set('')


def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    operator = ''


cal = tk.Tk()
cal.title('Calculator')
operator = ''
text_input = tk.StringVar()

txtDisplay = tk.Entry(cal, font=('arial', 20, 'bold'),
                      textvariable=text_input, bd=30, insertwidth=4,
                      bg='powder blue', justify='right').grid(columnspan=4)

btn7 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                 fg='black', text='7', command=lambda: btnClick(7),
                 bg='powder blue').grid(row=1, column=0)

btn8 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                 fg='black', text='8', command=lambda: btnClick(8),
                 bg='powder blue').grid(row=1, column=1)

btn9 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                 fg='black', text='9', command=lambda: btnClick(9),
                 bg='powder blue').grid(row=1, column=2)

addition = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                     fg='black', text='+', command=lambda: btnClick('+'),
                     bg='powder blue').grid(row=1, column=3)


btn4 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(4),
                 text='4', bg='powder blue').grid(row=2, column=0)

btn5 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(5),
                 text='5', bg='powder blue').grid(row=2, column=1)

btn6 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(6),
                 text='6', bg='powder blue').grid(row=2, column=2)

subtraction = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                        bd=8, fg='black', text='-',
                        command=lambda: btnClick('-'),
                        bg='powder blue').grid(row=2, column=3)


btn1 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(1),
                 text='1', bg='powder blue').grid(row=3, column=0)

btn2 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(2),
                 text='2', bg='powder blue').grid(row=3, column=1)

btn3 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(3),
                 text='3', bg='powder blue').grid(row=3, column=2)

multiplication = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                           bd=8, fg='black', command=lambda: btnClick('*'),
                           text='*', bg='powder blue').grid(row=3, column=3)


btn0 = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16,
                 bd=8, fg='black', command=lambda: btnClick(0),
                 text='0', bg='powder blue').grid(row=4, column=0)

btnClear = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                     fg='black', command=btnClearDisplay,
                     text='C', bg='powder blue').grid(row=4, column=1)

btnEquals = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                      fg='black', command=btnEqualsInput,
                      text='=', bg='powder blue').grid(row=4, column=2)

division = tk.Button(cal, font=('arial', 20, 'bold'), padx=16, pady=16, bd=8,
                     fg='black', command=lambda: btnClick('/'),
                     text='/', bg='powder blue').grid(row=4, column=3)


cal.mainloop()
