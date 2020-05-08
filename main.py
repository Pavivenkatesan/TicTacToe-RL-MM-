#!/usr/bin/env python3

import kivy
kivy.require("1.9.1")

from kivy.app import App
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import WipeTransition

from lib.view.reinforcement.RLmainmenuview import RLMainMenuView
from lib.view.minmax.MMmainmenuview import MMMainMenuView
from lib.view.selectionmenuview import SelectionMenuView
from lib.view.reinforcement.RLsingleplayerview import RLSinglePlayerView
from lib.view.reinforcement.RLbotplayerview import RLBotPlayerView
from lib.view.minmax.MMbotplayerview import MMBotPlayerView
from lib.view.minmax.MMsingleplayerview import MMSinglePlayerView


class TicTacToeApp(App):

	title = "Tic-Tac-Toe"
	icon = "assets/icon.ico"


	def init_screen(self):
		screenManager = ScreenManager(transition = WipeTransition())
		screenManager.add_widget(SelectionMenuView(name="selection"))
		screenManager.add_widget(RLMainMenuView(name = "rl-mainmenu"))
		screenManager.add_widget(MMMainMenuView(name="mm-mainmenu"))
		screenManager.add_widget(RLSinglePlayerView(name ="rl-singleplayer-gameplay"))
		screenManager.add_widget(RLBotPlayerView(name="rl-botplayer-gameplay"))
		screenManager.add_widget(MMSinglePlayerView(name="mm-singleplayer-gameplay"))
		screenManager.add_widget(MMBotPlayerView(name="mm-botplayer-gameplay"))

		return screenManager


	def init_config(self):
		Config.set("graphics", "fullscreen", 0)
		Config.set("graphics", "resizable", 0)
		Config.set("graphics", "height", 600)
		Config.set("graphics", "width", 600)
		Config.set("kivy", "exit_on_escape", 0)
		Config.set("input", "mouse", "mouse,multitouch_on_demand")
		Config.write()


	def build(self):
		self.init_config()
		return self.init_screen()


if __name__ == "__main__":
	TicTacToeApp().run()
