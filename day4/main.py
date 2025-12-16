comp_num = 100
user_num = 0

while comp_num != user_num:
	user_num = int(input('enter ur number: '))
	if user_num > comp_num:
		print('too high!')
	elif user_num < comp_num:
		print('too low!')
	elif user_num == comp_num:
		print('ur right nigga')
	else:
		break
