# My Timer

print("This Timer Was Made By Me, ByMetehan(As Metehan Bayhan)")


answer = input("Would You Like To Start? y/n?")



if answer == "y":
Sec = 0
Min = 0	
  timerstart = "start"
	while timerstart == "start":
		Sec + 1
		print(str(Min) + " Mins " + str(Sec) + " Secs " + "Have Passed")

		sleep(1)

		if Sec == 60:
			Min + 1
         print(str(Min) + " Mins " + str(Sec) + " Secs " + "Have Passed")




else:
 if answer == "n":
 	exit()
 else:
 print("You should write y or n.Close The Program To Reuse.You Typed " + answer)
