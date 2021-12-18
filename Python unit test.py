import unittest
import game
import mock
from game import score,high_score
from unittest.mock import  MagicMock

class MyTestCase(unittest.TestCase):
    @mock.patch('game.birdr')
    @mock.patch('game.can_score')
    def test_check(self,birdr,can_score):
        can_score = False
        birdr = game.birdr
        tubes = [game.create_tube()]
        game.check()
        self.assertTrue(can_score)


if __name__ == '__main__':
    unittest.main
