# 🌿 Plant Disease Detection System

A deep learning-powered jungle-themed web app to detect diseases in plant leaves and suggest organic and chemical treatments along with prevention tips. It also speaks out the diagnosis using voice! 🔊🌱
## 🧠 What is This Project?
This is a machine learning-based plant leaf disease classification system built using a Convolutional Neural Network (CNN). It allows users to:
- Upload an image of a plant leaf 🍃
- Detect the disease (if any) 😷
- Get **organic** & **chemical treatments**, and **prevention tips** 🌿
- Hear the result out loud using **Google Text-to-Speech (gTTS)** 🎙️
- Enjoy a jungle-themed interface with falling leaves, flying butterflies, and vines! 🦋🌳

🗂 Dataset
This project uses a subset of the **PlantVillage Dataset**, which contains labeled images of healthy and diseased plant leaves.
📥 Download Dataset:
👉 https://www.kaggle.com/datasets/emmarex/plantdisease?resource=download
Using split_dataset.py, the dataset gets divided into train,test & validation.The name of the dataset will be "PlantVillageSplit"

🧠 Trained Model
We used TensorFlow to train a CNN model on the PlantVillage dataset.
📥 Download Trained Model:
👉 [https://drive.google.com/file/d/1zOgtS7w3ARE8M6T4CDeTRuTea6VAnkHx/view?usp=sharing- plant_disease_model.keras](url)
👉 [https://drive.google.com/file/d/1kZZTy0GMDN1Qv4YhTAG6V_rZdNfZdw5l/view?usp=sharing- classes.txt](url)
> Place it inside 'plant_disease_app/model/ as: plant_disease_model.keras, Place classes.txt under the same folder as well.

🎨 Jungle-Themed Background
The app uses a beautiful jungle-style animated background.
📥 Download Background GIF:
👉 [https://drive.google.com/file/d/1Bz_wn2c94ekn8snTmX6Dwz8TreR6UMwe/view?usp=sharing](url)
> Save it inside: plant_disease_app/assets/bg.gif

🗃️ Project Structure
PlantDiseaseProject/
└── plant_disease_app/
├── app.py ← Main Streamlit app
├── utils.py ← Image preprocessor
├── treatment.py ← Disease treatment database
├── model/
│ └── plant_disease_model.keras ← Trained model (downloaded manually)
├── assets/
│ ├── bg.gif ← Jungle background (downloaded manually)

⚙️ Setup Instructions
1. Clone the repository
**bash**
git clone https://github.com/your-username/plant-disease-detector.git
cd plant-disease-detector/plant_disease_app

2. Install Python dependencies
**bash**
pip install -r requirements.txt


3. Add the missing files:
Trained model (plant_disease_model.keras) to model/
Background GIF (bg.gif) to assets/

🚀 Run the App
**bash**
streamlit run app.py
It will open automatically at:
📍 http://localhost:8501

🎯 Features
🧠 CNN-based plant disease prediction
📷 Image upload via Streamlit
🧪 Organic and chemical treatment display
🛡️ Prevention tips
🎙️ Voice assistant using Google Text-to-Speech (gTTS)
🎨 Animated jungle-themed UI with:
🍃 Falling leaf emojis
🦋 Floating butterfly emojis
🎥 Animated background (GIF)

💻 Technologies Used
Python
TensorFlow + Keras
Streamlit
gTTS (Google Text-to-Speech)
HTML/CSS (embedded in Streamlit)
Numpy, Pillow

🙌 Credits
PlantVillage Dataset
Streamlit
Google Text-to-Speech (gTTS)

📬 Contact
Created with 💚 by Kushi Anil Kumbar
Open an issue or reach out if you’d like to contribute or ask questions!








