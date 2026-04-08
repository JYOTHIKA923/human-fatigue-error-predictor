import tkinter as tk
import threading

from typing_tracker_dy import start_tracking
from main import predict_fatigue


def run_analysis():
    status_label.config(text="Tracking... Type for 10 seconds", fg="orange")
    thread = threading.Thread(target=track_and_display)
    thread.start()


-
def track_and_display():
    typing_speed, pause_time, backspace, mouse_move, word_count = start_tracking(10)

    
    level, reasons, fatigue_score = predict_fatigue(
        typing_speed, pause_time, backspace, mouse_move, word_count
    )

    root.after(0, update_gui, typing_speed, pause_time, backspace,
               mouse_move, word_count, level, reasons, fatigue_score)


def update_gui(typing_speed, pause_time, backspace, mouse_move,
               word_count, level, reasons, fatigue_score):

   
    if "HIGH" in level:
        color = "red"
    elif "MEDIUM" in level:
        color = "orange"
    else:
        color = "green"

    
    result_text.set(f"Fatigue Level: {level}\nFatigue Score: {fatigue_score}/10")
    result_label.config(fg=color)


    details = f"""
Typing Speed: {round(typing_speed, 2)}
Pause Time: {round(pause_time, 2)}
Backspace: {backspace}
Mouse Movement: {round(mouse_move, 2)}
Word Count: {word_count}

Reasons:
"""
    for r in reasons:
        details += f"• {r}\n"

    details_label.config(text=details)

  
    status_label.config(text="Analysis Complete ", fg="green")



root = tk.Tk()
root.title("AI Fatigue Detection System")
root.geometry("600x520")
root.configure(bg="#1e1e2f")


title = tk.Label(
    root,
    text=" Human Fatigue Predictor",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=15)


start_button = tk.Button(
    root,
    text="Start Analysis",
    command=run_analysis,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=15,
    pady=6
)
start_button.pack(pady=10)


status_label = tk.Label(
    root,
    text="Click 'Start Analysis' to begin",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="lightgray"
)
status_label.pack(pady=5)


result_text = tk.StringVar()
result_label = tk.Label(
    root,
    textvariable=result_text,
    font=("Arial", 16, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=15)


details_label = tk.Label(
    root,
    text="",
    justify="left",
    font=("Consolas", 10),
    bg="#2a2a40",
    fg="white",
    padx=10,
    pady=10,
    anchor="nw"
)
details_label.pack(pady=10, fill="both", expand=True)


root.mainloop()