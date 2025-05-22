from datetime import datetime
import json

contador_arquivo = "contador.json"
readme_arquivo = "README.md"

# Carregar contador existente
try:
    with open(contador_arquivo, "r") as f:
        data = json.load(f)
        contador = data.get("contador", 0)
        ultima_atualizacao = data.get("ultima_atualizacao", "")
except FileNotFoundError:
    contador = 0
    ultima_atualizacao = ""

# Obter a data atual
hoje = datetime.now().strftime("%Y-%m-%d")

if hoje > ultima_atualizacao and datetime.now().strftime("%m-%d") == "04-15":
    contador += 1
    ultima_atualizacao = hoje

# Salvar contador atualizado
with open(contador_arquivo, "w") as f:
    json.dump({"contador": contador, "ultima_atualizacao": ultima_atualizacao}, f)

# Atualizar README.md
with open(readme_arquivo, "r") as f:
    conteudo = f.read()

novo_texto = f"**Atualizações:** {contador} vezes desde a criação.\n"
if "Atualizações:" in conteudo:
    conteudo = conteudo.replace("Atualizações:", novo_texto)
else:
    conteudo += f"\n{novo_texto}"

with open(readme_arquivo, "w") as f:
    f.write(conteudo)

print(f"✅ Contador atualizado para {contador}.")
