# 🤖 Suraksha-AI: Guarding Motherhood with Intelligence

## 🌟 Overview

**Suraksha-AI** is a machine learning-powered health monitoring system designed to reduce maternal mortality by detecting **hypertensive disorders** and **anemia** using non-invasive methods in low-resource settings. Our mission is to ensure **safe pregnancies** through early and intelligent health monitoring, especially in rural or underserved areas.

---

## 🚨 The Problem

India loses approximately **30,000 mothers every year** due to preventable conditions like:

- **Hypertensive disorders** (preeclampsia/eclampsia)
- **Anemia**, often undetected between antenatal visits

These complications go unnoticed because of:
- Limited healthcare access in rural areas
- Infrequent ANC visits
- Lack of immediate diagnostic tools

---

## 💡 Our 2-in-1 Solution: Suraksha-AI

### 🤖 1. AI-Based Anemia Detector

> A non-invasive, low-cost tool to detect anemia using just a smartphone camera.

- 📷 Uses image of **lower eyelid** or **nail bed**
- 🧠 Applies **deep learning and image processing** to analyze color/brightness
- 📊 Classifies anemia into **Low / Medium / High Risk**
- 🌐 Works offline, ideal for **rural or resource-poor settings**

### 🩺 2. mPatch: Wearable Vital Sign Monitor

> A smart, flexible patch that monitors essential vitals for pregnant women.

- ❤️ Tracks **Blood Pressure, Temperature, SpO₂, and Heart Rate**
- 📡 Sends real-time **danger alerts** via **mock LoRa / SMS**
- 📲 **Health Dashboard** displays alerts to caregivers and family
- 🔋 Designed to be **low-power and low-cost**, ideal for long-term use

---

## 🔁 How Suraksha-AI Works (Pipeline)

📸 Take photo of lower eyelid/nail bed  
↓  
🧠 Image analyzed by AI model (color/brightness + ML classification)  
↓  
🔴 Predicts anemia risk: Low / Medium / High  
↓  
📍 mPatch worn on arm tracks BP, SpO₂, Temp, HR  
↓  
🚨 Detects abnormal vitals, triggers danger signal  
↓  
📶 Sends alert through mock LoRa / SMS  
↓  
📱 Users receive real-time alerts on health dashboard

---

## 🛠️ Tech Stack

| Component         | Current MVP                     | Future Prototype (Planned)           |
|------------------|----------------------------------|--------------------------------------|
| **Frontend**      | HTML, JavaScript, Tailwind CSS   | React.js + Tailwind CSS              |
| **Backend**       | Flask (Python)                   | Flask (modular microservices)        |
| **ML Model**      | Scikit-learn (RandomForest)      | XGBoost or LightGBM (via joblib)     |
| **Image Processing** | OpenCV, NumPy                 | Enhanced Deep Learning (CNN)         |

---

## 📁 Folder Structure

suraksha-ai/
│
├── backend/
│ └── anemia_rf_model.pkl # Trained ML model
│
├── frontend/
│ ├── index.html # UI homepage
│ ├── script.js # JS logic
│ └── styles.css # Tailwind CSS styles
│
├── app.py # Flask backend
├── requirements.txt # Python dependencies
└── TempCodeRunnerFile.py # Temporary script file


---

## 🧪 How to Run Locally

1. Clone the repo  

git clone https://github.com/your-username/suraksha-ai.git
cd suraksha-ai

2. Install dependencies


pip install -r requirements.txt

3. Run the app


python app/app.py


4. Open in browser
   Go to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 👩‍💻 Team CloudCoder

* Soumya Rai
* Vanshika Pandey

We participated in **ClodeClash 2.0 Hackathon**, aiming to create real-world solutions for maternal health.

---

## 📈 Future Scope

* Integration with **deep learning models** for higher accuracy
* Real-time **BP analysis from video streams**
* **Multilingual support** for rural health workers
* Integration with **Aarogya Setu / government APIs**

---


## 🙏 Acknowledgments

* UCI & WHO datasets on maternal health
* Scikit-learn, OpenCV, Flask
* CodeClash Organizers

---

## 🔗 Useful Links

* [Presentation Slides](https://www.canva.com/design/DAGqIoSQXW8/igmnEN9ccqxdGMc0CiniXw/edit?utm_content=DAGqIoSQXW8&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
* [Link](http://127.0.0.1:5500/SURAKSH/frontend/index.html)

---

