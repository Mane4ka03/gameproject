import unittest
import game
import mock


class MyTestCase(unittest.TestCase):
        @mock.patch('game.birdr')
        @mock.patch('game.can_score')
        def test_check(self, birdr, can_score):
            can_score = False
            birdr = game.birdr
            birdr.center =(600,100)
            tubes = [game.tubesu.get_rect(midtop=(600, 100))]
            self.assertFalse(game.check(tubes))
            self.assertTrue(game.can_score)

        def test_check2(self):
            self.assertEqual(game.new_score(0,1),1)
            self.assertEqual(game.new_score(1, 0), 1)
            self.assertEqual(game.new_score(2,0),2)
            self.assertEqual(game.new_score(0,5),5)

if __name__ == '__main__':
    unittest.main()
