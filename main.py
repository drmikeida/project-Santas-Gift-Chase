import pyxel
import random
import time

class App:
  #random circle
  def __init__(self):
      # Initialize the Pyxel window (width, height)
      pyxel.init(160, 120)

      # my_resource.pyxres
      pyxel.load("my_resource.pyxres")
      
      # Set the initial position of the square
      self.x = 75
      self.y = 55
      self.score = 0
      self.die = 0
      self.start = 1

      # Set the initial position and velocity of the sprite
      self.sprite_x = 0
      self.sprite_y = 0
      self.sprite_dx = 2
      self.sprite_dy = 2

      #collectable
      self.collectable_x = 90
      self.collectable_y = 50
      self.collectable_dx = 3
      self.collectable_dy = 3

      # Start the game loop
      pyxel.run(self.update, self.draw)

  def update(self):
      if abs(self.x - self.sprite_x) < 12 and abs(self.y - self.sprite_y) < 12:
        self.die = 1
      
      # Update the square's position based on arrow keys
      if pyxel.btn(pyxel.KEY_W):
          self.y -= 2
      if pyxel.btn(pyxel.KEY_S):
          self.y += 2
      if pyxel.btn(pyxel.KEY_A):
          self.x -= 2
      if pyxel.btn(pyxel.KEY_D):
          self.x += 2

      # update score on touch

      if abs(self.x - self.collectable_x) < 10 and abs(self.y - self.collectable_y) < 10:
          self.score += 1  
          self.collectable_x = random.randint(0, 160)
          self.collectable_y = random.randint(0, 120)
          self.collectable_dx *= -1
          self.collectable_dy *= -1
          self.sprite_dx += 0.2
          self.sprite_dy += 0.2
          
          
      # Increase score if square touches the sprite
      
      # Update the sprite's position
      self.sprite_x += self.sprite_dx
      self.sprite_y += self.sprite_dy

      self.collectable_x += self.collectable_dx
      self.collectable_y += self.collectable_dy

      # Bounce the sprite off the edges of the screen
      if self.sprite_x <= 0 or self.sprite_x >= 160:
          self.sprite_dx *= -1
      if self.sprite_y <= 0 or self.sprite_y >= 120:
          self.sprite_dy *= -1
      #bounce collectabnle
      if self.collectable_x <= 0 or self.collectable_x >= 160:
            self.collectable_dx *= -1
      if self.collectable_y <= 0 or self.collectable_y >= 120:
            self.collectable_dy *= -1
          
  def draw(self):
      #Game over
      #if abs(self.x - self.sprite_x) < 12 and abs(self.y - self.sprite_y) < 12:
        #pyxel.cls(0)
        #pyxel.text(50, 50, "Game Over", 7)
        #time.sleep(2)
        #pyxel.quit()
          
      # Clear the screen with black (color 0)
      pyxel.cls(0)

      pyxel.bltm(0, 0, 0, 0, 0, 160, 120)

      # Draw a square (color 9)
      pyxel.blt(self.x, self.y, 0, 16, 0, 16, 16, 13)

      # Draw the moving sprite (color 11)
      pyxel.blt(self.sprite_x, self.sprite_y, 0, 32, 16, 16, 16,13)
      #pyxel.circ(self.sprite_x, self.sprite_y, 5, 11)

      #Draw collectable
      pyxel.blt(self.collectable_x, self.collectable_y, 0, 16, 16, 16, 16, 13)

      # Display the score
      pyxel.text(5, 5, f"Score: {self.score}", 0)

      # Display a message when score is high
      if self.score >= 5:
          pyxel.text(50, 60, "Ho, Ho, Ho", 8)
      if self.die == 1:
          pyxel.cls(0)
          pyxel.text(65, 60, "Game Over", 7)
      if self.start == 1:
          pyxel.cls(0)
          pyxel.text(50, 40, "Santa's Gift Chase", 8)
          pyxel.text(45, 60, "Press Space to Start", 7)
          pyxel.text(50, 80, "Use WASD to move", 7)
          pyxel.text(0, 100, "Collect the presents and avoid the elf", 7)
          if pyxel.btnp(pyxel.KEY_SPACE):
              self.start = 0
              self.die = 0
          
# Run the game
App()
