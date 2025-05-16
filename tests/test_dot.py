import pygame
import pytest
from src.dot import Dot


@pytest.fixture
def screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    yield screen
    pygame.quit()


def test_dot_init_power():
    dot = Dot(5, 5, 30, is_power=True)
    assert dot.is_power is True
    assert dot.rate == 10
    assert dot.rect.width == 10
    assert dot.rect.height == 10


def test_dot_init_normal():
    dot = Dot(5, 5, 30)
    assert dot.is_power is False
    assert dot.rate == 5
    assert dot.rect.width == 5
    assert dot.rect.height == 5


def test_dot_draw(screen):
    dot = Dot(5, 5, 30)
    dot.draw(screen)
