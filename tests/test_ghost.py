import pygame
import pytest
from src.ghost import Ghost


@pytest.fixture(scope='module', autouse=True)
def pygame_setup():
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def ghost(monkeypatch):
    monkeypatch.setattr(
        pygame.image, 'load', lambda path: pygame.Surface((10, 10))
    )
    return Ghost(row=1, col=2, size=32, ghost_name='blinky', level=1)


def test_move_to_start(ghost):
    ghost.rect.x += 100
    ghost.rect.y += 100
    ghost.move_to_start()
    assert ghost.rect.x == ghost.x
    assert ghost.rect.y == ghost.y


def test_is_collide_no_collision(ghost):
    walls = []
    result = ghost.is_collide(0, 0, walls)
    assert not result


def test_is_collide_with_collision(ghost):
    wall = pygame.Rect(ghost.rect.x + 5, ghost.rect.y, 10, 10)
    walls = [wall]
    result = ghost.is_collide(5, 0, walls)
    assert result


def test_animate_power_mode(ghost, monkeypatch):
    called = []

    def fake_load(path):
        called.append(path)
        return pygame.Surface((10, 10))

    monkeypatch.setattr(pygame.image, 'load', fake_load)
    ghost.animate(power_mode=True)
    assert 'assets/edible/ghost.png' in called[0]


def test_animate_normal_mode(ghost, monkeypatch):
    called = []

    def fake_load(path):
        called.append(path)
        return pygame.Surface((10, 10))

    monkeypatch.setattr(pygame.image, 'load', fake_load)
    ghost.animate(power_mode=False)
    assert f'assets/{ghost.ghost_name}/{ghost.move_dir}.png' in called[0]
