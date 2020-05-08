from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from lib.view.minmax.MMmainmenuview import MMMainMenuView
from lib.view.reinforcement.RLmainmenuview import RLMainMenuView


class SelectionMenuView(Screen):
    soundClick = SoundLoader.load("assets/menu_selection_click.ogg")
    _isOver = False
    def reinforcement_release(self):
        reinforcementGame = RLMainMenuView()
        self.manager.current = "rl-mainmenu"

    def minmax_release(self):
        mmGame = MMMainMenuView()
        self.manager.current = "mm-mainmenu"