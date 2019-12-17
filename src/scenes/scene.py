# -*- encoding: utf-8 -*-


class Scene:
    """
    Represents an abstract scene of the game.
    A scene is a visible part of the game, like a loading screen
    or an option menu. For creating a working scene the object
    should be derived from this class.
    """

    def __init__(self, director):
        self.director = director

    def read_settings(self):
        """
        Reads and sets the settings of the current game instance
        """
        raise NotImplemented("read_settings method should be implemented.")

    def on_update(self):
        """
        Logic update called directly from the director.
        """
        raise NotImplemented("on_update method should be implemented.")

    def on_event(self, events):
        """
        Processes pygame events for the concrete scene
        """
        raise NotImplemented("on_event method should be implemented.")

    def on_draw(self, screen):
        """
        Called when something is to be drawn on the screen.
        """
        raise NotImplemented("on_draw method should be implemented.")
