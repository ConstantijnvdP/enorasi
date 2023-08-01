from dataclasses import dataclass
import PySimpleGUI as sg

import characters

enorasi_gk = u"\u03B5\u03BD\u03CC\u03C1\u03B1\u03C3\u03B7" ## ενόραση


## UI
#layout = [[sg.Text("DEMO")], [sg.Button("Close")]]
gaulius = characters.CharacterPane("../data/party.json")
layout = gaulius.get_layout()

window = sg.Window(title=enorasi_gk, layout=layout)

def run_gui():
    while True:
        event, values = window.read(timeout=50)
        # End program if user closes window or
        # presses the OK button
        if event == "Close" or event == sg.WIN_CLOSED:
            break

        gaulius.update_gif(window)


if __name__ == "__main__":
    run_gui()
