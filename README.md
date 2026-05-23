# 🖤 BlackMa1ny - Open Source Prank 

⚠️ **CRITICAL DISCLAIMER & SAFETY WARNING**
* **USE AT YOUR OWN RESPONSIBILITY:** The developer assumes no liability for any disruption, temporary system unresponsiveness, or misuse of this software. 
* **TESTING ENVIRONMENT ONLY:** This program is strictly designed to be executed inside a **dedicated testing environment (e.g., Virtual Machines or isolated test benches)**. Do **NOT** run this program on your daily driver computer, production machines, or any active personal workspace.
* **SOURCE-ONLY REPOSITORY:** For infrastructure safety and compliance, this repository **contains only the raw source codes**. No pre-compiled binaries (`.exe`) are provided. You must inspect and compile the binary yourself.

---

## 🎭 The Concept: PlayGames Camouflage (Social Engineering Trick)
While the real project identity is **BlackMa1ny** (or known as **Chase Me**), the compilation automation is engineered to output a standalone binary disguised as **`PlayGames.exe`**. 
* To the target, it looks like a harmless, lightweight retro game application (inviting them to play **"VS BOT"**).
* Once executed, it unpacks the core **BlackMa1ny** architecture (`Main.py` window manipulation loops and the embedded `MEME.wav` sound matrix) to trigger the chaotic simulator.
<img width="482" height="321" alt="Image" src="https://github.com/user-attachments/assets/644e7ace-3627-4873-a762-42eb9b74d10d" />
---

## ⚠️ Infrastructure & System Compatibility
* **CURRENT SUPPORT:** Target architectures are strictly limited to **Windows 10 and Windows 11**. 
* **LEGACY SYSTEMS:** Windows 7/8 support is explicitly **Coming Soon** 🕒 (requires modular downgrade compilation tooling).
* **SAFETY CHECK:** It **DOES NOT** contain any malicious payloads, backdoors, or system bypasses. It **DOES NOT** damage, encrypt, or permanently modify any operating system files. It is purely a benign, chaotic graphical experiment.

---

## ✨ Features
* **Disguised Deployment:** Automated setup that binds the assets into a decoy game identity (`PlayGames.exe`).
* **Boundary Physics:** Dynamic window loops (`CrazyWindow` class) with custom boundary bounce-back physics.
* **Stitched Audio Loop:** Asynchronous audio looping using native Windows components (`winsound`) embedded directly into the final compiled standalone process.

## 🛠️ How to Build and Run (For Windows 10 / 11)

1. Make sure you have **Python 3.10 or higher** installed on your Windows 10/11 development machine.
2. Clone this repository or download the source files into your local `/MM/` directory.
3. Open your terminal and install the compiler dependency:
   ```bash
   pip install pyinstaller
   if exist build rmdir /s /q build
   if exist dist rmdir /s /q dist
   if exist Main.spec del /q Main.spec
   py -m PyInstaller --clean --onefile --noconsole --exclude pygame --add-data "MEME.wav;." Main.py
4. The compiled binary will be generated inside the newly created `dist/` folder as **`PlayGames.exe`** (carrying the hidden BlackMa1ny engine).

---

## 🚨 Resource Usage & Emergency Stop (Safety First)

Because this program spawns windows continuously, it is designed to intensely consume CPU and RAM resources, Pranking a heavy desktop freeze or local system lag. **This is a local Denial of Service (DoS) joking, NOT a destructive virus.** 

If your testing environment starts freezing or lagging during the demonstration, do not panic! You do not need to hard-reset the machine.

### How to Stop the Prank Malware Safely:
1. **Run `fix.cmd`:** Execute the emergency script `fix.cmd` included in the source files. It will instantly terminate the background process loop and clear the desktop.
2. **Task Manager:** Press `Ctrl + Shift + Esc`, locate `PlayGames.exe` (or `python` if running the raw script), and click **End Task**.
3. **Emergency Shortcut:** Alternatively, you can press the `Escape` key on your keyboard while focusing on any of the active prank windows to instantly destroy the program loop and stop the looping audio.
