import os
import cv2
import dlib
import scipy.misc

face_detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
workDirectory = os.path.dirname(__file__)
trainDirectory = os.path.join(workDirectory,'images')
peopleTrainFolder = [os.path.join(trainDirectory, f) for f in os.listdir(trainDirectory)]

count = 0

def rect_to_bb(rect):
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def get_face_detect(imagePath):
    print(count, imagePath)
    image = scipy.misc.imread(imagePath)
    detected_faces = face_detector(image, 1)
    shapes_faces = [shape_predictor(image, face) for face in detected_faces]
    for face_pose in shapes_faces:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (x, y, w, h) = rect_to_bb(face_pose.rect)
        image = cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        crop_img = image[y:y + h, x:x + w]
        crop_img = cv2.resize(crop_img, (200, 200), interpolation=cv2.INTER_CUBIC)
        return crop_img

people=['Taylor_Swift','Bear_Grylls','Cillian_Murphy','Aamir_Khan','Harry_Styles']

for i in peopleTrainFolder:
    imagePath = [os.path.join(i,f) for f in os.listdir(i)]
    for f in imagePath:
        sub_face = get_face_detect(f)
        person = None
        for pp in people:
            if pp in f:
                person=pp
                break
        person_dir=workDirectory + "/train/" +person 
        if not os.path.exists(person_dir):
            os.makedirs(person_dir)
        face_file_name = person_dir +"/" + person+ "_" + str(count) + ".jpg"
        count = count + 1
        cv2.imwrite(face_file_name, sub_face)
