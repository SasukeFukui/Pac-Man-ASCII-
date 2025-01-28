# Função para mostrar os dados guardados
def mostrame():
    with open('score.bin', 'r') as arquivo:  
        conteudo = arquivo.read()  
        ave = conteudo.split("----------------------------------------")  
        ave_limpa = [linha.strip() for linha in ave if linha.strip()]  

        jogadores = []
        for linha in ave_limpa:
            dados = linha.split('\n')  
            jogador = {}
            for dado in dados:
                if ': ' in dado:  
                    chave, valor = dado.split(': ', 1) 
                    jogador[chave] = valor.strip() 

            if 'Player' in jogador:
                jogadores.append(jogador)

        for jogador in jogadores:
            if 'Score' not in jogador:
                jogador['Score'] = 0  
            if 'venceu' not in jogador:
                jogador['venceu'] = 'Não'  
            if 'Tempo' in jogador and not jogador['Tempo'].replace('.', '', 1).isdigit():
                jogador['Tempo'] = float('inf')  
    
        jogadores.sort(key=lambda x: (
            x.get('venceu') != 'Sim',  
            float(x.get('Tempo', float('inf'))), 
            -float(x.get('Score', 0))  
        ))

        for idx, jogador in enumerate(jogadores[:5], start=1): 
            print(f"{idx}. Player: {jogador.get('Player', 'Não informado')}")
            print(f"   O jogador: {jogador.get('O jogador', 'Não informado')}")
            if 'Tempo' in jogador:
                print(f"   Tempo: {jogador['Tempo']}")
            print(f"   Modo de jogo: {jogador.get('Modo de jogo', 'Não informado')}")
            print(f"   Pontos: {jogador.get('Pontos', 'Não informado')}")
            print(f"   Score: {jogador.get('Score', 'Não informado')}")
            print("----------------------------------------")

        a = input('Deseja sair da tela de scores? <s/n>: ')
        while a.lower() != 's':  
            a = input('Deseja sair da tela de scores? <s/n>: ')
