Projeto IronManV2
Laura Portella de Souza
RA: 1139306

Descrição do Jogo
Naruto: Sobrevivência Ninja é um jogo desenvolvido em Python utilizando a biblioteca Pygame. O jogador controla Naruto e deve sobreviver aos ataques de Pain, desviando dos inimigos que atravessam a tela.
A cada inimigo desviado, o jogador ganha pontos e a dificuldade aumenta gradativamente, tornando o desafio cada vez maior. O objetivo é permanecer vivo o maior tempo possível e superar o recorde de pontuação armazenado no sistema. Ao perder todas as vidas, o jogador recebe uma mensagem de Game Over e pode iniciar uma nova partida para tentar bater o recorde.

Tecnologias Utilizadas:
- Python 3
- Pygame
- Pyttsx3
- JSON
- CX_Freeze

Como Executar
Instale as dependências:

pip install pygame pyttsx3 cx_Freeze

Execute o jogo:

python main.py

Geração do Executável

Para gerar o executável do jogo:

python setup.py build

Para gerar o instalador MSI:

python setup.py bdist_msi