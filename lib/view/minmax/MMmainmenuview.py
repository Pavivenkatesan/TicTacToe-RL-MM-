from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.core.audio import SoundLoader
from lib.view.minmax.MMsingleplayerview import MMSinglePlayerView
from lib.view.minmax.MMbotplayerview import MMBotPlayerView


class MMMainMenuView(Screen):
    soundClick = SoundLoader.load("assets/menu_selection_click.ogg")
    _isOver = False

    def btnMMHumanPlayer_release(self):
        humanGame = MMSinglePlayerView()
        humanGame.restart_game()
        self.manager.current = "mm-singleplayer-gameplay"

    def btnMMBotPlayer_release(self):
        botGame = MMBotPlayerView()
        botGame.restart_game()
        self.manager.current = "mm-botplayer-gameplay"

    def btnMMExit_release(self):
        App.get_running_app().stop()
