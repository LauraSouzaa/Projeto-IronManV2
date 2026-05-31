import pygame
import random
import pyttsx3
from recursos.funcoes import inicializarBancoDeDados, limpar_tela, escreverDados, maior_pontuador,cor_texto
from recursos.trabalho import mostrar_vida

limpar_tela()
inicializarBancoDeDados()
nome_maior, maior_pontos, dataJogada = maior_pontuador()
pygame.init()
engine=pyttsx3.init()
engine.setProperty("rate",180)
engine.setProperty("volume", 1.0)
sol=40
velocidadeSol=0.1
while True:
    nome = input("NickName: ")
    if len(nome) > 0: 
        break
    else:
        print("Nome Inválido!")
tamanho = (1000,700)
pygame.display.set_caption("Naruto: Sobrevivência Ninja")
icone  = pygame.image.load("bases/icone.png")
pygame.display.set_icon(icone)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode( tamanho )
branco=cor_texto("branco")
preto=cor_texto("preto")

fundo = pygame.image.load("bases/background.png")
fundo=pygame.transform.scale(fundo,(1000,700))
larguraFundo=fundo.get_width()
fundoDead = pygame.image.load("bases/backgroundDead.png")
fundoDead=pygame.transform.scale(fundoDead,(1000,700))
fundoStart = pygame.image.load("bases/backgroundStart.png")
fundoStart=pygame.transform.scale(fundoStart,(1000,700))

personagem= pygame.image.load("bases/personagem.png")
personagem = pygame.transform.scale(personagem, (90,90))
pain = pygame.image.load("bases/pain.png")
pain = pygame.transform.flip(pain, True, False)
pain = pygame.transform.scale(pain, (120,120))
painSound = pygame.mixer.Sound("bases/audioPain.mp3")
explosaoSound = pygame.mixer.Sound("bases/explosao.wav")
pygame.mixer.music.load("bases/narutoAudio.mp3")
fonteMenu = pygame.font.SysFont("comicsans",18)

