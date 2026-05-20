import tkinter as tk
import subprocess

def rafraichir_compteur():
    nb_cmd = 0
    nb_blackma1ny = 0
    
    try:
        output = subprocess.check_output("tasklist", shell=True, text=True)
        nb_blackma1ny = output.count("BlackMa1ny.exe")
        nb_cmd = output.count("cmd.exe")
    except:
        pass

    # Met à jour les statistiques à l'écran
    lbl_black.config(text=f"⚙️ BlackMa1ny.exe : {nb_blackma1ny} fenêtre(s)")
    lbl_autres.config(text=f"💻 Invites CMD (Watch) : {nb_cmd - 1 if nb_cmd > 0 else 0} fenêtre(s)")

    root.after(500, rafraichir_compteur)

root = tk.Tk()
root.title("PlayGames - Live Monitor")
root.geometry("320x150")
root.configure(bg="#222222")

style_font = ("Courier", 11, "bold")

tk.Label(root, text="--- LIVE WINDOWS COUNT ---", font=("Courier", 12, "bold"), fg="white", bg="#222222").pack(pady=10)
lbl_black = tk.Label(root, text="⚙️ BlackMa1ny.exe : 0", font=style_font, fg="#00FF00", bg="#222222")
lbl_black.pack(anchor="w", padx=20, pady=5)
lbl_autres = tk.Label(root, text="💻 Invites CMD (Watch) : 0", font=style_font, fg="#00FF00", bg="#222222")
lbl_autres.pack(anchor="w", padx=20, pady=5)

rafraichir_compteur()
root.mainloop()