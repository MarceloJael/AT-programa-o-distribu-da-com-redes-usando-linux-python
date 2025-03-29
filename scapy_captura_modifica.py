from scapy.all import sniff, IP, send

# Função de callback chamada para cada pacote capturado
def manipular_pacote(pacote):
    if IP in pacote:
        print(f"\n📦 Pacote capturado:")
        print(f"De: {pacote[IP].src} → Para: {pacote[IP].dst} | TTL: {pacote[IP].ttl}")

        # Modifica o TTL do pacote
        pacote[IP].ttl = 99

        # Reenvia o pacote modificado
        send(pacote)
        print("✅ Pacote modificado e reenviado (TTL = 99)")

# Captura 5 pacotes na interface padrão (modo promíscuo opcional)
print("🎯 Capturando pacotes... Pressione Ctrl+C para sair.")
sniff(filter="ip", prn=manipular_pacote, count=5)

