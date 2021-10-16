#!/usr/bin/python3
import cv2
import os
import time
import pytesseract



def get_text_from_image(img_path, try_count, image_count):
    if not os.path.exists('image_text'):
        os.mkdir('image_text')
    if not os.path.exists(img_path):
        return None
    if os.path.exists(os.path.join('image_text', '{}.txt'.format(img_path[7:]))):
        print('[{}/{}] Already extracted text from {}!'.format(try_count, image_count, img_path))
        return

    img = cv2.imread(img_path)
    text = pytesseract.image_to_string(img)
    
    print('[{}/{}] Found text in {}, writing...'.format(try_count, image_count, img_path))
    open(os.path.join('image_text', '{}.txt'.format(img_path[7:])), 'wb').write(bytes(text, 'UTF-8'))

try_count = 0
if __name__ == "__main__":
    try:
        image_count = len(os.listdir('images'))
        non_images = []
        for image in os.listdir('images'):
            try:
                try_count = try_count + 1
                get_text_from_image(os.path.join('images/', image), try_count, image_count)
                time.sleep(2)
            except Exception as e:
                non_images.append(image)
        print(non_images)
    except KeyboardInterrupt:
        print('\n[-] Exiting find-text.py, goodbye!')
        exit(0)