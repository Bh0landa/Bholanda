import math
import shutil
import subprocess
import sys
import turtle
from math import hypot

# =========================
# Configuration
# =========================
WIDTH, HEIGHT = 800, 600
PADDLE_H, PADDLE_W = 100, 20
PADDLE_SPEED = 8              # pixels per frame when a key is held

BALL_BASE_SPEED = 6.0         # pixels per tick
ACCEL_FACTOR = 1.06           # acceleration on each paddle hit
MAX_SPEED = 18.0              # max ball speed
TICK_MS = 16                  # ~60 FPS
MAX_BOUNCE_ANGLE_DEG = 60.0   # max reflection angle off paddles
FONT = ("Press Start 2P", 24, "normal")

# =========================
# Beeper (no files)
# =========================
def tone(freq_hz: int, dur_ms: int) -> None:
    # Generate a simple square/sine-like beep, best-effort per OS
    try:
        if sys.platform.startswith("win"):
            import winsound  # type: ignore
            winsound.Beep(freq_hz, dur_ms)
            return

        # macOS / Linux: try SoX 'play -n synth'
        if shutil.which("play"):
            # Example: play -nq synth 0.05 sine 800
            seconds = max(0.005, dur_ms / 1000.0)
            subprocess.Popen(
                ["play", "-nq", "synth", f"{seconds:.3f}", "sine", str(freq_hz)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            return
    except Exception:
        pass
    # If nothing available, do nothing (silent fallback)


def beep_bounce() -> None:
    # Short, higher-pitched blip
    tone(800, 50)


def beep_score() -> None:
    # Slightly lower, longer bloop for scoring
    tone(240, 150)


# =========================
# Utilities
# =========================
def clamp(value: float, lo: float, hi: float) -> float:
    # Clamp a value between lo and hi
    return max(lo, min(hi, value))


def rects_overlap(ax, ay, aw, ah, bx, by, bw, bh) -> bool:
    # Axis-Aligned Bounding Box (AABB) overlap check
    return (abs(ax - bx) * 2 < (aw + bw)) and (abs(ay - by) * 2 < (ah + bh))


def next_speed(dx: float, dy: float) -> float:
    # Compute next speed after acceleration, capped by MAX_SPEED
    speed = hypot(dx, dy) * ACCEL_FACTOR
    return min(speed, MAX_SPEED)


def velocity_from_angle(speed: float, angle_rad: float, go_right: bool) -> tuple[float, float]:
    # Build (dx, dy) from speed and angle; go_right controls horizontal direction
    dx = speed * math.cos(angle_rad)
    dy = speed * math.sin(angle_rad)
    dx = abs(dx) if go_right else -abs(dx)
    return dx, dy


# =========================
# Screen and objects
# =========================
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

# Left paddle
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)  # 100x20
paddle_1.penup()
paddle_1.goto(-WIDTH // 2 + 50, 0)

# Right paddle
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(WIDTH // 2 - 50, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = BALL_BASE_SPEED
ball.dy = BALL_BASE_SPEED

# Score
score_1, score_2 = 0, 0
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, HEIGHT // 2 - 40)
hud.write("0 : 0", align="center", font=FONT)

# =========================
# Key state (press/release)
# =========================
keys = {"w": False, "s": False, "Up": False, "Down": False}

def on_press_w() -> None:
    keys["w"] = True

def on_release_w() -> None:
    keys["w"] = False

def on_press_s() -> None:
    keys["s"] = True

def on_release_s() -> None:
    keys["s"] = False

def on_press_up() -> None:
    keys["Up"] = True

def on_release_up() -> None:
    keys["Up"] = False

def on_press_down() -> None:
    keys["Down"] = True

def on_release_down() -> None:
    keys["Down"] = False

# Bind key press and release (continuous movement without OS auto-repeat)
screen.listen()
screen.onkeypress(on_press_w, "w")
screen.onkeyrelease(on_release_w, "w")
screen.onkeypress(on_press_s, "s")
screen.onkeyrelease(on_release_s, "s")
screen.onkeypress(on_press_up, "Up")
screen.onkeyrelease(on_release_up, "Up")
screen.onkeypress(on_press_down, "Down")
screen.onkeyrelease(on_release_down, "Down")

# =========================
# Helpers
# =========================
def move_paddles_continuous() -> None:
    # Move paddles each frame based on key state
    if keys["w"]:
        new_y = clamp(
            paddle_1.ycor() + PADDLE_SPEED,
            -HEIGHT // 2 + PADDLE_H // 2,
            HEIGHT // 2 - PADDLE_H // 2,
        )
        paddle_1.sety(new_y)

    if keys["s"]:
        new_y = clamp(
            paddle_1.ycor() - PADDLE_SPEED,
            -HEIGHT // 2 + PADDLE_H // 2,
            HEIGHT // 2 - PADDLE_H // 2,
        )
        paddle_1.sety(new_y)

    if keys["Up"]:
        new_y = clamp(
            paddle_2.ycor() + PADDLE_SPEED,
            -HEIGHT // 2 + PADDLE_H // 2,
            HEIGHT // 2 - PADDLE_H // 2,
        )
        paddle_2.sety(new_y)

    if keys["Down"]:
        new_y = clamp(
            paddle_2.ycor() - PADDLE_SPEED,
            -HEIGHT // 2 + PADDLE_H // 2,
            HEIGHT // 2 - PADDLE_H // 2,
        )
        paddle_2.sety(new_y)

def update_score() -> None:
    # Update scoreboard HUD
    hud.clear()
    hud.write(f"{score_1} : {score_2}", align="center", font=FONT)

# =========================
# Game loop
# =========================
def game_loop() -> None:
    # Main game loop: input, physics, collisions, scoring
    global score_1, score_2

    # 1) Input
    move_paddles_continuous()

    # 2) Physics
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # 3) Walls
    top_y = HEIGHT // 2 - 10
    bottom_y = -HEIGHT // 2 + 10
    if ball.ycor() > top_y:
        ball.sety(top_y)
        ball.dy *= -1
        beep_bounce()

    if ball.ycor() < bottom_y:
        ball.sety(bottom_y)
        ball.dy *= -1
        beep_bounce()

    # 4) Scoring
    left_x = -WIDTH // 2 + 10
    right_x = WIDTH // 2 - 10
    if ball.xcor() < left_x:
        score_2 += 1
        update_score()
        beep_score()
        ball.goto(0, 0)
        ball.dx, ball.dy = BALL_BASE_SPEED, BALL_BASE_SPEED

    if ball.xcor() > right_x:
        score_1 += 1
        update_score()
        beep_score()
        ball.goto(0, 0)
        ball.dx, ball.dy = -BALL_BASE_SPEED, -BALL_BASE_SPEED

    # 5) Paddle collisions with angle variation and acceleration
    max_angle = math.radians(MAX_BOUNCE_ANGLE_DEG)

    if rects_overlap(
        ball.xcor(), ball.ycor(), 20, 20,
        paddle_1.xcor(), paddle_1.ycor(), PADDLE_W, PADDLE_H,
    ) and ball.dx < 0:
        ball.setx(paddle_1.xcor() + PADDLE_W // 2 + 10)
        offset = (ball.ycor() - paddle_1.ycor()) / (PADDLE_H / 2)
        offset = clamp(offset, -1.0, 1.0)
        angle = offset * max_angle
        speed = next_speed(ball.dx, ball.dy)
        ball.dx, ball.dy = velocity_from_angle(speed, angle, go_right=True)
        beep_bounce()

    if rects_overlap(
        ball.xcor(), ball.ycor(), 20, 20,
        paddle_2.xcor(), paddle_2.ycor(), PADDLE_W, PADDLE_H,
    ) and ball.dx > 0:
        ball.setx(paddle_2.xcor() - PADDLE_W // 2 - 10)
        offset = (ball.ycor() - paddle_2.ycor()) / (PADDLE_H / 2)
        offset = clamp(offset, -1.0, 1.0)
        angle = offset * max_angle
        speed = next_speed(ball.dx, ball.dy)
        ball.dx, ball.dy = velocity_from_angle(speed, angle, go_right=False)
        beep_bounce()

    # 6) Render and next frame
    screen.update()
    screen.ontimer(game_loop, TICK_MS)


# Start game
update_score()
game_loop()
screen.mainloop()
