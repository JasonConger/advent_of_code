from pathlib import Path
import re

def part1():
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        calibrationValues = 0
        lines = f.readlines()
        for line in lines:
            firstDigit, lastDigit = None, None
            digits = re.findall(r'\d', line)
            
            if not digits:
                raise Exception("Um, thish shouldn't happen. Check your input text.")
            
            firstDigit = digits[0]

            if len(digits) > 1:
                lastDigit = digits[len(digits) - 1]
            else:
                lastDigit = firstDigit

            calibrationValue = firstDigit + lastDigit
            calibrationValues = calibrationValues + int(calibrationValue)

    print(calibrationValues)

def toNumber(n):
    try:
        num = int(n)
        return n
    except:
        numDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        return numDict[n]


def part2():
    p = Path(__file__).with_name('input.txt')
    with p.open('r') as f:
        calibrationValues = 0
        lines = f.readlines()
        for line in lines:
            firstDigit, lastDigit = None, None
            digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
            
            if not digits:
                raise Exception("Um, thish shouldn't happen. Check your input text.")
            
            firstDigit = toNumber(digits[0])

            if len(digits) > 1:
                lastDigit = toNumber(digits[len(digits) - 1])
            else:
                lastDigit = firstDigit

            calibrationValue = firstDigit + lastDigit
            calibrationValues = calibrationValues + int(calibrationValue)

    print(calibrationValues)

if __name__ == "__main__":
    part1()
    part2()