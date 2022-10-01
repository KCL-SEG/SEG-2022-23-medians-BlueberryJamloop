"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
count = 0
numbers = []

def median_func(numbers, count):
    if count % 2 != 0:
        return(numbers[(count//2)])
    else:
        median = (numbers[count//2]+numbers[(count//2)-1])/2
        return(median)

        
while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        for value in input().split(","):
            numbers.append(float(value))
            count = count + 1
        finalMedian = median_func(numbers, count)
    except ValueError:
        print("Some input could not be converted to a number!")
    except EOFError:
        print("End of line")
    finally:
        print(numbers)
        print(count)
        print(finalMedian)
        break
