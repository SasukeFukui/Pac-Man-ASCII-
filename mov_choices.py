import WConio2 as w
import os


ope1 = [
    '           ██╗ ██████╗  ██████╗  █████╗ ██████╗  ',
    '           ██║██╔═══██╗██╔════╝ ██╔══██╗██╔══██╗ ',
    '           ██║██║   ██║██║  ███╗███████║██████╔╝',
    '       ██  ██║██║   ██║██║   ██║██╔══██║██║  ██║',
    '       █████╔╝╚██████╔╝╚██████╔╝██║  ██║██║  ██║',
    '       ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝',]
ope2 = [
    '       ███████╗███████╗ ██████╗ ██████╗ ███████╗',
    '       ██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝',
    '       ███████╗██║     ██║   ██║██████╔╝█████╗  ',
    '       ╚════██║██║     ██║   ██║██║  ██║██╔══╝  ',
    '       ███████║███████╗╚██████╔╝██║  ██║███████╗',
    '       ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝',]
ope3 = [
    '       ███████╗ █████╗ ██╗██████╗ ',
    '       ██╔════╝██╔══██╗██║██╔══██╗',
    '       ███████╗███████║██║██████╔╝',
    '       ╚════██║██╔══██║██║██║  ██║',
    '       ███████║██║  ██║██║██║  ██║',
    '       ╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═╝',]

options = [ope1, ope2, ope3]

def print_options(selected_index):
    """Função para exibir as opções com a seta indicando a opção selecionada"""
    os.system('cls' if os.name == 'nt' else 'clear')
    while w.kbhit():
        
        key = w.getkey()
        if key=="w":
            pass
    for i, option in enumerate(options):
        if i == selected_index:
            print("  ===>")
        else:
            print("\n")

        for linha in option:
            print(linha)
        print("\n")

#funcao para iniciar as opcoes
def screen():

    selected_index = 0

    while True:
        print_options(selected_index)

        key = w.getkey()

        if key == "w":  
            selected_index = (selected_index - 1) % len(options)
        elif key == "s":  
            selected_index = (selected_index + 1) % len(options)
        elif key == "\r" :  
            os.system('cls' if os.name == 'nt' else 'clear')
            return selected_index
        elif key == "\x1b":
            os._exit(0)


