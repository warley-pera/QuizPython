# Perguntas
perguntas.extend([
    {
        "pergunta": "Quem foi o físico responsável pela formulação da teoria da relatividade?",
        "opcoes": ["Isaac Newton", "Albert Einstein", "Galileu Galilei", "Charles Darwin"],
        "resposta": "Albert Einstein"
    },
    {
        "pergunta": "Qual é o maior oceano do mundo?",
        "opcoes": ["Oceano Atlântico", "Oceano Índico", "Oceano Pacífico", "Oceano Ártico"],
        "resposta": "Oceano Pacífico"
    },
    {
        "pergunta": "Qual é o país mais populoso do mundo?",
        "opcoes": ["Índia", "China", "Estados Unidos", "Brasil"],
        "resposta": "China"
    },
    {
        "pergunta": "Quem escreveu a peça de teatro 'Romeu e Julieta'?",
        "opcoes": ["William Shakespeare", "Miguel de Cervantes", "Friedrich Nietzsche", "Charles Dickens"],
        "resposta": "William Shakespeare"
    },
    {
        "pergunta": "Qual é a fórmula matemática mais famosa?",
        "opcoes": ["E = mc^2", "Pythagorean theorem", "F = ma", "y = mx + b"],
        "resposta": "E = mc^2"
    }
])
# Função para exibir uma pergunta e receber a resposta do usuário
def exibir_pergunta(pergunta):
    print(pergunta["pergunta"])
    for i, opcao in enumerate(pergunta["opcoes"]):
        print(f"{i+1}. {opcao}")
    resposta = input("Digite o número da opção correta: ")
    return resposta

# Função para verificar se a resposta está correta
def verificar_resposta(pergunta, resposta):
    return pergunta["opcoes"][int(resposta)-1] == pergunta["resposta"]

# Função principal do quiz
def quiz():
    pontuacao = 0
    for pergunta in perguntas:
        resposta = exibir_pergunta(pergunta)
        if verificar_resposta(pergunta, resposta):
            print("Resposta correta!\n")
            pontuacao += 1
        else:
            print("Resposta incorreta!\n")
    print(f"Você acertou {pontuacao} de {len(perguntas)} perguntas.")

# Executar o quiz
quiz()