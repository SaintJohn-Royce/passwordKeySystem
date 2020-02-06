
correctPassword = 'a123456'

inputValue = input('please enter the password: ')

inputValue = str(inputValue)

authorizationAttempts = 2

if inputValue == correctPassword:

	print('successful entry')

else:

	while authorizationAttempts >= 1:

		print('unsuccessful entry, you still have', authorizationAttempts, 'attempt(s) left')

		new_inputValue = input('try again: ')

		new_inputValue = str(new_inputValue)

		if new_inputValue == correctPassword:

			print('successful entry')

			break

		else:

			authorizationAttempts = authorizationAttempts - 1

			if authorizationAttempts == 0:

				print('piss off')

				break


