import pyglet
from game import resources, load


game_window = pyglet.window.Window(800, 600)


main_batch = pyglet.graphics.Batch()


#   Sprites     #
player_ship = pyglet.sprite.Sprite(img=resources.player_image, x=400, y=300, batch=main_batch)
asteroids = load.asteroids(3, player_ship.position, main_batch)
lives = load.player_lives(3, main_batch)


#       Labels      #
score_label = pyglet.text.Label(text="Score: 0", x=10, y=game_window.height - 20, batch=main_batch)
# level_label = pyglet.text.Label(text="Example Pyglet Game", batch=main_batch,
#                                x=game_window.width//2, y=game_window.height//2, anchor_x='center')


#       Event Handlers      #
@game_window.event
def on_draw():
    game_window.clear()

    main_batch.draw()


if __name__ == '__main__':
    pyglet.app.run()
