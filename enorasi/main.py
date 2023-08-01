from dataclasses import dataclass
import PySimpleGUI as sg

import characters

enorasi_gk = u"\u03B5\u03BD\u03CC\u03C1\u03B1\u03C3\u03B7" ## ενόραση


## UI
def run_gui():
    dmg = {}

    while True:
        event, values = window.read(timeout=50)
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break

        elif event == f"{gaulius.char.name}-DMG":
            try:
                dmg[f"{gaulius.char.name}"] = int(values[f"{gaulius.char.name}-DMG"])
            except:
                dmg[f"{gaulius.char.name}"] = 0

        elif event == "Damage":
            gaulius.update_hp(dmg[f"{gaulius.char.name}"])

        gaulius.update_gif()


if __name__ == "__main__":
    gaulius = characters.CharacterPane("../data/party.json")
    layout = gaulius.get_layout()
    layout += [[sg.Button("Damage")]]

    window = sg.Window(title=enorasi_gk, layout=layout)

    gaulius.set_window(window)

    run_gui()
