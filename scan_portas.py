from scapy.all import IP, TCP, sr1
import sys

alvo = input("Digite o IP do alvo: ")
portas = [22, 80, 443, 8080]  # portas a escanear

print(f"\n🔍 Escaneando portas de {alvo}...\n")

for porta in portas:
    pacote = IP(dst=alvo)/TCP(dport=porta, flags="S")
    resposta = sr1(pacote, timeout=1, verbose=0)

    if resposta is None:
        print(f"❌ Porta {porta}: sem resposta (filtrada ou fechada)")
    elif resposta.haslayer(TCP):
        if resposta[TCP].flags == 0x12:
            print(f"✅ Porta {porta}: ABERTA")
            # Enviar RST para fechar a conexão
            rst = IP(dst=alvo)/TCP(dport=porta, flags="R")
            sr1(rst, timeout=1, verbose=0)
        elif resposta[TCP].flags == 0x14:
            print(f"⛔ Porta {porta}: FECHADA")

