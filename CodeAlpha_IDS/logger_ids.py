from scapy.all import sniff, IP, TCP, ICMP
from datetime import datetime

print("=" * 60)
print(" Packet Logger Intrusion Detection System")
print(" Monitoring Network Traffic...")
print(" Alerts are being saved into ids_alerts.txt")
print(" Press CTRL + C to stop")
print("=" * 60)

# Log file
log_file = open("ids_alerts.txt", "a")

# Detection function

def detect_intrusion(packet):

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        current_time = datetime.now()

        # ICMP Ping Detection
        if packet.haslayer(ICMP):

            alert = f"[ALERT] ICMP Ping Detected | Time: {current_time} | Source: {source_ip} -> Target: {destination_ip}\n"

            print(alert)
            log_file.write(alert)
            log_file.flush()

        # TCP SYN Scan Detection
        if packet.haslayer(TCP):

            flags = packet[TCP].flags

            if flags == "S":

                alert = f"[ALERT] Possible Port Scan | Time: {current_time} | Source: {source_ip} -> Port: {packet[TCP].dport}\n"

                print(alert)
                log_file.write(alert)
                log_file.flush()

# Start monitoring
sniff(prn=detect_intrusion, store=False)