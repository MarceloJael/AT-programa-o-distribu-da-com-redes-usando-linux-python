import dns.resolver
import dns.query
import subprocess

dominio = input("Digite o domínio a consultar (ex: google.com): ")

def consultar(registro):
    try:
        resposta = dns.resolver.resolve(dominio, registro)
        for r in resposta:
            print(f"{registro} → {r}")
    except:
        print(f"{registro} → Nenhum registro encontrado ou erro.")

print(f"\n🔎 Coletando informações DNS sobre {dominio}\n")

for tipo in ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT']:
    consultar(tipo)

# Executar dnsrecon (caso instalado)
print("\n📡 Executando dnsrecon (se estiver instalado)...")
try:
    subprocess.run(["dnsrecon", "-d", dominio], check=True)
except:
    print("dnsrecon não está instalado. Ignorando...")

