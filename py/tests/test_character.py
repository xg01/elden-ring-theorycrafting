import unittest
from theorycraft.character import MainStats, DefensiveStats, OffensiveStats, Character

def test_character_creation(self):
    """ Testing instantiation of a Character class with static stat data. """
    # TODO: Property-based testing would be a good fit for these dataclasses
    main_stats = MainStats(10, 10, 10, 10, 10, 10, 10, 10),
    def_stats = DefensiveStats(10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10),
    off_stats= OffensiveStats(10, 10, 10, 10, 10, 10, 10, 10),

    # Instantiation of Character class using generated dataclasses
    mock_character = Character(main_stats, def_stats, off_stats)
    self.assertIsInstance(mock_character, Character, "Failed to properly instantiate a character class.")

if __name__ == '__main__':
    unittest.main()


