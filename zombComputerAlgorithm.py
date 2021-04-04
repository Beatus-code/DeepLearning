

class Zomb:
	def ZombFunction(self):
		po, earliesttime, latestTime = 0, -1, -1
		numberZomb = int(input('Enter the Total number of Zombies: ' ))
		BridgeLength = int(input('Enter length of the bridge: '))
		currentPos = [None] * int(numberZomb)
		ZombInit = input('Initial Position of each Zombe:')
		for a in ZombInit.split(' '):
			currentPos[po] = a
			po+=1

		for p in currentPos:
			if p == None:
				print("Something went wrong! ")
				break
			elif int(p) <= 0 or int(p) > BridgeLength:
				print("Wrong position of the bridge")
				return 1

		for w in range(numberZomb):
			etime = max(earliesttime, max(BridgeLength-int(currentPos[w])+1, int(currentPos[w])))
			ltime = max(latestTime, min(BridgeLength-int(currentPos[w]), int(currentPos[w])))
		print('The earliest time  : ', etime)
		print('The latest time  : ', ltime)

#creating Zomb object
Zomb=Zomb()
#calling Zomb Function
Zomb.ZombFunction()
