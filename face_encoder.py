import os 
import face_recognition
import pickle 
import cv2 

folder_path="Data"
pathlist=os.listdir(folder_path)
print(pathlist)
images=[]
names=[]
for path in pathlist:
    img_path = os.path.join(folder_path, path)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Warning: Couldn't read image {img_path}")
        continue
    images.append(img)
    names.append(os.path.splitext(path)[0])
print(names)

def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        print(f"Image shape: {img.shape}")
        face_locations=face_recognition.face_locations(img)
        print(f"Face locations:{face_locations}")
        encode=face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
        
    return encodeList

print("Encode Started ...")
encodeListKnown = findEncodings(images)
encodeListKnownwithNames = [encodeListKnown, names]
print(encodeListKnownwithNames)
print("Encoding completed.")

file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownwithNames, file)
file.close()
print("File saved")


