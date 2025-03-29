import pcapy
import sys

# Lista interfaces disponíveis
interfaces = pcapy.findalldevs()
print("Interfaces disponíveis:")
for i, iface in enumerate(interfaces):
    print(f"{i} - {iface}")

# Escolha da interface
iface = interfaces[0]
print(f"\nCapturando na interface: {iface}")

# Abre a interface em modo promiscuo
cap = pcapy.open_live(iface, 65536, 1, 1000)

# Callback para exibir pacotes
def receber_pacote(hdr, data):
    print(f"\n📦 Pacote capturado: {len(data)} bytes")
    print(data.hex())

# Inicia captura de 5 pacotes
cap.loop(5, receber_pacote)

