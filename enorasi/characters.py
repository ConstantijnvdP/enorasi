import random
import json
from dataclasses import dataclass
import PySimpleGUI as sg

enorasi_gk = u"\u03B5\u03BD\u03CC\u03C1\u03B1\u03C3\u03B7" ## ενόραση

## Utility functions
def load_party_panes(file_path):
    with open(file_path, "r") as f:
        party_data = json.load(f)

    return [CharacterPane(Character(**char_dict)) for char_dict in party_data]

def roll_initiative(character_list):
    queue = []
    for char in character_list:
        roll = random.randint(1, 20)
        init = roll + char.initiative
        queue.append((char.name, init, roll))

    random.shuffle(queue) ## Shuffle in case there are ties with initiative AND modifier
    queue.sort(key=lambda x: (x[1], x[1]-x[2]), reverse=True)

    return [f"{x[0]}    {x[2]}+{x[1]-x[2]}" for x in queue]


@dataclass
class Character:
    name: str
    hp_max: int
    ac: int
    initiative: int
    perception: int
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    path_to_img: str

    def get_ability_mod(self, ability_score):
        return (ability_score - 10) // 2


class CharacterPane:
    def __init__(self, character: Character):
        self.char = character
        self.hp_current = self.char.hp_max
        self.status = "Healthy"


    def get_layout(self):
        hp_row = [
            sg.Text(f"HP  {self.hp_current}/{self.char.hp_max}", key=f"{self.char.name}-HP"),
            sg.ProgressBar(self.char.hp_max, orientation='h', size=(20,20), key=f"{self.char.name}-HPBar"),
            sg.Input(key=f"{self.char.name}-DMG", enable_events=True, size=(8,8))
        ]

        return [
            [sg.Text(self.char.name)],
            [
                sg.Image(self.char.path_to_img, key=f"{self.char.name}-PROFILE", size=(50,50)),
                #sg.Column([hp_row, [sg.StatusBar(self.status, size=(8,8))]])
                hp_row
            ],
            #[sg.StatusBar(self.status, size=(8,2))]
        ]

    
    def set_window(self, window):
        self._window = window
        window[f"{self.char.name}-HPBar"].UpdateBar(self.hp_current)

    def update_hp(self, damage):
        try:
            ## Update current HP, but restrict to range [0, Max HP]
            self.hp_current = max(min(self.char.hp_max, self.hp_current + int(damage)), 0)
        except Exception:
            return ## If damage can't be converted to an int, do nothing
        self._window[f"{self.char.name}-HPBar"].UpdateBar(self.hp_current)
        self._window[f"{self.char.name}-HP"].update(f"HP  {self.hp_current}/{self.char.hp_max}")


    def update_gif(self):
        self._window.Element(f"{self.char.name}-PROFILE").UpdateAnimation(self.char.path_to_img, time_between_frames=50)
