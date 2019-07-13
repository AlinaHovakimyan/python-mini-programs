mirg = {"apply":250, "orange":150, "mango":100, "pear":100, "grapes":800, "granata":200, "banana":400}

print("Hello, Please enter name of the fruit that  you want to buy\n");

while input() != 'q' :
	print("Hello, Please enter name of the fruit that  you want to buy\n");
	for i in mirg :
		print(i)

	fruitName = input();
	if fruitName in mirg:
		kg = int(input("how much\n"))
		mirg[fruitName] = mirg[fruitName] - kg
	else:
		print("ERROR: Entered incorrect key\n")

print(mirg)