# Basic Network Sniffer

## 📌 Project Overview
This project is a Python-based Network Sniffer developed as part of the CodeAlpha Cyber Security Internship.

The tool captures live network traffic packets and analyzes their structure and content in real time.

It displays:
- Source IP Address
- Destination IP Address
- Protocol Type
- Source & Destination Ports
- Packet Length
- Packet Payload Information

---

## 🚀 Features

✅ Live packet capturing  
✅ Real-time traffic monitoring  
✅ TCP/UDP/ICMP protocol detection  
✅ Source and destination IP analysis  
✅ Port number monitoring  
✅ Packet size analysis  
✅ Packet payload inspection  
✅ Professional terminal output formatting  

---

## 🛠️ Technologies Used

- Python 3
- Scapy
- Npcap
- Visual Studio Code

---

## 📂 Project Structure

```bash
CodeAlpha_NetworkSniffer/
│
├── sniffer.py
├── README.md
└── screenshots/
```

---

## ▶️ Installation

### Step 1: Install Python
Download Python from:
https://www.python.org/downloads/

### Step 2: Install Scapy

```bash
pip install scapy
```

### Step 3: Install Npcap
Download Npcap from:
https://npcap.com/#download

During installation enable:
- Install Npcap in WinPcap API-compatible Mode

---

## ▶️ How to Run

Open terminal inside project folder and run:

```bash
python sniffer.py
```

---

## 📌 Sample Output

```text
==================================================
Packet Number : 1
Time          : 2026-05-06 21:40:11

Source IP     : 192.168.1.5
Destination IP: 142.250.183.78
Protocol      : TCP
Source Port   : 52431
Destination Port: 443
Packet Length : 74 bytes
Payload       : IP / TCP
==================================================
```

---

## 📚 Concepts Learned

- Packet Sniffing
- TCP/IP Networking
- Protocol Analysis
- Network Monitoring
- Cyber Security Fundamentals
- Real-time Traffic Inspection

---

## 🎯 Internship Task Objective

The objective of this task is to:
- Understand how network packets flow
- Analyze packet structure
- Learn protocol behavior
- Build hands-on cybersecurity skills using Python

---

## 👨‍💻 Author

**Ch. Tej Avinash Reddy**  
Cyber Security Intern — CodeAlpha

---

## 📜 License

This project is created for educational and internship purposes.
