import pygame

# Inicializa o mixer do pygame
pygame.mixer.init()

# Carrega o arquivo MP3
pygame.mixer.music.load("Slipknot-Duality.mp3")

# Toca a música
pygame.mixer.music.play()

# Mantém o programa em execução enquanto a música toca
while pygame.mixer.music.get_busy():
    pass  # Espera terminar
