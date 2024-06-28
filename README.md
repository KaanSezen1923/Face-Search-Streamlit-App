Face Searching Project
This project is a facial recognition application that allows users to upload an image and search for matching faces from a pre-encoded dataset. The application uses Streamlit for the user interface, OpenCV for image processing, and face_recognition for face detection and encoding.

Features
Upload an image and find matching faces from a pre-encoded dataset.
Display the uploaded image and matching results side by side.
Provide feedback on the matching confidence level.
Installation
Clone the repository:

bash
Kodu kopyala
git clone https://github.com/KaanSezen1923/Face-Search-Streamlit-App.git
cd face-searching-project
Create and activate a virtual environment:

bash
Kodu kopyala
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the required packages:

bash
Kodu kopyala
pip install -r requirements.txt
Data Preparation
Place the images you want to encode in a folder, e.g., C:/Users/KAAN/Desktop/Data.
Run the encoding script to generate the encoded data:
bash
Kodu kopyala
python encode_faces.py
Running the Application
Start the Streamlit application:

bash
Kodu kopyala
streamlit run main.py
Open the provided local URL in your web browser to use the application.

Project Structure
bash
Kodu kopyala
face-searching-project/
│
├── encode_faces.py         # Script to encode faces from the dataset
├── main.py                 # Streamlit application script
├── EncodeFile.p            # Encoded data file
├── requirements.txt        # Required Python packages
└── README.md               # Project documentation
Scripts
encode_faces.py
This script reads images from the specified folder, encodes the faces, and saves the encodings to a file.
main.py
This script contains the Streamlit application that allows users to upload an image and find matching faces.
Requirements
Python 3.x
face_recognition
numpy
opencv-python
Pillow
streamlit
Ensure all dependencies are installed by running:

bash
Kodu kopyala
pip install -r requirements.txt
Contributing
Feel free to open issues or submit pull requests for improvements and bug fixes.

License
This project is licensed under the MIT License.

This README provides an overview of your project, instructions for setup and running, and information about the project structure and scripts. Make sure to replace placeholders like your-username with your actual GitHub username or project details.

![image](https://github.com/KaanSezen1923/Face-Search-Streamlit-App/assets/119515258/4b364eb8-23cd-49a5-a8f8-208a339e0230)

![image](https://github.com/KaanSezen1923/Face-Search-Streamlit-App/assets/119515258/36634328-544f-4afe-896b-d03c4a1efcc0)

![image](https://github.com/KaanSezen1923/Face-Search-Streamlit-App/assets/119515258/e647ba8d-b372-464d-aaf8-6f72c7ce92f3)


