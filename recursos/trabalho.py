def mostrar_vida(tela,fonte,vida,cor):
    sombraVida=fonte.render(f"Vidas: {vida}", True, (0,0,0))
    tela.blit(sombraVida,(12,42))

    textoVida=fonte.render(f"Vidas: {vida}", True, cor)
    tela.blit(textoVida,(10,40))