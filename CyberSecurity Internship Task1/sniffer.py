from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import os

LOG_FILE = "network_log.txt"

def analyze_packet(packet):
    if not packet.haslayer(IP):
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    src_ip    = packet[IP].src
    dst_ip    = packet[IP].dst

    if packet.haslayer(TCP):
        protocol = "TCP"
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
    elif packet.haslayer(UDP):
        protocol = "UDP"
        src_port = packet[UDP].sport
        dst_port = packet[UDP].dport
    elif packet.haslayer(ICMP):
        protocol = "ICMP"
        src_port = "-"
        dst_port = "-"
    else:
        protocol = "OTHER"
        src_port = "-"
        dst_port = "-"

    log_line = (
        f"[{timestamp}] {protocol} | "
        f"{src_ip}:{src_port} -> {dst_ip}:{dst_port}"
    )

    print(log_line)

    with open(LOG_FILE, "a") as f:
        f.write(log_line + "\n")


def main():
    print("=" * 60)
    print("   ARCH TECHNOLOGIES - Basic Network Sniffer")
    print("=" * 60)
    print(f"Capturing packets... Logs saved to: {LOG_FILE}")
    print("Press Ctrl+C to stop.\n")

    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    sniff(prn=analyze_packet, store=False, count=0)


if __name__ == "__main__":
    main()