from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

def get_class(image_path, model_path, labels_path):
    # Bilimsel gösterimi kapat
    np.set_printoptions(suppress=True)

    # Model ve etiketleri yükle
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r").readlines()

    # Görseli hazırlama
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)

    # Normalize et
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Tahmin yap
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]

    print(f"Class: {class_name}, Confidence Score: {confidence_score}")

    return (class_name, confidence_score)