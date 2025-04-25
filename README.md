# Fugindo da Orientadora

## Apresentação de slides
[canvas - slides](https://www.canva.com/design/DAGi09UdvY0/xymncvL3GXo8DZfDygkBFg/edit)

## 🎮 Jogue agora mesmo
https://maryclaires.itch.io/fugindodaorientadora

## 📝 Descrição do Projeto
Este projeto consiste em um minigame desenvolvido em Python com a biblioteca Pygame. O objetivo principal é sobreviver o máximo possível, fugindo dos trabalhos lançados pela Orientadora que persegue o jogador, inspirado no clássico jogo do dinossauro do Google Chrome.

## 📌 Estrutura do Projeto

```
.
├── assets
│   ├── backgrounds          # Imagens para o fundo animado do jogo
│   ├── dano.png             # Sprite de dano
│   ├── nuvem.png            # Imagem da nuvem
│   ├── obstaculo.png        # Imagem do obstáculo
│   ├── orientadora.png      # Imagem da orientadora (inimigo)
│   ├── pedra.png            # Imagem da pedra (obstáculo)
│   └── player.png           # Imagem do jogador
├── background.py            # Gerenciamento do cenário animado
├── constants.py             # Constantes usadas no jogo (tamanhos, velocidades, etc.)
├── core.py                  # Lógica principal e inicialização do jogo
├── gameObjects.py           # Classes dos personagens e objetos interativos
├── main.py                  # Arquivo principal que executa o jogo
├── states                   # Gerenciamento dos estados do jogo
│   ├── base.py              # Classe base para todos os estados
│   ├── gameover.py          # Estado "Game Over"
│   ├── play.py              # Estado de Gameplay principal
│   └── title.py             # Estado inicial (menu)
└── utils                     # Arquivos antigos/testes (ignorar)
```

## 🛠️ Como Instalar e Executar o Jogo

### Requisitos
- Python instalado (versão 3.8 ou superior)
- Pygame instalado

### Instalação do Pygame
Execute no terminal:

```bash
pip install pygame
```

### Execução do Jogo
Abra um terminal no diretório do projeto e execute:

```bash
python main.py
```

## 🎲 Funcionamento do Jogo

### Objetivo
- Sobreviver o maior tempo possível enquanto desvia de trabalhos lançados pela orientadora.

### Controles
- **Espaço**: Pular

### Mecânicas
- Obstáculos reduzem a vida do jogador.
- Aumento progressivo da aceleração dos obstáculos.

## 📂 Explicação da Estrutura

### `assets/`
Contém todas as imagens utilizadas no jogo.

### `background.py`
Gerencia o cenário do jogo, alternando entre imagens de fundo e também gerenciando o movimento das nuvens.

### `constants.py`
Centraliza constantes do jogo como tamanhos, velocidades, e posições.

### `gameObjects.py`
Usa programação orientada a objetos (POO) para criar classes reutilizáveis como:
- `Player`
- `Orientadora`
- `Obstaculo`

### `states/`
Utiliza o padrão State para gerenciar diferentes estados do jogo:
- Menu inicial (`title.py`)
- Gameplay principal (`play.py`)
- Tela de fim de jogo (`gameover.py`)

### `core.py`
Inicializa elementos essenciais como personagens, obstáculos, cenário e controla mecânicas principais (ex.: colisões e aumento de dificuldade).

### `main.py`
Responsável por iniciar e manter o loop principal do jogo.

## 🔨 Sugestões para Testes
- Alterar a aceleração progressiva dos obstáculos.
- Testar diferentes valores de gravidade.
- Redimensionar o jogo para novas configurações de telas. 

## 🎯 Sugestões para Expansão
- Adicionar pontuação com ranking.
- Implementar novos obstáculos e desafios.
- Implementar responsividade.

## 📚 Referências Úteis
- Documentação oficial do [Pygame](https://www.pygame.org/docs/)
- Exemplos de jogos em Pygame no [GitHub](https://github.com/search?q=pygame+examples&type=repositories)

**Obrigada por visitar esse repositório! 🎮🚀**

