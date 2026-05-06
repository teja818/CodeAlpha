# Intrusion Detection System (IDS) Projects

## 📌 Project Overview

This repository contains multiple Python-based Intrusion Detection System (IDS) projects developed as part of the CodeAlpha Cyber Security Internship.

The projects monitor live network traffic, detect suspicious activities, generate alerts, and perform real-time network analysis.

The IDS projects include:
- Basic Packet-Based IDS
- GUI Intrusion Detection System
- Packet Logger IDS

These projects demonstrate practical concepts of:
- Network Security
- Packet Analysis
- Threat Detection
- Intrusion Detection
- Real-Time Traffic Monitoring

---

# 🚀 Projects Included

## 1️⃣ Basic IDS

A simple IDS that monitors packets and detects:
- ICMP Ping Requests
- TCP SYN Scans
- Suspicious Network Traffic

File:
```bash
ids.py
```

---

## 2️⃣ GUI IDS

A graphical Intrusion Detection System with:
- Live dashboard
- Real-time alerts
- Packet monitoring
- Threat detection
- Packet counter

File:
```bash
gui_ids.py
```

---

## 3️⃣ Packet Logger IDS

A logging-based IDS that:
- Detects suspicious traffic
- Generates alerts
- Stores alerts into log files

File:
```bash
logger_ids.py
```

---

# 🛠️ Technologies Used

- Python 3
- Scapy
- Tkinter
- Npcap
- Visual Studio Code

---

# 📂 Project Structure

```bash
CodeAlpha_IDS/
│
├── gui_ids.py
├── ids.py
├── logger_ids.py
├── ids_alerts.txt
├── README.md
└── screenshots/
```

---

# 🚀 Features

✅ Real-time packet monitoring  
✅ ICMP ping detection  
✅ TCP SYN scan detection  
✅ GUI dashboard monitoring  
✅ Packet logging system  
✅ Threat alert generation  
✅ Network traffic analysis  
✅ Live intrusion detection  
✅ Timestamp-based alert logging  

---

# ▶️ Installation

## Step 1 — Install Python

Download Python:
https://www.python.org/downloads/

---

## Step 2 — Install Scapy

```bash
pip install scapy
```

---

## Step 3 — Install Npcap

Download Npcap:
https://npcap.com/#download

During installation enable:
- Install Npcap in WinPcap API-compatible Mode

---

# ▶️ How to Run

## Run Basic IDS

```bash
python ids.py
```

---

## Run GUI IDS

```bash
python gui_ids.py
```

---

## Run Packet Logger IDS

```bash
python logger_ids.py
```

---

# 📌 How the IDS Works

The IDS continuously monitors network traffic and detects suspicious activities.

## ICMP Detection
Detects ping requests and generates alerts.

## TCP SYN Scan Detection
Detects possible port scanning attempts.

## Packet Logging
Stores detected alerts into:
```text
ids_alerts.txt
```

---

# 📌 Sample Alerts

```text
[ALERT] ICMP Ping Detected
[ALERT] Possible TCP Port Scan
```

---

# 📸 Project Screenshots

## GUI IDS Dashboard

![GUI IDS](screenshots/Output-1.png)

## Live Alert Monitoring

![Alerts](screenshots/Output-2.png)

## Network Detection Output

![Detection](screenshots/Output-3.png)

## IDS Monitoring

![Monitoring](screenshots/Output-4.png)

---

# 📚 Concepts Learned

- Intrusion Detection Systems
- Packet Analysis
- Threat Detection
- Network Monitoring
- TCP/IP Networking
- Cyber Security Fundamentals
- Real-Time Traffic Analysis

---

# 🎯 Internship Task Objective

The objective of this task is to:
- Monitor live network traffic
- Detect suspicious activity
- Generate alerts
- Analyze packets
- Understand IDS concepts and network security

---

# 👨‍💻 Author

**Ch. Tej Avinash Reddy**  
Cyber Security Intern — CodeAlpha

---

# 📜 Disclaimer

This project is created for educational and internship purposes only.