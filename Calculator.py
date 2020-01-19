#Made by Samin Qureshi on Jan 15th

import PySimpleGUI as sg

bw: dict = {'size':(7,2), 'font':("Comic Sans", 24), 'button_color':("black","#F8F8F8")}
bt: dict = {'size':(7,2), 'font':("Comic Sans", 24), 'button_color':("black","#F1EABC")}
bo: dict = {'size':(21,2), 'font':("Comic Sans", 24), 'button_color':("black","#ECA527"), 'focus':True}

layout: list = [
    [sg.Text('BOI CAN YOU EVEN MATH', size=(50,1), justification='right', background_color="#272533", 
        text_color='white', font=("Comic Sans", 14, 'bold'))],
    [sg.Text('0', size=(18,1), justification='right', background_color='black', text_color='red', 
        font=('Digital-7',48), relief='sunken', key="_DISPLAY_")],
    [sg.Button('C',**bt), sg.Button('CE',**bt), sg.Button('%',**bt), sg.Button("/",**bt)],
    [sg.Button('7',**bw), sg.Button('8',**bw), sg.Button('9',**bw), sg.Button("*",**bt)],
    [sg.Button('4',**bw), sg.Button('5',**bw), sg.Button('6',**bw), sg.Button("-",**bt)],
    [sg.Button('1',**bw), sg.Button('2',**bw), sg.Button('3',**bw), sg.Button("+",**bt)],    
    [sg.Button('0',**bw), sg.Button('=',**bo, bind_return_key=True)]
]

window: object = sg.Window('BOI CAN YOU EVEN MATH', layout=layout, background_color="#272533", size=(700, 800), return_keyboard_events=True)




def update_display(x):
    window['_DISPLAY_'].update(value='{:,.4f}'.format(x))
     
def main():
    total = ""
    while True:
        event, values = window.read()
        print(event)
        if event is None:
            break

        if event in ['0','1','2','3','4','5','6','7','8','9', '+', '-', '/', '*']:
            print("K")
            total += event
            if event not in ['+', '-', '/', '*']:
                update_display(int(event))

        elif event == "=":
            total = eval(total)
            update_display(total)

        elif event == "C":
            total = ""

        elif event == "CE":
            total = total.replace(total[-1:-3], "")
            print(total)

        print(total)

main()











    
