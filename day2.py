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

def 

def GetConvertedNumbersInValue(values):
	newValues = []
	textNumbers = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
	for singleValue in values:
		updateValue = singleValue
		# compare index of values and change only solo, first or last
		numbersInTextWithId = []
		for number in textNumbers.keys():
			index = updateValue.find(number)
			if index > -1 :
				numbersInTextWithId.append([number , index] )
		#sortByIndex
		for number in textNumbers.keys():
			updateValue = updateValue.replace(number, textNumbers[number])
		newValues.append(updateValue)
	return newValues

def SetValuesToFile(content, path):
	f = open(path,"w")
	for line in content:
		f.write(line + '\n')
	f.close()

# one, two, three, four, five, six, seven, eight, nine


if __name__ == "__main__":
	print("adventOfCode2023-day2")

	inportedValues = day1.GetValuesFromFile("day2_input.txt")
	newValues = GetConvertedNumbersInValue(inportedValues)
	SetValuesToFile(newValues, "day2_input.txt")
	print(day1.GetcalibrationValuesSumFromfile("day2_input.txt")) 