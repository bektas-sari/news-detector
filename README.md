# News Detector

## Overview
This project is a **Fake News Detection Web Application** that verifies whether a news headline or content exists on trusted news websites using **Google Custom Search API**. If the news is found, it is considered **real**, otherwise, it might be **fake**.

## Features
- **Google Custom Search API Integration** ✅
- **Flask Web Application** with a modern UI ✅
- **Daily Query Limit of 100 Searches (Free Usage)** ✅
- **Fully English Interface & Messages** ✅
- **Checks News Existence in Trusted Sources** ✅
- **Responsive & User-Friendly Design** ✅

## Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/bektas-sari/news-detector.git
cd news-detector
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate  # For Windows
pip install -r requirements.txt
```

### **3️⃣ Set Up Your Google API Credentials**
1. Get an **API Key** from Google Cloud Console.
2. Get a **Custom Search Engine (CX ID)** from Google Custom Search Engine.
3. Add them to `app.py`:
```python
API_KEY = "YOUR_GOOGLE_API_KEY"
CX = "YOUR_CX_ID"
```

### **4️⃣ Run the Flask App**
```bash
python app.py
```
Then open your browser and go to:
```
http://127.0.0.1:5000/
```

## 📂 Dataset  
I used `Fake.csv`, `True.csv`, `final_news.csv`, and `processed_news.csv` to train our machine learning model.  
These files are too large to be uploaded to GitHub, so you can download them from the link below:  

🔗 **Download the dataset here:** [https://www.kaggle.com/datasets/emineyetm/fake-news-detection-datasets]


## Usage
1. Enter a **news headline or content** in the text box.
2. Click **Analyze**.
3. The system will search for the news online.
4. If found, it will return **Real News ✅**.
5. If not found, it will return **Fake News ❌**.

## Technologies Used
- **Python 3.x**
- **Flask** (Backend Framework)
- **Google Custom Search API**
- **HTML, CSS (for frontend UI)**

## API Limitations
- Free plan allows **100 searches per day**.
- If the quota is exceeded, wait 24 hours or upgrade to a paid plan.

## License
This project is **open-source** under the MIT License.

## Contributing
Feel free to submit pull requests to improve the project! 😊

## Contact
Mail: bektas.sari@gmail.com

---

⭐ **If you find this project useful, don't forget to give it a star on GitHub!** ⭐
