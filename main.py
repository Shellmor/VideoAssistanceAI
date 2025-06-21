from analysis.audio_writer import record_while_key_pressed
from win_alert.win import WindowManager
import threading

window_app = None
window_thread = None

def ai_assistant():
    return record_while_key_pressed()


if __name__ == "__main__":
    print("Удерживайте клавишу caps lock для записи...")
    manager = WindowManager()

    def listen_and_notify():
        while True:
            ai_message = record_while_key_pressed()
            manager.show_window(ai_message)

    threading.Thread(target=listen_and_notify, daemon=True).start()
    manager.mainloop()
