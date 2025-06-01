from game.logic.base import BaseLogic
from game import models
from typing import Optional, Tuple
from game.logic.NazarickSublogic.nazarick_movement import GreedyMovement
from game.logic.NazarickSublogic.nazarick_targeting import GreedyTargeting


class NazarickNPC(BaseLogic):
    def __init__(self):
        self.movement = GreedyMovement()
        self.targeting = GreedyTargeting()
        self.last_position: Optional[models.Position] = None
        self.stuck_counter: int = 0

    def next_move(
        self, board_bot: models.GameObject, board: models.Board
    ) -> Tuple[int, int]:
        current_pos = board_bot.position

        if self.last_position and self._positions_equal(
            self.last_position, current_pos
        ):
            self.stuck_counter += 1
        else:
            self.stuck_counter = 0
        self.last_position = models.Position(x=current_pos.x, y=current_pos.y)

        if self.stuck_counter >= 3:
            return self.movement.get_random_move(current_pos, board)

        target_pos = self.targeting.find_target(board_bot, board)
        return self.movement.move_towards(current_pos, target_pos, board)

    def _positions_equal(self, a: models.Position, b: models.Position) -> bool:
        return a.x == b.x and a.y == b.y
