from services.window_service import (
    snap_left,
    snap_right
)
from commands.registry import WINDOW_ALIASES



def apply_layout(command, layout):

    if not layout:
        return
    
    keyword = WINDOW_ALIASES.get(
        command,
        command
    )

    match layout:

        case "left":
            snap_left(keyword)

        case "right":
            snap_right(keyword)


