from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = PROJECT_ROOT / "assets"
FONTS_DIR = ASSETS_DIR / "fonts"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
LOG_DIR = PROJECT_ROOT / "logs"

OUTPUT_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

LOG_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

FONT_BOLD = FONTS_DIR / "NotoSans-Bold.ttf"
FONT_REGULAR = FONTS_DIR / "NotoSans-Regular.ttf"

RED = (239, 57, 53)
YELLOW = (255, 206, 73)
WHITE = (255, 255, 255)
BLACK = (25, 25, 25)