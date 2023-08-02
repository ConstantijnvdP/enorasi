from dataclasses import dataclass
import PySimpleGUI as sg

import characters

enorasi_gk = u"\u03B5\u03BD\u03CC\u03C1\u03B1\u03C3\u03B7" ## ενόραση


## UI
def get_character_panes(party_json_path):
    return characters.load_party_panes(party_json_path)

def get_party_layout(char_pane_list):
    layout = [[char.get_layout()] for char in char_pane_list]
    layout += [[sg.Button("Damage")]]
    return layout


def run_gui(pane_list, read_timeout=50):
    dmg = {pane.char.name: 0 for pane in pane_list}

    while True:
        event, values = window.read(timeout=read_timeout)
        # End program if user closes window
        if event == sg.WIN_CLOSED:
            break

        ## Damage event will have key "{character name}-DMG"
        elif event[-4:] == "-DMG":
            dmg[event[:-4]] = values[event]

        for pane in pane_list:
            pane.update_gif()

        if event == "Damage":
            for pane in pane_list:
                pane.update_hp(dmg[pane.char.name])


if __name__ == "__main__":
    party_panes = get_character_panes("../data/party.json")[:2]
    layout = get_party_layout(party_panes)
    window = sg.Window(title=enorasi_gk, layout=layout)

    _ = window.read()
    for pane in party_panes:
        pane.set_window(window)

    run_gui(party_panes)
