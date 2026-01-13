PROJETO: Pipeline de ETL com Python (Desafio DIO / Santander Dev Week)
Objetivo: Demonstrar o fluxo de Extração, Transformação e Carregamento de dados.

1. EXTRACT (Extração)
#Simulando a extração de dados de uma lista de usuários (Alternativa 1 do desafio)
users = [
    {"id": 1, "nome": "Marcelo", "saldo": 1500.0, "mensagens": []},
    {"id": 2, "nome": "Ana", "saldo": 25000.0, "mensagens": []},
    {"id": 3, "nome": "Felipe", "saldo": 500.0, "mensagens": []}
]
print(f"Extraídos {len(users)} usuários com sucesso.")

2. TRANSFORM (Transformação)
#Criando uma lógica de recomendação personalizada
def gerar_recomendacao(user):
    if user['saldo'] > 10000:
        return f"Olá {user['nome']}, você tem perfil para nossos investimentos Premium!"
    else:
        return f"Olá {user['nome']}, que tal começar a poupar hoje? Confira nossas dicas!"

for user in users:
    notificacao = gerar_recomendacao(user)
    user['mensagens'].append(notificacao)
    print(f"Transformação concluída para: {user['nome']}")

3. LOAD (Carregamento) ---
#Exibindo os resultados processados (simulando o envio para uma interface ou banco)
print("\n--- RESULTADO FINAL DO PROCESSO ETL ---")
for user in users:
    print(f"ID: {user['id']} | Nome: {user['nome']} | Mensagem: {user['mensagens'][0]}")
