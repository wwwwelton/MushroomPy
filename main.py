import arcade
import time

SPRITE_SCALING = 2
SPRITE_SIZE = 30

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "PyLong"

MOVEMENT_SPEED = 10

class Player(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 50:
            self.left = 100
        elif self.right > SCREEN_WIDTH - 50:
            self.right = SCREEN_WIDTH - 100
        if self.bottom < 50:
            self.bottom = 100
        elif self.top > SCREEN_HEIGHT - 50:
            self.top = SCREEN_HEIGHT - 100

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player_list = None
        self.terrain_list = None
        self.wall_list = None
        self.player_sprite = None
        self.terrain_sprite = None
        self.wall_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.terrain_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.player_sprite = Player("Hit.png", SPRITE_SCALING)
        self.player_sprite.center_x = 100
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)
        #SNOW
        for i in range(SPRITE_SIZE, SCREEN_HEIGHT, 50):
          for j in range(SPRITE_SIZE, SCREEN_WIDTH, 50):
            terrain_sprite = arcade.Sprite("terrain.jpg", SPRITE_SCALING)
            terrain_sprite.center_y = i
            terrain_sprite.center_x = j
            self.terrain_list.append(terrain_sprite)
        #BOTTOM
        for i in range(SPRITE_SIZE, SCREEN_WIDTH, 50):
          terrain_sprite = arcade.Sprite("wall.jpg", SPRITE_SCALING)
          terrain_sprite.center_y = 25
          terrain_sprite.center_x = i
          self.terrain_list.append(terrain_sprite)
        #LEFT
        for i in range(SPRITE_SIZE, SCREEN_HEIGHT, 50):
          terrain_sprite = arcade.Sprite("wall.jpg", SPRITE_SCALING)
          terrain_sprite.center_y = i
          terrain_sprite.center_x = 25
          self.terrain_list.append(terrain_sprite)
        #RIGHT
        for i in range(SCREEN_HEIGHT - 25, 0, -50):
          terrain_sprite = arcade.Sprite("wall.jpg", SPRITE_SCALING)
          terrain_sprite.center_y = i
          terrain_sprite.center_x = SCREEN_WIDTH - 25
          self.terrain_list.append(terrain_sprite)
        #TOP
        for i in range(25, SCREEN_WIDTH, 50):
          terrain_sprite = arcade.Sprite("wall.jpg", SPRITE_SCALING)
          terrain_sprite.center_y = SCREEN_HEIGHT - 25
          terrain_sprite.center_x = i
          self.terrain_list.append(terrain_sprite)

    def on_draw(self):
        arcade.start_render()
        self.terrain_list.draw()
        self.player_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main function """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()