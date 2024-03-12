import pygame
from pygame import Rect, Surface

# Tamanho da janela
SC_WIDTH = 576
SC_HEIGHT = 324

# Inicializar o modulo pygame
pygame.init()

# Criação da janela do pygame
screen: Surface = pygame.display.set_mode(size=(SC_WIDTH, SC_HEIGHT))

# Carregar img e gerar uma superficie
bg_surf: Surface = pygame.image.load('./assets/PRE_ORIG_SIZE.png').convert_alpha()
player1: Surface = pygame.image.load('./assets/Shot_1.png').convert_alpha() 

# obter o retangulo da superficie
bg_rect: Rect = bg_surf.get_rect(left=0, top=0)
player1_rect: Rect = player1.get_rect(left=100, top=100)


# desenhar na tela
screen.blit(source=bg_surf, dest=bg_rect)
screen.blit(source=player1, dest=player1_rect)
pygame.display.update()

clock = pygame.time.Clock()
while True:
  clock.tick(60)
  # print(clock.get_fps()) # mostrar o fps o fps
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      quit()
  pressed_key = pygame.key.get_pressed()
  if pressed_key[pygame.K_w]:
    player1_rect.centery -= 1
    screen.blit(source=bg_surf, dest=bg_rect)
    screen.blit(source=player1, dest=player1_rect)
    pygame.display.flip()
  
  if pressed_key[pygame.K_s]:
    player1_rect.centery += 1
    screen.blit(source=bg_surf, dest=bg_rect)
    screen.blit(source=player1, dest=player1_rect)
    pygame.display.flip()

  if pressed_key[pygame.K_d]:
    player1_rect.centerx += 1
    screen.blit(source=bg_surf, dest=bg_rect)
    screen.blit(source=player1, dest=player1_rect)
    pygame.display.flip()
  
  if pressed_key[pygame.K_a]:
    player1_rect.centerx -= 1
    screen.blit(source=bg_surf, dest=bg_rect)
    screen.blit(source=player1, dest=player1_rect)
    pygame.display.flip()