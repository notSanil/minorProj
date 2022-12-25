import cv2
import pytesseract


def image_path_to_text(path):
    img = cv2.imread(path)
    return image_to_text(img)

def image_to_text(img):
    img = process_image(img)

    custom_config = r'--oem 3 --psm 6'
    return pytesseract.image_to_string(img, config=custom_config), img

def process_image(img):
    img = convert_to_grayscale(img)
    img = remove_noise(img)
    img = threshold(img)
    return img

def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noise(img):
    se = cv2.getStructuringElement(cv2.MORPH_RECT , (10,10))
    bg = cv2.morphologyEx(img, cv2.MORPH_DILATE, se)
    img = cv2.divide(img, bg, scale=255)

    blurred = cv2.GaussianBlur(img, (3,3), sigmaX=5, sigmaY=5)
    img = cv2.addWeighted(img, 0.7, blurred, 0.3, 0)

    medianBlurred = cv2.medianBlur(img, 3)
    img = cv2.addWeighted(img, 0.5, medianBlurred, 0.5, 0)

    return img

def threshold(img):
    equalised = cv2.equalizeHist(img)
    img = cv2.addWeighted(img, 0.8, equalised, 0.2, 0)
    img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    return img