import os
import threading
import time
import datetime
import pandas as pd
import io
import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk

# --- CONFIGURE CUSTOMTKINTER THEME ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# --- MAIN APP CLASS ---
class AIProtectionApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🛡️ AI Protection Console")
        self.geometry("1000x600")

        # Log storage
        self.logs = []

        # Create sidebar + main area
        self._create_sidebar()
        self._create_pages()

        # Start on Home
        self.select_page("Home")

    def _create_sidebar(self):
        self.sidebar = ctk.CTkFrame(self, width=150)
        self.sidebar.pack(side="left", fill="y")

        # Navigation buttons
        for name in ["Home","Monitor","Scan","Controls","Logs"]:
            btn = ctk.CTkButton(self.sidebar, text=name, command=lambda n=name: self.select_page(n))
            btn.pack(fill="x", pady=5, padx=10)

    def _create_pages(self):
        self.pages = {}

        # Container for pages
        container = ctk.CTkFrame(self)
        container.pack(side="right", fill="both", expand=True)

        # Home Page
        home = ctk.CTkFrame(container)
        self.pages["Home"] = home
        # Hero text
        ctk.CTkLabel(home, text="AI Protection Console", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=(20,10))
        ctk.CTkLabel(home, text="Monitor AI chats in real‑time, detect threats, and intervene instantly.").pack(pady=(0,20))
        # Feature cards
        feats = ["Live Monitor","Threat Detection","Automated Controls","Logs & Reports"]
        frame = ctk.CTkFrame(home)
        frame.pack(pady=10, padx=20, fill="x")
        for feat in feats:
            card = ctk.CTkFrame(frame, fg_color="#2b2b38", corner_radius=8)
            card.pack(side="left", expand=True, fill="both", padx=10, pady=10)
            ctk.CTkLabel(card, text=feat, font=ctk.CTkFont(size=16, weight="bold")).pack(pady=20)

        # Monitor Page
        mon = ctk.CTkFrame(container)
        self.pages["Monitor"] = mon
        ctk.CTkLabel(mon, text="🔌 Live Monitor", font=ctk.CTkFont(size=20)).pack(pady=10)
        self.mon_text = ctk.CTkTextbox(mon, width=700, height=400)
        self.mon_text.pack(padx=20, pady=10)
        ctk.CTkButton(mon, text="Start Stream", command=self._start_monitor).pack(pady=5)

        # Scan Page
        scan = ctk.CTkFrame(container)
        self.pages["Scan"] = scan
        ctk.CTkLabel(scan, text="⚠️ Threat Scanner", font=ctk.CTkFont(size=20)).pack(pady=10)
        self.sample_input = ctk.CTkTextbox(scan, width=700, height=200)
        self.sample_input.pack(pady=5)
        self.scan_progress = ctk.CTkProgressBar(scan, width=700)
        self.scan_progress.pack(pady=5)
        ctk.CTkButton(scan, text="Analyze", command=self._run_scan).pack(pady=5)

        # Controls Page
        ctrl = ctk.CTkFrame(container)
        self.pages["Controls"] = ctrl
        ctk.CTkLabel(ctrl, text="⚙️ Automated Controls", font=ctk.CTkFont(size=20)).pack(pady=10)
        for action in ["Emergency Stop","Lock Output","Safe Mode","Purge Memory"]:
            btn = ctk.CTkButton(ctrl, text=action, command=lambda a=action: self._control_action(a))
            btn.pack(fill="x", padx=200, pady=5)

        # Logs Page
        logs = ctk.CTkFrame(container)
        self.pages["Logs"] = logs
        ctk.CTkLabel(logs, text="📜 Logs & Reports", font=ctk.CTkFont(size=20)).pack(pady=10)
        self.logbox = ctk.CTkTextbox(logs, width=700, height=350)
        self.logbox.pack(pady=5)
        btn_frame = ctk.CTkFrame(logs)
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="Export CSV", command=self._export_csv).pack(side="left", padx=10)
        ctk.CTkButton(btn_frame, text="Export PDF", command=self._export_pdf).pack(side="left", padx=10)

        # Place all pages but hide
        for p in self.pages.values():
            p.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

    # Navigation
    def select_page(self, name):
        for n, p in self.pages.items():
            p.lower()
        self.pages[name].lift()

    # Monitor Simulation
    def _start_monitor(self):
        def stream():
            self.mon_text.delete("0.0","end")
            for i in range(8):
                speaker = "User" if i%2==0 else "AI"
                self.mon_text.insert("end", f"[{speaker}] Message {i+1}\n")
                time.sleep(0.5)
            self._log("Stream ended")
        threading.Thread(target=stream, daemon=True).start()
        self._log("Started monitor")

    # Scan Simulation
    def _run_scan(self):
        text = self.sample_input.get("0.0","end")
        words = sum(text.lower().count(w) for w in ["kill","hate","bomb","threat"])
        score = min(words*25, 100)
        def scan():
            self.scan_progress.set(0)
            for i in range(score+1):
                self.scan_progress.set(i/100)
                time.sleep(0.01)
            level = "LOW" if score<30 else "MEDIUM" if score<70 else "HIGH"
            self._log(f"Scan complete (score={score}%, level={level})")
        threading.Thread(target=scan, daemon=True).start()

    # Controls
    def _control_action(self, action):
        self._log(f"Action: {action}")

    # Logging
    def _log(self, event):
        ts = datetime.now().strftime("%H:%M:%S")
        self.logs.append((ts, event))
        self.logbox.insert("end", f"{ts} — {event}\n")

    # Export CSV
    def _export_csv(self):
        df = pd.DataFrame(self.logs, columns=["Time","Event"])
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV","*.csv")])
        if path:
            df.to_csv(path, index=False)
            self._log(f"Exported CSV: {os.path.basename(path)}")

    # Export PDF (basic)
    def _export_pdf(self):
        from reportlab.pdfgen import canvas
        path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF","*.pdf")])
        if path:
            c = canvas.Canvas(path)
            y = 800
            for ts, ev in self.logs:
                c.drawString(50, y, f"{ts} — {ev}")
                y -= 20
                if y < 50:
                    c.showPage(); y = 800
            c.save()
            self._log(f"Exported PDF: {os.path.basename(path)}")

if __name__ == "__main__":
    app = AIProtectionApp()
    app.mainloop()
