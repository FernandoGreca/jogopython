import pygame
import random


pygame.init()
width, height = 1024, 640
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
speed = 5
ash_x = width // 2
ash_y = height // 1.2
ash_width = 50
ash_height = 100
ground_height = 100
gravity = 0.5
ball_x = width // 2
ball_y = height // 6
ball_speed = 5
ball_radius = 50
ball_height_spawn = 20
score = 0 
ash_y_velocity = 0
ball_y = height // 6
ball_x = random.randint(0, width)
wall = 986


def draw_background():
    background_img = pygame.image.load("img\\backjogo.jpg")
    background_width, background_height = background_img.get_size()
    screen.blit(background_img, (0, 0))


def draw_ball():
    ball_img = pygame.image.load("img\\pokebola.png")
    ball_width, ball_height = ball_img.get_size()
    screen.blit(ball_img, (ball_x, ball_y))


def draw_ash():
    ash_img = pygame.image.load("img\\ash.png")
    ash_width, ash_height = ash_img.get_size()
    ash_redimencionado = pygame.transform.scale(ash_img, (100, 110))
    screen.blit(ash_redimencionado, (ash_x, ash_y))


def draw():
    screen.fill("pink")
    
    draw_background()
    draw_ball()
    draw_ash()
    
    # Contador de pontos
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()


def walk_ash():
    global ash_x, ash_y
    # Faz com que ele ande
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ash_y -= 8
    if keys[pygame.K_q]:
        ash_y -= 8
        ash_x -= speed   
    if keys[pygame.K_e]:
        ash_y -= 8
        ash_x += speed
    if keys[pygame.K_a]:
        ash_x -= speed
    if keys[pygame.K_d]:
        ash_x += speed
    

def fall_ball():
    global ash_y, ash_y_velocity, ball_y, ball_x, score, wall, ball_height_spawn, ball_speed

    ball_y += ball_speed
    # Variável da colisao
    distance = ((ball_x - ash_x) ** 2 + (ball_y - ash_y) ** 2) ** 0.5
    
    if distance < ball_radius + ash_width / 2:
        # Caso o personagem pegue a pokebola outra nasce no topo em um X variado
        ball_y = random.randint(0, ball_height_spawn)
        ball_x = random.randint(0, wall)
        ash_y = height // 1.2
        ash_y_velocity = 0
        # Adiciona um ponto ao contador
        score += 1

    # Verifica se a pokebola ultrapassou o chão
    if ball_y > height - ground_height:
        ball_y = random.randint(0, ball_height_spawn)
        ball_x = random.randint(0, wall)


def box():
    global ash_x, ash_y, ash_y_velocity, wall
    # Cria-se um chao e paredes
    if ash_y + ash_height > height - ground_height:
        ash_y = height - ground_height - ash_height
        ash_y_velocity = 0
    if ash_y < 0:
        ash_y = 0
    if ash_x + ash_width > wall:
        ash_x = wall - ash_width
    if ash_x < 0:
        ash_x = 0


def update():
    global ash_y, ash_y_velocity, score, running

    walk_ash()
    fall_ball()
    box()
    
    # Gravidade
    ash_y_velocity += gravity
    ash_y += ash_y_velocity

    # Finaliza o jogo ao chegar em 10
    if score >= 10:
        running = False
    
    
# Loop principal
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_ESCAPE: 
                running = False

    update()
    draw()
    clock.tick(60)

# Quando o loop terminar, mostra a pontuação final
font = pygame.font.Font(None, 72)
score_gameover = font.render("You Win!!!", True, (255, 255, 255))
score_text = font.render(f"Final Score: {score}", True, (255, 255, 255))
score_background = screen.fill("black")
screen.blit(score_gameover, (width // 2.6, height // 2.8))
screen.blit(score_text, (width // 3.1, height // 2))
pygame.display.update()

# Aguarda alguns segundos antes de fechar
pygame.time.wait(3000)

pygame.quit()
