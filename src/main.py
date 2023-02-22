from fastapi import FastAPI, UploadFile, File
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

IMG_HEIGHT = 224
IMG_WIDTH = 224
BATCH_SIZE=32
normalization_layer = tf.keras.layers.Rescaling(1./255)
unique_labels = ['Bed','Chair','Sofa']

app = FastAPI()

def load_model(model_path):
  """
  Loads a saved model from a specified path.
  """
  print(f"Loading saved model from: {model_path}")
  model = tf.keras.models.load_model(model_path, 
                                     custom_objects={"KerasLayer":hub.KerasLayer})
  return model

model = load_model("./ml/20230222-20051677096320-fullhaus_mobilenet_v2_130_224_5.h5")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/predicts-image")
async def predicts_image(file: UploadFile = File(description="upload an image here (Bed | Chair | Sofa)")):
    image = await file.read()
    data = convert_to_data_batch(image)
    preds = model.predict(data)
    label = unique_labels[np.argmax(preds[0])]
    return {"label": label}

def convert_to_data_batch(image):
    image = tf.image.decode_image(image, channels=3)
    image = tf.image.resize(image, size=[IMG_WIDTH, IMG_HEIGHT])
    data = tf.data.Dataset.from_tensors((tf.constant(image)))
    data_batch = data.map(lambda x: normalization_layer(x)).batch(BATCH_SIZE)
    return data_batch
