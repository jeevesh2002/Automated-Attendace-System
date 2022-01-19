from PIL import Image
import face_recognition

def save_faces(file):
    image = face_recognition.load_image_file(file)
    face_locations = face_recognition.face_locations(image, model="cnn")
    for n, face_loaction in enumerate(face_locations, start=1):
        top, right, bottom, left = face_loaction
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.save(f"assets/{n}.jpg")

