import pickle
from sklearn.ensemble import GradientBoostingClassifier


class QuinielaModel:
    def __init__(self):
        self.model = GradientBoostingClassifier()

    def train(self, train_data):
        features = [
            'Local_id',
            'Away_id',
            'Local_Elo',
            'Away_Elo',
            'Elo_diff',
            'division'
        ]
        target = ['results_encoded']
        X, y = train_data[features], train_data[target]
        self.model.fit(X, y)

    def predict(self, predict_data):
        features = [
            'Local_id',
            'Away_id',
            'Local_Elo',
            'Away_Elo',
            'Elo_diff',
            'division'
        ]
        predict_data = predict_data[features]
        predicted_results = self.model.predict(predict_data)

        for i in range(len(predicted_results)):
            if predicted_results[i] == 2:
                predicted_results[i] = 'X'
            elif predicted_results[i] == 3:
                predicted_results[i] = 2
        return predicted_results

    @classmethod
    def load(cls, filename):
        """ Load model from file """
        with open(filename, "rb") as f:
            model = pickle.load(f)
            assert type(model) == cls
        return model

    def save(self, filename):
        """ Save a model in a file """
        with open(filename, "wb") as f:
            pickle.dump(self, f)
