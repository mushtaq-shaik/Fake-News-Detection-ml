# Fake News Detection System (ML Model and Deployment)

## 📌 Overview
The Fake News Detection System is a Machine Learning–based web application that classifies news articles as *Real* or *Fake* using Natural Language Processing (NLP).  
The project aims to combat misinformation by providing an automated, reliable, and easy-to-use news verification tool.

---

## 🚀 Features
- NLP-based text preprocessing
- Machine Learning model for fake news classification
- Real-time prediction using a web interface
- Simple and beginner-friendly UI
- Deployable on cloud platforms

---

## 🧠 Problem Statement
The rapid spread of fake news on digital platforms can mislead people and cause serious social impact.  
This project addresses the problem by applying *Machine Learning and NLP techniques* to analyze and classify news content accurately.

---

## 🛠 Tech Stack
- *Programming Language:* Python  
- *Machine Learning:* Scikit-learn  
- *Natural Language Processing:* NLTK  
- *Data Handling:* Pandas, NumPy  
- *Web Framework:* Flask  
- *Frontend:* HTML, CSS  
- *Deployment:* Gunicorn (Production) / Flask (Local)  

---

## ⚙ How It Works
1. User enters a news article or text
2. Text is preprocessed using NLP techniques (tokenization, stopword removal, stemming)
3. Trained ML model analyzes the content
4. System predicts whether the news is *Real* or *Fake*
5. Result is displayed on the web interface

---

## 🧪 Example Inputs

### ✅ Example of Real News

The Government of India announced a new digital initiative aimed at improving access to public services through online platforms. The program focuses on transparency, efficiency, and citizen engagement.

*Expected Output:*  
➡ *Real News*

---

### ❌ Example of Fake News

Scientists have confirmed that drinking two glasses of salt water every morning can completely cure all diseases within a week, according to a secret study that was never published.

*Expected Output:*  
➡ *Fake News*

> Note: The above examples are for demonstration purposes only.

---

## 📂 Project Structure

![structure](https://github.com/user-attachments/assets/18da9565-9289-4956-a058-9cdba0d67273)

---

## 📋 Project Requirements

### Functional Requirements
- Accept news text as user input
- Preprocess text using NLP techniques
- Classify news as Real or Fake
- Display prediction result clearly
- Support real-time predictions

### Non-Functional Requirements
- Easy-to-use interface
- Fast response time
- Modular and readable code
- Deployable locally or on cloud platforms
- Scalable for future enhancements

### Software Requirements
- Python 3.8+
- Flask
- Scikit-learn
- NLTK
- Pandas
- NumPy

### Hardware Requirements
- Minimum 4 GB RAM
- Intel i3 / equivalent processor or higher
- Internet connection (for dataset & deployment)

---

## ▶ How to Run Locally

1. Clone the repository

git clone https://github.com/your-username/fake-news-detection-ml.git

2. Navigate to the project directory

cd fake-news-detection-ml

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python app.py

5. Open browser and visit

http://127.0.0.1:5000/

---

## 📦 requirements.txt

- flask
- scikit-learn
- pandas
- numpy
- nltk
- gunicorn

---

## 📈 Future Enhancements
- Improve accuracy using Deep Learning models (LSTM, BERT)
- Support multilingual fake news detection
- Add REST API support
- Integrate browser extension

---

## 👨‍💻 Author
*Shaik Mushtaq*  

---

## 📜 License
This project is licensed under the *MIT License*.
