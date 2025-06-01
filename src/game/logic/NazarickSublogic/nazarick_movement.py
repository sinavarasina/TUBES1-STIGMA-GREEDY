from game import models
from typing import Tuple
import random


class GreedyMovement:
    def move_towards(
        self, current: models.Position, target: models.Position, board: models.Board
    ) -> Tuple[int, int]:
        dx = target.x - current.x
        dy = target.y - current.y

        primary_move = (0, 0)
        secondary_move = (0, 0)

        if abs(dx) > abs(dy):
            primary_move = (1 if dx > 0 else -1, 0)
            if dy != 0:
                secondary_move = (0, 1 if dy > 0 else -1)
        elif abs(dy) > abs(dx):
            primary_move = (0, 1 if dy > 0 else -1)
            if dx != 0:
                secondary_move = (1 if dx > 0 else -1, 0)
        elif dx != 0:
            primary_move = (1 if dx > 0 else -1, 0)
            secondary_move = (0, 1 if dy > 0 else -1)
        else:
            return (0, 0)

        if primary_move != (0, 0) and board.is_valid_move(current, *primary_move):
            return primary_move

        if secondary_move != (0, 0) and board.is_valid_move(current, *secondary_move):
            return secondary_move

        moves_fallback = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(moves_fallback)
        for move in moves_fallback:
            if move != primary_move and move != secondary_move:
                if board.is_valid_move(current, *move):
                    return move

        return (0, 0)

    def get_random_move(
        self, current: models.Position, board: models.Board
    ) -> Tuple[int, int]:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        random.shuffle(moves)
        for move in moves:
            if board.is_valid_move(current, *move):
                return move
        return (0, 0)
