def jogar():

    print('****************************************')
    print('BEM VINDO AO JOGO DA FORCA')
    print('****************************************')

    palavra_secreta = 'banana'

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = (input('Qual letra ?'))

        index = 0 

        for letra in palavra_secreta:
            if(chute == letra):
                print('Encontrei a letras {} na posição {}'.format(letra, index))
            index = index + 1 

    print('Fim do jogo')

if(__name__ == '__main__'):
    jogar()