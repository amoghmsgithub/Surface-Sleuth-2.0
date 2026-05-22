# 🔍 Surface Sleuth 2.0

AI-Powered Forensic Fingerprint Matching System built using Python, OpenCV, Deep Learning, and Streamlit.

---

## 🚀 Features

* Fingerprint preprocessing using OpenCV
* Hybrid fingerprint matching system
* ORB feature matching
* Deep embedding similarity using ResNet18
* Encrypted fingerprint database
* Streamlit interactive UI
* Secure fingerprint storage
* Real-time fingerprint comparison

---

## 🧠 Technologies Used

* Python
* OpenCV
* PyTorch
* Streamlit
* NumPy
* Cryptography
* ORB Feature Detection
* ResNet18 Deep Learning Model

---

## 📂 Project Structure

```bash
Surface-Sleuth-2.0/
│
├── app.py
├── main.py
├── requirements.txt
│
├── data/
│   └── fingerprints/
│       ├── train/
│       └── test/
│
├── preprocessing/
├── matching/
├── models/
├── database/
├── security/
```

---

## ⚙️ How It Works

### Step 1 — Build Fingerprint Database

The system reads all fingerprint images from:

```bash
data/fingerprints/train
```

Each fingerprint is:

* Preprocessed
* Converted into deep embeddings
* Stored securely in encrypted format

---

### Step 2 — Upload Test Fingerprint

Upload a fingerprint image through the Streamlit interface.

The system:

* Preprocesses the uploaded fingerprint
* Extracts ORB + Deep Learning features
* Compares against stored fingerprints
* Returns the best matching fingerprint

---

## 🛠️ Installation

Clone the repository:

```bash
git clone https://github.com/amoghmsgithub/Surface-Sleuth-2.0.git
```

Move into the project folder:

```bash
cd Surface-Sleuth-2.0
```

Create virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Screenshots

* Fingerprint Upload Interface
* Database Builder
* Match Result Output


---

## 🔐 Security

The fingerprint database is encrypted before storage to improve forensic data security.

---

## 🎯 Future Improvements

* Live camera fingerprint scanning
* Better fingerprint enhancement
* CNN-based fingerprint classifier
* Cloud database integration
* Multi-user forensic dashboard


---

## ⭐ Project Highlights

* Combines Computer Vision + AI
* Practical forensic application
* Secure biometric handling
* Hybrid matching architecture
* Streamlit-based interactive system
