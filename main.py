from utils.image_utils import (
    clean_price,
    create_product_folder,
    download_image,
    calculate_discount,
)

from utils.badge import draw_discount_badge
from utils.price_card import draw_price_card
from utils.google_sheet import get_sheet_dataframe
from utils.logger import setup_logger

from utils.config import (
    SERVICE_ACCOUNT_PATH,
    SPREADSHEET_ID,
    WORKSHEET_NAME,
    IMAGE_QUALITY,
)


logger = setup_logger()


def process_row(row, index):

    required_fields = [
        "Product Id",
        "image_url",
        "original_price",
        "sale_price",
    ]

    missing = [
        field
        for field in required_fields
        if not str(row.get(field, "")).strip()
    ]

    if missing:

        logger.warning(
            f"Skipping row {index + 2}: Missing {', '.join(missing)}"
        )

        return "skipped"

    product_id = int(float(row["Product Id"]))

    image_url = row["image_url"]

    mrp = clean_price(row["original_price"])

    sale_price = clean_price(row["sale_price"])

    logger.info(f"Processing Product {product_id}")

    image = download_image(image_url)

    discount = calculate_discount(
        mrp,
        sale_price,
    )

    folder = create_product_folder(product_id)

    if discount > 0:

        discount_image = image.copy()

        draw_discount_badge(
            discount_image,
            discount,
        )

        discount_image.save(
            folder / f"{product_id}_discount.jpg",
            quality=IMAGE_QUALITY,
        )

    price_image = image.copy()

    draw_price_card(
        price_image,
        sale_price,
        mrp,
    )

    price_image.save(
        folder / f"{product_id}_strikeoff.jpg",
        quality=IMAGE_QUALITY,
    )

    return "processed"

#main orchestration 

def main():

    logger.info("Starting product asset generation")

    df = get_sheet_dataframe(
        SERVICE_ACCOUNT_PATH,
        SPREADSHEET_ID,
        WORKSHEET_NAME,
    )

    logger.info(
        f"Loaded {len(df)} products from Google Sheets."
    )

    processed = 0
    skipped = 0
    failed = 0

    for index, row in df.iterrows():

        try:

            status = process_row(
                row,
                index,
            )

            if status == "processed":
                processed += 1

            else:
                skipped += 1

        except Exception as e:

            failed += 1

            logger.error(
                f"Row {index + 2}: {e}"
            )

    logger.info("-" * 50)
    logger.info("Processing Summary")
    logger.info("-" * 50)
    logger.info(f"Processed : {processed}")
    logger.info(f"Skipped  : {skipped}")
    logger.info(f"Failed   : {failed}")
    logger.info("-" * 50)

    logger.info("Asset generation completed.")


if __name__ == "__main__":
    main()