from game import models
from .nazarick_config import GreedyBotConfig


class GreedyTargeting:
    def _manhattan(self, a: models.Position, b: models.Position) -> int:
        return abs(a.x - b.x) + abs(a.y - b.y)

    def find_target(
        self, board_bot: models.GameObject, board: models.Board
    ) -> models.Position:
        props = board_bot.properties
        current_pos = board_bot.position

        if not props or not props.base:
            return current_pos

        diamonds_carried = props.diamonds if props.diamonds is not None else 0
        inventory_size = (
            props.inventory_size
            if props.inventory_size is not None
            else GreedyBotConfig.DEFAULT_INVENTORY_SIZE
        )

        is_inventory_full = diamonds_carried >= inventory_size
        has_enough_diamonds_threshold_met = (
            diamonds_carried >= GreedyBotConfig.RETURN_THRESHOLD_DIAMONDS
        )

        if is_inventory_full or has_enough_diamonds_threshold_met:
            return props.base

        if board.diamonds:
            valid_diamonds = [d for d in board.diamonds if d.position]
            if valid_diamonds:
                closest_diamond = min(
                    valid_diamonds,
                    key=lambda d: self._manhattan(current_pos, d.position),
                )
                return closest_diamond.position

        return props.base
