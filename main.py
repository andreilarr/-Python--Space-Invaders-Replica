from graphics import *

def main():
    win = GraphWin("Circle in Square World and Space", 1000, 500, autoflush=False)
    win.setBackground('white')

    # Layout
    textoContador = 0
    podeContadorTexto = 1
    contadorTexto = 1
    contador = 0  # contador de inimigos que começa com zero

    textoPausePode=1

    # TEXTOS
    permitirTexto = 1
    texto1 = Text(Point(500, 250), "Por que eu sou redondo?")
    texto1.setSize(20)
    texto1.setFill(color="red")

    permitirTexto2 = 0
    permitirTexto3 = 0

    textoVencedorSim = 1
    textoVencedor = Text(Point(500, 200), "Level concluído! Pressione ENTER")
    textoVencedor.setSize(30)
    textoVencedor.setFill(color="black")

    # VARIÁVEIS FUNCIONAIS
    bossDano=0
    boss2ColisaoX=0
    bossMorre=0
    CenarioMove=0
    bossMover = 0
    fase1=1
    fasee2=0
    textoPausePode = 1
    podeReiniciar=0
    passou = 0
    morto = 0
    jogoPausado=0
    pausou=1
    jogoNaoComecou=1
    textoPressioneParaComecarPodeAparecer = 0
    voar = 0  # Permite ao jogador voar
    passarSemTutorial = 1
    podeComeca = 1
    mudarVariavel = 0  # muda variaveis ao pressionar uma tecla, sem a necessidade de ficar pressionando
    animacao = 0  # permite a animacao do cenario
    pular = 1  # permite o jogador realizar um pulo, desativa qnd está no ar
    inimigoMover = 0  # Só é ativado qnd começar o jogo
    inimigo1 = 2  # Define o maximo de inimigos primários

    # variaveis de posição de inimigos para evitar erros de possíveis variáveis não declaradas
    posicaoInimigoTotal = 0
    posicaoInimigoYTotal = 0
    posicaoInimigoX = 0
    posicaoInimigoX1 = 0
    posicaoInimigoX2 = 0
    posicaoInimigoX3 = 0
    posicaoInimigoX4 = 0
    posicaoInimigoX5 = 0
    posicaoInimigoX6 = 0
    posicaoInimigoX7 = 0
    posicaoInimigoX8 = 0
    posicaoInimigoX9 = 0
    posicaoInimigoX10 = 0
    inimigo = 0
    inimigoc1x = 0
    inimigoc2x = 0
    inimigoc3x = 0
    inimigoc4x = 0
    inimigoc5x = 0
    inimigoc6x = 0
    inimigoc7x = 0
    inimigoc8x = 0
    inimigoc9x = 0
    inimigoc10x = 0
    inimigoc1y = 0
    inimigoc2y = 0
    inimigoc3y = 0
    inimigoc4y = 0
    inimigoc5y = 0
    inimigoc6y = 0
    inimigoc7y = 0
    inimigoc8y = 0
    inimigoc9y = 0
    inimigoc10y = 0
    inimigoc11y = 0
    inimigoc12y = 0
    inimigoc13y = 0
    inimigoc14y = 0
    inimigoc15y = 0
    inimigoc16y = 0
    inimigoc17y = 0
    inimigoc18y = 0
    inimigoc19y = 0
    inimigoc20y = 0
    inimigoc21y = 0

    # TIRO
    tiroDown = (Point(0, 0))  # ponto do cooldown do tiro, somente para evitar erros de declaração
    tiroDownX = tiroDown.getX()  # Obter coordenada do cooldown
    tiroc = Point(0, 0)  # Criando ponto de colisão do tiro
    tiroX = tiroc.getX()  # Obter coordenada da colisão do tiro no eixo X
    tiro = 0  # Variável do quadrado do tiro, somente para evitar erro.
    podeAtira = 0  # Permite atirar, começo do jogo não pode atirar, muda quando iniciar o jogo
    tiroMove = 0  # Permite dar movimento no eixo X para o tiro, desativada no inicio. atira quando puder atirar
    posicaotiroX = 0            #Para evitar erro por n ter declarado colisao do tiro no x
    posicaotiroY = 0            # ''    ''      ''  ''  ''  ''         ''    ''   ''  '' y

    # Objetos
    #céu
    fundo = Rectangle(Point(0, -1000), Point(50000, 310))  # Céu
    fundo.setFill(color="blue1")
    fundo.draw(win)

    #sol
    sol = Circle(Point(500, 300), 100)  # Solddddddddddd
    sol.setFill(color="Yellow")
    sol.draw(win)

    #paralax
    paralax = Image(Point(800, 97), "fundo.gif")
    paralax.draw(win)

    #chao
    quadrado = Rectangle(Point(-1000, 310), Point(50000, 1000))  # Chão
    quadrado.setFill(color="green")
    quadrado.draw(win)

    #marcador do chao
    pontoChao = Point(0, 0)  # ponto do inicio do chão, vai servir para definir roteiro de eventos
    pontoChaoX = pontoChao.getX()  # obtem coordenada
    pontoChaoMax = (Point(1050, 0))  # ponto do fim da janela no eixo X, para definir que as coisas não saiam da janela
    pontoChaoXMax = pontoChaoMax.getX()  # coordenada do maximo do chao

    #objeto laranja
    cenario = Rectangle(Point(pontoChaoX + 650, 310), Point(pontoChaoX + 850, 180))  # Cenário laranja
    cenario.setFill(color="orange2")
    cenario.draw(win)

    #nuvem
    nuvem = Oval(Point(10, 20), Point(200, 100))
    nuvem.setFill(color="white")  # Nuvem
    nuvem.draw(win)

    #nuvem2
    nuvem2 = Oval(Point(800, 20), Point(1000, 100))
    nuvem2.setFill(color="white")  # Nuvem
    nuvem2.draw(win)

    #passaro
    passaro = Polygon(Point(100 + 3, 100 + 10), Point(100 + 10, 100 + 0), Point(100 + 10, 100 + 1),
                      Point(100 + 0, 100 + 10))
    passaro.setFill(color="gray")  # Passaro
    passaro.draw(win)

    #velho
    quadradinho = Rectangle(Point(950, 310), Point(900, 250))  # Velho
    quadradinho.setFill(color="grey")
    quadradinho.draw(win)

    #boss
    boss = Rectangle(Point(-2500,310), Point(-1500,-710))
    boss.setFill(color_rgb(139,69,19))
    boss.draw(win)
    bossColisao = Point(-1500,310)

    # Jogador
    c = Circle(Point(200, 290), 10)  # bola
    c.setFill(color="red")
    c.draw(win)
    # Sistema de colisão do jogador
    P = Point(200, 280)
    P1 = Point(201, 281)
    P2 = Point(202, 282)
    P3 = Point(203, 283)
    P4 = Point(204, 284)
    P5 = Point(205, 285)
    P6 = Point(206, 286)
    P7 = Point(207, 287)
    P8 = Point(208, 288)
    P9 = Point(209, 289)
    P10 = Point(210, 290)
    P11 = Point(209, 291)
    P12 = Point(208, 292)
    P13 = Point(207, 293)
    P14 = Point(206, 294)
    P15 = Point(205, 295)
    P16 = Point(204, 296)
    P17 = Point(203, 297)
    P18 = Point(202, 298)
    P19 = Point(201, 299)
    P20 = Point(200, 300)

    # Menu Principal
    contadorDoMenu = Point(0, 0)
    contadorDoPause= Point(0, 0)

    imagem = Image(Point(500, 250), "capaJogo.gif")
    imagem.draw(win)

    textoPressioneParaComecar1 = Text(Point(500, 248), "PRESSIONE ENTER PARA COMEÇAR")
    textoPressioneParaComecar1.setSize(20)
    textoPressioneParaComecar1.setFill(color="black")
    textoPressioneParaComecar1.draw(win)

    textoPressioneParaComecar = Text(Point(500, 250), "PRESSIONE ENTER PARA COMEÇAR")
    textoPressioneParaComecar.setSize(20)
    textoPressioneParaComecar.setFill(color="Gold")
    textoPressioneParaComecar.draw(win)

    # programacao para comecar o jogo
    key = win.checkKey()
    while key != "Escape":  # Começa o looping do jogo
        # reiniciar jogo
        if podeReiniciar==1 and fase1==1:
            if key == "r" or morto==1:
                #INIMIGOS BUGADOS
                posicaoInimigoTotal = 0
                posicaoInimigoYTotal = 0
                posicaoInimigoX = 0
                posicaoInimigoX1 = 0
                posicaoInimigoX2 = 0
                posicaoInimigoX3 = 0
                posicaoInimigoX4 = 0
                posicaoInimigoX5 = 0
                posicaoInimigoX6 = 0
                posicaoInimigoX7 = 0
                posicaoInimigoX8 = 0
                posicaoInimigoX9 = 0
                posicaoInimigoX10 = 0
                posicaoInimigoY = 0
                inimigo = 0
                inimigoc1x = 0
                inimigoc2x = 0
                inimigoc3x = 0
                inimigoc4x = 0
                inimigoc5x = 0
                inimigoc6x = 0
                inimigoc7x = 0
                inimigoc8x = 0
                inimigoc9x = 0
                inimigoc10x = 0
                inimigoc1y = 0
                inimigoc2y = 0
                inimigoc3y = 0
                inimigoc4y = 0
                inimigoc5y = 0
                inimigoc6y = 0
                inimigoc7y = 0
                inimigoc8y = 0
                inimigoc9y = 0
                inimigoc10y = 0
                inimigoc11y = 0
                inimigoc12y = 0
                inimigoc13y = 0
                inimigoc14y = 0
                inimigoc15y = 0
                inimigoc16y = 0
                inimigoc17y = 0
                inimigoc18y = 0
                inimigoc19y = 0
                inimigoc20y = 0
                inimigoc21y = 0
                pausou=0
                jogoNaoComecou=0
                podeAtira=0
                passou = 0
                morto = 0
                contador=0
                jogoPausado = 0
                voar = 0  # Permite ao jogador voar
                passarSemTutorial = 1
                podeComeca = 1
                mudarVariavel = 0  # muda variaveis ao pressionar uma tecla, sem a necessidade de ficar pressionando
                animacao = 0  # permite a animacao do cenario
                pular = 1  # permite o jogador realizar um pulo, desativa qnd está no ar
                inimigoMover = 0  # Só é ativado qnd começar o jogo
                inimigo1 = 2  # Define o maximo de inimigos primários
                permitirTexto = 1

                c.undraw()
                cenario.undraw()
                quadradinho.undraw()
                sol.undraw()
                nuvem.undraw()
                nuvem2.undraw()
                quadrado.undraw()
                paralax.undraw()
                fundo.undraw()
                boss.undraw()

                #Redesenhar Objetos
                fundo = Rectangle(Point(0, -1000), Point(50000, 310))  # Céu
                fundo.setFill(color="blue1")
                fundo.draw(win)

                sol = Circle(Point(500, 300), 100)  # Sol
                sol.setFill(color="Yellow")
                sol.draw(win)

                paralax = Image(Point(1000, 97), "fundo.gif")
                paralax.draw(win)

                quadrado = Rectangle(Point(-1000, 310), Point(50000, 1000))  # Chão
                quadrado.setFill(color="green")
                quadrado.draw(win)

                pontoChao = Point(0, 0)  # ponto do inicio do chão, vai servir para definir roteiro de eventos
                pontoChaoX = pontoChao.getX()  # obtem coordenada
                pontoChaoMax = (
                    Point(1050, 0))  # ponto do fim da janela no eixo X, para definir que as coisas não saiam da janela
                pontoChaoXMax = pontoChaoMax.getX()  # coordenada do maximo do chao

                cenario = Rectangle(Point(pontoChaoX + 650, 310), Point(pontoChaoX + 850, 180))  # Cenário laranja
                cenario.setFill(color="orange2")
                cenario.draw(win)

                nuvem = Oval(Point(10, 20), Point(200, 100))
                nuvem.setFill(color="white")  # Nuvem
                nuvem.draw(win)

                nuvem2 = Oval(Point(800, 20), Point(1000, 100))
                nuvem2.setFill(color="white")  # Nuvem
                nuvem2.draw(win)

                passaro = Polygon(Point(100 + 3, 100 + 10), Point(100 + 10, 100 + 0), Point(100 + 10, 100 + 1),
                                  Point(100 + 0, 100 + 10))
                passaro.setFill(color="gray")  # Passaro
                passaro.draw(win)

                quadradinho = Rectangle(Point(950, 310), Point(900, 250))  # Velho
                quadradinho.setFill(color="grey")
                quadradinho.draw(win)

                boss = Rectangle(Point(-1500,310), Point(-2500,-710))
                boss.setFill(color_rgb(139, 69, 19))
                boss.draw(win)
                bossColisao=(Point(-1500,110))

                # Jogador
                c = Circle(Point(200, 290), 10)  # bola
                c.setFill(color="red")
                c.draw(win)
                # Sistema de colisão
                P = Point(200, 280)
                P1 = Point(201, 281)
                P2 = Point(202, 282)
                P3 = Point(203, 283)
                P4 = Point(204, 284)
                P5 = Point(205, 285)
                P6 = Point(206, 286)
                P7 = Point(207, 287)
                P8 = Point(208, 288)
                P9 = Point(209, 289)
                P10 = Point(210, 290)
                P11 = Point(209, 291)
                P12 = Point(208, 292)
                P13 = Point(207, 293)
                P14 = Point(206, 294)
                P15 = Point(205, 295)
                P16 = Point(204, 296)
                P17 = Point(203, 297)
                P18 = Point(202, 298)
                P19 = Point(201, 299)
                P20 = Point(200, 300)

        if jogoNaoComecou==1 and pausou==1:
            contadorDoMenu.move(-3, 0)

        contadorDoMenuX = contadorDoMenu.getX()
        if contadorDoMenuX < -500:
            textoPressioneParaComecar.undraw()
            textoPressioneParaComecar1.undraw()
            textoPressioneParaComecarPodeAparecer = 1

        if textoPressioneParaComecarPodeAparecer == 1 and jogoNaoComecou==1:
            if contadorDoMenuX < -1000:
                textoPressioneParaComecar1.draw(win)
                textoPressioneParaComecar.draw(win)
                contadorDoMenu.move(1000, 0)
                textoPressioneParaComecarPodeAparecer = 0
                jogoNaoComecou=1

        if passou == 0:
            if key == "Return":
                imagem.undraw()
                textoPressioneParaComecar.undraw()
                textoPressioneParaComecar1.undraw()
                jogoNaoComecou=0
                pausou=0
                podeReiniciar=1
                bossMover=1

        # Layout
        if jogoNaoComecou==0:
            if podeContadorTexto == 1:
                textoContador = Text(Point(950, 480), contador)
                textoContador.setSize(15)
                textoContador.setFill(color="black")
                textoContador.draw(win)
                podeContadorTexto = 0

        # Colisao jogador
        X = P.getX()  # Colisão do personagem principal
        Y = P.getY()  # Colisão do personagem principal
        Y1 = P1.getY()
        X1 = P1.getX()
        Y2 = P2.getY()
        X2 = P2.getX()
        Y3 = P3.getY()
        X3 = P3.getX()
        Y4 = P4.getY()
        X4 = P4.getX()
        Y5 = P5.getY()
        X5 = P5.getX()
        Y6 = P6.getY()
        X6 = P6.getX()
        Y7 = P7.getY()
        X7 = P7.getX()
        Y8 = P8.getY()
        X8 = P8.getX()
        Y9 = P9.getY()
        X9 = P9.getX()
        Y10 = P10.getY()
        X10 = P10.getX()
        Y11 = P11.getY()
        X11 = P11.getX()
        Y12 = P12.getY()
        X12 = P12.getX()
        Y13 = P13.getY()
        X13 = P13.getX()
        Y14 = P14.getY()
        X14 = P14.getX()
        Y15 = P15.getY()
        X15 = P15.getX()
        Y16 = P16.getY()
        X16 = P16.getX()
        Y17 = P17.getY()
        X17 = P17.getX()
        Y18 = P18.getY()
        X18 = P18.getX()
        Y19 = P19.getY()
        X19 = P19.getX()
        Y20 = P20.getY()
        X20 = P20.getX()
        colisãoJogadorXTotal=X or X1 or X2 or X3 or X4 or X5 or X6 or X7 or X8 or X9 or X10 or X11 or X12 or X13 or X14 or X15 or X16 or X17 or X18 or X19 or X20
        colisaoJogadorYTotal=Y or Y1 or Y2 or Y3 or Y4 or Y5 or Y6 or Y7 or Y8 or Y9 or Y10 or Y11 or Y12 or Y13 or Y14 or Y15 or Y16 or Y17 or Y18 or Y19 or Y20

        # Coordenadas da tela
        pontoChaoXMax = pontoChaoMax.getX()  # Limite da tela a direita
        pontoChaoX = pontoChao.getX()  # Define o roteiro do jogo

        # Inimigo 1
        if inimigo1 < 1:
            inimigo = Rectangle(Point(X + 1500, Y), Point((X + 1520), (Y + 20)))
            inimigo.setFill(color_rgb(18,10,143))
            inimigo.draw(win)
            inimigocx = Point(X + 1500, Y)
            inimigoc1x = Point(X + 1501, Y)
            inimigoc2x = Point(X + 1502, Y)
            inimigoc3x = Point(X + 1503, Y)
            inimigoc4x = Point(X + 1504, Y)
            inimigoc5x = Point(X + 1505, Y)
            inimigoc6x = Point(X + 1506, Y)
            inimigoc7x = Point(X + 1507, Y)
            inimigoc8x = Point(X + 1508, Y)
            inimigoc9x = Point(X + 1509, Y)
            inimigoc10x = Point(X + 1510, Y)
            inimigoc1y = Point(X + 1500, Y)
            inimigoc2y = Point(X + 1500, Y + 1)
            inimigoc3y = Point(X + 1500, Y + 2)
            inimigoc4y = Point(X + 1500, Y + 3)
            inimigoc5y = Point(X + 1500, Y + 4)
            inimigoc6y = Point(X + 1500, Y + 5)
            inimigoc7y = Point(X + 1500, Y + 6)
            inimigoc8y = Point(X + 1500, Y + 7)
            inimigoc9y = Point(X + 1500, Y + 8)
            inimigoc10y = Point(X + 1500, Y + 9)
            inimigoc11y = Point(X + 1500, Y + 10)
            inimigoc12y = Point(X + 1500, Y + 11)
            inimigoc13y = Point(X + 1500, Y + 12)
            inimigoc14y = Point(X + 1500, Y + 13)
            inimigoc15y = Point(X + 1500, Y + 14)
            inimigoc16y = Point(X + 1500, Y + 15)
            inimigoc17y = Point(X + 1500, Y + 16)
            inimigoc18y = Point(X + 1500, Y + 17)
            inimigoc19y = Point(X + 1500, Y + 18)
            inimigoc20y = Point(X + 1500, Y + 19)
            inimigoc21y = Point(X + 1500, Y + 20)
            # Variavel do inimigo
            inimigo1 = inimigo1 + 1  # Aumenta a quantidade de inimigo para evitar spawn
            inimigoMover = 1  # Permite ele se mover

        #SISTEMA PARA PAUSE E MENU
        if jogoNaoComecou==0:        #significa que o jogo começou

            if fase1==1: # Objetos se mexendo no tutorial
                passaro.move(0.08, 0)
                sol.move(-0.000001, 0.002)
                nuvem.move(-0.002, 0)
                nuvem2.move(-0.002, 0)

            # Movimentação
            # Movimentar para direita sem passar da extremidade
            if X < 900 and fase1==1:  # Só pode se mover para direita se não passar do pixel 900, pois se passar,
                # pode sair da tela
                if voar == 1:  # Condição para se mover enquanto voa
                    if key == "d" or key=="D":
                        c.move(8, 0)
                        P.move(8, 0)
                        P1.move(8, 0)
                        P2.move(8, 0)
                        P3.move(8, 0)
                        P4.move(8, 0)
                        P5.move(8, 0)
                        P6.move(8, 0)
                        P7.move(8, 0)
                        P8.move(8, 0)
                        P9.move(8, 0)
                        P10.move(8, 0)
                        P11.move(8, 0)
                        P12.move(8, 0)
                        P13.move(8, 0)
                        P14.move(8, 0)
                        P15.move(8, 0)
                        P16.move(8, 0)
                        P17.move(8, 0)
                        P18.move(8, 0)
                        P19.move(8, 0)
                        P20.move(8, 0)
                        pontoChao.move(-8, 0)  # define acontecimentos
                        inimigo.move(-4, 0)
                        inimigoc1x.move(-4, 0)
                        inimigoc2x.move(-4, 0)
                        inimigoc3x.move(-4, 0)
                        inimigoc4x.move(-4, 0)
                        inimigoc5x.move(-4, 0)
                        inimigoc6x.move(-4, 0)
                        inimigoc7x.move(-4, 0)
                        inimigoc8x.move(-4, 0)
                        inimigoc9x.move(-4, 0)
                        inimigoc10x.move(-4, 0)
                        passaro.move(-1, 0)
                        paralax.move(-0.2,0)

                if voar==0 and X<=650:  # condição para quando voar==0.
                    if key == "d" or key == "D":
                        c.move(3, 0)
                        P.move(3, 0)
                        P1.move(3, 0)
                        P2.move(3, 0)
                        P3.move(3, 0)
                        P4.move(3, 0)
                        P5.move(3, 0)
                        P6.move(3, 0)
                        P7.move(3, 0)
                        P8.move(3, 0)
                        P9.move(3, 0)
                        P10.move(3, 0)
                        P11.move(3, 0)
                        P12.move(3, 0)
                        P13.move(3, 0)
                        P14.move(3, 0)
                        P15.move(3, 0)
                        P16.move(3, 0)
                        P17.move(3, 0)
                        P18.move(3, 0)
                        P19.move(3, 0)
                        P20.move(3, 0)
                        pontoChao.move(-3, 0)
                        passaro.move(-0.5, 0)
                        paralax.move(-0.2,0)

            # Se mover para esquerda sem passar da extremidade
            if X > 100 and fase1==1:
                if voar == 1:
                    if key == "a" or key == "A":
                        c.move(-8, 0)
                        P.move(-8, 0)
                        P1.move(-8, 0)
                        P2.move(-8, 0)
                        P3.move(-8, 0)
                        P4.move(-8, 0)
                        P5.move(-8, 0)
                        P6.move(-8, 0)
                        P7.move(-8, 0)
                        P8.move(-8, 0)
                        P9.move(-8, 0)
                        P10.move(-8, 0)
                        P11.move(-8, 0)
                        P12.move(-8, 0)
                        P13.move(-8, 0)
                        P14.move(-8, 0)
                        P15.move(-8, 0)
                        P16.move(-8, 0)
                        P17.move(-8, 0)
                        P18.move(-8, 0)
                        P19.move(-8, 0)
                        P20.move(-8, 0)
                        pontoChao.move(8, 0)
                        inimigo.move(4, 0)
                        inimigoc1x.move(4, 0)
                        inimigoc2x.move(4, 0)
                        inimigoc3x.move(4, 0)
                        inimigoc4x.move(4, 0)
                        inimigoc5x.move(4, 0)
                        inimigoc6x.move(4, 0)
                        inimigoc7x.move(4, 0)
                        inimigoc8x.move(4, 0)
                        inimigoc9x.move(4, 0)
                        inimigoc10x.move(4, 0)
                        passaro.move(1, 0)
                        paralax.move(0.3,0)

                else:
                    if key == "a" or key == "A":
                        c.move(-3, 0)
                        P.move(-3, 0)
                        P1.move(-3, 0)
                        P2.move(-3, 0)
                        P3.move(-3, 0)
                        P4.move(-3, 0)
                        P5.move(-3, 0)
                        P6.move(-3, 0)
                        P7.move(-3, 0)
                        P8.move(-3, 0)
                        P9.move(-3, 0)
                        P10.move(-3, 0)
                        P11.move(-3, 0)
                        P12.move(-3, 0)
                        P13.move(-3, 0)
                        P14.move(-3, 0)
                        P15.move(-3, 0)
                        P16.move(-3, 0)
                        P17.move(-3, 0)
                        P18.move(-3, 0)
                        P19.move(-3, 0)
                        P20.move(-3, 0)
                        pontoChaoMax.move(3, 0)
                        pontoChao.move(3, 0)
                        passaro.move(1, 0)
                        paralax.move(0.3,0)
                        pontoChao.move(2,0)
            # Se mover para baixo
            if voar == 1 and fase1==1:  # Enquanto voa
                if Y < 270:  # Manter o personagem na tela
                    if key == "s" or key == "S":
                        # Movimentação e colisao do jogador para baixo
                        P.move(0, 5)
                        P1.move(0, 5)
                        P2.move(0, 5)
                        P3.move(0, 5)
                        P4.move(0, 5)
                        P5.move(0, 5)
                        P6.move(0, 5)
                        P7.move(0, 5)
                        P8.move(0, 5)
                        P9.move(0, 5)
                        P10.move(0, 5)
                        P11.move(0, 5)
                        P12.move(0, 5)
                        P13.move(0, 5)
                        P14.move(0, 5)
                        P15.move(0, 5)
                        P16.move(0, 5)
                        P17.move(0, 5)
                        P18.move(0, 5)
                        P19.move(0, 5)
                        P20.move(0, 5)
                        c.move(0, 5)

                        # Movimentação e colisão do inimigo para baixo
                        inimigoc1y.move(0, -5)
                        inimigoc2y.move(0, -5)
                        inimigoc3y.move(0, -5)
                        inimigoc4y.move(0, -5)
                        inimigoc5y.move(0, -5)
                        inimigoc6y.move(0, -5)
                        inimigoc7y.move(0, -5)
                        inimigoc8y.move(0, -5)
                        inimigoc9y.move(0, -5)
                        inimigoc10y.move(0, -5)
                        inimigoc11y.move(0, -5)
                        inimigoc12y.move(0, -5)
                        inimigoc13y.move(0, -5)
                        inimigoc14y.move(0, -5)
                        inimigoc15y.move(0, -5)
                        inimigoc16y.move(0, -5)
                        inimigoc17y.move(0, -5)
                        inimigoc18y.move(0, -5)
                        inimigoc19y.move(0, -5)
                        inimigoc20y.move(0, -5)
                        inimigoc21y.move(0, -5)
                        boss.move(0,-5)
                        # Objetos do cenário
                        passaro.move(0, -5)
                        quadradinho.move(0, -5)
                        quadrado.move(0, -5)
                        sol.move(0, -5)
                        nuvem.move(0, -5)
                        nuvem2.move(0, -5)
                        cenario.move(0, -5)
                        fundo.move(0, -5)
                        inimigo.move(0, -5)
                        paralax.move(0, -5)

                # Se mover para cima enquanto voar==1:
                if Y > 20:
                    if key == "w" or key == "W":  # movimentacao para cima
                        P.move(0, -5)
                        P1.move(0, -5)
                        P2.move(0, -5)
                        P3.move(0, -5)
                        P4.move(0, -5)
                        P5.move(0, -5)
                        P6.move(0, -5)
                        P7.move(0, -5)
                        P8.move(0, -5)
                        P9.move(0, -5)
                        P10.move(0, -5)
                        P11.move(0, -5)
                        P12.move(0, -5)
                        P13.move(0, -5)
                        P14.move(0, -5)
                        P15.move(0, -5)
                        P16.move(0, -5)
                        P17.move(0, -5)
                        P18.move(0, -5)
                        P19.move(0, -5)
                        P20.move(0, -5)
                        c.move(0, -5)  # circulo que mexe

                        # inimigo se move
                        inimigo.move(0, 5)
                        inimigoc1y.move(0, 5)
                        inimigoc2y.move(0, 5)
                        inimigoc3y.move(0, 5)
                        inimigoc4y.move(0, 5)
                        inimigoc5y.move(0, 5)
                        inimigoc6y.move(0, 5)
                        inimigoc7y.move(0, 5)
                        inimigoc8y.move(0, 5)
                        inimigoc9y.move(0, 5)
                        inimigoc10y.move(0, 5)
                        inimigoc11y.move(0, 5)
                        inimigoc12y.move(0, 5)
                        inimigoc13y.move(0, 5)
                        inimigoc13y.move(0, 5)
                        inimigoc13y.move(0, 5)
                        inimigoc13y.move(0, 5)
                        inimigoc14y.move(0, 5)
                        inimigoc15y.move(0, 5)
                        inimigoc16y.move(0, 5)
                        inimigoc17y.move(0, 5)
                        inimigoc18y.move(0, 5)
                        inimigoc19y.move(0, 5)
                        inimigoc20y.move(0, 5)
                        inimigoc21y.move(0, 5)
                        boss.move(0, 5)

                        # cenario se move
                        passaro.move(0, 5)
                        quadradinho.move(0, 5)
                        quadrado.move(0, 5)
                        sol.move(0, 5)
                        nuvem.move(0, 5)
                        nuvem2.move(0, 5)
                        cenario.move(0, 5)
                        fundo.move(0, 5)
                        paralax.move(0, 5)

            # Sistema de pulo
            if voar == 0:
                if pular == 1:
                    if key == "w" or key == "W":
                        P.move(0, -30)
                        P1.move(0, -30)
                        P2.move(0, -30)
                        P3.move(0, -30)
                        P4.move(0, -30)
                        P5.move(0, -30)
                        P6.move(0, -30)
                        P7.move(0, -30)
                        P8.move(0, -30)
                        P9.move(0, -30)
                        P10.move(0, -30)
                        P11.move(0, -30)
                        P12.move(0, -30)
                        P13.move(0, -30)
                        P14.move(0, -30)
                        P15.move(0, -30)
                        P16.move(0, -30)
                        P17.move(0, -30)
                        P18.move(0, -30)
                        P19.move(0, -30)
                        P19.move(0, -30)
                        c.move(0, -30)
                        pular = 0

                    if key == "w" or key == "W":
                        P.move(0, -20)
                        P1.move(0, -20)
                        P2.move(0, -20)
                        P3.move(0, -20)
                        P4.move(0, -20)
                        P5.move(0, -20)
                        P6.move(0, -20)
                        P7.move(0, -20)
                        P8.move(0, -20)
                        P9.move(0, -20)
                        P10.move(0, -20)
                        P11.move(0, -20)
                        P12.move(0, -20)
                        P13.move(0, -20)
                        P14.move(0, -20)
                        P15.move(0, -20)
                        P16.move(0, -20)
                        P17.move(0, -20)
                        P18.move(0, -20)
                        P19.move(0, -20)
                        P20.move(0, -20)
                        c.move(0, -20)  # bola se mexe

                if Y != 290:
                    c.move(0, 1)
                    P1.move(0, 1)
                    P2.move(0, 1)
                    P3.move(0, 1)
                    P4.move(0, 1)
                    P5.move(0, 1)
                    P6.move(0, 1)
                    P7.move(0, 1)
                    P8.move(0, 1)
                    P9.move(0, 1)
                    P10.move(0, 1)
                    P11.move(0, 1)
                    P12.move(0, 1)
                    P13.move(0, 1)
                    P14.move(0, 1)
                    P15.move(0, 1)
                    P16.move(0, 1)
                    P17.move(0, 1)
                    P18.move(0, 1)
                    P19.move(0, 1)
                    P20.move(0, 1)
                    P.move(0, 1)

                if Y == 290:
                    pular = 1

            # MOVIMENTA O CENÁRIO. SOMENTE QUANDO ANDA, POIS, QUANDO VOA, O CENÁRIO SE MOVE SOZINHO
            if key == "d" or key == "D":
                pontoChao.move(-3, 0)
                quadradinho.move(-5, 0)
                quadrado.move(-3, 0)
                sol.move(-0.1, 0)
                nuvem.move(-0.5, 0)
                nuvem2.move(-0.5, 0)
                cenario.move(-5, 0)
                if voar == 0 and (X>= 650 and X <= 660):  # condição para quando voar==0.
                    quadradinho.move(-5, 0)
                    quadrado.move(-3, 0)
                    sol.move(-0.1, 0)
                    nuvem.move(-0.5, 0)
                    nuvem2.move(-0.5, 0)
                    cenario.move(-5, 0)
                    paralax.move(-0.3,0)

            # MOVIMENTA PARA ESQUERDA O CENÁRIO, PORÉM, TUDO VAI PARA A DIREITA
            elif key == "a" or key == "A":
                quadradinho.move(5, 0)
                quadrado.move(3, 0)
                sol.move(0.1, 0)
                nuvem.move(0.5, 0)
                nuvem2.move(0.5, 0)
                cenario.move(5, 0)
                pontoChao.move(3, 0)
            # DIÁLOGOS
            if permitirTexto == 1:  # dialogo sobre pq sou redondo?
                if X > 250:
                    texto1.draw(win)
                    permitirTexto = 0
                    permitirTexto2 = 1

            if X > 400:
                texto1.undraw()

            if permitirTexto2 == 1:
                if X>450:
                    texto2 = Text(Point(500, 200), "Você é uma aberração, todos nesse mundo vão tentar te matar!")
                    texto2.setSize(20)
                    texto2.setFill(color="grey")
                    texto2.draw(win)
                    permitirTexto2=0
                    permitirTexto3=1

            if X>600:
                texto2.undraw()

            if permitirTexto3==1:
                if pontoChaoX<-1050:
                    texto3 = Text(Point(500, 200), "Pressione enter para voar e começar o jogo")
                    texto3.setSize(20)
                    texto3.setFill(color="black")
                    texto3.draw(win)
                    permitirTexto3=0

            if key == "space":
                texto1.undraw()

            # Pressionar para começar a segunda fase
            if pontoChaoX<-1000 and (passou == 0):
                if podeComeca == 1:  # regra para arrumar bug do apertar enter e para inimigo
                    if key == "Return":  # Começar o jogo
                        mudarVariavel = 1
                        podeAtira = 1
                        texto3.undraw()
                        podeComeca = 0
                        pausou=0

            # TIRO
            if podeAtira == 1:  # Se puder atirar
                if key == "space":
                    tiro = Rectangle(Point(X, Y), Point((X + 5), (Y + 5)))  # origem do tiro
                    tiro.setFill(color="red")  # cor do tiro
                    tiroc = Point(X, Y)  # origem da colisao
                    tiroDown = Point(X - 1, Y)  # origem do ponto do cooldown
                    tiroMove = int(1)  # permite o tiro se mover
                    tiro.draw(win)  # desenha o tiro
                    podeAtira = 0  # impede de atirar após lançar o tiro

            # Movimento do tiro
            if tiroMove == 1:  # variavel q permite o tiro se mover
                tiro.move(2, 0)
                tiroc.move(2, 0)
                tiroDown.move(2, 0)
                posicaotiroX = float(tiroc.getX())
                posicaotiroY = float(tiroc.getY())

            # Coordenadas do tiro
            tiroDownX = tiroDown.getX()
            tiroX = tiroc.getX()
            distanciaMax = int(pontoChaoXMax)
            distanciaEntreJogador = int(tiroDownX) - int(X)

            # Limitador de tiro
            if distanciaEntreJogador > 1000 and (mudarVariavel==1 or somenteVoar==1):
                tiroMove = 0
                podeAtira = 1

            # Limite de tiro a partir da tela
            if tiroX >= distanciaMax:  # se o tiro for maior que a distancia maxima da tela, parar o tiro
                tiro.undraw()
                tiroc.move(-2, 10000)

            # Mudar variavel para ocorrer animacao e voo
            if mudarVariavel == 1:
                voar = 1
                animacao = 1
                boss.move(-0.8,0)
                bossColisao.move(-0.8,0)

            # Regra que permite o inimigo se mover
            if inimigoMover == 1:
                inimigo.move(-2, 0)
                inimigoc1x.move(-2, 0)
                inimigoc2x.move(-2, 0)
                inimigoc3x.move(-2, 0)
                inimigoc4x.move(-2, 0)
                inimigoc5x.move(-2, 0)
                inimigoc6x.move(-2, 0)
                inimigoc7x.move(-2, 0)
                inimigoc8x.move(-2, 0)
                inimigoc9x.move(-2, 0)
                inimigoc10x.move(-2, 0)
                inimigoc1y.move(-2, 0)
                inimigoc2y.move(-2, 0)
                inimigoc3y.move(-2, 0)
                inimigoc4y.move(-2, 0)
                inimigoc5y.move(-2, 0)
                inimigoc6y.move(-2, 0)
                inimigoc7y.move(-2, 0)
                inimigoc8y.move(-2, 0)
                inimigoc9y.move(-2, 0)
                inimigoc10y.move(-2, 0)
                inimigoc11y.move(-2, 0)
                inimigoc12y.move(-2, 0)
                inimigoc13y.move(-2, 0)
                inimigoc14y.move(-2, 0)
                inimigoc15y.move(-2, 0)
                inimigoc16y.move(-2, 0)
                inimigoc17y.move(-2, 0)
                inimigoc18y.move(-2, 0)
                inimigoc19y.move(-2, 0)
                inimigoc20y.move(-2, 0)
                inimigoc21y.move(-2, 0)

                # Pegar coordenada inimigo
                posicaoInimigoTotal = posicaoInimigoX or posicaoInimigoX1 or posicaoInimigoX2 or posicaoInimigoX3 or posicaoInimigoX4 or posicaoInimigoX5 or posicaoInimigoX6 or posicaoInimigoX7 or posicaoInimigoX8 or posicaoInimigoX9 or posicaoInimigoX10
                posicaoInimigoX = float(inimigoc1x.getX())
                posicaoInimigoX1 = float(inimigoc1x.getX())
                posicaoInimigoX2 = float(inimigoc2x.getX())
                posicaoInimigoX3 = float(inimigoc3x.getX())
                posicaoInimigoX4 = float(inimigoc4x.getX())
                posicaoInimigoX5 = float(inimigoc5x.getX())
                posicaoInimigoX6 = float(inimigoc6x.getX())
                posicaoInimigoX7 = float(inimigoc7x.getX())
                posicaoInimigoX8 = float(inimigoc8x.getX())
                posicaoInimigoX9 = float(inimigoc9x.getX())
                posicaoInimigoX10 = float(inimigoc10x.getX())
                posicaoInimigoY = float(inimigoc1y.getY())
                posicaoInimigoY1 = float(inimigoc2y.getY())
                posicaoInimigoY2 = float(inimigoc3y.getY())
                posicaoInimigoY3 = float(inimigoc4y.getY())
                posicaoInimigoY4 = float(inimigoc5y.getY())
                posicaoInimigoY5 = float(inimigoc6y.getY())
                posicaoInimigoY6 = float(inimigoc7y.getY())
                posicaoInimigoY7 = float(inimigoc8y.getY())
                posicaoInimigoY8 = float(inimigoc9y.getY())
                posicaoInimigoY9 = float(inimigoc10y.getY())
                posicaoInimigoY10 = float(inimigoc11y.getY())
                posicaoInimigoY11 = float(inimigoc12y.getY())
                posicaoInimigoY12 = float(inimigoc13y.getY())
                posicaoInimigoY13 = float(inimigoc14y.getY())
                posicaoInimigoY14 = float(inimigoc15y.getY())
                posicaoInimigoY15 = float(inimigoc16y.getY())
                posicaoInimigoY16 = float(inimigoc17y.getY())
                posicaoInimigoY17 = float(inimigoc18y.getY())
                posicaoInimigoY18 = float(inimigoc19y.getY())
                posicaoInimigoY19 = float(inimigoc20y.getY())
                posicaoInimigoY20 = float(inimigoc21y.getY())
                posicaoInimigoYTotal = posicaoInimigoY or posicaoInimigoY1 or posicaoInimigoY2 or posicaoInimigoY3 or posicaoInimigoY4 or posicaoInimigoY5 or posicaoInimigoY6 or posicaoInimigoY7 or posicaoInimigoY8 or posicaoInimigoY9 or posicaoInimigoY10 or posicaoInimigoY11 or posicaoInimigoY12 or posicaoInimigoY13 or posicaoInimigoY14 or posicaoInimigoY15 or posicaoInimigoY16 or posicaoInimigoY17 or posicaoInimigoY18 or posicaoInimigoY19 or posicaoInimigoY20

                # Morte inimigo
                if (
                        posicaotiroX == posicaoInimigoTotal or posicaotiroX == posicaoInimigoX1 or posicaotiroX == posicaoInimigoX2 or posicaotiroX == posicaoInimigoX3 or posicaotiroX == posicaoInimigoX4 or posicaotiroX == posicaoInimigoX5 or posicaotiroX == posicaoInimigoX6 or posicaotiroX == posicaoInimigoX7 or posicaotiroX == posicaoInimigoX8 or posicaotiroX == posicaoInimigoX9 or posicaotiroX == posicaoInimigoX10) and (
                        posicaotiroY == posicaoInimigoY or posicaotiroY == posicaoInimigoY1 or posicaotiroY == posicaoInimigoY2 or posicaotiroY == posicaoInimigoY3 or posicaotiroY == posicaoInimigoY4 or posicaotiroY == posicaoInimigoY5 or posicaotiroY == posicaoInimigoY6 or posicaotiroY == posicaoInimigoY7 or posicaotiroY == posicaoInimigoY8 or posicaotiroY == posicaoInimigoY9 or posicaotiroY == posicaoInimigoY10 or posicaotiroY == posicaoInimigoY11 or posicaotiroY == posicaoInimigoY12 or posicaotiroY == posicaoInimigoY13 or posicaotiroY == posicaoInimigoY14 or posicaotiroY == posicaoInimigoY15 or posicaotiroY == posicaoInimigoY16 or posicaotiroY == posicaoInimigoY17 or posicaotiroY == posicaoInimigoY18 or posicaotiroY == posicaoInimigoY19 or posicaotiroY == posicaoInimigoY20):
                    tiro.undraw()  # Some tiro
                    inimigo.undraw()  # Some inimigo
                    tiroc.move(0, 1000)
                    inimigoMover = 0
                    inimigo1 = inimigo1 - 1
                    textoContador.undraw()
                    contador = contador + 1
                    podeContadorTexto = 1

            if posicaoInimigoX < (X - 930):
                inimigo1 = 0

            #Boss se mexer
            if bossMover == 1:
                boss.move(0.6, 0)
                bossColisao.move(0.6, 0)

            bossColisaoX = bossColisao.getX()
            if X == int(bossColisaoX):
                morto = 1


            # Morrer
            if (
                    posicaoInimigoTotal == X or posicaoInimigoTotal == X1 or posicaoInimigoTotal == X2 or posicaoInimigoTotal == X3 or posicaoInimigoTotal == X4 or posicaoInimigoTotal == X5 or posicaoInimigoTotal == X6 or posicaoInimigoTotal == X7 or posicaoInimigoTotal == X8 or posicaoInimigoTotal == X9 or posicaoInimigoTotal == X9 or posicaoInimigoTotal == X10 or posicaoInimigoTotal == X11 or posicaoInimigoTotal == X12 or posicaoInimigoTotal == X13 or posicaoInimigoTotal == X14 or posicaoInimigoTotal == X15 or posicaoInimigoTotal == X16 or posicaoInimigoTotal == X17 or posicaoInimigoTotal == X18 or posicaoInimigoTotal == X19 or posicaoInimigoTotal == X20) and (
                    posicaoInimigoYTotal == Y or posicaoInimigoYTotal == Y1 or posicaoInimigoYTotal == Y2 or posicaoInimigoYTotal == Y3 or posicaoInimigoYTotal == Y4 or posicaoInimigoYTotal == Y5 or posicaoInimigoYTotal == Y6 or posicaoInimigoYTotal == Y7 or posicaoInimigoYTotal == Y8 or posicaoInimigoYTotal == Y9 or posicaoInimigoYTotal == Y10 or posicaoInimigoYTotal == Y11 or posicaoInimigoYTotal == Y12 or posicaoInimigoYTotal == Y13 or posicaoInimigoYTotal == Y14 or posicaoInimigoYTotal == Y15 or posicaoInimigoYTotal == Y16 or posicaoInimigoYTotal == Y17 or posicaoInimigoYTotal == Y18 or posicaoInimigoYTotal == Y19 or posicaoInimigoYTotal == Y20):
                c.undraw()  # morre
                podeAtira = 0
                morto=1


            # Animação do cenário
            if animacao == 1:
                for animacao in range(1):
                    fundo.move(-1, 0)
                    quadradinho.move(-1, 0)
                    quadrado.move(-1, 0)
                    sol.move(-0.01, 0)
                    nuvem.move(-1, 0)
                    nuvem2.move(-1, 0)
                    cenario.move(-1, 0)
                    pontoChao.move(-1, 0)  # define o quanto o cenário vai andar
                    paralax.move(-0.1,0)

            # Passar tutorial
            if passarSemTutorial == 1:
                if X > 600:
                    inimigo1 = 0
                    passarSemTutorial = 0

            # Concluir
            if pontoChaoX <= -8000 and passou==0:
                passou = 1
                if textoVencedorSim == 1:
                    textoVencedor.draw(win)
                    textoVencedorSim = 0
                    jogoNaoComecou=1

        if pausou == 0:
            if key == "p":
                contadorDoPause.move(-1,0)
                contadorDoPauseX = contadorDoPause.getX()
                jogoNaoComecou = 1
                podeReiniciar=0

                if textoPausePode == 1:
                    jogoPausado = Text(Point(500, 250), "JOGO PAUSADO")
                    jogoPausado.setFill(color="black")
                    jogoPausado.setSize(35)
                    jogoPausado.draw(win)
                    textoPausePode = 0

                if contadorDoPauseX<-1:
                    pausou = 1
                    contadorDoPause.move(1,0)
                    contadorDoPause=Point(0,0)
                    jogoPausado.undraw()
                    textoPausePode=1

            if pausou == 1:
                if key == "p":
                    jogoNaoComecou = 0
                    pausou = 0
                    podeReiniciar=1

            #passar para fase 2
            if passou==1:
                if key=="Return":
                    cenario.undraw()
                    quadradinho.undraw()
                    sol.undraw()
                    nuvem.undraw()
                    nuvem2.undraw()
                    quadrado.undraw()
                    paralax.undraw()
                    bossMover=0
                    morto=0
                    fasee2=1
                    fase1=0
                    passou=2
                    contadorTotal=contador

            #MECANICA FASE 2
            if (fasee2==1 or key=="r" or morto==1) and passou==2:
                contador=0
                mudarVariavel=0
                morto = 0
                CenarioMove=1
                jogoNaoComecou=0
                fasee2=0
                somenteVoar=1
                inimigo1 = 0
                podeAtira = 1
                voar=1
                fase1=0
                bossMover=0
                c.undraw()
                fundo.undraw()
                boss.undraw()

                #redesenhar tudo dnv
                fase2 = Image(Point(5000, 250), "fundo2.gif")
                fase2.draw(win)

                pontoChao = Point(0, 0)  # ponto do inicio do chão, vai servir para definir roteiro de eventos
                pontoChaoX = pontoChao.getX()  # obtem coordenada
                pontoChaoMax = (
                    Point(1050, 0))  # ponto do fim da janela no eixo X, para definir que as coisas não saiam da janela
                pontoChaoXMax = pontoChaoMax.getX()  # coordenada do maximo do chao

                # Jogador
                c = Circle(Point(200, 290), 10)  # bola
                c.setFill(color="red")
                c.draw(win)
                # Sistema de colisão
                P = Point(200, 280)
                P1 = Point(201, 281)
                P2 = Point(202, 282)
                P3 = Point(203, 283)
                P4 = Point(204, 284)
                P5 = Point(205, 285)
                P6 = Point(206, 286)
                P7 = Point(207, 287)
                P8 = Point(208, 288)
                P9 = Point(209, 289)
                P10 = Point(210, 290)
                P11 = Point(209, 291)
                P12 = Point(208, 292)
                P13 = Point(207, 293)
                P14 = Point(206, 294)
                P15 = Point(205, 295)
                P16 = Point(204, 296)
                P17 = Point(203, 297)
                P18 = Point(202, 298)
                P19 = Point(201, 299)
                P20 = Point(200, 300)

            if CenarioMove == 1 and jogoNaoComecou==0:
                if X < 800 and somenteVoar == 1:  # Só pode se mover para direita se não passar do pixel 900, pois se passar,
                    # pode sair da tela
                    if voar == 1:  # Condição para se mover enquanto voa
                        if key == "d" or key == "D":
                            c.move(8, 0)
                            P.move(8, 0)
                            P1.move(8, 0)
                            P2.move(8, 0)
                            P3.move(8, 0)
                            P4.move(8, 0)
                            P5.move(8, 0)
                            P6.move(8, 0)
                            P7.move(8, 0)
                            P8.move(8, 0)
                            P9.move(8, 0)
                            P10.move(8, 0)
                            P11.move(8, 0)
                            P12.move(8, 0)
                            P13.move(8, 0)
                            P14.move(8, 0)
                            P15.move(8, 0)
                            P16.move(8, 0)
                            P17.move(8, 0)
                            P18.move(8, 0)
                            P19.move(8, 0)
                            P20.move(8, 0)

                # Se mover para esquerda sem passar da extremidade
                if X > 30 and somenteVoar == 1:
                    if voar == 1:
                        if key == "a" or key == "A":
                            c.move(-8, 0)
                            P.move(-8, 0)
                            P1.move(-8, 0)
                            P2.move(-8, 0)
                            P3.move(-8, 0)
                            P4.move(-8, 0)
                            P5.move(-8, 0)
                            P6.move(-8, 0)
                            P7.move(-8, 0)
                            P8.move(-8, 0)
                            P9.move(-8, 0)
                            P10.move(-8, 0)
                            P11.move(-8, 0)
                            P12.move(-8, 0)
                            P13.move(-8, 0)
                            P14.move(-8, 0)
                            P15.move(-8, 0)
                            P16.move(-8, 0)
                            P17.move(-8, 0)
                            P18.move(-8, 0)
                            P19.move(-8, 0)
                            P20.move(-8, 0)

                # Se mover para baixo
                if voar == 1 and somenteVoar == 1:  # Enquanto voa
                    if Y < 470:  # Manter o personagem na tela
                        if key == "s" or key == "S":
                            # Movimentação e colisao do jogador para baixo
                            P.move(0, 8)
                            P1.move(0, 8)
                            P2.move(0, 8)
                            P3.move(0, 8)
                            P4.move(0, 8)
                            P5.move(0, 8)
                            P6.move(0, 8)
                            P7.move(0, 8)
                            P8.move(0, 8)
                            P9.move(0, 8)
                            P10.move(0, 8)
                            P11.move(0, 8)
                            P12.move(0, 8)
                            P13.move(0, 8)
                            P14.move(0, 8)
                            P15.move(0, 8)
                            P16.move(0, 8)
                            P17.move(0, 8)
                            P18.move(0, 8)
                            P19.move(0, 8)
                            P20.move(0, 8)
                            c.move(0, 8)

                    # Se mover para cima enquanto voar==1:
                    if Y > 10 and somenteVoar==1:
                        if key == "w" or key == "W":  # movimentacao para cima
                            P.move(0, -8)
                            P1.move(0, -8)
                            P2.move(0, -8)
                            P3.move(0, -8)
                            P4.move(0, -8)
                            P5.move(0, -8)
                            P6.move(0, -8)
                            P7.move(0, -8)
                            P8.move(0, -8)
                            P9.move(0, -8)
                            P10.move(0, -8)
                            P11.move(0, -8)
                            P12.move(0, -8)
                            P13.move(0, -8)
                            P14.move(0, -8)
                            P15.move(0, -8)
                            P16.move(0, -8)
                            P17.move(0, -8)
                            P18.move(0, -8)
                            P19.move(0, -8)
                            P20.move(0, -8)
                            c.move(0, -8)  # circulo que mexe


                    if pontoChaoX >= -9000:
                        fase2.move(-1, 0)
                        pontoChao.move(-1, 0)

                    if pontoChaoX<-9000:
                        textoVencedorParabens=1
                        if textoVencedorParabens == 1:
                            contadorTotal=contadorTotal + contador
                            textoFim = Text(Point(500, 250), "Parabéns! Você venceu. Seus pontos:")
                            textoFim.setSize(20)
                            textoFim.setFill(color="black")
                            textoFim.draw(win)
                            textoContador1 = Text(Point(530, 280), (contadorTotal))
                            textoContador1.setSize(30)
                            textoContador1.setFill(color="red")
                            textoContador1.draw(win)
                            textoVencedorParabens = 0
                        jogoNaoComecou=1

                    if pontoChaoX==-1400:
                        boss = Rectangle(Point(1000,0),Point(2000,500))
                        boss.setFill(color_rgb(139, 69, 19))
                        boss.draw(win)
                        bossColisao2 = (Point(1000, 200))
                        bossDano=1

                    if bossDano==1:
                        boss.move(-0.1,0)
                        bossColisao2.move(-0.1,0)
                        boss2ColisaoX = int(bossColisao2.getX())
                        if X==boss2ColisaoX:
                            bossDano=0
                            morto=1

                        if boss2ColisaoX==tiroX or boss2ColisaoX==tiroDownX:
                            tiro.undraw()
                            bossMorre = bossMorre + 1
                            tiroc.move(-20,-1000)
                        if bossMorre == 12:
                            boss.undraw()
                            bossDano=0
                            contador=contador+1

        key = win.checkKey()
        update(500)

    win.close()

main()