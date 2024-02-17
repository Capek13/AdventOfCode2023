# adventofcode.com/2023/day2/

# Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

# Equipped with this new information, you now need to find the real first and last digit on each line. For example:

# two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

# What is the sum of all of the calibration values?

import day1

def GetSortedNumbersById(numbers, indexs):
	sortedIndexs = sorted(indexs)
	sortedNubers = []
	for i in sortedIndexs:
		sortedNubers.append(numbers[indexs.index(i)])
	return sortedNubers, sortedIndexs

def GetAndRemoveNumbersSharingAlphabets(numbers, indexs):
	removeThisIndexs = []
	for i in range(len(numbers)-1):
		if (indexs[i] + len(numbers[i])) > indexs[i+1]:
			del numbers[i+1]
			del indexs[i+1]
			return GetAndRemoveNumbersSharingAlphabets(numbers, indexs)
	return numbers, indexs

def GetConvertedNumbersInValue(values):
	newValues = []
	textNumbers = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
	for singleValue in values:
		findedNumbers = []
		findedNumbersIndexs = []
		for number in (list(textNumbers.keys()) + ['1','2','3','4','5','6','7','8','9']):
			index = 0
			while singleValue.find(number, index) > -1:
				index = singleValue.find(number, index)
				if index > -1 :
					findedNumbers.append(number)
					findedNumbersIndexs.append(index)
					index += len(number)
		sortedNubers, sortedIndexs = GetSortedNumbersById(findedNumbers, findedNumbersIndexs)
		# sortedNubers, sortedIndexs = GetAndRemoveNumbersSharingAlphabets(sortedNubers, sortedIndexs)
		# print(sortedNubers,' ; ',singleValue)

		if len(sortedIndexs)<= 2:
			endOfFirstNumber = sortedIndexs[0] + len(sortedNubers[0])
			if sortedIndexs[-1] < endOfFirstNumber:
				sortedNubers[-1]=sortedNubers[0]

		newValue = sortedNubers[0] + sortedNubers[-1]
		for number in textNumbers.keys():
			newValue = newValue.replace(number, textNumbers[number])
		newValues.append(int(newValue))
	return newValues

def SetValuesToFile(content, path):
	f = open(path,"w")
	for line in content:
		f.write(f"{line}" + '\n')
	f.close()

if __name__ == "__main__":
	print("adventOfCode2023-day1-part2")

	inportedValues = day1.GetValuesFromFile("day2_input.txt")
	newValues = GetConvertedNumbersInValue(inportedValues)
	SetValuesToFile(newValues , "day2_output1.txt")
	# print(day1.GetcalibrationValuesSumFromfile("day2_input.txt")) 
	print(sum(newValues))

	