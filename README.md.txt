🪞 MoodMirror – Emotion-Based Python Assistant

*MoodMirror* is a mini project developed using Python that detects your mood from the text you type and gives motivational quotes based on how you feel – happy, sad, anxious, or neutral.

It uses *TextBlob* for sentiment analysis and *Tkinter* for creating a simple dark-themed GUI. The project also includes a *quote randomizer* and *mood log feature* to keep track of how you're feeling each time.

---

## 💡 Features

- 🔍 Detects emotion from user input
- 💬 Gives motivational quotes based on detected mood
- 🔀 Shows a new quote every time (non-repetitive)
- 🖤 Dark mode GUI using Tkinter
- 🧠 Sentiment analysis with TextBlob
- 📝 Logs mood history to a .txt file

---

## 🛠 Tech Stack

- Python 3.13.5  
- Tkinter  
- TextBlob  
- Random module  

---

## 📂 Project Structure

```bash
MoodMirror-Emotion-Assistant/
│
├── moodmirror.py         # Main GUI program
├── quotes.json           # Quotes stored by emotion
├── mood_log.txt          # Automatically generated mood log
└── README.md 
