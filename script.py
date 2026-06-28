
def jogar():
    print("=" * 40)
    print("A LENDA DO CRISTAL PERDIDO")
    print("=" * 40)

    nome = input("Olá, aventureiro(a)! Qual é o seu nome? ")

    print(f"Bem vindo(a), {nome}! Sua aventura começa agora...")

    print("Você ouviu falar de um cristal valioso escondido em uma caverna, e após anos de busca, você finalmente encontra o local correto.")

    print("Ao entrar, encontra três passagens:")

    print("\n1 - Passagem iluminada")
    print("2 - Passagem escura")
    print("3 - Passagem inundada")

    caminho = input("\nEscolha (1, 2 ou 3): ")

    if caminho == "1":
        print("\nVocê chega ao final da passagem iluminada, e encontra uma porta antiga com a seguinte mensagem gravada:")

        print("'Para me abrir, resolva o enigma: ")

        print("△ + △ = 8")
        print("□ + △ = 10")
        print("○ + □ = 9")

        print("○ + △ = ?")

        resposta1 = input("Resposta: ")

        if resposta1 == "7":
            print("\nA porta se abre!")

            print("\nVocê encontra três túneis, cada um com uma mensagem:")

            print("Túnel Vermelho: O cristal está no Túnel Azul.")
            print("Túnel Azul: O cristal está no Túnel Vermelho.")
            print("Túnel Verde: As duas mensagens acima são falsas.")

            print("\nApenas uma mensagem é verdadeira.")

            resposta2 = input("\nEm qual túnel está o cristal? (vermelho/azul/verde) ").lower()

            if resposta2 == "vermelho":
                print("\nFINAL BOM")
                print("Você encontra o Cristal Perdido e retorna para casa famoso(a) e rico(a)!")
            else:
                print("\nFINAL RUIM")
                print("Você escolhe o túnel errado e se perde na caverna para sempre!")

        else:
            print("\nFINAL RUIM")
            print("A porta continua fechada. Você volta para casa sem o cristal!")

    elif caminho == "2":
        print("\nVocê se arrisca pela passagem escura, e encontra um enigma ao final do caminho:")

        print("\n3 → 9")
        print("4 → 16")
        print("5 → 25")
        print("8 → ?")

        resposta = input("Qual número completa a sequência? ")

        if resposta == "64":
            print("\nVocê decifra o enigma e uma passagem secreta se abre!")

            print("\nAo atravessar a passagem, você encontra uma placa com uma sequência de números, porém o último está faltando:")
            print("2, 5, 4, 10, 8, 20, ?")
            print("Qual número completa a sequência?")

            resposta2 = input("Resposta: ")

            if resposta2 == "16":
                print("\nFINAL BOM")
                print("Ao completar a sequência, você encontra o Cristal Perdido e retorna para casa famoso(a) e rico(a)!")
            else:
                print("\nFINAL RUIM")
                print("Você escolhe o caminho errado e sai da caverna sem o cristal!")
        else:
            print("\nFINAL RUIM")
            print("Você não consegue decifrar o enigma e volta para casa sem o cristal!")

    elif caminho == "3":
        print("\nVocê segue pela passagem inundada. A água chega até os joelhos e, após alguns metros, encontra uma ponte quebrada.")

        print("\nEm uma pedra, você vê gravado:")
        print("1 → 2")
        print("2 → 6")
        print("3 → 12")
        print("4 → 20")
        print("5 → ?")

        resposta = input("Qual número completa a sequência? ")

        if resposta == "30":
            print("\nAs pedras da ponte começam a se mover sozinhas, formando uma passagem até o outro lado!")

            print("\nApós atravessar, você encontra uma antiga porta de pedra com a seguinte mensagem:")

            print("\nPEDRA = 5")
            print("ESPADA = 6")
            print("CRISTAL = 7")
            print("CAVERNA = ?")

            print("\nQual número completa o enigma? ")

            resposta2 = input("Resposta: ")

            if resposta2 == "7":
                print("\nFINAL BOM")
                print("A porta se abre lentamente.")
                print("Atrás dela está o Cristal Perdido!")
                print("Você retorna para casa famoso(a) e rico(a)!")
            else:
                print("\nFINAL RUIM")
                print("A porta continua fechada e você sai da caverna sem o cristal.")

        else:
            print("\nFINAL RUIM")
            print("Você não consegue resolver o enigma e não consegue atravessar a ponte.")

    else:
        print("\nEscolha inválida.")


while True:
    jogar()

    repetir = input("\nJogar novamente? (s/n): ").lower()

    if repetir != "s":
        break


