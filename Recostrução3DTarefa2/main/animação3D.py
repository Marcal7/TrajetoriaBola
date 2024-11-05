from statistics import mean
from vpython import sphere, vector, rate, canvas
import pandas as pd

# Carregar o arquivo CSV com as métricas Frame, X, Y, Z
csv_file_path = 'CoordenadasBolaCorreto.csv'  # Substitua pelo caminho do seu arquivo CSV
data = pd.read_csv(csv_file_path)

# Encontrar as dimensões da trajetória para centralizar a visão
x_min, x_max = data['X'].min(), data['X'].max()
y_min, y_max = data['Y'].min(), data['Y'].max()
z_min, z_max = data['Z'].min(), data['Z'].max()

mediaX = mean(data['X'])
# Calcular o centro da trajetória
center_x = (x_max + x_min) / mean(data['X'])
center_y = (y_max + y_min) / mean(data['Y'])
center_z = (z_max + z_min) / 2
trajectory_center = vector(center_x, center_y, center_z)

# Configuração da cena para visão ampla
scene = canvas(background=vector(0.8, 0.9, 1))  # Fundo azul claro
scene.width = 1280
scene.height = 720

# Definir a câmera mais distante e centralizar a direção para uma visão ampla
scene.camera.pos = vector(center_x, center_y, center_z + max(x_max - x_min, y_max - y_min, z_max - z_min) * 2)
scene.camera.axis = trajectory_center - scene.camera.pos  # Apontar para o centro da trajetória

# Criar a bola
ball = sphere(pos=vector(0, 0, 0), radius=5, color=vector(1, 0.5, 0))  # Bola laranja e maior

# Configuração da taxa de atualização
rate_of_animation = 10  # Limitar a animação a 10 frames por segundo

frame_files = []
i = 0
# Animação da bola com base nos dados do CSV
while True:
    for _, row in data.iterrows():
        rate(rate_of_animation)
        i = i + 1

        # Obter coordenadas X, Y, Z do frame atual
        x, y, z = row['X'], row['Y'], row['Z']

        # Atualizar posição da bola
        ball.pos = vector(x, y, z)
