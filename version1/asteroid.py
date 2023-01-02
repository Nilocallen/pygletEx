import pyglet
from game import resources, load


game_window = pyglet.window.Window(800, 600)


#   Sprites     #
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300)
asteroids = load.asteroids(3, player_ship.position)


#       Labels      #
score_label = pyglet.text.Label(text="Score: 0", x=10, y=game_window.height - 20)
level_label = pyglet.text.Label(text="Example Pyglet Game",
                                x=game_window.width//2, y=game_window.height//2, anchor_x='center')


#       Event Handlers      #
@game_window.event
def on_draw():
    game_window.clear()

    level_label.draw()
    score_label.draw()

    player_ship.draw()
    for asteroid in asteroids:
        asteroid.draw()


if __name__ == '__main__':
    pyglet.app.run()
