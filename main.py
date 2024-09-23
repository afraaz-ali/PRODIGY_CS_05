from scapy.all import sniff, IP, TCP, UDP, ICMP

# Function to handle captured packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")

        # Identify and print protocol type (TCP, UDP, ICMP)
        if protocol == 6 and TCP in packet:  # TCP Protocol
            print(f"Protocol: TCP, Source Port: {packet[TCP].sport}, Destination Port: {packet[TCP].dport}")
            # Check if there is a payload in the TCP packet
            if packet[TCP].payload:
                print(f"Payload Data: {bytes(packet[TCP].payload)[:50]}")  # Display a portion of the payload
        elif protocol == 17 and UDP in packet:  # UDP Protocol
            print(f"Protocol: UDP, Source Port: {packet[UDP].sport}, Destination Port: {packet[UDP].dport}")
            # Check if there is a payload in the UDP packet
            if packet[UDP].payload:
                print(f"Payload Data: {bytes(packet[UDP].payload)[:50]}")  # Display a portion of the payload
        elif protocol == 1 and ICMP in packet:  # ICMP Protocol
            print("Protocol: ICMP")
        print("\n")

# Sniff packets using Scapy
def start_sniffing():
    print("Starting packet sniffing...")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    start_sniffing()
