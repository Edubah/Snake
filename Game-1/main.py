import pygame   #Importando a biblioteca

#Sub-biblioteca
from pygame.locals import *
#função dentro do módulo sys. Exit - Clicando na opção ela será chamada e fechará a janela
from sys import exit
#função para sortear valores dentro de um determinado intervalo
from random import randint

#Inicializa todos os comandos da biblioteca pygame
pygame.init()

#Inclusão da musica de fundo
pygame.mixer.music.set_volume(0.7)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Mission.mp3')
pygame.mixer.music.play(-1)


#Colisão
barulho_colisão = pygame.mixer.Sound('smw_fireball.wav')

largura = 640
altura = 480

#Controle de movimento
x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
#Variável para a fonte do texto que aparecerá na tela do jogo
fonte = pygame.font.SysFont('arial', 40, True, True)

#Tela principal do game. Set_mode é uma túpula
tela = pygame.display.set_mode((largura, altura))

#Alterar o nome do título da tela
pygame.display.set_caption('Jogo')

#Controle de frames
relogio = pygame.time.Clock()

lista_cobra = [] #Lista para o corpo da cobra
comprimento_inicial = 10
morreu = False

def aumenta_cobra(lista_cobra): #Função para o corpo da cobra
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (XeY[0], XeY[1], 20, 20))


def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu, velocidade
    pontos = 0
    comprimento_inicial = 10
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40,600)
    y_maca = randint(50, 430)
    morreu = False
    velocidade = 10
#Looping principal do jogo (Infinito)
while True:
    relogio.tick(15)
    tela.fill((255,255,255)) #sensação de movimento
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True,  (0,0,0))
    #Aqui terá a tarefa de checar um evento a cada tarefa do usuário
    for event in pygame.event.get():
        if event.type == QUIT: #Função para fechar o jogo
            pygame.quit()
            exit()

        #Teclas para mexer o ponto
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle


    #retangulo dentro da tela
    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra, y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca,y_maca,20,20))



    #colisão
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50,430)
        pontos += 1
        barulho_colisão.play()
        comprimento_inicial += 2
        velocidade += 1

    lista_cabeca = [] #Criação da lista apenas da cabeça
    lista_cabeca.append(x_cobra) #Armazena o valor da posição x da cobra
    lista_cabeca.append(y_cobra) #Armazena o valor da posição y da cobra

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1: #Cobra encosta nela mesma
        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = ' Game Over! Pressione a tecla R para jogar novamente!'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        ret_texto = texto_formatado.get_rect()

        #Tela de morte
        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2, altura//2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0] #Deleta o comprimento infinito

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450, 40))
    pygame.display.update() #Atualiza a tela, cada interação com a tela
