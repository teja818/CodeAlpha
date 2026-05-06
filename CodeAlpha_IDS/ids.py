from scapy.all import sniff, IP, TCP, ICMP
from datetime import datetime

print("=" * 60)
print(" Basic Intrusion Detection System (IDS)")
print(" Monitoring Network Traffic...")
print(" Press CTRL + C to stop")
print("=" * 60)

# Detect suspicious packets
def detect_intrusion(packet):

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        current_time = datetime.now()

        # ICMP Detection (Ping)
        if packet.haslayer(ICMP):

            print("\n[ALERT] ICMP Ping Detected!")
            print(f"Time       : {current_time}")
            print(f"Source IP  : {source_ip}")
            print(f"Target IP  : {destination_ip}")

        # TCP Port Scan Detection
        if packet.haslayer(TCP):

            tcp_flags = packet[TCP].flags

            # SYN packet detection
            if tcp_flags == "S":

                print("\n[ALERT] Possible TCP Port Scan Detected!")
                print(f"Time       : {current_time}")
                print(f"Source IP  : {source_ip}")
                print(f"Target IP  : {destination_ip}")
                print(f"Destination Port : {packet[TCP].dport}")

# Start sniffing
sniff(prn=detect_intrusion, store=False)