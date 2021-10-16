# prntscrn-scraper
Due to the fact that prnt.sc openly hosts all of the uploaded photos publicly, we can generate a random string of chars and create a link. If
the link is a valid one, the scraper will automatically scan the webpage for the image and download it. Using `python3 find-text.py`, we
can automatically extract the text from the image files using pytesseract.

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
![github_scraper](https://user-images.githubusercontent.com/10734039/137588474-0d5ffefa-165e-474b-a51c-2ef26aaf4d1f.png)


## find-text.py
This script uses pytesseract to find text in images and output it into a txt file in image_text/
![github_findtext](https://user-images.githubusercontent.com/10734039/137588566-5379cb0c-e10f-484e-95f2-abba04b6d972.png)
