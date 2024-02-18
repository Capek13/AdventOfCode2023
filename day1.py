# adventofcode.com/2023/day1/

# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

# You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

# You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

# As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

# The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

# For example:

# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

# Consider your entire calibration document. What is the sum of all of the calibration values?

# To play, please identify yourself via one of these services:
	
def GetNumbersFromValue(text):
	numbers = []
	for symbol in text:
		if symbol.isdigit():
			numbers.append(symbol)
	return numbers

def GetTwoNumbersFromNumbers(numbers):
	return int(f"{numbers[0]}{numbers[-1]}")

def GetValuesFromFile(path = "day1_input.txt"):
	f = open(path,"r")
	contant = f.read().splitlines()
	f.close()
	return contant

def GetcalibrationValuesSumFromfile(path = "day1_input.txt"):
	inportedValues = GetValuesFromFile(path)
	calibrationNumbers = []
	for value in inportedValues:
		valueNumbers = GetNumbersFromValue(value)
		calibrationValue = GetTwoNumbersFromNumbers(valueNumbers)
		calibrationNumbers.append(calibrationValue)
	return sum(calibrationNumbers)

if __name__ == "__main__":
	print("adventOfCode2023-day1")
	print(GetcalibrationValuesSumFromfile()) 

# adventofcode.com/2023/day1-part2/

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

	inportedValues = GetValuesFromFile("day1_input.txt")
	newValues = GetConvertedNumbersInValue(inportedValues)
	SetValuesToFile(newValues , "day2_output1.txt")
	print(sum(newValues))


