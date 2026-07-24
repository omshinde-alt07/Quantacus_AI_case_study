from PIL import ImageDraw, ImageFont

#importing colour and fonts

from utils.constants import (
    FONT_BOLD,
    RED,
    WHITE,
    YELLOW,
)


def draw_discount_badge(image, discount):

    draw = ImageDraw.Draw(image)

    width, height = image.size

    
    # Dynamic sizing to adjust any of the image


    margin = int(min(width, height) * 0.04)

    diameter = int(min(width, height) * 0.25)

    font_size = int(diameter * 0.36)

    font = ImageFont.truetype(
        str(FONT_BOLD),
        font_size,
    )

    
    # Position (Top Right) 

    x = width - diameter - margin
    y = margin

    
    # Draw Circle for discount badge
    

    draw.ellipse(
        (
            x,
            y,
            x + diameter,
            y + diameter,
        ),
        fill=RED,
    )

    # Text

    line1 = f"{discount}%"
    line2 = "OFF"

    bbox1 = draw.textbbox((0, 0), line1, font=font)
    bbox2 = draw.textbbox((0, 0), line2, font=font)

    w1 = bbox1[2] - bbox1[0]
    h1 = bbox1[3] - bbox1[1]

    w2 = bbox2[2] - bbox2[0]
    h2 = bbox2[3] - bbox2[1]

    gap = int(diameter * 0.02)

# Total text block height
    total_height = h1 + h2 + gap

# Start exactly at vertical center
    start_y = y + (diameter - total_height) / 2

# Draw first line
    draw.text(
    (
        x + (diameter - w1) / 2 - bbox1[0],
        start_y - bbox1[1],
    ),
    line1,
    fill=YELLOW,
    font=font,
)

# Draw second line
    draw.text(
    (
        x + (diameter - w2) / 2 - bbox2[0],
        start_y + h1 + gap - bbox2[1],
    ),
    line2,
    fill=YELLOW,
    font=font,
)