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


def problem_13():
    total_hr_work = int(input("Enter the number of hrs worked : "))
    hrly_pay = int(input("Enter hourly pay : "))
    regularpay = total_hr_work + hrly_pay
    if total_hr_work < 40:
        print("")
    else:
        extra_hrs_pay = (total_hr_work + hrly_pay) * 1.5
        print("Regular pay of employee : ", regularpay)
        print("Extra hour pay with 50% : ", extra_hrs_pay)




def problem_14():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    if num1>num2:
        print(f"{num1} first number is greater than {num2} second number.")
    else:
        print(f"{num2} second number is greater than {num1} first number.")

def problem_15():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    num3 = int(input("Enter third number : "))
    if num1>num2>num3:
        print(f"{num1} first number is greater.")
    elif num1<num2>num3:
        print(f"{num2} second number is greater.")
    else:
        print(f"{num3} third number is greater.")


def problem_16():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    num3 = int(input("Enter third number : "))
    num4 = int(input("Enter fourth number : "))
    if num1 > num2 > num3 > num4:
        print(f"{num1} first number is greater.")
    elif num1 < num2 > num3 > num4:
        print(f"{num2} second number is greater.")
    elif num1 < num2 < num3 > num4:
        print(f"{num3} third number is greater.")
    else:
        print(f"{num4} fourth number is greater.")

def problem_17():
    mark = int(input("Enter marks of student : "))
    if mark>=90 and mark<=100:
        print("Student got the A grade.")
    elif mark>=80 and mark<=89:
        print("Student got the B grade.")
    elif mark>=70 and mark<=79:
        print("Student got the C grade.")
    elif mark>=60 and mark<=69:
        print("Student got the D grade.")
    else:
        print("Student got the F grade.")


def problem_18():
    n = int(input("Enter your no. : "))
    if n % 2 == 0:
        print("Number is Even.")
    else:
        print("Number is Odd.")


# def problem_19():
    # Get user input for the times in 24-hour format
    # time1 = input("Enter the first time : ")
    # time2 = input("Enter the second time : ")
    #
    # # Parse hours and minutes from the user input
    # hours1, minutes1 = map(int, time1.split(':'))
    # hours2, minutes2 = map(int, time2.split(':'))
    #
    # # Convert times to minutes
    # total_minutes1 = hours1 * 60 + minutes1
    # total_minutes2 = hours2 * 60 + minutes2
    #
    # # Calculate the time difference in minutes
    # time_diff_minutes = total_minutes2 - total_minutes1
    #
    # # Convert the time difference back to hours and minutes
    # hours_diff = time_diff_minutes // 60
    # minutes_diff = time_diff_minutes % 60
    #
    # # Display the result
    # print(f"The time difference is {hours_diff} hours and {minutes_diff} minutes.")

def problem_20():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))
    num3 = int(input("Enter third number : "))
    if num1 == num2 == num3:
        print("All are same")
    elif num1 == num2 or num2 == num3 or num1 == num3:
        print("Any two are same.")
    else:
        print("No same.")


def problem_21():
    m = [int(input("Enter numbers : "))
                    for i in range(10)]
    x = sum(m)
    print(x)

def problem_22():
    n = int(input("Enter the n number : "))
    m = [int(input("Enter numbers : "))
         for i in range(n)]
    x = sum(m)
    print(x)

def problem_23():
    n = int(input("Enter the n number : "))
    m = [int(input("Enter numbers for total : "))
         for i in range(n)]
    x = sum(m)
    y= x/n
    print(f"Average = {y}")


def problem_24():
    n = int(input("Enter a positive integer : "))
    print("Positive integers from 1 to", n, "are:")
    for i in range(1, n + 1):
        print(i)


def problem_25():
    import math
    n = int(input("Enter a positive number : "))
    print(math.factorial(n))


def problem_26():
    a = int(input("Enter 1st number : "))
    n = int(input("Enter 2nd number : "))
    x = a ** n
    print(f"Exponent is {x}")

def problem_27():
    m = [int(input("Enter numbers for : "))
         for i in range(3)]
    print("max number is : " , max(m))

def problem_28():
    n = int(input("Enter the n number : "))
    m = [int(input("Enter number for : "))
         for i in range(n)]
    print("max number is : ", max(m))


def problem_29():
    n = int(input("Enter the n number : "))
    m = [int(input("Enter number for : "))
         for i in range(n)]
    print("max number is : ", max(m))
    print("min number is : ", min(m))

