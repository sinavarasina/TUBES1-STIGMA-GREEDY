from game import models
from typing import Tuple
import random


class GreedyMovement:
    def move_towards(
        self, current: models.Position, target: models.Position, board: models.Board
    ) -> Tuple[int, int]:
        dx = target.x - current.x
        dy = target.y - current.y

        primary_move = (
            (1 if dx > 0 else -1, 0) if abs(dx) > abs(dy) else (0, 1 if dy > 0 else -1)
        )
        if board.is_valid_move(current, *primary_move):
            return primary_move

        secondary_move = (
            (0, 1 if dy > 0 else -1) if abs(dx) > abs(dy) else (1 if dx > 0 else -1, 0)
        )
        if board.is_valid_move(current, *secondary_move):
            return secondary_move

        return self.get_random_move(current, board)

    def get_random_move(
        self, current: models.Position, board: models.Board
    ) -> Tuple[int, int]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(moves)
        for move in moves:
            if board.is_valid_move(current, *move):
                return move
        return (0, 0)
