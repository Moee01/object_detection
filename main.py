import cv2 
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound


camera = cv2.VideoCapture(1)
labels = []


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("./sound/output.mp3")
    playsound("./sound/output.mp3")


while True:
    ret, frame = camera.read()

    if not ret:
        break

   
    bbox, label, conf = cv.detect_common_objects(frame)
    output_image = draw_bbox(frame, bbox, label, conf)
    
    
    cv2.imshow("Object Detection", output_image)

   
    for item in label:
        if item not in labels:
            labels.append(item)  
            speech(f" i see a {item}")
    
   
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


i = 0
new_sentence = []
for label_item in labels:
    if i == 0:
        new_sentence.append(f"I saw a {label_item}, and")
    else:
        new_sentence.append(f"a {label_item}")
    i += 1


speech(" ".join(new_sentence))


camera.release()
cv2.destroyAllWindows()
