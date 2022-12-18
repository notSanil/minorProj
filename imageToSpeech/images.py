from flask import Blueprint, request, render_template
import cv2
import numpy as np
from imageToSpeech.image_processing import image_to_text

import io
from PIL import Image
from base64 import b64encode


bp = Blueprint('images', __name__, url_prefix='/')

@bp.route("/", methods=["GET", "POST"])
def index():    
    if request.method == "POST":
        file = request.files.get("image")
        if (file.filename == ""):
            return render_template("index.html")

        img = convert_to_cv_img(file)
        text, processed_image = image_to_text(img)

        file_object = io.BytesIO()
        img = Image.fromarray(processed_image.astype("uint8"))
        img.save(file_object, 'PNG')
        base64img = "data:image/png;base64," + b64encode(file_object.getvalue()).decode('ascii')

        return render_template("result.html", text=text, image=base64img)
    
    return render_template("index.html")

def convert_to_cv_img(file):
    x = np.fromstring(file.stream.read(), dtype='uint8')
    img = cv2.imdecode(x, cv2.IMREAD_UNCHANGED)

    return img