import pygame
import sys

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 30
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

class Ball:
	def _init_(self):
		self.x = WIDTH // 2
		self.y = HEIGHT // 2
		self.dx = 5
		self.dy = -5

#main function
def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption("Breakout")
	clock = pygame.time.Clock()

	paddle = Paddle()
	ball = Ball()
	bricks = create_bricks()
	lives = 3
	score = 0
	font = pygame.font.SysFont(None, 36)

	running = True
	game_over = False
	win = False
	while running:
		clock.tick(FPS)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		if not game_over:
			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				paddle.move('left')
			if keys[pygame.K_RIGHT]:
				paddle.move('right')

			ball.move()

			# Ball and paddle collision
			if ball.get_rect().colliderect(paddle.rect):
				ball.dy *= -1
				# Bounce the ball according to the position on the paddle
				offset = (ball.x - paddle.rect.centerx) / (PADDLE_WIDTH // 2)
				ball.dx = int(7 * offset)
				ball.y = paddle.rect.y - BALL_RADIUS

			# Ball and brick collision
			for brick in bricks:
				if brick.alive and ball.get_rect().colliderect(brick.rect):
					brick.alive = False
					score += 10
					# Bounce the ball correctly
					if abs(ball.x - brick.rect.left) < BALL_RADIUS or abs(ball.x - brick.rect.right) < BALL_RADIUS:
						ball.dx *= -1
					else:
						ball.dy *= -1
					break

			# Ball out of bounds
			if ball.y > HEIGHT:
				game_over = True

			# Win condition
			if all(not brick.alive for brick in bricks):
				win = True
				game_over = True

		screen.fill((0, 0, 0))
		paddle.draw(screen)
		ball.draw(screen)
		for brick in bricks:
			brick.draw(screen)

		# Draw score only
		score_text = font.render(f"Score: {score}", True, (255, 255, 255))
		screen.blit(score_text, (10, 10))

		# Draw game over or win
		if game_over:
			if win:
				msg = "YOU WIN!"
			else:
				msg = "GAME OVER"
			msg_text = font.render(msg, True, (255, 255, 255))
			screen.blit(msg_text, (WIDTH // 2 - msg_text.get_width() // 2, HEIGHT // 2))
			keys = pygame.key.get_pressed()
			if keys[pygame.K_ESCAPE]:
				running = False

		pygame.display.flip()

	pygame.quit()
	sys.exit()


if __name__ == "__main__":
	main()