def jogar():
    global sol,velocidadeSol
    pause=False
    velocidadeMovPersona = 8
    posicaoXpain = 800
    posicaoYpainposicaoXpain = 100
    posicaoNuvemX = 1000
    posicaoNuvemY = 80
    nuvem = pygame.image.load("bases/nuvem.webp")
    nuvem = pygame.transform.scale(nuvem, (120, 120))
    velocidadepainposicaoXpain = 5
    personagemPiscando=False
    contadorPisca=0
    vida=3
    posicaoYPersona = 320
    movimentoYPersona  = 0
    pontos = 0
    pygame.mixer.music.play(-1)
    dificuldade = 20
    while True:
        sol+=velocidadeSol
        if sol>=50 or sol<=40:
            velocidadeSol*=-1
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if evento.type==pygame.KEYDOWN and evento.key==pygame.K_SPACE:
                pause=not pause
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
            if not pause:
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_UP:
                    movimentoYPersona = -velocidadeMovPersona
                elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_DOWN:
                    movimentoYPersona = velocidadeMovPersona
                elif evento.type == pygame.KEYUP and evento.key == pygame.K_UP:
                    movimentoYPersona = 0
                elif evento.type == pygame.KEYUP and evento.key == pygame.K_DOWN:
                    movimentoYPersona = 0
        if not pause:
            posicaoYPersona = posicaoYPersona + movimentoYPersona
            posicaoNuvemX -= random.randint(1,3)       
        if posicaoYPersona < 350 :
            posicaoYPersona = 350
        elif posicaoYPersona > 550:
            posicaoYPersona = 550
        
        if not pause:
            posicaoXpain = posicaoXpain - velocidadepainposicaoXpain
        if posicaoXpain < -125:
            posicaoXpain = 800
            posicaoYpainposicaoXpain = random.randint(350,550)
            velocidadepainposicaoXpain = velocidadepainposicaoXpain + 1
            pontos += 1
        if posicaoNuvemX < -120:
            posicaoNuvemX = 1000
            posicaoNuvemY = random.randint(50,200)
        tela.fill(branco)
        escrever_tela(fundo,(0,0))
        pygame.draw.circle(tela,(255,255,0),(920,80),int(sol))
        escrever_tela(nuvem, (posicaoNuvemX, posicaoNuvemY))
        if personagemPiscando==False or contadorPisca%6<3:
            escrever_tela(personagem, (100,posicaoYPersona))
        escrever_tela(pain, (posicaoXpain, posicaoYpainposicaoXpain))
        sombraPontos= fonteMenu.render("Pontos: "+str(pontos), True, (0,0,0))
        escrever_tela(sombraPontos, (702,17))
        texto=fonteMenu.render("Pontos: "+str(pontos),True,branco)
        escrever_tela(texto,(700,15))
        sombraPause=fonteMenu.render("Press Space to Pause Game", True, (0,0,0))
        escrever_tela(sombraPause,(12,12))
        textoPauseInfo=fonteMenu.render("Press Space to Pause Game", True, branco)
        escrever_tela(textoPauseInfo,(10,10))
        mostrar_vida(tela,fonteMenu,vida,branco)
        pixelsPersonaX = list(range(115,155))
        pixelsPersonaY = list(range(posicaoYPersona+15, posicaoYPersona+80))
        pixelspainposicaoXpainX = list(range(posicaoXpain+30, posicaoXpain+90))
        pixelspainposicaoXpainY = list(range(posicaoYpainposicaoXpain+15, posicaoYpainposicaoXpain+95))
        if len(list(set(pixelspainposicaoXpainY).intersection(set(pixelsPersonaY)))) > dificuldade:
            if len(list(set(pixelspainposicaoXpainX).intersection(set(pixelsPersonaX)))) > dificuldade and personagemPiscando==False:
                vida -= 1
                pygame.mixer.Sound.play(painSound)
                personagemPiscando = True
                contadorPisca = 50
                posicaoXpain = 800
                posicaoYpainposicaoXpain = random.randint(320,520)
        if vida <= 0:
            escreverDados(nome,pontos)
            dead()
            return

        if personagemPiscando:
            contadorPisca -= 1
        if contadorPisca <= 0:
            personagemPiscando = False
        if pause:
            fontePause= pygame.font.SysFont("comicsans",60)
            textoPause=fontePause.render("PAUSE",True,branco)
            x=500-textoPause.get_width()//2
            y=350-textoPause.get_width()//2
            escrever_tela(textoPause,(x,y))
        pygame.display.update()
        relogio.tick(60)

