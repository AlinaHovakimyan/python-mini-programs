import datetime
import logging

mirg = {"apply":250, "orange":150, "mango":100, "pear":100, "grapes":800, "granata":200, "banana":400}

log = {}
time = {}
for i in mirg :
	log[i] = []

print("Hello, Please enter name of the fruit that  you want to buy(q to quit)\n");
for i in mirg :
        print(i)
fruitName = input()

while fruitName != 'q' :
    if fruitName in mirg:
        kg = int(input("how much\n"))
        if(kg < mirg[fruitName]):
            mirg[fruitName] = mirg[fruitName] - kg
            log[fruitName].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif(kg == mirg[fruitName]):
            log[fruitName].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            mirg.pop(fruitName)
        else:
            print("We havn't enought kg of " + fruitName)
    else:
        print("ERROR: Entered incorrect key\n")
    print("Please enter name of the fruit that  you want to buy(q to quit)\n");
    for i in mirg :
        print(i)
    fruitName = input()
logging.basicConfig(filename='logFile.log', filemode = 'w', level = logging.INFO)
for i in log:
    if len(log[i]):
        logging.info("%s %s", i, log[i])