import os
import sys
import pandas as pd

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features: pd.DataFrame):
        try:
            # Import inside method to avoid circular import
            from src.utils import load_object
            from src.exception import CustomException

            # Absolute path to artifacts folder
            PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            ARTIFACTS_DIR = os.path.join(PROJECT_ROOT, "artifacts")

            model_path = os.path.join(ARTIFACTS_DIR, "model.pkl")
            preprocessor_path = os.path.join(ARTIFACTS_DIR, "preprocessor.pkl")

            # Check files exist
            if not os.path.exists(model_path):
                raise FileNotFoundError(f"Model file not found: {model_path}")
            if not os.path.exists(preprocessor_path):
                raise FileNotFoundError(f"Preprocessor file not found: {preprocessor_path}")

            # Load objects
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # Transform features and predict
            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            return preds

        except Exception as e:
            raise CustomException(e, sys)
