from sklearn.linear_model import LogisticRegression as LR
import pandas as pd
import numpy as np
from joblib import dump, load
import os

def train(X, y, model_output='diabetes.joblib'):
    model = LR(max_iter=200)
    model.fit(X,y)
    dump(model, model_output)

def prepare_input(input_dict):
    def get_value(key, default_value):
        return float(input_dict[key]) if key in input_dict else default_value
    features = ["Pregnancies", "Glucose", "BloodPressure",
                "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
    feature_values = np.array([get_value(k, 0.0) for k in features])
    return feature_values.reshape(1, -1)

def get_prediction(input_dict):
    inp = prepare_input(input_dict)
    prediction_class = int(model.predict(inp)[0])
    prediction_label = 'Negative' if prediction_class == 0 else "Positive"
    return dict(
        class_idx=prediction_class,
        class_name=prediction_label
    )

def load_model(model_path):
    assert os.path.exists(model_path)
    return load(model_path)

if __name__ == "__main__":
    df = pd.read_csv("diabetes.csv")
    X, y = df.iloc[:,:-1].values, df.iloc[:, -1].values
    train(X, y, "diabetes.joblib")
else:
    model = load_model('diabetes.joblib')