def dead():
    global engine
    print("ENTROU NO DEAD")
    pygame.mixer.Sound.play(explosaoSound)
    pygame.mixer.music.stop()
    painSound.stop()
    pygame.time.wait(4000)
    painSound.stop()
    nome_maior, maior_pontos, _ = maior_pontuador()
    print("RECORDE NA TELA FINAL:", nome_maior, maior_pontos)
    larguraButtonStart = 150
    alturaButtonStart  = 40
    explosaoSound.stop()
    engine.stop()
    engine.say("Você foi derrotado pelo Pein")
    engine.runAndWait()
    while True:
        tela.fill(branco)
        escrever_tela(fundoDead, (0,0))
       
        startButton = pygame.draw.rect(tela, branco, (425,620, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        textoX=425+larguraButtonStart// 2 - startTexto.get_width()//2
        textoY = 620 + alturaButtonStart // 2 - startTexto.get_height() // 2
        escrever_tela(startTexto, (textoX,textoY))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if evento.type == pygame.QUIT:
                pygame.quit()
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
        
        textoRecorde = fonteMenu.render(f"Maior pontuador: {nome_maior} - {maior_pontos} pontos",True,branco)
        sombraRecorde=fonteMenu.render(f"Maior pontuador: {nome_maior} - {maior_pontos} pontos", True,preto)
        textoX = 500 - textoRecorde.get_width() // 2
        escrever_tela(sombraRecorde,(textoX+2, 202))
        escrever_tela(textoRecorde,(textoX, 200))
        pygame.display.update()
        relogio.tick(60)

def escrever_tela(mensagem,posicao):
    tela.blit(mensagem,posicao)

def start():
    larguraButtonStart = 150
    alturaButtonStart  = 40
    while True:
        nome_maior, maior_pontos, dataJogada = maior_pontuador()
        tela.fill(branco)
        escrever_tela(fundoStart, (0,0))
        startButton = pygame.draw.rect(tela, branco, (425,602, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        textoX=500-startTexto.get_width()//2
        escrever_tela(startTexto, (textoX,611))
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if evento.type == pygame.QUIT:
                pygame.quit()
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

        fonteTitulo=pygame.font.SysFont("comicsans",40)
        sombraTitulo = fonteTitulo.render("Naruto: Sobrevivência Ninja", True, preto)
        textoTitulo=fonteTitulo.render("Naruto: Sobrevivência Ninja",True,branco)
        tituloX=500-textoTitulo.get_width()//2
        escrever_tela(sombraTitulo,(tituloX+2,52))
        escrever_tela(textoTitulo,(tituloX,50))
        
        textoBoasVindas=fonteMenu.render(f"Bem vindo(a) {nome}",True, branco)
        sombraBoasVindas = fonteMenu.render(f"Bem vindo(a) {nome}", True, preto)
        boasVindasX=500-textoBoasVindas.get_width()//2
        escrever_tela(sombraBoasVindas, (boasVindasX+2,132))
        escrever_tela(textoBoasVindas,(boasVindasX,130))

        textoDescricaoGame=fonteMenu.render("Sobreviva aos ataques da Akatsuki e bata o recorde.",True,branco)
        sombraDescricaoGame = fonteMenu.render("Sobreviva aos ataques da Akatsuki e bata o recorde.",True,preto)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(sombraDescricaoGame, (textoDescricaoX+2,202))
        escrever_tela(textoDescricaoGame,(textoDescricaoX,200))
        
        textoDescricaoGame=fonteMenu.render("Desvie dos inimigos e tente bater o recorde do último jogador!",True,branco)
        sombraDescricaoGame = fonteMenu.render("Desvie dos inimigos e tente bater o recorde do último jogador!",True,preto)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(sombraDescricaoGame, (textoDescricaoX+2,252))
        escrever_tela(textoDescricaoGame,(textoDescricaoX,250))

        
        textoDescricaoGame=fonteMenu.render("Recorde: ",True,branco)
        sombraDescricaoGame = fonteMenu.render("Recorde: ",True,preto)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(sombraDescricaoGame, (textoDescricaoX+2,292))
        escrever_tela(textoDescricaoGame,(textoDescricaoX,290))
        
        textoDescricaoGame=fonteMenu.render(f"Jogador: {nome_maior} - pontos: {maior_pontos}",True,branco)
        sombraDescricaoGame = fonteMenu.render(f"Jogador: {nome_maior} - pontos: {maior_pontos}",True,preto)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(sombraDescricaoGame, (textoDescricaoX+2,320))
        escrever_tela(textoDescricaoGame,(textoDescricaoX,320))

        textoDescricaoGame=fonteMenu.render(f"{dataJogada}",True,branco)
        sombraDescricaoGame = fonteMenu.render(f"{dataJogada}",True,preto)
        textoDescricaoX=500-textoDescricaoGame.get_width()//2
        escrever_tela(sombraDescricaoGame, (textoDescricaoX+2,352))
        escrever_tela(textoDescricaoGame,(textoDescricaoX,350))

        pygame.display.update()
        relogio.tick(60)
        

start()