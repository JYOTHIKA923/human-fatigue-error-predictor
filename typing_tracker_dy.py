from pynput import keyboard, mouse
import time


key_count = 0
backspace_count = 0
pause_time_total = 0
last_key_time = None

mouse_movement = 0
last_mouse_position = None

typed_text = ""



def on_press(key):
    global key_count, backspace_count, last_key_time, pause_time_total, typed_text

    current_time = time.time()

    
    if last_key_time is None:
        last_key_time = current_time

  
    pause = current_time - last_key_time
    if pause > 1:
        pause_time_total += pause

    
    last_key_time = current_time

    
    if hasattr(key, 'char') and key.char is not None:
        key_count += 1
        typed_text += key.char
        
    elif key == keyboard.Key.space:
        key_count += 1
        typed_text += " "

   
    elif key == keyboard.Key.backspace:
        backspace_count += 1
        typed_text = typed_text[:-1]



def on_move(x, y):
    global mouse_movement, last_mouse_position

    if last_mouse_position is None:
        last_mouse_position = (x, y)
        return

    dx = x - last_mouse_position[0]
    dy = y - last_mouse_position[1]

    
    distance = (dx**2 + dy**2) ** 0.5
    mouse_movement += distance

    last_mouse_position = (x, y)



def start_tracking(duration=10):
    global key_count, backspace_count, pause_time_total, last_key_time
    global mouse_movement, last_mouse_position, typed_text

   
    key_count = 0
    backspace_count = 0
    pause_time_total = 0
    last_key_time = None

    mouse_movement = 0
    last_mouse_position = None

    typed_text = ""

    print(f"\nStart typing... (Tracking for {duration} seconds)")

    start_time = time.time()

    
    keyboard_listener = keyboard.Listener(on_press=on_press)
    mouse_listener = mouse.Listener(on_move=on_move)

    keyboard_listener.start()
    mouse_listener.start()

    
    time.sleep(duration)

   
    keyboard_listener.stop()
    mouse_listener.stop()

    total_time = time.time() - start_time

   
    typing_speed = key_count / total_time if total_time > 0 else 0

    
    word_count = len(typed_text.split())

    return typing_speed, pause_time_total, backspace_count, mouse_movement, word_count



if __name__ == "__main__":
    typing_speed, pause_time, backspace, mouse_move, word_count = start_tracking(10)

    print("\n--- RESULTS ---")
    print("Typing Speed (keys/sec):", round(typing_speed, 2))
    print("Total Pause Time (sec):", round(pause_time, 2))
    print("Backspace Count:", backspace)
    print("Mouse Movement:", round(mouse_move, 2))
    print("Word Count (Text Clarity):", word_count)