import re
import requests
from io import BytesIO
from pathlib import Path
from utils.constants import OUTPUT_DIR
from PIL import Image, UnidentifiedImageError

#clean prices

def clean_price(price):

    if isinstance(price, (int, float)):
        return int(price)

    matches = re.findall(
        r"\d+\.?\d*",
        str(price),
    )

    if not matches:
        raise ValueError(
            f"No numeric value found in '{price}'"
        )

    return int(float(matches[0]))

#download image from url

def download_image(url):

    response = requests.get(
        url,
        timeout=30,
    )

    response.raise_for_status()

    content_type = response.headers.get(
        "Content-Type",
        "",
    )

    if not content_type.startswith("image/"):
        raise ValueError(
            f"URL does not contain an image ({content_type})"
        )

    try:

        return Image.open(
            BytesIO(response.content)
        ).convert("RGB")

    except UnidentifiedImageError:

        raise ValueError(
            "Downloaded file is not a valid image."
        )

#Create product folder with one folder to one product

def create_product_folder(product_id):

    folder = OUTPUT_DIR / str(product_id)

    folder.mkdir(
        parents=True,
        exist_ok=True,
    )

    return folder

#calculate discount

def calculate_discount(mrp, sale_price):

    if mrp <= 0:
        raise ValueError("MRP must be greater than zero.")

    if sale_price > mrp:
        raise ValueError("Sale price cannot exceed MRP.")

    return round(
        ((mrp - sale_price) / mrp) * 100
    )