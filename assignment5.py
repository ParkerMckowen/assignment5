import math as math
import datetime

if __name__ == "__main__":
    date = datetime.date.today()

    firstn = input("Enter your first name: ").lower()

    lastn = input("Enter your last name: ").upper()

    print(f"Hello, {firstn} {lastn}\n\n")

    wholename = firstn + " " + lastn

    print([char for char in lastn])

    wholename_list = wholename.split(" ")
    print(wholename_list[1] + " Walsh College Student")

    print(
        "\"Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible - Francis of Assisi\""
    )

    num1 = 2.15
    num2 = 3.19

    add = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    div = num1 / num2

    print(f"\n{num1} plus {num2} equals {add}")
    print(f"\n{num1} minus {num2} equals {sub}")
    print(f"\n{num1} times {num2} equals {mul}")
    print(f"\n{num1} divided by {num2} equals {div}\n")
    """
    you could just as easily take it to the 1/2 slash 0.5 power, but importing math 
    is less lines of code/makes more sense to me personally
    """

    # Shout out to Carl Lentz, root boy, for this variable name ;)
    my_root = math.sqrt(mul)
    print(f"The square root of {mul} equals {my_root}")

    month = str(date.strftime("%B"))
    day = int(date.strftime("%d"))
    print(f"\n\t\tToday is day {day} of the month {month}")
