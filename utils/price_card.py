from PIL import ImageDraw, ImageFont

from utils.constants import (
    FONT_BOLD,
    FONT_REGULAR,
    RED,
    YELLOW,
    WHITE,
    BLACK,
)



def draw_price_card(image, sale_price, mrp):

    draw = ImageDraw.Draw(image)

    width, height = image.size
    show_discount = mrp > sale_price

    # Responsive Dimensions to create price card

    margin = int(min(width, height) * 0.04)

    card_width = int(width * 0.36)
    card_height = int(height * 0.24)

    radius = int(card_height * 0.10)

    # Fonts

    sale_font = ImageFont.truetype(
        str(FONT_BOLD),
        int(card_height * 0.44),
    )

    mrp_font = ImageFont.truetype(
        str(FONT_REGULAR),
        int(card_height * 0.34),
    )

    # Card Position

    x = width - card_width - margin
    y = margin

    draw.rounded_rectangle(
        (
            x,
            y,
            x + card_width,
            y + card_height,
        ),
        radius=radius,
        fill=RED,
    )


# No Discount flow to handle products with no discount


    if not show_discount:
        only_font = ImageFont.truetype(
            str(FONT_BOLD),
            int(card_height * 0.22),
        )

        price_font = ImageFont.truetype(
            str(FONT_BOLD),
            int(card_height * 0.44),
        )

        only_text = "Only"
        price_text = f"₹{sale_price}"

        # only text fonts and sizing

        only_bbox = draw.textbbox(
            (0, 0),
            only_text,
            font=only_font,
        )

        only_width = only_bbox[2] - only_bbox[0]

        only_x = x + (card_width - only_width) / 2 - only_bbox[0]
        only_y = y + card_height * 0.18 - only_bbox[1]

        draw.text(
            (
                only_x,
                only_y,
            ),
            only_text,
            font=only_font,
            fill=WHITE,
        )

        # -------- Price --------

        price_bbox = draw.textbbox(
            (0, 0),
            price_text,
            font=price_font,
        )

        price_width = price_bbox[2] - price_bbox[0]

        price_x = x + (card_width - price_width) / 2 - price_bbox[0]
        price_y = y + card_height * 0.42 - price_bbox[1]

        draw.text(
            (
                price_x,
                price_y,
            ),
            price_text,
            font=price_font,
            fill=YELLOW,
        )

        return image


    # Original Price

    mrp_text = f"₹{mrp}"

    bbox = draw.textbbox(
        (0, 0),
        mrp_text,
        font=mrp_font,
    )

    mw = bbox[2] - bbox[0]
    mh = bbox[3] - bbox[1]

    mrp_x = x + (card_width - mw) / 2 - bbox[0]
    mrp_y = y + card_height * 0.12 - bbox[1]

    draw.text(
        (
            mrp_x,
            mrp_y,
        ),
        mrp_text,
        font=mrp_font,
        fill=WHITE,
    )

    # Strike Through box 

    strike_y = mrp_y + (bbox[1] + bbox[3]) / 2

    padding = int(card_width * 0.03)

    draw.line(
        (
            mrp_x - padding,
            strike_y,
            mrp_x + mw + padding,
            strike_y,
        ),
        fill=BLACK,
        width=max(3, int(card_height * 0.01)),
    )

    # Sale Price font and sizing

    sale_text = f"₹{sale_price}"

    sale_bbox = draw.textbbox(
        (0, 0),
        sale_text,
        font=sale_font,
    )

    sw = sale_bbox[2] - sale_bbox[0]

    sale_x = x + (card_width - sw) / 2 - sale_bbox[0]
    sale_y = y + card_height * 0.53 - sale_bbox[1]

    draw.text(
        (
            sale_x,
            sale_y,
        ),
        sale_text,
        font=sale_font,
        fill=YELLOW,
    )

    return image