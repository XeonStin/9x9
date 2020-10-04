import random
import tkinter as tk

Width = 300
Height1 = 250
FontSize = 20
correctCount = 0
errorCount = 0
a = random.randint(0, 9)
b = random.randint(0, 9)

root = top = tk.Tk()
root.minsize(Width, Height1+400)
root.resizable(0, 0)
root.title('乘法练习')


stateVar = tk.StringVar(root, '正确：' + str(correctCount) + '    错误：' + str(errorCount))
stateLabel = tk.Label(root, textvariable=stateVar, font=("微软雅黑", FontSize))
stateLabel.place(x=0, y=0, width=Width, height=75)


problemVar = tk.StringVar(root, str(a) + ' 乘以 ' + str(b) + ' 等于：')
problemLabel = tk.Label(root, textvariable=problemVar, font=("微软雅黑", FontSize))
problemLabel.place(x=0, y=75, width=Width, height=75)


contentVar = tk.StringVar(root, '')
contentEntry = tk.Entry(root, textvariable=contentVar, state='readonly', font=("微软雅黑", FontSize))
contentEntry.place(x=0, y=Height1-100, width=Width, height=100)


def buttonClick(x):
    content = contentVar.get()
    problem = problemVar.get()
    state = stateVar.get()
    
    if content in ['正确', '错误']:
        content = ''

    if x in '0123456789':
        content = content + x
    elif x == '←':
        content = content[0: -1]
    elif x == '=':
        global a, b, correctCount, errorCount
        if content != '':
            if int(content) == a * b:        
                a = random.randint(0, 9)
                b = random.randint(0, 9)
                
                problem = str(a) + ' 乘以 ' + str(b) + ' 等于：'
                correctCount = correctCount + 1
                content = '正确'
            else:
                errorCount = errorCount + 1
                content = '错误'
            state = '正确：' + str(correctCount) + '    错误：' + str(errorCount)

    contentVar.set(content)
    problemVar.set(problem)
    stateVar.set(state)


numBtnList = []
numBtnList.append(tk.Button(root, text = '0', font=('微软雅黑', FontSize), fg=('#000000'), bd=0.5, command=lambda x='0': buttonClick(x)))
numBtnList[0].place(x=100, y=Height1+300, width=100, height=100)

for i in range(1, 10):
    numBtnList.append(tk.Button(root, text = str(i), font=('微软雅黑', FontSize), fg=('#000000'), bd=0.5, command=lambda x=str(i): buttonClick(x)))
    numBtnList[i].place(x=100*((i-1)%3), y=Height1+100*((i-1)//3), width=100, height=100)
    
deleteBtn = tk.Button(root, text = '删除', font=('微软雅黑', FontSize), fg=('#000000'), bd=0.5, command=lambda x='←': buttonClick(x))
deleteBtn.place(x=0, y=Height1+300, width=100, height=100)

enterBtn  = tk.Button(root, text = '确认', font=('微软雅黑', FontSize), fg=('#000000'), bd=0.5, command=lambda x='=': buttonClick(x))
enterBtn.place(x=200, y=Height1+300, width=100, height=100)


root.mainloop()