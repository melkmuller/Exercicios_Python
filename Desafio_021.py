# Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('arquivos\Quem é Você.mp3')
pygame.mixer.music.play(start=0)
pygame.event.wait()

