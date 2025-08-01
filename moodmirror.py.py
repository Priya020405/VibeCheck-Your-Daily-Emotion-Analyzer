import tkinter as tk
from tkinter import messagebox
from textblob import TextBlob
import datetime
import random

# --- Motivational Quotes with Emojis ---
quotes = {
    "happy": [
        "Smile big 😊 Laugh loud 😂 Shine bright ✨",
        "You’re glowing today! 🌟 Keep spreading sunshine ☀",
        "Dance like nobody’s watching 💃🎶 Be your happiest self!",
        "Joy is in the little things 🌸✨",
        "Keep that sparkle in your soul ✨ and a smile on your face 😊"
    ],
    "sad": [
        "It's okay to not be okay 😔 Just take a deep breath 🌬 and start again 🌱",
        "Even the darkest night will end 🌌 and the sun will rise again ☀",
        "Crying doesn’t make you weak 😢 It means you’ve been strong for too long 💗",
        "Pause. Breathe. Trust. 🌬💖 You’re doing better than you think.",
        "Sending you a virtual hug 🤗 You’re not alone."
    ],
    "anxious": [
        "Breathe in calm 🌬 Breathe out stress 😮‍💨 You’ve got this 💪",
        "One step at a time 👣 You don’t need to figure it all out today 🕊",
        "It’s okay to pause ⏸ Rest is also part of progress 🌱",
        "Let go of what you can’t control 🕊 Focus on your next small move 🎯",
        "Be kind to yourself 💖 You’re trying your best and that’s enough 🌷"
    ],
    "neutral": [
        "Not every day needs to be exciting ✨ Peace is also beautiful 🌿",
        "Take it slow today 🐢 You’re allowed to just be 🤍",
        "Be present 🕰 Not perfect 🌼",
        "Breathe. Pause. Repeat. 🌬 Sometimes stillness is progress too ⏳",
        "You’re doing fine — even if nothing big is happening today 🌸"
    ]
}

# --- Detect Mood from Text ---
def detect_mood(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.3:
        return "happy"
    elif polarity < -0.3:
        return "sad"
    elif -0.3 <= polarity <= 0.3 and len(text.strip()) > 3:
        return "anxious"
    else:
        return "neutral"

# --- Analyze and Display Mood ---
def check_mood():
    user_input = entry.get()
    if not user_input.strip():
        messagebox.showwarning("Warning", "Please type something.")
        return

    mood = detect_mood(user_input)
    quote = random.choice(quotes[mood])

    result_label.config(text=f"Mood: {mood.upper()}\n\n\"{quote}\"")

    #Change background color
    colors = {
        "happy": "lightyellow",
        "sad": "lightblue",
        "anxious": "lightgrey",
        "neutral": "white"
    }
    window.config(bg=colors[mood])
    result_label.config(bg=colors[mood])
    title_label.config(bg=colors[mood])
    entry.config(bg="black")

    # Log entry
    now = datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")
    with open("mood_log.txt", "a") as log_file:
        log_file.write(f"[{now}] Mood: {mood.capitalize()} → \"{user_input.strip()}\"\n")

# --- Tkinter GUI Setup ---
window = tk.Tk()
window.title("MoodMirror - Emotion Assistant")
window.geometry("420x320")
window.config(bg="black")

title_label = tk.Label(window, text="MoodMirror 🪞", font=("Arial", 16, "bold"), bg="white", fg="black")
title_label.pack(pady=10)

entry = tk.Entry(window, width=50, bg="#1e1e1e", fg="white", insertbackground="white")
entry.pack(pady=10)

check_button = tk.Button(window, text="Check Mood", command=check_mood, bg="#444444", fg="white", activebackground="#666666")
check_button.pack(pady=5)

result_label = tk.Label(window, text="", font=("Arial", 12), bg="black", fg="black", wraplength=380, justify="center")
result_label.pack(pady=20)

window.mainloop()
