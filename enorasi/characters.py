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
            [sg.ProgressBar(self.char.hp_max, orientation='h', size=(20,20), key=f"{self.char.name}-HP")],
            [sg.Image(self.char.path_to_img, key=f"{self.char.name}-PROFILE")]
        ]

    def update_gif(self, window):
        window.Element(f"{self.char.name}-PROFILE").UpdateAnimation(self.char.path_to_img, time_between_frames=50)
