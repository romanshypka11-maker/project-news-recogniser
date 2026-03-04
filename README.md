# Fake News Detector API 📰🤖

This project is an AI-powered service designed to classify news articles as **Fake** or **True**. It features a Machine Learning model built with **Scikit-learn**, wrapped in a **FastAPI** web server, and fully **Dockerized** for easy deployment.

---

## 🚀 Key Features
* **ML Pipeline:** Combines TF-IDF Vectorization and Logistic Regression.
* **Reliable Evaluation:** Validated using **Stratified 5-Fold Cross-Validation** on the full dataset of **9,024 samples**.
* **FastAPI Integration:** Provides a RESTful endpoint for real-time predictions.
* **Docker Ready:** Containerized environment for consistent behavior across different systems.

---

## 📊 Model Performance
The final model was evaluated using cross-validation to ensure stable and honest metrics:

* **Accuracy:** `0.94`
* **Precision (Macro Avg):** `0.92`
* **Recall (Macro Avg):** `0.89`
* **F1-Score (Macro Avg):** `0.91`

---

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **ML Libraries:** Scikit-learn, Pandas, Joblib
* **API Framework:** FastAPI, Uvicorn
* **DevOps:** Docker, Git

---

## 📦 How to Run with Docker

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/romanshypka11-maker/project-news-recogniser.git](https://github.com/romanshypka11-maker/project-news-recogniser.git)
   cd project-news-recogniser
   ```
2. **Build the Docker image:**
   ```bash
   docker build -t fake_news_api .
    ```
3. **Run the container:**
   ```bash
   docker run -p 8000:8000 fake_news_api
    ```
## 🧠 Model Insights
The model uses Logistic Regression coefficients to identify key markers:

* Fake Indicators: Specific sensationalist keywords with negative weights.


* True Indicators: Neutral and factual reporting terms with positive weights.

**Author:** Roman Shypka 
[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github)](https://github.com/romanshypka11-maker)

*First-year CS Student @ Ivan Franko National University of Lviv*