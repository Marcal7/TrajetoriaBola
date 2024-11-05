import cv2
import glob
import csv
import numpy as np

# Carrega as imagens em ordem
frames = sorted(glob.glob("frames/c1/*.png"))
delay = 30

controle = False

# Abre o arquivo CSV para salvar as coordenadas
with open('CoordenadasBolaCorreto.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Frame', 'X', 'Y', 'Z'])  # Cabeçalhos do CSV

    # Variável para armazenar o ponto inicial
    ponto_inicial = None

    for idx, frame_path in enumerate(frames):
        frame = cv2.imread(frame_path, cv2.IMREAD_GRAYSCALE)

        # Aplicar um desfoque para reduzir ruído
        frame_blur = cv2.GaussianBlur(frame, (9, 9), 2)

        # Detectar círculos usando a Transformada de Hough
        circles = cv2.HoughCircles(
            frame_blur,
            cv2.HOUGH_GRADIENT,
            dp=1.2,
            minDist=10,
            param1=40,
            param2=27,
            minRadius=15,
            maxRadius=30
        )

        # Verifica se algum círculo foi detectado
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")

            # Pegue o primeiro círculo detectado (presume que seja a bola)
            x, y, r = circles[0]

            # Desenha o círculo na imagem para visualização
            cv2.circle(frame, (x, y), r, (255, 0, 0), 2)

            # Define o ponto inicial se ele ainda não estiver definido
            if ponto_inicial is None:
                ponto_inicial = (x, y)

            # Calcula a posição relativa em relação ao ponto inicial
            x_relativo = x - ponto_inicial[0]
            y_relativo = y - ponto_inicial[1]

            if y_relativo <0:
                y_relativo = y_relativo * -1

            if x_relativo != 0 and -1 and +1:
                writer.writerow([idx, x_relativo, y_relativo, 0])

        # Mostra a imagem com a marcação
        cv2.imshow("Video", frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()

