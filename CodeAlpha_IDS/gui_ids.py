import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from scapy.all import sniff, IP, TCP, ICMP
from datetime import datetime
import threading

packet_count = 0

# Main GUI Window
root = tk.Tk()
root.title("Mini IDS Dashboard")
root.geometry("800x500")

# Title Label
label = tk.Label(root, text="Intrusion Detection System", font=("Arial", 18, "bold"))
label.pack(pady=10)

# Packet Counter
counter_label = tk.Label(root, text="Packets Monitored: 0", font=("Arial", 12))
counter_label.pack()

# Alert Box
alert_box = ScrolledText(root, width=95, height=22)
alert_box.pack(pady=10)

# Packet Detection Function

def detect_intrusion(packet):
    global packet_count

    packet_count += 1

    counter_label.config(text=f"Packets Monitored: {packet_count}")

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        current_time = datetime.now().strftime("%H:%M:%S")
               # ICMP Detection
        if packet.haslayer(ICMP):
            alert = f"[ALERT] ICMP Ping Detected | Time: {current_time} | Source: {source_ip} -> Target: {destination_ip}\n"
            alert_box.insert(tk.END, alert)
            alert_box.see(tk.END)

        # TCP SYN Scan Detection
        if packet.haslayer(TCP):
            flags = packet[TCP].flags

            if flags == "S":
                alert = f"[ALERT] Possible Port Scan | Time: {current_time} | Source: {source_ip} -> Port: {packet[TCP].dport}\n"
                alert_box.insert(tk.END, alert)
                alert_box.see(tk.END)

# Start Monitoring Function

def start_monitoring():
    sniff(prn=detect_intrusion, store=False)

# Threading for GUI responsiveness

def run_ids():
    thread = threading.Thread(target=start_monitoring)
    thread.daemon = True
    thread.start()

# Start Button
start_button = tk.Button(root, text="Start Monitoring", font=("Arial", 12), command=run_ids)
start_button.pack(pady=5)

root.mainloop()