# 📚 Book Recommender System

## Overview
The **Book Recommender System** is a machine learning project that recommends similar books to users based on their preferences.  
It uses collaborative filtering with a **K-Nearest Neighbors (KNN)** algorithm to find books that are most similar in terms of user ratings.

This project demonstrates data preprocessing, similarity-based recommendation, and configuration management using YAML for clean and reproducible experimentation.

---

## 🚀 Features
- Reads and processes **Books**, **Users**, and **Ratings** datasets  
- Applies filters based on configurable parameters  
- Builds a **sparse matrix** of books and users  
- Uses **Cosine Similarity** and **KNN** for book recommendations  
- Interactive recommendation system using `ipywidgets`  
- Configuration handled via `config/params.yaml`

## 🏗️ Project Structure

```
Book-Recommender-System/
│
├── config/
│   └── params.yaml                # Configuration parameters
│
├── data/
│   └── dataset_info.md            # Dataset description or data link info
│
├── src/
│   └── book_recommender_system.py # Main recommendation logic
│
├── .gitignore                     # Files/folders to exclude from Git
├── LICENSE                        # MIT open-source license
├── README.md                      # Project documentation
├── main.py                        # Entry point to run the project
└── requirements.txt               # Required Python libraries
```

## ⚙️ Installation

### 1. Clone this repository
```bash
git clone https://github.com/your-username/Book-Recommender-System.git
cd Book-Recommender-System

2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

3. Install dependencies
pip install -r requirements.txt

🧩 Configuration

All key parameters are stored in config/params.yaml, including:

RATING_THRESHOLD

MIN_USER_RATINGS

MIN_BOOK_RATINGS

TOP_K

You can easily modify these values without editing the main Python code.

▶️ How to Run
Option 1: Run Locally
python main.py

Option 2: Run in Google Colab
!git clone https://github.com/your-username/Book-Recommender-System.git
%cd Book-Recommender-System
!python main.py

📊 Dataset Information

The project uses the Book Recommendation Dataset from Kaggle:
🔗 Book Recommendation Dataset – Kaggle

File	Description
Books.csv	Contains book details such as ISBN, title, author, publisher, and publication year.
Ratings.csv	Stores user ratings for books.
Users.csv	Contains user demographic data (User-ID, Location, Age).

🧠 Technologies Used

Python 3.x

pandas, numpy, scipy

scikit-learn (KNN algorithm)

PyYAML (for configuration)

ipywidgets (for interactive input)

--License

This project is licensed under the MIT License
.
You’re free to use, modify, and distribute it with proper credit.

👩‍💻 Author

Zainab Jamil
📧 zainab-jamil-b73824329 (linkedin )
GitHub: zanijamil30-ops

⭐ Acknowledgment

Dataset Source: Kaggle - Book Recommendation Dataset
