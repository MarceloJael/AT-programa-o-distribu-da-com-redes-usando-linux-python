import nmap
import threading

nm = nmap.PortScanner()

alvo = input("Digite o IP ou domínio do alvo: ")

# ---------- SCAN SÍNCRONO ----------
print(f"\n🔍 Varredura SÍNCRONA em {alvo} nas portas 20-100...\n")
nm.scan(hosts=alvo, arguments='-p 20-100')
for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"Estado: {nm[host].state()}")
    for proto in nm[host].all_protocols():
        portas = nm[host][proto].keys()
        for porta in sorted(portas):
            estado = nm[host][proto][porta]['state']
            print(f"Porta {porta}/{proto} → {estado}")

# ---------- SCAN ASSÍNCRONO ----------
def scan_assincrono(ip, porta):
    try:
        resultado = nmap.PortScanner()
        resultado.scan(ip, str(porta))
        estado = resultado[ip]['tcp'][porta]['state']
        if estado == 'open':
            print(f"✅ Porta {porta} ABERTA em {ip}")
    except:
        pass

print(f"\n⚡ Iniciando SCAN ASSÍNCRONO nas portas 80, 443, 8080...\n")
portas_para_testar = [80, 443, 8080]
threads = []

for p in portas_para_testar:
    t = threading.Thread(target=scan_assincrono, args=(alvo, p))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

