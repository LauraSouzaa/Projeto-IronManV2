def mostrar_vida(tela,fonte,vida,cor):
    textoVida=fonte.render("Vida: "+ str(vida), True, cor)
    tela.blit(textoVida,)