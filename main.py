from typing_tracker_dy import start_tracking


def predict_fatigue(typing_speed, pause_time, backspace, mouse_move, word_count):
    score = 0
    reasons = []

   
    if typing_speed < 3:
        score += 2
        reasons.append("Low typing speed")

   
    if pause_time > 5:
        score += 2
        reasons.append("Long pauses")

   
    if backspace > 10:
        score += 2
        reasons.append("High typing mistakes")

    
    if mouse_move > 1000:
        score += 1
        reasons.append("Unstable mouse movement")

 
    if word_count < 3:
        score += 1
        reasons.append("Poor text clarity")

    
    score = min(score * 2, 10)
    
    
    if score >= 6 :
        level = "HIGH fatigue"
    elif 3 <= score <= 5:
        level = "MEDIUM fatigue"
    else:
        level = "LOW fatigue"

    return level, reasons, score


if __name__ == "__main__":

    
    typing_speed, pause_time, backspace, mouse_move, word_count = start_tracking(10)

    print("\n--- TRACKING RESULTS ---")
    print("Typing Speed:", round(typing_speed, 2))
    print("Pause Time:", round(pause_time, 2))
    print("Backspace:", backspace)
    print("Mouse Movement:", round(mouse_move, 2))
    print("Word Count:", word_count)

   
    level, reasons, fatigue_score = predict_fatigue(
        typing_speed, pause_time, backspace, mouse_move, word_count
    )

    print("\n--- FATIGUE RESULT ---")
    print("Fatigue Level:", level)
    print("Fatigue Score:", fatigue_score)

    print("Reasons:")
    for r in reasons:
        print("-", r)

 