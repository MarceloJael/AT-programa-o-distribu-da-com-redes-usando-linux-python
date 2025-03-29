from scapy.all import sniff, IP, TCP, UDP, ICMP

def analisar_pacote(pacote):
    if IP in pacote:
        src = pacote[IP].src
        dst = pacote[IP].dst

        if TCP in pacote:
            print(f"[TCP] {src} → {dst} | Porta: {pacote[TCP].dport}")
        elif UDP in pacote:
            print(f"[UDP] {src} → {dst} | Porta: {pacote[UDP].dport}")
        elif ICMP in pacote:
            print(f"[ICMP] {src} → {dst}")
        else:
            print(f"[IP] {src} → {dst}")

print("🔎 Monitorando tráfego de pacotes... Pressione Ctrl+C para parar.")
sniff(prn=analisar_pacote, filter="ip", store=0)

