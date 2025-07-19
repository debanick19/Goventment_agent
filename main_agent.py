from joblib import load
import random

def generate_adaptive_prompt():
    try:
        model, vectorizer = load("agent_policy.joblib")
    except:
        return "Namaste! Main PM-KUSUM yojna se bol raha hoon. Aap solar pump ke liye 60% subsidy pa sakte hain. Kya aap jaankari chahenge?"

    candidate_prompts = [
        "Namaste! Aapko pata hai sarkar aapko 60% subsidy de rahi hai solar pump ke liye?",
        "Main PM-KUSUM yojna se bol raha hoon, kya aapko solar pump mein ruchi hai?",
        "Sirf 40% kharcha aapka, baaki sarkar degi. Solar pump lagwana chahenge?"
    ]

    best_prompt = candidate_prompts[0]
    best_score = -1

    for prompt in candidate_prompts:
        vec = vectorizer.transform([prompt + " haan"])
        score = model.predict_proba(vec)[0][1]
        if score > best_score:
            best_score = score
            best_prompt = prompt

    return best_prompt
