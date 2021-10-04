from flask import request
from flask import jsonify
from flask import Flask
from flask_cors import CORS
import random
import numpy as np
import tensorflow as tf

app = Flask(__name__)
CORS(app)
cors = CORS(app, resources={
    r"/*":{
        "origins": "*"
    }
})

model = tf.keras.models.load_model('trained_model.h5')
print('loaded the model')

@app.route('/predict')
def hello():
    print("requsted")
    F18_38 = random.randrange(1,75)
    F39_59 = random.randrange(1,65)
    F60_80 = random.randrange(1,61)
    Female = F18_38 + F39_59 + F60_80
    M18_38 = random.randrange(1,83)
    M39_59 = random.randrange(1,86)
    M60_80 = random.randrange(1,86)
    Male = M18_38 + M39_59 + M60_80
    Daytime = random.randrange(0,2)
    Season_Num = random.randrange(0,4)
    Day = random.randrange(0,2)
    seasons=["Spring","Summer","Autumn","Winter"]

    inputs=np.array([Male,Female,F18_38,F39_59,F60_80,M18_38,M39_59,M60_80,Daytime,Season_Num,Day], dtype='float32')
    inputs = np.reshape(inputs, (1,11))
    result = model.predict(inputs)
    label = np.argmax(result,axis=1)

    print("predicted successfully")

    response = {
        "male":str(Male),
        "female":str(Female),
        "F18_38":str(F18_38),
        "F39_59":str(F39_59),
        "F60_80":str(F60_80),
        "M18_38":str(M18_38),
        "M39_59":str(M39_59),
        "M60_80":str(M60_80),
        "Daytime":str(Daytime),
        "Season":seasons[Season_Num],
        "Day":str(Day),
        "Label":str(label[0])
    }
    return jsonify(response)