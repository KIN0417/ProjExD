import pygame as pg
import sys

def main():
    clock=pg.time.Clock()
    pg.display.set_caption("逃げろ！こうかとん")
    screen_sfc=pg.display.set_mode((1600,900))
    screen_rct=screen_sfc.get_rect()
    bgimg_sfc=pg.image.load("fig/pg_bg.jpg")
    bgimg_rct=bgimg_sfc.get_rect()
    screen_sfc.blit(bgimg_sfc,bgimg_rct)


    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
        pg.display.update()
        clock.tick(1000)



if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()