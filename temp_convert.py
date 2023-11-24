#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 23, 2023
# This program converts inputted celsius to fahrenheit.


def celsius_to_fahrenheit():
    # introduce program to user
    print("Hello, this program converts temperatures from celsius to fahrenheit.")

    # get user input for celsius
    celsius_str = input("Please enter a temperature in celsius: ")

    # try casting input to an integer
    try:
        celsius_float = float(celsius_str)

        # convert celsius to fahrenheit
        fahrenheit = 9 / 5 * (celsius_float) + 32

        # display celsius to fahrenheit to user
        print("{:.2f}c to fahrenheit is {:.2f}f.".format(celsius_float, fahrenheit))

    # catch invalid inputs from user
    except Exception:
        print("{} is not a number.".format(celsius_str))


def main():
    # call function
    celsius_to_fahrenheit()


if __name__ == "__main__":
    main()
