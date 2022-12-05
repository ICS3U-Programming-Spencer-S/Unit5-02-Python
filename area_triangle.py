#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 5, 2022
# A program which calculates Area of a triangle
# Using functions with perimeters


# function to calculate area
def calc_area(base, height):
    area_tri = 1 / 2 * (base * height)
    return area_tri


def main():
    # input
    try:
        inp_base = float(input("Enter a positive base (cm): "))

    # for string inputs
    except Exception:
        print("Base is invalid, use positive numbers only!")

    # to deny inputs that are 0 or less
    else:
        if inp_base <= 0:
            print(
                f"{inp_base} is a invalid base! Base can't be a negative number or 0!"
            )

        else:
            # input
            try:
                inp_height = float(input("Enter a positive height (cm): "))

            # for string inputs
            except Exception:
                print("Height is invalid, use positive numbers only!")

            # To deny inputs that are 0 or less
            else:
                if inp_height <= 0:
                    print(
                        f"{inp_height} is a invalid height! Height can't be a negative number or 0!"
                    )

                # output results
                else:
                    output_area = calc_area(inp_base, inp_height)
                    print(
                        f"The area of a triangle with a base of {inp_base} and a height of {inp_height} is"
                    )
                    print("{:.2f}".format(output_area))


if __name__ == "__main__":
    main()
