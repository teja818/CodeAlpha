from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

packet_count = 0

# Function to identify protocol names
def get_protocol_name(protocol_num):
    if protocol_num == 6:
        return "TCP"
    elif protocol_num == 17:
        return "UDP"
    elif protocol_num == 1:
        return "ICMP"
    else:
        return "Other"

# Packet processing function
def packet_callback(packet):
    global packet_count
    packet_count += 1

    print("\n" + "=" * 50)
    print(f"Packet Number : {packet_count}")
    print(f"Time          : {datetime.now()}")

    if packet.haslayer(IP):

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol_num = packet[IP].proto
        protocol_name = get_protocol_name(protocol_num)

        print(f"Source IP     : {source_ip}")
        print(f"Destination IP: {destination_ip}")
        print(f"Protocol      : {protocol_name}")

        # TCP Details
        if packet.haslayer(TCP):
            print(f"Source Port   : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        # UDP Details
        elif packet.haslayer(UDP):
            print(f"Source Port   : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        # ICMP Details
        elif packet.haslayer(ICMP):
            print("ICMP Packet Detected")

        # Packet Length
        print(f"Packet Length : {len(packet)} bytes")

        # Payload
        print(f"Payload       : {packet.summary()}")

# Start sniffing
print("=" * 50)
print("Starting Advanced Network Sniffer...")
print("Press CTRL + C to stop")
print("=" * 50)

sniff(prn=packet_callback, store=False)