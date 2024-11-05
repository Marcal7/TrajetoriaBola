## Trajetória da Bola 

### Análise da Trajetória em 3D

Este projeto explora a análise da trajetória de uma bola utilizando técnicas de visão computacional. A partir de uma sequência de imagens, a bola é detectada e suas coordenadas são utilizadas para gerar uma animação 3D realista.

### Metodologia

1. **Aquisição de Imagens:** As imagens foram capturadas em um ambiente controlado, garantindo condições de iluminação e contraste adequados.
2. **Detecção da Bola:**
   * **Pré-processamento:** As imagens foram convertidas para escala de cinza e aplicados filtros para reduzir ruído.
   * **Transformada de Hough:** A Transformada de Hough foi utilizada para detectar círculos nas imagens, representando a bola. A transformada de Hough é um método de detecção de formas geométricas em imagens, ideal para detectar objetos circulares como a bola.
3. **Rastreamento da Bola:** As coordenadas do centro da bola foram extraídas em cada frame, permitindo rastrear sua trajetória ao longo do tempo.
4. **Visualização 3D:** Utilizando a biblioteca VPython, as coordenadas 3D da bola foram plotadas em um gráfico 3D, gerando uma animação realista da trajetória.

### Resultados

A animação gerada demonstra a efetividade das técnicas utilizadas para detectar e rastrear a bola. A visualização 3D permite uma análise detalhada da trajetória, identificando pontos de inflexão e variações de velocidade.

![Image of GIF animation]('https://github.com/Marcal7/TrajetoriaBola/blob/main/bola.gif')

### Referências
* OpenCV Documentation: https://docs.opencv.org/4.x/index.html
* VPython Documentation: https://vpython.org/contents/doc.html
