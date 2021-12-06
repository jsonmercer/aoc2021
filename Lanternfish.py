lanternFish = [3,4,3,1,2]

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

