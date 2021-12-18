import unittest
import game
import mock


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

        @mock.patch('game.birdr')
        @mock.patch('game.can_score')
        def test_check(self, birdr, can_score):
            can_score = False
            birdr = game.birdr
            birdr.center =(600,100)
            tubes = [game.tubesu.get_rect(midtop=(600, 100))]
            self.assertFalse(game.check(tubes))
            self.assertTrue(can_score)

if __name__ == '__main__':
    unittest.main()
