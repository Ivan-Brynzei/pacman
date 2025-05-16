import pytest
import pygame
from src.pacman import Pacman
from src.settings import PACMAN_SPEED, WIDTH


@pytest.fixture
def pacman():
    pygame.init()
    pacman = Pacman(row=1, col=1, size=32, life=3)
    yield pacman
    pygame.quit()


def test_pacman_init(pacman):
    assert pacman.x == 32
    assert pacman.y == 32
    assert pacman.speed == PACMAN_SPEED
    assert pacman.life == 3
    assert len(pacman.frames) == 4
    assert pacman.rect.topleft == (32, 32)
    assert pacman.direction == (0, 0)
    assert pacman.direction_name == ''


def test_pacman_move_right(pacman):
    pressed_key = {
        pygame.K_RIGHT: True,
        pygame.K_LEFT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False
    }
    walls_collide_list = []
    initial_x = pacman.rect.x
    pacman.move(pressed_key, walls_collide_list)
    assert pacman.direction == (PACMAN_SPEED, 0)
    assert pacman.direction_name == 'right'
    assert pacman.rect.x == initial_x + PACMAN_SPEED


def test_pacman_collision(pacman):
    pressed_key = {
        pygame.K_RIGHT: True,
        pygame.K_LEFT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False
    }
    walls_collide_list = [pygame.Rect(64, 32, 32, 32)]
    pacman.move(pressed_key, walls_collide_list)
    assert pacman.direction == (0, 0)
    assert pacman.rect.x == 32


def test_pacman_teleport(pacman):
    pacman.rect.x = WIDTH
    pressed_key = {
        pygame.K_RIGHT: False,
        pygame.K_LEFT: False,
        pygame.K_UP: False,
        pygame.K_DOWN: False
    }
    walls_collide_list = []
    pacman.move(pressed_key, walls_collide_list)
    assert pacman.rect.x == 0


def test_pacman_animation(pacman):
    initial_frame = pacman.frame_index
    for _ in range(pacman.frame_speed):
        pacman.animate_pacman()
    assert pacman.frame_index == (initial_frame + 1) % len(pacman.frames)
