from tkinter import *
import openai

window = Tk()
window.geometry('550x550')
window.title('ChatBot')

frame = Frame(window)
frame1 = Frame(window)
frame2 = Frame(frame)

enter = Text(frame)

entry = Entry(frame1,width = 50)

ybar = Scrollbar(frame,background = 'grey')
xbar = Scrollbar(frame)

openai.api_key = ''

def api():
    enter1 = entry.get()
    user_input = enter.insert(END, f"User: {enter1}"),
    i = [
        {'role':'user','content': enter1}
    ]
    x = openai.ChatCompletion.create(model = "gpt-3.5-turbo",messages = i)
    j = x["choices"][0]["message"]["content"]
    new_line = '\n'
    Content = enter.insert(END,f"{new_line}OUTPUT: {j}")
    return Content


enter_button = Button(frame1,text = 'Enter',command = api)
    
ybar.pack(side = RIGHT,fill = BOTH)
enter.pack(expand = True,fill = BOTH)
enter.config(yscrollcommand = ybar.set)
ybar.config(command = enter.yview())
enter.config(xscrollcommand = xbar.set)
xbar.config(command = enter.xview())
frame.pack(expand = True,fill = BOTH)
frame1.pack(side = BOTTOM)
entry.pack(side = LEFT)
entry.focus()
enter_button.pack(side = RIGHT)
frame.lift()




window.mainloop()
