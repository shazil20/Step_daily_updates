def problem_01():
# print("problem 1")
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))

    quotient = a / b
    print("Quotient:", quotient)


def problem_02():
# print("problem 02")
    num1 = int(input("Enter 1st number : "))
    num2 = int(input("Enter 2nd number : "))
    num3 = int(input("Enter 3rd number : "))
    num4 = int(input("Enter 4th number : "))

    sum = num1+num2+num3+num4
    print("Sum is : ", sum)


def problem_03():
    std1 = int(input("Enter 1st student's marks : "))
    std2 = int(input("Enter 2nd student's marks : "))
    std3 = int(input("Enter 3rd student's marks : "))
    std4 = int(input("Enter 4th student's marks : "))
    std5 = int(input("Enter 5th student's marks : "))
    sum = std1+std2+std3+std4+std5
    average = sum/5
    print("Sum is = ",sum,)
    print("average is = ", average)

def problem_04():
    std1 = int(input("Enter 1st student's marks : "))
    std2 = int(input("Enter 2nd student's marks : "))
    std3 = int(input("Enter 3rd student's marks : "))
    std4 = int(input("Enter 4th student's marks : "))
    sum = std1 + std2 + std3 + std4
    percentage = sum/ 400 * 100
    print("Percentage of TM of 4 students is = ",percentage)

def problem_05():
    num1 = int(input("Enter any random number : "))
    if num1 < 80:
        print("Good")
    else:
        print("Try again")

def problem_06():
    a = int(input("Enter any number : "))
    b = int(input("Enter 2nd number : "))
    if a%b == 0:
        print("Divisible")
    else:
        print("not Divisuble")
def problem_07():
    user_numbers = [int(input("Enter numbers of user: "))
                    for i in range(10)]
    x = sum(user_numbers)
    if x % 2 != 0:
        print(f"Sum of ODD number is : {x}")
    else:
        print("Sum is even which is not the required output.")

def problem_08():
    n = int(input("Enter number of user : "))
    user_numbers = [int(input("Enter numbers : "))
                    for i in range(n)]
    x = sum(user_numbers)
    if x % 2 == 0:
        print(f"Sum of even number is : {x}")
    else:
        print("Sum is odd which is not the required output.")

def problem_09():
    a = 0
    b = 1
    n = int(input("Enter numbers for fibonacci series selection : "))

    for i in range(n):
        print(a)
        a, b = b, a + b

def problem_10():
    temp_f = int(input("Enter temperature in fahrenheit : "))
    celsius = (temp_f-32) * (5/9)
    print(f"Temperature in calsius is : {celsius}")

def problem_11():
    rate_per_hour = int(input("Enter the rate per hour salary : "))
    given_hour = int(input("Enter the hours employee work : "))
    pay = rate_per_hour*given_hour
    print("pay is : ",pay)

def problem_12():
    marks = int(input("Enter the marks : "))
    if marks >= 50:
        print("Pass")
    else:
        print("Fail")



if __name__ == "__main__":
#add function name to execute it
    problem_12()