import pygame
import random
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador
from recursos.trabalho import mostrar_vida

limpar_tela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.init()

while True:
    nome = input("NickName: ")
    if len(nome) > 0: 
        break
    else:
        print("Nome Inválido!")

tamanho = (1000,700)
pygame.display.set_caption("O último Sobrevivente")
icone  = pygame.image.load("bases/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho ) 
branco = (255, 255, 255)
preto = (0, 0, 0)

fundo = pygame.image.load("bases/background.jpg")
fundoDead = pygame.image.load("bases/backgroundDead.jpg")
fundoStart = pygame.image.load("bases/backgroundStart.jpg")
fundoStart=pygame.transform.scale(fundoStart,(1000,700))

iron = pygame.image.load("bases/IronMan.png")
iron = pygame.transform.scale(iron, (116,51))
missel = pygame.image.load("bases/missile.png")
missel = pygame.transform.scale(missel, (125,25))
missileSound = pygame.mixer.Sound("bases/missile.wav")
explosaoSound = pygame.mixer.Sound("bases/explosao.wav")
pygame.mixer.music.load("bases/ironsound.mp3")
fonteMenu = pygame.font.SysFont("comicsans",18)

def jogar():
    vida=3
    fundoMov1 = 0
    fundoMov2 = 1129
    posicaoXPersona = 0
    posicaoYPersona = 60
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    velocidadeMovPersona = 5
    posicaoXMissel = 800
    posicaoYMissel = 100
    velocidadeMissel = 2
    pontos = 0
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    dificuldade = 20
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
                movimentoXPersona = 0
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                movimentoYPersona = -velocidadeMovPersona
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                movimentoYPersona = velocidadeMovPersona
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
                movimentoYPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
                movimentoYPersona = 0
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = velocidadeMovPersona
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -velocidadeMovPersona
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
                
        
        posicaoXPersona = posicaoXPersona + movimentoXPersona          
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        if posicaoXPersona < 0 :
            posicaoXPersona = 0
        elif posicaoXPersona > 685:
            posicaoXPersona = 685
        if posicaoYPersona < 0 :
            posicaoYPersona = 0
        elif posicaoYPersona > 150:
            posicaoYPersona = 150
            
            
        posicaoXMissel = posicaoXMissel - velocidadeMissel
        if posicaoXMissel < -125:
            pygame.mixer.Sound.play(missileSound)
            posicaoXMissel = 800
            pontos = pontos + 1
            velocidadeMissel = velocidadeMissel + 1
            posicaoYMissel = random.randint(0,200)
                            
        tela.fill(branco)
        escrever_tela(fundo, (fundoMov1,0) )
        escrever_tela(fundo, (fundoMov2,0) )
        fundoMov1 -= 1
        fundoMov2 -= 1
        if fundoMov1 <= -1129:
            fundoMov1 = 1129
        elif fundoMov2 <= -1129:
            fundoMov2 = 1129
        
        escrever_tela(iron, (posicaoXPersona,posicaoYPersona))
        escrever_tela( missel, (posicaoXMissel, posicaoYMissel) )
        texto = fonteMenu.render("Pontos: "+str(pontos), True, branco)
        escrever_tela(texto, (700,15))
        mostrar_vida(tela,fonteMenu,vida,branco)
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+116))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+51))
        pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel + 125))
        pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel + 25))
        if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                vida-=1
                posicaoXMissel=800
                posicaoYMissel=(random.randint(0,200))
            if vida <=0:
                escreverDados(nome,pontos)
                dead()
            else:
                print("Ainda Vivo, mas por pouco!")
        else:
            print("Ainda Vivo")
        
        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    larguraButtonStart = 150
    alturaButtonStart  = 40
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35
                    
            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()
            
        tela.fill(branco)
        escrever_tela(fundoDead, (0,0))
        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        escrever_tela(startTexto, (25,12))

        pygame.display.update()
        relogio.tick(60)

def escrever_tela(mensagem,posicao):
    tela.blit(mensagem,posicao)
def start():
    larguraButtonStart = 150
    alturaButtonStart  = 40
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart  = 35

            elif evento.type == pygame.MOUSEBUTTONUP:
                # Verifica se o clique foi dentro do retângulo
                if startButton.collidepoint(evento.pos):
                    #pygame.mixer.music.play(-1)
                    larguraButtonStart = 150
                    alturaButtonStart  = 40
                    jogar()

        tela.fill(branco)
        escrever_tela(fundoStart, (0,0))

        fonteTitulo=pygame.font.SysFont("comicsans",40)
        textoTitulo=fonteTitulo.render("O Último Sobrevivente",True,branco)
        tituloX=500-textoTitulo.get_width()//2
        escrever_tela(textoTitulo,(tituloX,50))
        
        textoBoasVindas=fonteMenu.render(f"Bem vindo(a) {nome}",True, branco)
        boasVindasX=500-textoBoasVindas.get_width()//2
        escrever_tela(textoBoasVindas,(boasVindasX,130))

        textoDescricaoGame=fonteMenu.render("Sobreviva aos Zumbis o máximo possível",True,branco)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(textoDescricaoGame,(textoDescricaoX,200))
        
        textoDescricaoGame=fonteMenu.render("Desvie dos inimigos e tente bater o recorde do último jogador!",True,branco)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(textoDescricaoGame,(textoDescricaoX,250))

        
        textoDescricaoGame=fonteMenu.render("Recorde: ",True,branco)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(textoDescricaoGame,(textoDescricaoX,290))
        
        textoDescricaoGame=fonteMenu.render(f"jogador: {nome_maior} - pontos: {maior_pontos}",True,branco)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(textoDescricaoGame,(textoDescricaoX,320))

        
        textoDescricaoGame=fonteMenu.render(f"{dataJogada}",True,branco)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(textoDescricaoGame,(textoDescricaoX,350))

        startButton = pygame.draw.rect(tela, branco, (425,402, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        textoX=500-startTexto.get_width()//2
        escrever_tela(startTexto, (textoX,402))
        
        pygame.display.update()
        relogio.tick(60)

start()