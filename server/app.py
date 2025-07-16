from flask import Flask, request, jsonify
from ultralytics import YOLO
import os

app= Flask(__name__)
model= YOLO("runs/detect/train/weights/best.pt")

@app.route('/detect',methods=['image'])
def detectionDogs():
    if 'image' not in request.files:
        return jsonify({"Error"}), 400
    image= request.files['image']
    image_path= "temp.jpg"
    image.save(image_path)

    results= model(image_path)
    names= results[0].names
    classDetect= [names[int(c)] for c in results[0].boxes.cls]

    os.remove(image_path)

    containDog= "dog" in classDetect
    return jsonify({containDog})
if __name__=='__main__':
    app.run(host='0.0.0.0', port= 5000)
    