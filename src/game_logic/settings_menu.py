import pygame
import pygameMenu
from game_logic import helper


class SettingsMenu(object):

    def __init__(self, screen):
        # Settings menu
        self.__settings_menu = pygameMenu.Menu(
            screen,
            bgfun=lambda: screen.fill(helper.WHITE),
            color_selected=helper.BLACK,
            font=pygameMenu.font.FONT_HELVETICA,
            font_color=helper.BLACK,
            font_size=15,
            font_size_title=35,
            menu_alpha=100,
            menu_color=helper.WHITE,
            menu_height=int(helper.HEIGHT * 0.85),
            menu_width=int(helper.WIDTH * 0.9),
            # onclose=pygameMenu.events.DISABLE_CLOSE,
            title='Settings',
            widget_alignment=pygameMenu.locals.ALIGN_LEFT,
            window_height=helper.HEIGHT,
            window_width=helper.WIDTH
        )

        self.__trials_widg = self.__settings_menu.add_text_input(
            'Trials: ',
            default=1000,
            maxchar=6,
            textinput_id='trials',
            input_type=pygameMenu.locals.INPUT_INT,
            enable_selection=False)

        # Create selector with 3 difficulty options
        self.__opponent_widg = self.__settings_menu.add_selector(
            'Select opponent: ',
            [('Computer', 'COMPUTER'),
             ('Human', 'HUMAN')],
            selector_id='opponent',
            default=0)

        # Create selector with 3 difficulty options
        self.__player_widg = self.__settings_menu.add_selector(
            'Choose Player:',
            [('O', 'O'),
             ('X', 'X')],
            selector_id='player',
            default=0)

        self.__settings_menu.add_option(
            'Back', pygameMenu.events.CLOSE,
            align=pygameMenu.locals.ALIGN_CENTER)

    def __call__(self):
        # Loop until back button is pressed
        self.__settings_menu.mainloop(disable_loop=False)
        # print('Settings data:')
        # data = self.__settings_menu.get_input_data()
        # for k in data.keys():
        #     print(u'\t{0}\t=>\t{1}'.format(k, data[k]))
        return self.__settings_menu.get_input_data()

    def load_settings(self, settings):
        self.__trials_widg.set_value(settings.trials)
        self.__opponent_widg.set_value(settings.opponent)
        self.__player_widg.set_value(settings.player)
