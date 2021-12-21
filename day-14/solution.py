# Import Module
from PySimpleGUI import *

# Program Greeting
user_name = popup_get_text("Please enter your name to proceed:")
popup("Hey " + user_name.upper() + ", welcome to Calculator GUI!")

# GUI Layout
layout = [[Txt('' * 10)],  # adds 10 spaces to skip a line to center the output
          [Text('', size=(17, 1), font=('Arial', 18), text_color='white', key='input')],
          [Txt('' * 10)],  # adds 10 spaces to skip a line to center the output
          [Button('Clear'), Button('<'), Button(''), Button('/')],
          [Button('7'), Button('8'), Button('9'), Button('*')],
          [Button('4'), Button('5'), Button('6'), Button('-')],
          [Button('1'), Button('2'), Button('3'), Button('+')],
          [Button('0'), Button('.'), Button(''), Button('=')],
          ]

# Window/From Section: Setup GUI and size buttons
form = Window('My Calculator GUI', default_button_element_size=(6, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)  # chooses the above layout

# Return Value
Return = ''

# Event Loop
while True:
    # Button Values
    button, value = form.Read()  # reads in the values from the form when a button is clicked

    # Check Selected Buttons
    if button == 'Clear':
        Return = ''
        form.FindElement('input').Update(Return)  # updates input key with return value
    elif button == '<':
        Return = Return[:-1]
        form.FindElement('input').Update(Return)
    elif len(Return) == 17:  # If return value is over 17 digits no action taken
        pass
    # Quit Program
    elif button == 'Quit' or button == None:
        break

    # Evaluates the return values in the expression to get an answer
    elif button == '=':
        Answer = eval(Return)
        Answer = str(round(float(Answer), 3))
        form.FindElement('input').Update(Answer)
        Return = Answer
    else:
        Return += button
        form.FindElement('input').Update(Return)