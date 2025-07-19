An AI-powered Hindi voice agent that informs farmers about government schemes like PM-KUSUM. It listens, responds naturally, collects feedback, and learns over time using machine learning.


# Government Agent: Hindi Voice Assistant for PM-KUSUM Yojana

An AI-powered Hindi voice agent that informs farmers about government schemes like PM-KUSUM. It listens, responds naturally, collects feedback, and learns over time using machine learning.

## 🧠 Project Overview

The `Government Agent` is a voice-based intelligent assistant designed to communicate with Indian farmers in Hindi about the **PM-KUSUM Yojana**, offering details like solar pump subsidies and more. It supports natural speech interaction and adapts over time using collected feedback and training mechanisms.

---

## 📁 Project Structure

```
├── voice_agent.py          # Handles speech recognition and TTS with ElevenLabs
├── feedback_collector.py   # Collects feedback from users for model improvement
├── logger.py               # Logs conversations and feedback for analysis
├── trainer.py              # Trains a simple ML model (Logistic Regression) on feedback
├── main_agent.py           # Orchestrates the voice interaction loop
├── requirements.txt        # All required libraries and versions
└── README.md               # Project documentation
```

---

## 🚀 How It Works

1. **Voice Interaction**: Starts with an introductory message about the PM-KUSUM Yojana in Hindi.
2. **Speech Recognition**: Converts farmer's Hindi speech into text using `SpeechRecognition`.
3. **AI Response**: Uses OpenAI's GPT to generate helpful responses in Hindi.
4. **Text-to-Speech**: Speaks the response using ElevenLabs' Anika voice.
5. **Feedback Logging**: Optionally collects farmer feedback to improve future responses.
6. **Model Training**: `trainer.py` uses feedback to train a logistic regression model to categorize good/bad responses.

---

## 📊 Architecture Diagram

![Flowchart](A_flowchart_infographic_with_a_white_background_de.png)

---

## 🔧 Requirements

Install all dependencies with:

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
openai==1.14.2
elevenlabs==1.1.1
pyaudio==0.2.13
SpeechRecognition==3.10.0
requests==2.31.0
python-dotenv==1.0.1
soundfile==0.12.1
numpy==1.26.4
transformers==4.41.1
torch==2.2.2
librosa==0.10.1
scikit-learn==1.4.2
tqdm==4.66.4
```

---

## 📌 Usage

1. Add your API keys in a `.env` file:

```
OPENAI_API_KEY=your-openai-key
ELEVENLABS_API_KEY=your-elevenlabs-key
```

2. Run the voice agent:

```bash
python main_agent.py
```

3. To retrain model based on user feedback:

```bash
python trainer.py
```

---

## 💡 Future Enhancements

- Multilingual support (Marathi, Bengali, etc.)
- Integration with WhatsApp for farmer queries
- Real-time data analytics dashboard for scheme monitoring

---

## 🧾 License

MIT License © 2025

---
