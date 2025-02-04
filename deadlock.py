import sys
import pygame
import time
from misc import *
clock = pygame.time.Clock()
times = [bignum,bignum,bignum,bignum]
class circle:
	def __init__(self, num, color, speed, direction, start_x, start_y, delta_x, delta_y):
		self.id = num
		self.color = color
		self.spd = speed
		self.dir = direction
		self.X = start_x
		self.Y = start_y
		self.dX = delta_x
		self.dY = delta_y
		self.timestamp = bignum
		self.wait = False
		self.other_people = []
		self.on_bridge = False
		self.acks = []
		self.buffer = []
	def request_access(self):
		self.timestamp = time.time()
		print("{0} is requesting access to the bridge.".format(self.id))
		for p in self.other_people:
			if p.on_bridge == True:
				p.buffer.append(self)
			elif p.timestamp < self.timestamp:
				p.buffer.append(self)
			else:
				self.acks.append(p)
				print("{0} sends ack to {1}".format(p.id,self.id))
		times[self.id] = self.timestamp
		self.wait = True
	def try_enter_bridge(self):
		if set(self.acks) == set(self.other_people):
			print("{0} is crossing the bridge.".format(self.id))
			self.wait = False
			self.on_bridge = True
	def exit_bridge(self):
		print("{0} has exited the bridge.".format(self.id))
		for p in self.buffer:
			print("{0} sends ack to {1}".format(self.id, p.id))
			p.acks.append(self)
		self.timestamp = bignum
		del self.acks[:]
		del self.buffer[:]
		self.on_bridge = False
		times[self.id] = self.timestamp
def deadlock_sol(speed1, speed2):
	screen = pygame.display.set_mode((screen_x,screen_y))
	p1 = circle(0, blue, speed1, 'E', NW[0], NW[1], 1, 1)
	p2 = circle(1, red, speed2, 'E', SW[0], SW[1], 0, -1)
	draw_stage(screen)
	people = [p1, p2]
	p1.other_people = [p2]
	p2.other_people = [p1]
	for person in people:
		pygame.draw.circle(screen, person.color, (person.X, person.Y), 20, 0)
	pygame.display.update()
	while(True):
		clock.tick(30)		#Set update rate to 30 frames per second
		draw_stage(screen)
		for person in people:
			if person.X == NW[0] and person.Y == NW[1]:
				person.dX = person.spd
				person.dY = person.spd
				person.dir = 'E'
			elif person.X == SW[0] and person.Y == SW[1]:
				person.dX = 0
				person.dY = -person.spd
			elif person.X == bridge_W[0] and person.Y == bridge_W[1] and person.dir == 'W':
				person.dX = -person.spd
				person.dY = person.spd
				person.exit_bridge()
			elif person.X == bridge_W[0] and person.Y == bridge_W[1] and person.dir == 'E':
				person.dX = person.spd
				person.dY = 0
				if person.wait == False:
					person.request_access()
				if person.wait == True:
					person.try_enter_bridge()
			elif person.X == bridge_E[0] and person.Y == bridge_E[1] and person.dir == 'W':
				person.dX = -person.spd
				person.dY = 0
				if person.wait == False:
					person.request_access()
				if person.wait == True:
					person.try_enter_bridge()
			elif person.X == bridge_E[0] and person.Y == bridge_E[1] and person.dir == 'E':
				person.dX = person.spd
				person.dY = -person.spd
				person.exit_bridge()
			elif person.X == NE[0] and person.Y == NE[1]:
				person.dX = 0
				person.dY = person.spd
			elif person.X == SE[0] and person.Y == SE[1]:
				person.dX = -person.spd
				person.dY = -person.spd
				person.dir = 'W'
			if(person.wait == False):
				person.X = person.X + person.dX
				person.Y = person.Y + person.dY

			pygame.draw.circle(screen, person.color, (person.X, person.Y), 20, 0)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				clear_vars(people)
				pygame.quit(); 
				return
def draw_stage(screen):
	screen.fill(white)
	pygame.draw.lines(screen, black, True, [NE, SE, bridge_E], 1)
	pygame.draw.lines(screen, black, True, [NW, SW, bridge_W], 1)
	pygame.draw.lines(screen, black, False, [bridge_W, bridge_E], 1)
def clear_vars(people):
	del people[:]
	times = [bignum,bignum,bignum,bignum]