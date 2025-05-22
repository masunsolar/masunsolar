from datetime import datetime

# Data de nascimento
nascimento = datetime(2005, 4, 15)

# Data atual
hoje = datetime.now()

# Calcula idade
idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))

# Lê o arquivo README.md
with open("README.md", "r", encoding="utf-8") as file:
    conteudo = file.read()

# Substitui o placeholder {{idade}} pela idade atual
conteudo = conteudo.replace("{{idade}}", str(idade))

# Salva o arquivo atualizado
with open("README.md", "w", encoding="utf-8") as file:
    file.write(conteudo)
