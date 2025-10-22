# 📚 Book Recommender System

A collaborative filtering–based book recommender system built with **Python**, **pandas**, and **scikit-learn**, designed to suggest similar books by analyzing user rating behavior.

### Features
- Collaborative filtering using cosine similarity (item-based)
- Sparse matrix optimization for large datasets
- Interactive title matching and fuzzy search
- Exportable trained artifacts (`.pkl`, `.npz`, `.csv`) for deployment

### Files
- `book_recommender_system_f.py` — main model training and recommendation code
- `mappings.pkl`, `R_books_users.npz`, `merged_filtered_small.csv` — saved model artifacts
- `app.py` + `index.html` — Flask web interface (optional deployment)

### Example
```bash
python book_recommender_system_f.py
