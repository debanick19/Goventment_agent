###We'll log whether a conversation was successful or not.###
import json
from datetime import datetime

def save_feedback(dialogue_id, farmer_reply, success):
    feedback = {
        "dialogue_id": dialogue_id,
        "timestamp": str(datetime.now()),
        "farmer_reply": farmer_reply,
        "success": success  # True for positive, False for negative
    }

    with open("feedback_log.jsonl", "a") as f:
        f.write(json.dumps(feedback) + "\n")
