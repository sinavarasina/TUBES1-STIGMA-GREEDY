from game import models
from typing import Optional


class GreedyTargeting:
    def find_target(
        self, board_bot: models.GameObject, board: models.Board
    ) -> models.Position:
        props = board_bot.properties
        current_pos = board_bot.position

        if (
            props.diamonds
            and props.inventory_size
            and props.diamonds >= props.inventory_size
        ):
            return props.base

        if board.diamonds:
            closest = min(
                board.diamonds, key=lambda d: self._manhattan(current_pos, d.position)
            )
            return closest.position

        return props.base

    def _manhattan(self, a: models.Position, b: models.Position) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)
