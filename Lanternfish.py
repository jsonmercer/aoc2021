lanternFish = [3,4,3,1,2]
#lanternFish = [2,3,2,0,1]
#lanternFish = [1,2,1,6,0,8]
#lanternFish = [0,1,0,5,6,7,8]

def newCycle(i):

	if i == 0:

		return 6

	else:

		return i - 1

def countBirths(fish):

	count = 0

	for item in fish:

		if item == 0:

			count += 1

	return count

def newGeneration(lanternFish,cycles):

	for i in range(cycles):

		newFish = countBirths(lanternFish)
		lanternFish = list(map(lambda x: newCycle(x),lanternFish))

		for j in range(newFish):

			lanternFish.append(8)

	return lanternFish

lanternFish = newGeneration(lanternFish,80)

print(len(lanternFish))

