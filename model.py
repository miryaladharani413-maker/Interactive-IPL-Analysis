import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model(data):
    df = data.copy()

    df = df[['team1', 'team2', 'winner']].dropna()

    # Convert text to numbers
    df = pd.get_dummies(df)

    X = df.drop(columns=[col for col in df.columns if 'winner' in col])
    y = df[[col for col in df.columns if 'winner' in col]]

    model = RandomForestClassifier()
    model.fit(X, y)

    return model

def predict_winner(model, team1, team2):
    input_df = pd.DataFrame({
        'team1': [team1],
        'team2': [team2]
    })

    input_df = pd.get_dummies(input_df)

    prediction = model.predict(input_df)

    return "Team Prediction Done"