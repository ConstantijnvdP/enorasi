import json
from dataclasses import dataclass
import PySimpleGUI as sg

enorasi_gk = u"\u03B5\u03BD\u03CC\u03C1\u03B1\u03C3\u03B7" ## ενόραση

## Utility functions
def load_character(file_path):
    with open(file_path, "r") as f:
        char_data = json.load(f)

    return Character(**char_data)


@dataclass
class Character:
    name: str
    hp_max: int
    ac: int
    initiative: int
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
    def __init__(self, char_path):
        self.char = load_character(char_path)
        self.hp_current = self.char.hp_max


    def get_layout(self):
        return [
            [sg.Text(self.char.name)],
            [
                sg.Text(f"HP  {self.hp_current}/{self.char.hp_max}", key=f"{self.char.name}-HP"),
                sg.ProgressBar(self.char.hp_max, orientation='h', size=(20,20), key=f"{self.char.name}-HPBar"),
                sg.Input(key=f"{self.char.name}-DMG", enable_events=True)
            ],
            [sg.Image(self.char.path_to_img, key=f"{self.char.name}-PROFILE")]
        ]

    
    def set_window(self, window):
        self._window = window


    def update_hp(self, damage):
        assert type(damage) is int, "Can only update HP with int!"
        self.hp_current += damage
        
        if self.hp_current > self.char.hp_max:
            self.hp_current = self.char.hp_max

        if self.hp_current < 0:
            self.hp_current = 0

        self._window[f"{self.char.name}-HPBar"].UpdateBar(self.hp_current)
        self._window[f"{self.char.name}-HP"].update(f"HP  {self.hp_current}/{self.char.hp_max}")


    def update_gif(self):
        self._window.Element(f"{self.char.name}-PROFILE").UpdateAnimation(self.char.path_to_img, time_between_frames=50)
