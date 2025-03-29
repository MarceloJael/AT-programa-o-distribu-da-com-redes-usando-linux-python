from scapy.all import sniff, ARP

# Tabela para armazenar pares IP↔MAC conhecidos
tabela_arp = {}

def detectar_spoof(pacote):
    if pacote.haslayer(ARP) and pacote[ARP].op == 2:  # ARP reply
        ip = pacote[ARP].psrc
        mac = pacote[ARP].hwsrc

        if ip in tabela_arp:
            if tabela_arp[ip] != mac:
                print(f"\n🚨 POSSÍVEL ATAQUE ARP SPOOFING DETECTADO!")
                print(f"↪ IP: {ip} estava com MAC: {tabela_arp[ip]}, agora responde com MAC: {mac}")
        else:
            tabela_arp[ip] = mac
            print(f"[INFO] Novo IP detectado: {ip} ↔ {mac}")

print("🔎 Monitorando pacotes ARP... Pressione Ctrl+C para encerrar.")
sniff(filter="arp", store=0, prn=detectar_spoof)

