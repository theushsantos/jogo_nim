
# ALUNO: Matheus Henrique dos Santos Silva
# R.A: N8522F6

# ALUNO: Gabriel Aías
# R.A: G56GDJ9


import emoji
def Vez_da_Maquina(n,m):

    Maquina_Remove = 1

    while (Maquina_Remove != m):
        if (n - Maquina_Remove) % (m+1) == 0:
            return Maquina_Remove
        else:
            Maquina_Remove += 1

    return Maquina_Remove

def Vez_do_Usuario(n,m):
    valida = False
    while not valida:
        usuario_remove = int(input('Digite a quantidade que vai remover: '))
        if(usuario_remove < 1 or usuario_remove > m):
            print('\nJOGADA INVÁLIDA, tente novamente!!\n')
        else:
            valida = True
    return usuario_remove
def partida():
    n = int(input('1- Digite a quantidade de peças do jogo: '))
    m = int(input('2- Digite a qandidade maxima de peça que vai retirar: '))
    Maquina = False
    if n % (m+1) == 0:
        print(emoji.emojize('\nVou deixar você começar!! :stuck_out_tongue_closed_eyes:', language='alias'))
    else:
        print(emoji.emojize('\nEu vou começar!! :sunglasses:', language='alias'))
        Maquina = True
    while n > 0:
        if Maquina:
            Maquina_Remove = Vez_da_Maquina(n,m)
            n = n - Maquina_Remove
            if(Maquina_Remove == 1):
                print('\nA maquina removeu 1 peça!!')
            else:
                print('\nA maquina removeu {} peças'.format(Maquina_Remove))

            Maquina = False
        else:
            usuario_remove = Vez_do_Usuario(n,m)
            n = n - usuario_remove
            if usuario_remove == 1:
                print('\nVocê removeu 1 peça!!')
            else:
                print('\nVocê removeu {} peças!!'.format(usuario_remove))
            Maquina = True
        if(n == 1):
            print('\nResta apenas 1 peça !!')
        else:
            if n!= 0:
                print('\nRestam {} peças!!'.format(n))
    print(emoji.emojize('\nFim de jogo, Você perdeu!! :thumbsdown:', language='alias'))

print('Bem Vindo ao jogo nim!!!\nDigite 1 para começar!!\nDigite qualquer 2 e "Enter" para sair!!')
inicio = int(input('\nVamos lá? '))
if(inicio == 1):
    print('\nEntão você quer me desafiar, não é mesmo !!!')
    partida()
else:
    print(emoji.emojize('Até mais!!! :wave:', language='alias'))