def problem_30():
    n = int(input("Enter the number of elements: "))
    m = [int(input("Enter list elements : "))
         for i in range(n)]
    x = []
    y = []
    for num in m:
        if num > 0:
            x.append(num)
        else:
            y.append(num)
    print(f"The number of positive numbers is: {len(x)}")
    print(f"The number of negative numbers is: {len(y)}")


def problem_31():
    n = int(input("Enter the positive number : "))
    temp = []
    for i in range(1, n + 1):
        if n % i == 0:
            temp.append(i)
    print(f"The divisors of {n} are: {temp}")


def problem_32():
    n = int(input("Enter the number : "))
    temp = []
    for i in range(1, n + 1):
        if n % i == 0:
            temp.append(i)
    m = sum(temp) - 1
    print("Divisors:", temp)
    print("Sum of Divisors:", m)
    if m == n :
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")

def problem_33():
    n = int(input("Enter a number : "))
    if n > 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print(f"{n} is not a prime number.")
                break
        else:
            print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")


def problem_34():
    while True:
        try:
            n = int(input("Enter a number : "))
            if n <= 0:
                raise ValueError("You enter an invalid number.")
        except ValueError:
            print("Enter a valid input number.")
        else:
            break
    print(f"You enter a valid number {n}.")


def problem_36():
    def num(number):
        if number > 0:
            return -number
        elif number < 0:
            return number
        else:
            return 0

    n = int(input("Enter a number : "))
    result = num(n)
    print(f"The negative of {num} is {result}")


def problem_37():
    n = int(input("Enter any number : "))
    m = abs(n)
    print(f"The absolute of {n} is {m}.")

def problem_38():
    m = int(input("Enter first number : "))
    n = int(input("Enter second number : "))
    if m % 2 == 0 and n % 2 == 0:
        print("Both numbers are even.")
    elif m % 2 == 0 and n % 2 != 0:
        print(f"{m} is even and {n} is odd.")
    elif m % 2 != 0 and n % 2 == 0:
        print(f"{m} is odd and {n} is even.")
    else:
        print("Both numbers are odd.")


def problem_39():
    a = [int(input("Enter your numbers : ")) for i in range(3)]
    temp = []
    for num in a:
        if num % 2 != 0:
            temp.append(a)
    print(f"The number of odds are {len(temp)}")



def problem_40():
    a = int(input("Enter your numbers : "))
    b = int(input("Enter your numbers : "))
    c = int(input("Enter your numbers : "))
    largest_1 = max(a,b,c)
    temp = [a,b,c]
    temp.remove(largest_1)
    largest_2 = max(temp)
    print(f"The largest numbers are {largest_1} & {largest_2}.")

def problem_41():
    n = int(input("Enter any number : "))
    if n % 2 == 0 and n>10:
        print(f"{n} is a 2 digits positive integer.")
    else:
        print(f"{n} is not a postive integer invalid value.")

def problem_42():
    n = int(input("Enter 1st value : "))
    m = int(input("Enter 2nd value : "))
    l = abs(n-m)
    print(f"The absolute difference of {n} and {m} is {l}.")


def problem_44():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(f"Before Interchanging : {a} and {b}")

    temp = a
    a = b
    b = temp
    print(f"After Interchanging : {a} and {b}")


def problem_45():
    a = int(input("Enter first number : "))
    b = int(input("Enter second number : "))
    print(f"Before Interchanging : {a} and {b}")

    a = a+b
    b = a-b
    b = a-b
    print(f"After Interchanging : {a} and {b}")



def problem_46():
    micro_sec = int(input("Enter time in micro seconds : "))
    week = micro_sec // (7 * 24 * 60 * 60 * 1_000_000)
    day = micro_sec // (24 * 60 * 60 * 1_000_000)
    hour = micro_sec // (60 * 60 * 1_000_000)
    mint = micro_sec // (60 * 60 * 1_000_000)
    sec = micro_sec // ( 60 * 1_000_000)
    print(f"{micro_sec} convert to {week}.")
    print(f"{micro_sec} convert to {day}.")
    print(f"{micro_sec} convert to {hour}.")
    print(f"{micro_sec} convert to {mint}.")
    print(f"{micro_sec} convert to {sec}.")


if __name__ == "__main__":
#add function name to execute it
    problem_46()