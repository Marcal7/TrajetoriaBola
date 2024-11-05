# TrajetoriaBola
Repositório referendo a Tarefa2


# Análise da Trajetória da Bola em 3D

Este projeto tem como objetivo analisar a trajetória de uma bola a partir de uma série de imagens, utilizando técnicas de visão computacional para detectar a bola e registrar suas coordenadas em um arquivo CSV. Em seguida, as coordenadas são utilizadas para criar uma animação 3D da trajetória da bola.

## Descrição do Trabalho

O trabalho foi realizado em duas etapas principais:

1. **Detecção da Bola**: Utilizamos a Transformada de Hough para detectar a bola nas imagens em escala de cinza.
2. **Animação 3D**: Com as coordenadas obtidas, foi gerada uma animação 3D da trajetória da bola usando a biblioteca VPython.

**Visualização da Animação**
A animação gerada foi salva no formato GIF e está disponível abaixo para visualização:
![]('https://raw.githubusercontent.com/Marcal7/TrajetoriaBola/main/bola.gif')

**Considerações Finais**
O projeto demonstrou a aplicação de técnicas de visão computacional na análise de trajetória de objetos. A Transformada de Hough foi eficaz na detecção da bola, e a visualização 3D proporcionou uma melhor compreensão da trajetória percorrida.

Referências
[OpenCV Documentation]('https://docs.opencv.org/4.x/index.html')
[VPython Documentation]('https://vpython.org/contents/doc.html')
