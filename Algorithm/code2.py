from enum import Enum, auto
class Menu(Enum):
    coffe = auto()
    bob = auto()


print(Menu.bob, Menu.coffe)
