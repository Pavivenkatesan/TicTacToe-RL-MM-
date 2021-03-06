from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from lib.game.tictactoegame import TicTacToeGame
from lib.game.player import Player
from lib.game.MMbot import MMBot


class MMBotPlayerView(Screen):
	dictIndexToButtonName = {
								1: "btn1",
								2: "btn2",
								3: "btn3",
								4: "btn4",
								5: "btn5",
								6: "btn6",
								7: "btn7",
								8: "btn8",
								9: "btn9"
							}

	soundClick = SoundLoader.load("assets/menu_selection_click.ogg")

	state_space = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

	game = TicTacToeGame()
	player = Player("Player", "X")
	enemy = MMBot("Computer", "O")

	game.add_player( [player, enemy] )

	enemy.start_first()
	game.start()

	def set_all_button_disable(self, isDisable):

		for index in range(1, len(self.dictIndexToButtonName) + 1):
			self.ids[ self.dictIndexToButtonName[index] ].disabled = isDisable


	def set_all_button_text(self, value):

		for index in range(1, len(self.dictIndexToButtonName) + 1):
			self.ids[ self.dictIndexToButtonName[index] ].text = value


	def restart_game(self):

		self.game = TicTacToeGame()
		self.player = Player("Player", "X")
		self.enemy = MMBot("Computer", "O")

		self.game.add_player([ self.player, self.enemy ])
		self.state_space = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		self.enemy.start_first()
		self.game.start()

		self.reset_button()


	def reset_button(self):
		self.set_all_button_text("")
		self.set_all_button_disable(False)


	def btnRestart_press(self, btn):
		self.restart_game()
		self.reset_button()
		self.state_space = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


	def btnMainMenu_press(self, btn):
		self.restart_game()
		self.manager.current = "selection"


	def btnMMGame_press(self, btn):
		print("In here-RLBot")
		if (self.soundClick):
			self.soundClick.play()

		if (not self.game.isOver):
			if (self.player.isTurn):
				selectedNum = 0
				totalButton = len(self.dictIndexToButtonName)

				for index in range(1, totalButton + 1):
					if (btn == self.ids[ self.dictIndexToButtonName[index] ]):
						selectedNum = index
						break

				self.player.pick(selectedNum)
				self.game.remove_choice(selectedNum)
				self.game.play(self.state_space, "X", selectedNum)
				print("Human placed at :" + str(selectedNum))

				btn.text = self.player.marking
				btn.disabled = True

				self.game.check_winner()

				if (self.game.isHasWinner or len(self.game.lstAvailableChoice) == 0):
					self.game.over()

				self.game.next_turn()

			if (self.enemy.isTurn):
				selectedNum = self.enemy.get_Predicted_Values(self.state_space)
				self.game.play(self.state_space, "O", selectedNum)
				print("AI placed at :" + str(selectedNum))

				if (selectedNum > 0):

					self.enemy.pick(selectedNum)
					self.game.remove_choice(selectedNum)

					self.ids[ self.dictIndexToButtonName[selectedNum] ].text = self.enemy.marking
					self.ids[ self.dictIndexToButtonName[selectedNum] ].disabled = True


				self.game.check_winner()


				if (self.game.isHasWinner or len(self.game.lstAvailableChoice) == 0):
					self.game.over()


				self.game.next_turn()


	def btnMMGame_release(self, btn):

		if (self.game.isOver):

			self.set_all_button_disable(True)

			boxLayout = BoxLayout(orientation = "vertical")

			dlgGameOver = Popup(title = "Game Over",
					size_hint = (None, None),
					size = (500, 400),
					auto_dismiss = False)


			lblWinner = Label(text = "")
			lblWinner.font_size = 24

			btnMainMenu = Button(text = "MainMenu")
			btnMainMenu.bind(on_press = self.btnMainMenu_press)
			btnMainMenu.bind(on_release = dlgGameOver.dismiss)


			if (self.player.isWin):
				lblWinner.text += "You won!"

			elif (self.enemy.isWin):
				lblWinner.text += "Yay!! I won"
			else:
				lblWinner.text = "Draw! You are tough to crack"


			boxLayout.add_widget(lblWinner)
			boxLayout.add_widget(btnMainMenu)

			dlgGameOver.content = boxLayout
			dlgGameOver.open()
