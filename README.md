# Product Image Generation System

A Python-based automation system that generates promotional product images using product information stored in Google Sheets.

The application downloads product images, validates the input, calculates discounts, and generates marketing assets such as discount badges and price cards. The project is designed with a modular architecture, centralized logging, and robust error handling to support batch processing of products.

---

## Features

- Read product data directly from Google Sheets
- Download product images from URLs
- Validate product information before processing
- Automatically calculate discount percentage
- Generate discount badge images
- Generate promotional price card images
- Skip invalid products without interrupting processing
- Timestamped logging for debugging and monitoring
- Modular and maintainable codebase
- Unit tests for utility functions

---

## Project Architecture

```
                   Google Sheets
          (Product Data & Image URLs)
                     │
                     ▼
          Image Generation Application
                (Python)
        ┌─────────────────────────┐
        │ Read Product Data       │
        │ Validate Input          │
        │ Download Images         │
        │ Generate Assets         │
        │ Record Logs             │
        └──────────┬──────────────┘
                   │
          ┌────────┴────────┐
          ▼                 ▼
   Generated Images     Log Files
```

---

## Project Structure

```
quantacus_ai_project/
│
├── assets/
│   └── fonts/
│
├── logs/
│
├── outputs/
│
├── tests/
│
├── utils/
│   ├── badge.py
│   ├── config.py
│   ├── constants.py
│   ├── google_sheet.py
│   ├── image_utils.py
│   ├── logger.py
│   └── price_card.py
│
├── main.py
├── requirements.txt
└── .gitignore
```

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Google Sheets | Product catalog management |
| Google Service Account | Secure authentication |
| Pillow (PIL) | Image processing and generation |
| Requests | Download product images |
| Pandas | Process tabular product data |
| Logging | Execution monitoring |
| Pytest | Unit testing |

---

## Processing Flow

1. Read configuration.
2. Connect to Google Sheets.
3. Load product data.
4. Validate required fields.
5. Download product image.
6. Verify downloaded image.
7. Calculate discount.
8. Generate:
   - Discount Badge
   - Price Card
9. Save generated images.
10. Record logs.
11. Continue processing remaining products.
12. Print processing summary.

---

## Output Structure

```
outputs/
├──101/
│   ├──101_discount.jpg
│   └──101_strikeoff.jpg
│
├──102/
│   └──102_strikeoff.jpg
```

Products without discounts generate only the strike-off image.

---

## Logging

Each execution creates a timestamped log file.

Example:

```
logs/
└── run_2026-07-24_12-30-15.txt
```

The logs contain:

- Product processing status
- Validation failures
- Download failures
- Image generation status
- Final execution summary

---

## Validation Rules

The application skips products when:

- Product ID is missing
- Image URL is missing
- Original price is invalid
- Sale price is invalid
- Sale price is greater than original price
- Image URL is inaccessible
- URL does not return an image
- Downloaded image is corrupted

Processing continues with the next product instead of terminating the application.

---

## Installation

Clone the repository

```bash
git clone https://github.com/omshinde-alt07/Quantacus_AI_case_study.git
```

Move into the project

```bash
cd Quantacus_AI_case_study
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python main.py
```

---

## Run Tests

```bash
pytest
```

or

```bash
pytest -v
```

---

## Future Improvements

- Parallel image processing
- Multiple promotional templates
- Cloud storage integration
- Retry mechanism for failed downloads
- Dashboard for monitoring processing
- AI-based image enhancement
- Direct integration with e-commerce platforms

---

## Author

**Om Shinde**

