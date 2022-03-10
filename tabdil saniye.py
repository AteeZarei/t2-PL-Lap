number=int(input("Enter your number is seconds : "))

Hour=number //3600

Minutes=(number % 3600) //60

seconds=(number % 3600) %60

print("the hour is {} ,minutes {} and second {}".format(Hour,Minutes,seconds))