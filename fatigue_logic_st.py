
def predict_fatigue(typing_speed, pause_time, backspace_count, mouse_movement, sentence_length):
    score = 0
    reasons = []

    
    if typing_speed < 3:
        score += 2
        reasons.append("Low typing speed")

    
    if pause_time > 5:
        score += 2
        reasons.append("Long pauses")

    
    if backspace_count > 10:
        score += 2
        reasons.append("High typing mistakes")

  
    if mouse_movement > 1050:   
        score += 1
        reasons.append("Unstable mouse movement")

    
    if sentence_length < 5:
        score += 1
        reasons.append("Poor sentence clarity")

    
    if score >= 6:
        level = "HIGH fatigue"
    elif score >= 3:
        level = "MEDIUM fatigue"
    else:
        level = "LOW fatigue"

    return level, reasons



if __name__ == "__main__":
    typing_speed = float(input("Enter typing speed (keys/sec): "))
    pause_time = float(input("Enter pause time (seconds): "))
    backspace_count = int(input("Enter backspace count: "))
    mouse_movement = float(input("Enter mouse movement value: "))
    sentence_length = int(input("Enter sentence length (number of words): "))

    result, reasons = predict_fatigue(
        typing_speed, pause_time, backspace_count, mouse_movement, sentence_length
    )

    print("\nFatigue Level:", result)
    print("Reasons:")
    for r in reasons:
        print("-", r)
        