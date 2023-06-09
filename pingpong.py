from pygame import*
class GameSprite(sprite.Sprite):
#class constructor
  def __init__(self, player_image, player_x, player_y, windows_with, windows_height, player_speed):
      #call for the class (Sprite) constructor:
      sprite.Sprite.__init__(self)
      #every sprite must store the image property
      self.image = transform.scale(image.load(player_image), (windows_with, windows_height))
      self.speed = player_speed
      #every sprite must have the rect property that represents the rectangle it is fitted in
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
#method drawing the character on the window
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#main player class
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < windows_height - 80:
           self.rect.y += self.speed
    def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < windows_height - 80:
           self.rect.y += self.speed

platforml = Player("racket.png", 30, 200, 4, 50, 250)
platformr = Player("racket.png", 520, 200, 4, 50, 250)
ball = GameSprite("tennis_ball.png", 200, 200, 4, 50, 50)

back = (200,255,255)
windows_with = 600
windows_height = 500
mw = display.set_mode((windows_with,windows_height))
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
        if finish != True

        mw.fill(back)
        platforml.reset()
        platformr.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)