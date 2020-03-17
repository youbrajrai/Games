import pygame
import math
import random
pygame.init()
clock=pygame.time.Clock()
width=500
height=500
win=pygame.display.set_mode((width,height))
class obj(object):
	def __init__(self, x,y):
		self.x=x
		self.y=y
		self.gravity=1.2
		self.velocity=0
		self.lift=-0.012
	def up(self):
		self.velocity+=self.lift	
	def update(self):
		self.velocity+=self.gravity/522
		self.y+=self.velocity
		if self.y>height-7:
			self.y=height-7
			self.velocity=0
		if self.y<0:
			self.y=0
			self.velocity=0	
class pipe(object):
	def __init__(self,top1,top2,top3,bottom1,bottom2,bottom3):
		self.top1=top1
		self.bottom1=bottom1
		self.top2=top2
		self.bottom2=bottom2
		self.top3=top3
		self.bottom3=bottom3
		self.w=50
		self.x1=780
		self.x2=580
		self.x3=380
		self.vel=0.5
		self.visible=True
		self.extra=2
	def pipeDraw(self):
		if self.x1==0-self.w:
			self.x1=780
			self.x2=580
			self.x3=380
			self.top1=self.extra+random.randrange(500/2)
			self.top2=self.extra+random.randrange(500/2)
			self.top3=self.extra+random.randrange(500/2)
			self.bottom2=self.extra+random.randrange(500/2)
			self.bottom1=self.extra+random.randrange(500/2)
			self.bottom3=self.extra+random.randrange(500/2)
		else:	
			pygame.draw.rect(win,(255,255,255),(self.x1,0,self.w,self.top1))
			pygame.draw.rect(win,(255,255,255),(self.x2,0,self.w,self.top2))
			pygame.draw.rect(win,(255,255,255),(self.x3,0,self.w,self.top3))
			pygame.draw.rect(win,(255,255,255),(self.x1,500-self.bottom1,self.w,self.bottom1))
			pygame.draw.rect(win,(255,255,255),(self.x2,500-self.bottom2,self.w,self.bottom2))
			pygame.draw.rect(win,(255,255,255),(self.x3,500-self.bottom3,self.w,self.bottom3))
			self.visible=True
	def update(self):
		self.x1-=self.vel
		self.x2-=self.vel
		self.x3-=self.vel			
def draw():
	xPos=math.floor(bird.x)
	yPos=math.floor(bird.y)
	pygame.draw.circle(win,(255,255,255),(xPos,yPos),7)
	bird.update()
	if pip.visible:
		pip.pipeDraw()
		pip.update()	
	pygame.display.update()		
x=math.floor(width/4)
y=math.floor(height/2) 
bird=obj(x,y)
top1=random.randrange(500/2)
bottom1=random.randrange(500/2)
top2=random.randrange(500/2)
bottom2=random.randrange(500/2)
top3=random.randrange(500/2)
bottom3=random.randrange(500/2)
pip=pipe(top1,top2,top3,bottom1,bottom2,bottom3)

run=True
while run:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					run=False
			keys=pygame.key.get_pressed()
			if keys[pygame.K_SPACE]:
				bird.up()		
			draw()
			win.fill((0,0,0))
			clock.tick(700)	