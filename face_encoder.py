import os
import face_recognition
import pickle
import cv2


folder_path = "Data"


try:
    pathlist = os.listdir(folder_path)
    if not pathlist:
        raise ValueError("No files found in the specified directory.")
    print(f"Found {len(pathlist)} files in {folder_path}.")
except Exception as e:
    print(f"Error: {e}")
    exit()


images = []
names = []

for path in pathlist:
    img_path = os.path.join(folder_path, path)
    img = cv2.imread(img_path)
    if img is None:
        print(f"Warning: Couldn't read image {img_path}. Skipping...")
        continue
    
    images.append(img)
    names.append(os.path.splitext(path)[0])
    
print(f"Images processed: {len(images)}")
print(f"Names extracted: {names}")

def find_encodings(images_list):
    encode_list = []
    for img in images_list:
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(f"Processing image with shape: {img_rgb.shape}")
        
        face_locations = face_recognition.face_locations(img_rgb)
        if not face_locations:
            print("Warning: No face found in the image. Skipping...")
            continue
        
        face_encoding = face_recognition.face_encodings(img_rgb)[0]
        encode_list.append(face_encoding)
    
    return encode_list


print("Starting face encoding...")
encode_list_known = find_encodings(images)

if not encode_list_known:
    print("No faces were encoded. Exiting...")
    exit()


encode_list_known_with_names = [encode_list_known, names]

print("Encoding completed successfully.")
print(f"Encoded data: {len(encode_list_known)} faces")


output_file = "EncodeFile.p"
try:
    with open(output_file, "wb") as file:
        pickle.dump(encode_list_known_with_names, file)
    print(f"Encoded data saved to {output_file}")
except Exception as e:
    print(f"Error saving file: {e}")



