import os

dominio = input("Digite o domínio (ex: google.com): ")

print(f"\n🔍 Coletando informações sobre {dominio}...\n")

# WHOIS
print("📄 WHOIS:")
os.system(f"whois {dominio}")

# DNS - NSLOOKUP
print("\n🌐 NSLOOKUP:")
os.system(f"nslookup {dominio}")

# DNS - DIG
print("\n🔎 DIG (registro A):")
os.system(f"dig {dominio} +short")

# HOST
print("\n📌 HOST:")
os.system(f"host {dominio}")

# PING
print("\n📶 PING:")
os.system(f"ping -c 3 {dominio}")

# HEADERS HTTP
print("\n📥 Cabeçalhos HTTP (curl -I):")
os.system(f"curl -I http://{dominio}")

# NMAP
print("\n🚪 NMAP - portas comuns:")
os.system(f"nmap -F {dominio}")

