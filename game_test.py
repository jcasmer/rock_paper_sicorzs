import unittest
import game

class TestGameMethods(unittest.TestCase):
    test_game = game.Game()

    def test_validate_spock(self):
        test_bad_choice = 'spok'
        test_good_choice = 'spock'
        self.assertNotIn(self.test_game.validate_option(test_bad_choice),  ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])
        self.assertIn(self.test_game.validate_option(test_good_choice), ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])

    def test_validate_lagarto(self):
        test_bad_choice = 'lizard'
        test_good_choice = 'lagarto'
        self.assertNotIn(self.test_game.validate_option(test_bad_choice),  ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])
        self.assertIn(self.test_game.validate_option(test_good_choice), ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])

    def test_validate_tijeras(self):
        test_bad_choice = 'tijer'
        test_good_choice = 'tijeras'
        self.assertNotIn(self.test_game.validate_option(test_bad_choice),  ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])
        self.assertIn(self.test_game.validate_option(test_good_choice), ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])

    def test_validate_papel(self):
        test_bad_choice = 'pap'
        test_good_choice = 'papel'
        self.assertNotIn(self.test_game.validate_option(test_bad_choice),  ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])
        self.assertIn(self.test_game.validate_option(test_good_choice), ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])

    def test_validate_piedra(self):
        test_bad_choice = 'pied'
        test_good_choice = 'piedra'
        self.assertNotIn(self.test_game.validate_option(test_bad_choice),  ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])
        self.assertIn(self.test_game.validate_option(test_good_choice), ['piedra', 'papel', 'tijeras', 'lagarto', 'spock'])


    def test_winner_bad_choice(self):
        test_bad_choice_one = 'h'
        test_good_choice_two = 'lagarto'
        test_good_choice_one = 'piedra'
        test_bad_choice_two = 'lizad'
        self.assertFalse(self.test_game.get_winner(test_bad_choice_one, test_good_choice_two))
        self.assertFalse(self.test_game.get_winner(test_good_choice_one, test_bad_choice_two))
        self.assertFalse(self.test_game.get_winner(test_bad_choice_one, test_bad_choice_two))

    def test_empate(self):
        sizors = 'tijeras'
        rock = 'piedra'
        paper = 'papel'
        lizard = 'lagarto'
        spock = 'spock'
        self.assertTrue(self.test_game.get_winner(sizors, sizors))
        self.assertTrue(self.test_game.get_winner(rock, rock))
        self.assertTrue(self.test_game.get_winner(paper, paper))
        self.assertTrue(self.test_game.get_winner(lizard, lizard))
        self.assertTrue(self.test_game.get_winner(spock, spock))

    def test_winner(self):
        sizors = 'tijeras'
        rock = 'piedra'
        paper = 'papel'
        lizard = 'lagarto'
        spock = 'spock'
        # Gana jugador 1
        self.assertTrue(self.test_game.get_winner(sizors, paper))
        self.assertTrue(self.test_game.get_winner(sizors, lizard))
        self.assertTrue(self.test_game.get_winner(rock, lizard))
        self.assertTrue(self.test_game.get_winner(rock, sizors))
        self.assertTrue(self.test_game.get_winner(paper, rock))
        self.assertTrue(self.test_game.get_winner(paper, spock))
        self.assertTrue(self.test_game.get_winner(lizard, spock))
        self.assertTrue(self.test_game.get_winner(lizard, paper))
        self.assertTrue(self.test_game.get_winner(spock, rock))
        self.assertTrue(self.test_game.get_winner(spock, sizors))
        #Gana jugador 2
        self.assertTrue(self.test_game.get_winner(rock, paper))
        self.assertTrue(self.test_game.get_winner(spock, paper))
        self.assertTrue(self.test_game.get_winner(spock, lizard))
        self.assertTrue(self.test_game.get_winner(paper, lizard))
        self.assertTrue(self.test_game.get_winner(sizors, rock))
        self.assertTrue(self.test_game.get_winner(lizard, rock))
        self.assertTrue(self.test_game.get_winner(rock, spock))
        self.assertTrue(self.test_game.get_winner(sizors, spock))
        self.assertTrue(self.test_game.get_winner(paper, sizors))
        self.assertTrue(self.test_game.get_winner(lizard, sizors))

if __name__ == '__main__':
    unittest.main()

