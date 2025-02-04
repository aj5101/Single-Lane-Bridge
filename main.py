import sys
import pygame
import deadlock
speeds = [1,1,1,1]	#Holder list for speeds of the 4 people
pygame.init()
clock = pygame.time.Clock()
def main():
	loop = True
	cont = 0
	while(loop == True):
		print("Please select which alogirthm you would like to run.")
		print("1. One-at-a-time bridge crossing.")
		print("2. Exit.")
		mode = input("Enter option 1 or 2: ")
		while(True):
			try:
				mode = int(mode)
				if mode < 1 or mode > 2:
					raise ValueError()
				break
			except ValueError:
				mode = input("Please enter valid input: ")
		if(mode == 1):
			get_speeds()
			deadlock.deadlock_sol(speeds[0],speeds[1])
		elif(mode == 2):
			sys.exit()
		print("Would you like to run again?")
		cont = input("1 = Yes, 0 = No: ")
		while(True):
			try:
				cont = int(cont)
				if cont != 0 and cont != 1:
					raise ValueError()
				break
			except ValueError:
				cont = input("Please enter valid input: ")
		if(cont == 1):
			loop = True
		elif(cont == 0):
			loop = False
			print("Exiting.")
def get_speeds():
	print("Please enter speeds for the 2 people.")
	print("1 = Slow, 2 = Medium, 3 = Fast, 4 = Very Fast.")
	for i in range(2):
		s = input("{0}: ".format(i))
		while(True):
			try:
				s = int(s)
				if s < 1 or s > 4:
					raise ValueError()
				break
			except ValueError:
				s = input("Please enter valid input for speed {0}: ".format(i))
		if(s == 3):
			speeds[i] = 5
		elif(s == 4):
			speeds[i] = 10
		else:
			speeds[i] = s
if __name__ == '__main__':
	main()


