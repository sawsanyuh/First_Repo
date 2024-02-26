import unittest
from Snake_And_Apple import SnakeAndApple

class TestSnakeAndApple(unittest.TestCase):
    def setUp(self):
        self.game = SnakeAndApple()

    def test_initialize_board(self):
        self.game.initialize_board()
        self.assertEqual(len(self.game.canvas.find_all()), 22)

    def test_initialize_snake(self):
        self.game.initialize_snake()
        self.assertEqual(len(self.game.snake), 3)
        self.assertEqual(self.game.snake[0], (0, 0))
        self.assertEqual(self.game.snake[1], (1, 0))
        self.assertEqual(self.game.snake[2], (2, 0))

    def test_place_apple(self):
        self.game.initialize_board()
        self.game.place_apple()
        apple = self.game.canvas.find_withtag("apple")[0]
        self.assertNotEqual(apple, self.game.snake_objects[0])

    def test_display_snake(self):
        self.game.initialize_board()
        self.game.initialize_snake()
        self.game.display_snake()
        self.assertEqual(len(self.game.canvas.find_all()), 25)

    def test_update_snake(self):
        self.game.initialize_board()
        self.game.initialize_snake()
        self.game.update_snake("Right")
        self.assertEqual(self.game.snake[0], (0, 0))
        self.assertEqual(self.game.snake[1], (1, 0))
        self.assertEqual(self.game.snake[2], (2, 0))
        self.game.update_snake("Right")
        self.assertEqual(self.game.snake[0], (0, 0))
        self.assertEqual(self.game.snake[1], (1, 0))
        self.assertEqual(self.game.snake[2], (3, 0))

if __name__ == '__main__':
    unittest.main()
