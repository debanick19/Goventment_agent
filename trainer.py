# basic reinforcement learning simulation. 
# We'll use a LogisticRegression classifier to learn from dialogues and feedback#

import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from joblib import dump

# Load data
def load_data():
    X, y = [], []

    with open("dialogue_log.jsonl", "r") as log_file, open("feedback_log.jsonl", "r") as fb_file:
        dialogues = [json.loads(line) for line in log_file]
        feedbacks = {json.loads(line)["dialogue_id"]: json.loads(line)["success"] for line in fb_file}

    for d in dialogues:
        if d["dialogue_id"] in feedbacks:
            combo = d["agent_prompt"] + " " + d["farmer_reply"]
            X.append(combo)
            y.append(int(feedbacks[d["dialogue_id"]]))

    return X, y

# Train model
def train_model():
    X, y = load_data()

    if len(X) < 5:
        print("Not enough data to train yet.")
        return

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = LogisticRegression()
    model.fit(X_vec, y)

    dump((model, vectorizer), "agent_policy.joblib")
    print("✅ Model trained and saved!")

if __name__ == "__main__":
    train_model()

