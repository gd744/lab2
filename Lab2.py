"""
start 
get the numbers of sheets
sheets / 5
cout the result to the user
end 
"""
import math

def calculate(sheet):
    answer = sheet / 5
    rounded = math.ceil(answer)
    print("sheet is : " , sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    return rounded

output = calculate(11)
print("The number of stamps needed is", output)