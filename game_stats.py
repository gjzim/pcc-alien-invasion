import json


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = self._get_high_score()

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def _get_high_score(self):
        """Get the stored high score from high_score.json file."""
        try :
            with open('high_score.json', 'r') as hs:
                high_score = json.load(hs)
        except:
            return 0
        else:
            return high_score

    def store_high_score(self, high_score):
        """Store the high score to the high_score.json file."""
        try :
            with open('high_score.json', 'w') as hs:
                json.dump(high_score, hs)

                return True
        except:
            return False