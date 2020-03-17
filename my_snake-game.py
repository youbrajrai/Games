import pygame
import numpy as np 
import random
import time
import math 
def main():
	pygame.init()
	win=pygame.display.set_mode((600,600))
	class snake(object):
		def __init__(self,x,y):
			self.x=x
			self.y=y
			self.body=[]
			self.body=np.array([self.x,self.y])
			self.xdir=0
			self.ydir=0
			self.foodpostion=[(random.randrange(1,59)*10,random.randrange(1,59)*10)]
			self.score=0
			self.length=1
			self.visible=True
			self.left=False
			self.right=False
			self.up=False
			self.down=False
			self.snakelist=[]
			self.snakeLength=1
			self.goingX = False
			self.goingY = False
			self.count=0
		def setdir(self,x,y):
			self.xdir=x
			self.ydir=y									
		def update(self):
				time.sleep(0.001)
				self.body[0]+=self.xdir
				self.body[1]+=self.ydir
				self.body[0]= np.clip(self.body[0],0,(600-15))
				self.body[1]= np.clip(self.body[1],0,(600-15))		
		def action(self):
			if self.left:
				self.setdir(-1,0)
			if self.right:
				self.setdir(1,0)
			if self.up:
				self.setdir(0,-1)
			if self.down:
				self.setdir(0,1)			
		def drawSnake(self,win):
			for xny in self.snakelist:
				pygame.draw.rect(win,(255,255,255),(xny[0],xny[1],9,9))

		def foodEat(self):
			[posx,posy]=self.foodpostion[0]
			dis=math.floor(calculateDist(self.body[0],self.body[1],posx,posy))
			if dis<12:
				self.score+=1
				return True
			else:
				return False   
		
		def drawFood(self,win):
			[x,y]=self.foodpostion[0]
			pygame.draw.circle(win,(0,255,0),(x,y),5)
			self.visible=True		

		
		def death(self):
			if self.body[0] >=600-15 or self.body[0]<=0:
				self.visible=False
				return True
			if self.body[1] >=600-15 or self.body[1]<=0:
				self.visible=False
				return True	


	def calculateDist(x1,y1,x2,y2):
			distance=math.sqrt((y2-y1)**2+(x2-x1)**2)
			return distance	 			
	
	def drawwin():
		pygame.display.set_caption('SnakeGame')
		if snake.visible:	    
		    snake.drawFood(win)
		    snakehead=[]
		    snakehead.append(snake.body[0])
		    snakehead.append(snake.body[1])
		    snake.snakelist.append(snakehead)
		    if len(snake.snakelist)>snake.snakeLength:
		    	del snake.snakelist[0]
		    pygame.draw.rect(win,(255,0,0),(snakehead[0],snakehead[1],9,9))
		    snake.drawSnake(win)
		    for segment in snake.snakelist[:-1]:
		    	if segment == snakehead:
		    		snake.visible=False
		    snake.action()		
		if snake.foodEat():
			snake.foodpostion=[(random.randrange(1,59)*10,random.randrange(1,59)*10)]
			snake.snakeLength+=20
		text=font.render('Score:'+str(snake.score),1,(0,0,200))
		win.blit(text,(450,30))
		snake.update()
		pygame.display.update()
	
	run=True
	font = pygame.font.SysFont('comicsans', 30, True)
	snake=snake(140,90)	
	
	while run:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				run=False
		
		keys=pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			if not snake.goingX:
				snake.left=True
				snake.right=False
				snake.up=False
				snake.down=False
				snake.action()
				snake.goingX=True
				snake.goingY=False
		if keys[pygame.K_RIGHT]:
			if not snake.goingX:
				snake.left=False
				snake.right=True
				snake.up=False
				snake.down=False
				snake.action()
				snake.goingX=True
				snake.goingY=False
		if keys[pygame.K_UP]:
			if not snake.goingY:
				snake.left=False
				snake.right=False
				snake.up=True
				snake.down=False
				snake.action()
				snake.goingX=False
				snake.goingY=True
		if keys[pygame.K_DOWN]:
			if not snake.goingY:
				snake.left=False
				snake.right=False
				snake.up=False
				snake.down=True
				snake.action()
				snake.goingX=False
				snake.goingY=True
		
		if snake.death():
			snake.score=0
			text=font.render("you lose the game",2,(255,255,255))
			win.blit(text,(200,190))
			text1=font.render("Enter 'SPACE' to continue and press 'q' to Quit",5,(255,0,0))
			win.blit(text1,(36,300))
			if keys[pygame.K_SPACE]:
			    snake.visible=True
			    snake.body=np.array([snake.x,snake.y])
			    win.fill((0,0,0))
			    main()
			elif keys[pygame.K_q]:
				run=False    

		drawwin()
		win.fill((0,0,0))
	pygame.quit()

if __name__ == '__main__':
    main()