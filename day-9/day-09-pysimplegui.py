# Part 1 - Import PySimpleGui
import PySimpleGUI as sg

# Part 2 - A window layout
layout = [[sg.Text("What's your name?")],
          [sg.Input()],
          [sg.Button('Ok')]]

# Part 3 - Create a window
window = sg.Window('The Name App!', layout)

# Part 4 - Interact with the window
event, values = window.read()

# Part 5 - Do something, with info entered on the window
print('Hello', values[0], '!Thanks for trying PySimpleGUI with pip!')

# Part 6 - Close the window
window.close()