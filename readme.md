# Gestational Diabetes Prediction Flask App

This is a web-based machine learning application that predicts the likelihood of a person developing gestational diabetes using clinical data such as glucose level, blood pressure, BMI, insulin, and more.

## 🔍 Features

- User-friendly web interface to enter health metrics
- Instant prediction using a trained machine learning model
- RESTful API endpoint for programmatic access
- Styled UI with input guidance and interpretation tips

## 🛠 Technologies Used

- Python 3
- Flask
- Scikit-learn
- Pandas
- HTML/CSS

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/diabetes-prediction-flask-app.git
cd diabetes-prediction-flask-app
```

### 2. Set up a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Start the Flask app
```bash
python src/app.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## 📈 Example Inputs

| Feature        | Example Value |
|----------------|---------------|
| Pregnancies    | 2             |
| Glucose        | 120           |
| BloodPressure  | 70            |
| Insulin        | 85            |
| BMI            | 24.5          |
| Age            | 30            |

## 💡 Prediction Output

- **"Will not develop gestational diabetes"** — indicates low risk.
- **"Will develop gestational diabetes"** — indicates high risk and suggests consulting a healthcare provider.

## 📁 Project Structure

```
diabetes-prediction-flask-app/
├── src/
    └── app.py
    └── templates/
        └── index.html
├── venv/
├── diabetes_model.pkl
├── Gestational_Diabetes_model.ipynb
├── requirements.txt
└── readme.md
```

---

Feel free to contribute or suggest improvements! For any queries you can react out at me.sahil.gg@gmail.com.