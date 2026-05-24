def mostrar_vida(tela,fonte,vida,cor):
    textoVida=fonte.render("Vidas: "+ str(vida), True, cor)
    tela.blit(textoVida,(20,20))