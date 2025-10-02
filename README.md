# 🎓 Student Performance Predictor

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange.svg)](https://scikit-learn.org/stable/)

A Flask-based ML web app to predict student math scores using factors like gender, ethnicity, parental education, lunch, test prep, reading/writing scores. Built on Kaggle data; R² ~0.75.

## ✨ Features
- Interactive form for predictions.
- Custom ML pipeline (preprocessing + RandomForest).
- Responsive Bootstrap UI.
- Instant results with ethical disclaimers.

## 📊 Dataset
- **Source**: [Kaggle Students Performance](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- **Features**: 7 inputs (categoricals + reading/writing scores); **Target**: Math score (0-100).
- Download `StudentsPerformance.csv` for training.

## 🛠 Tech Stack
| Category | Tools |
|----------|-------|
| Backend  | Flask, Pandas, NumPy |
| ML       | scikit-learn, Joblib |
| Frontend | Bootstrap, HTML/CSS |

## 🚀 Installation & Setup
1. Clone: `git clone https://github.com/yourusername/student-performance-predictor.git && cd student-performance-predictor`
2. Virtual env: `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. Install: `pip install -r requirements.txt` *(Flask, scikit-learn, etc.)*
4. Add dataset CSV.
5. Run: `python app.py` → Visit `http://localhost:5000`

## 📖 Usage
- Home (`/`): Overview → Click to predict.
- Form (`/predictdata`): Input details → Submit for math score prediction.
- Example: Female, Group B, Bachelor's, Standard lunch, Completed prep, Reading=72, Writing=74 → ~78/100.

## 🔄 Model Pipeline
- **Preprocess**: One-hot categoricals, scale numerics.
- **Predict**: `PredictPipeline` loads `model.pkl` for inference.
- Train: Extend with `train_test_split` in `src/pipeline`.

## 🤝 Contributing
Fork → Branch → PR. Issues welcome!

## 📄 License
MIT - see [LICENSE](LICENSE).

## 🙏 Acknowledgments
- Kaggle dataset by SPS Scientist.
- Flask & scikit-learn.

⭐ Star if useful! 🚀
