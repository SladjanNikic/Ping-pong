from pygame import*




back = (200,255,255)
windows_with = 600
windows_height = 500
mw = display.set_mode((windows_with,windows_height))
mw.fill(back)
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    


    display.update()
    clock.tick(FPS)