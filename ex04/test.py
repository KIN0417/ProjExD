import pygame as pg
import sys

def main():
    clock=pg.time.Clock()


    pg.display.set_caption("初めてのpygame")
    screen=pg.display.set_mode((800,600))

    tori_img=pg.image.load("fig/6.png")
    tori_rct=tori_img.get_rect()
    tori_rct.center=700,400
    screen.blit(tori_img,tori_rct)

    clock.tick(0.2)


if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()