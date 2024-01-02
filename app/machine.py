from pandas import DataFrame
from sklearn.linear_model import LogisticRegression
import joblib
from datetime import datetime

class Machine:

    def __init__(self, df: DataFrame):
        self.name = "Logistic Regression Classifier"
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S %p")
        
        self.model = LogisticRegression()
        X = df[['Level', 'Health', 'Energy', 'Sanity']]
        y = df['Rarity']
        self.model.fit(X, y)

    def __call__(self, pred_basis: DataFrame):
        prediction, *_ = self.model.predict(pred_basis)
        confidence = self.model.predict_proba(pred_basis).max()
        return prediction, confidence

    def save(self, filepath):
        joblib.dump(self, filepath)

    @staticmethod
    def open(filepath):
        return joblib.load(filepath)

    def info(self):
        return f"Base Model: {self.name} <br/> Timestamp: {self.timestamp}"
