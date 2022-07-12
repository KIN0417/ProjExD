import pygame as pg
import sys
import random


class Dekoi: #身代わりのクラス
    def __init__(self,image,size,xy,vxy): #image=画像、size=サイズ、xy=幅と高さのタプル、vxy=速度のタプル
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()    # Rect
        self.rct.center = xy
        self.vx, self.vy = vxy

    def blit(self,scr):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr):
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, scr.rct)
            self.vx *= yoko
            self.vy *= tate
            self.blit(scr)

class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode(wh) # Surface
        self.rct = self.sfc.get_rect()            # Rect
        self.bgi_sfc = pg.image.load(image)    # Surface
        self.bgi_rct = self.bgi_sfc.get_rect()    # Rect

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird:
    def __init__(self,image,size,xy):
        self.sfc = pg.image.load(image)    # Surface
        self.sfc = pg.transform.rotozoom(self.sfc, 0, size)  # Surface
        self.rct = self.sfc.get_rect()    # Rect
        self.rct.center = xy

    def blit(self,scr: Screen):
        scr.sfc.blit(self.sfc,self.rct)

    def update(self,scr: Screen):
        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_UP]:
             self.rct.centery -= 2
        if key_states[pg.K_DOWN]:
             self.rct.centery += 2
        if key_states[pg.K_LEFT]:
             self.rct.centerx -= 2
        if key_states[pg.K_RIGHT]:
             self.rct.centerx += 2
        # 練習7
        if check_bound(self.rct, scr.rct) != (1, 1): # 領域外だったら
            if key_states[pg.K_UP]:
                self.rct.centery += 2
            if key_states[pg.K_DOWN]:
                self.rct.centery -= 2
            if key_states[pg.K_LEFT]:
                self.rct.centerx += 2
            if key_states[pg.K_RIGHT]:
                self.rct.centerx -= 2
        self.blit(scr)


class Bomb:
    def __init__(self,color,size,vxy,scr):
        self.sfc = pg.Surface((2*size, 2*size)) # Surface
        self.sfc.set_colorkey((0,0,0)) 
        pg.draw.circle(self.sfc, color, (size, size), size)
        self.rct = self.sfc.get_rect() # Rect
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.vx, self.vy = vxy # 練習6

    def blit(self,scr):
        scr.sfc.blit(self.sfc,self.rct)
    
    def update(self,scr):
            self.rct.move_ip(self.vx, self.vy)
            yoko, tate = check_bound(self.rct, scr.rct)
            self.vx *= yoko
            self.vy *= tate
            self.blit(scr)


def dekoi_move(dekoi,bomb,scr):
    if dekoi.rct.colliderect(bomb.rct): #身代わりと爆弾がぶつかったかどうか
        dekoi.vx*=-1
        dekoi.vy*=-1
        bomb.vx*=-1
        bomb.vy*=-1
        dekoi.blit(scr)
        bomb.blit(scr)



def main():
    clock = pg.time.Clock()
    scr=Screen("逃げろ！こうかとん",(1600,900),"fig/pg_bg.jpg")
    kkt=Bird("fig/6.png",2.0,(900,400))
    bkd=Bomb((255,0,0),20,(+1,+1),scr)
    bkd2=Bomb((0,255,0),20,(+1,+1),scr)
    bkd3=Bomb((0,0,255),20,(+1,+1),scr)
    bkd4=Bomb((255,0,255),20,(+1,+1),scr)
    bkd5=Bomb((255,255,0),20,(+1,+1),scr)
    dekoi=Dekoi("fig/0.png",2.0,(900,400),(+2.5,+2.5))


    while True:
        scr.blit()
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        kkt.update(scr)
        bkd.update(scr)
        bkd2.update(scr)
        bkd3.update(scr)
        bkd4.update(scr)
        bkd5.update(scr)

        key_states = pg.key.get_pressed() # 辞書
        if key_states[pg.K_d]:
            dekoi_move(dekoi,bkd,scr)
            dekoi_move(dekoi,bkd2,scr)
            dekoi_move(dekoi,bkd3,scr)
            dekoi_move(dekoi,bkd4,scr)
            dekoi_move(dekoi,bkd5,scr)
            dekoi.update(scr)



        if kkt.rct.colliderect(bkd.rct) or kkt.rct.colliderect(bkd2.rct) or kkt.rct.colliderect(bkd3.rct) or kkt.rct.colliderect(bkd4.rct) or kkt.rct.colliderect(bkd5.rct):
            return

        pg.display.update()
        clock.tick(1000)

def check_bound(rct, scr_rct):
    '''
    [1] rct: こうかとん or 爆弾のRect
    [2] scr_rct: スクリーンのRect
    '''
    yoko, tate = +1, +1 # 領域内
    if rct.left < scr_rct.left or scr_rct.right  < rct.right : yoko = -1 # 領域外
    if rct.top  < scr_rct.top  or scr_rct.bottom < rct.bottom: tate = -1 # 領域外
    return yoko, tate



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()