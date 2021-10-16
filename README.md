# prntscrn-scraper

## Requirements
```bash
# Install tesseract
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev

# Install python3 OpenCV and other requirements
pip3 install -r requirements.txt
```

## scraper.py
This is just a simple scraper to generate random 6 character links for prnt.sc and download an image if there is one at that address.

## find-text.py
This script uses pytesseract to find text in images and output it into a txt file in image_text/
