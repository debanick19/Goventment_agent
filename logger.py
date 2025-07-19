import json
from datetime import datetime

def save_dialogue(dialogue_id, agent_prompt, farmer_reply):
    log = {
        "dialogue_id": dialogue_id,
        "timestamp": str(datetime.now()),
        "agent_prompt": agent_prompt,
        "farmer_reply": farmer_reply
    }

    with open("dialogue_log.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")
