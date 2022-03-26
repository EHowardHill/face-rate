import cv2, os, pprint, math
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Shebang01#!@localhost:3307/db")
base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class photo_info(base):
    __tablename__ = 'photo_info'
    id = Column(Integer, primary_key=True)
    isMale = Column(Integer)
    isSmiling = Column(Integer)
    isWearingGlasses = Column(Integer)
    ageLow = Column(Integer)
    ageHigh = Column(Integer)

faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
ageProto="age_deploy.prototxt"
ageModel="age_net.caffemodel"
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Male','Female']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_smile.xml')
glasses_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_eye_tree_eyeglasses.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    smiles = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        smile = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        smiles.append(smile)
    return smiles

def glasses(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    smiles = []
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        smile = glasses_cascade.detectMultiScale(roi_gray, 1.8, 20)
        smiles.append(smile)
    return smiles

for file in os.listdir('./static/'):
    face = cv2.imread('./static/' + file)
    facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    print(file + ":")

    blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
    genderNet.setInput(blob)
    genderPreds=genderNet.forward()
    gender=genderList[genderPreds[0].argmax()]
    print(f'Gender: {gender}')

    ageNet.setInput(blob)
    agePreds=ageNet.forward()
    age=ageList[agePreds[0].argmax()]
    print(f'Age: {age[1:-1]} years')

    gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) 
    canvas = detect(gray, face)  
    glass = glasses(gray, face)

    pprint.pprint(glass)
    if (len(glass) > 1): y = input()

    p = photo_info(
        id = int(file.replace('.jpg', '')),
        isMale = 1 if gender == 'Male' else 0,
        isSmiling = 1 if len(canvas) > 1 else 0,
        isWearingGlasses = 1 if len(glass) > 1 else 0,
        ageLow = age[1:age.index('-')] if age[1] != "-" else 0,
        ageHigh = age[age.index('-')+1:-1] if age[-1] != "-" else 0
    )

    session.add(p)
    session.commit()
    pprint.pprint(p)