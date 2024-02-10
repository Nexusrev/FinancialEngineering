from sklearn.model_selection import train_test_split
from sklearn.ensemble import RanmdomForestClassifier
from sklearn.metrics import accuracy_score 
import numpy as np

class StockPriceDirectionPredictor:
    def __init__(self, data):
        self.data = data

    def prepare_data(self):
        """Prepares data for ML model."""
        self.data['target'] = np.sign(self.data['Close'].diff())
        self.data.dropna(inplace=True)
        X = self.data.drop(['target'], axis=1)
        y = self.data['target']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        """Trains the ML"""
        self.prepare_data()
        self.model = RanmdomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)
        predictions = self.model.predict(self.X_test)
        print(f"Model Accuracy: {accuracy_score(self.y_test, predictions)}")