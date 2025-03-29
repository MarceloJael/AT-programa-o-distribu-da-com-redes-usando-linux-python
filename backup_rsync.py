import os
import subprocess

# Caminhos absolutos
origem = os.path.abspath("origem/")
destino = os.path.abspath("backup/")

# Comando rsync
comando = ["rsync", "-av", origem + "/", destino]

print(f"Executando backup de {origem} para {destino}...\n")

# Executa o comando rsync
processo = subprocess.run(comando, capture_output=True, text=True)

# Exibe saída do rsync
print(processo.stdout)
print("✅ Backup concluído com sucesso!")

