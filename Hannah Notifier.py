import requests
import os
from pystyle import Colorate, Colors
from winotify import Notification, audio
from colorama import Fore
from datetime import datetime

# Define fucntions

def clear():
    os.system("cls") if os.name == "nt" else os.system("cls")

def title(args):
    os.system(f"title {args}")

# Define main variables

ascii_art = """                               _           __      _   _  __ _           
  /\  /\__ _ _ __  _ __   __ _| |__     /\ \ \___ | |_(_)/ _(_) ___ _ __ 
 / /_/ / _` | '_ \| '_ \ / _` | '_ \   /  \/ / _ \| __| | |_| |/ _ \ '__|
/ __  / (_| | | | | | | | (_| | | | | / /\  / (_) | |_| |  _| |  __/ |   
\/ /_/ \__,_|_| |_|_| |_|\__,_|_| |_| \_\ \/ \___/ \__|_|_| |_|\___|_|       
"""

# Get the api info

url = "https://raw.githubusercontent.com/BrookeAFK/brookeafk-api/main/events.js"
r = requests.get(url)
pit_info = r.json()

# Set main lists

events = []
happend_events = []

# Log current events

for event in pit_info:
    event_time = datetime.fromtimestamp(event['timestamp'] / 1000)
    info = (f"{event['event']}|{event_time.strftime('%Y-%m-%d %H:%M')}\n")
    events.append(info)

# For debugging purposes
events.append("If you see this you did a good job|2023-12-02 23:17")

# Main menu

clear()
title("Hannah Notifier")
print(Colorate.Vertical(Colors.purple_to_blue, ascii_art))
print(Colorate.Vertical(Colors.purple_to_red, "\nWelcome to HannahHavens Hypixel pit event notifier"))


# Actual logic


while True:
    for event in events:
        e = event.split('|')
        crnt_time = datetime.now().strftime('%Y-%m-%d %H:%M')
        if e[-1] == crnt_time:
            if event not in happend_events:
                event_toast = Notification(app_id="Hannah Notifier",
                                           title="Event started",
                                           msg=f"Event: {e[0]}\nScheduled time: {e[-1]}\nTime of detection: {crnt_time}",
                                           duration="short"
                                           )
                event_toast.set_audio(audio.Default, loop=False)
                event_toast.show()
                print(f"""
{Fore.YELLOW}[{Fore.RESET}!{Fore.YELLOW}]{Fore.RESET} Event Starting or underway
[{Fore.MAGENTA}*{Fore.RESET}{Fore.RESET}] Event: {e[0]}
[{Fore.MAGENTA}*{Fore.RESET}{Fore.RESET}] Scheduled time: {e[-1]}
[{Fore.MAGENTA}*{Fore.RESET}{Fore.RESET}] Time of detection: {crnt_time}
""")
                happend_events.append(event)
