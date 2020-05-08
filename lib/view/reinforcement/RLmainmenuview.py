from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from lib.view.reinforcement.RLsingleplayerview import RLSinglePlayerView
from lib.view.reinforcement.RLbotplayerview import RLBotPlayerView


class RLMainMenuView(Screen):
    soundClick = SoundLoader.load("assets/menu_selection_click.ogg")
    _isOver = False

    def btnRLHumanPlayer_release(self):
        humanGame = RLSinglePlayerView()
        humanGame.restart_game()
        self.manager.current = "rl-singleplayer-gameplay"

    def btnRLBotPlayer_release(self):
        botGame = RLBotPlayerView()
        botGame.restart_game()
        self.manager.current = "rl-botplayer-gameplay"

    def btnRLExit_release(self):
        App.get_running_app().stop()
