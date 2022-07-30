from annotated_text import annotated_text
from src.loaders import ColorLookup


class BuildLegend:
    def __call__(self):
        colors = ColorLookup().preset_colors_remaining

        return annotated_text(
            (
                "",
                "",
                f"#B0B0B0",
            ),
            "  Part of largest cluster     ",
            (
                "",
                "",
                f"#B50009",
            ),
            "  Part of 2nd largest cluster     ",
            (
                " \n ",
                "\n",
                f"#00B023",
            ),
            "  Part of 3rd largest cluster     ",
        )
