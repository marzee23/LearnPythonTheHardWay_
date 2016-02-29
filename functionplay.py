def you_may_be_a_procrastinator_if(arg1, arg2, arg3):
	arg1 = input.lower(["Do you have a paper due?"])
	
	
	if arg1 == "yes":
		print("That sucks")
		arg2 = input.lower(["But have you started yet?"])
	else: 
		print("Alright well at least you have nothing serious to be doing.")
	if arg2 == "no":
		print("Wow you're a slacker")
		arg3 = input.lower(["When is it due?"])
	
	if arg3 == "today":
		print("OMG you're so irresponsible! Holy shit!")
	else:
		print("Alright well at least you have time.")

you_may_be_a_procrastinator_if()