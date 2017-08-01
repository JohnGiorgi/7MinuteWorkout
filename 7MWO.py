#!/usr/bin/python
from subprocess import call
import time

def main(): 
	# add the movements you would like to do to this list.  
	# default list is all movements from the 7MWO whitepaper
	workouts = ['Jumping jacks', 'Wall sits', 'Push ups', 'Adominal crunch', 
				'Chair step-ups', 'Squats', 'Chair tricep dips', 'Planks', 
				'High knees running in place', 'Lunges', 'Push ups with rotation', 
				'Side planks']

	# introduce the app and prompt user for number of cycles
	call(['say', 'Welcome to 7-minute workout. How many cycles would you like to do?'])
	num_cycles = input('Enter the number of cycles here: ')

	for cycle in range(0, int(num_cycles)):
		# announce cycle starting
		print('Starting cycle {} of {}. Ready in..'.format(cycle + 1, num_cycles))
		call(['say', 'Starting cycle {} of {}. Ready in..'.format(cycle + 1, num_cycles)])
		# 3, 2, 1 countdown before cycle starts
		for cnt_down in range(3, 0, -1):
			print(cnt_down)
			call(['say', '{}'.format(cnt_down)])
		for i, workout in enumerate(workouts):
			# announce movement, announce halfway point, and countdown at 3sec left
			print(workout + ', go!')
			call(['say', '{}, go!'.format(workout)])
			time.sleep(14)
			print('halfway there!')
			call(['say', 'halfway there!'])
			time.sleep(9)
			print('3')
			call(['say', '3'])
			time.sleep(0.8)
			print('2')
			call(['say', '2'])
			time.sleep(0.8)
			print('1')
			call(['say', '1'])
			time.sleep(0.8)
			print('Done.')
			call(['say', 'Done.'])
			time.sleep(0.8)
			# if this is not the last movement, announce the next movement
			try:
				print('Next up, {}.'.format(workouts[i+1]))
				call(['say', 'Next up, {}.'.format(workouts[i+1])])
				time.sleep(4)
				print('In 3...')
				call(['say', 'In 3'])
				time.sleep(0.8)
				print('2...')
				call(['say', '2'])
				time.sleep(0.8)
				print('1...')
				call(['say', '1'])
			except IndexError:
	  			pass
		# if this is not the last cycle, announce next cycle and wait for use conformation 
	  	try:
			print('Cycle {} is done. Press enter to start the next cycle...'.format(cycle + 1))
			call(['say', 'Cycle {} is done. Press enter to start the next cycle...'.format(cycle)])
			input()
		except IndexError:
			pass
	# announce workout completion
	print('Congratulations, workout complete.')
	call(['say', 'Congratulations, workout complete.'])

if __name__ == '__main__':
	main()