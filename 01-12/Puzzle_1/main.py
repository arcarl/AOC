def main():
    # getting data
    with open('data.txt') as raw_data:
        calibration_data = raw_data.readlines()
        raw_data.close()

    # calculation function for the data
    # data : str
    def calibration_sum(data):
        c_sum = 0
        for line in data:

            # adding first digit
            i = 0
            find_digit = True
            while find_digit:
                if line[i].isdigit():
                    digit1 = line[i]
                    find_digit = False
                else:
                    i += 1

            # adding second digit
            reversed_line = line[::-1]
            find_digit_reversed = True
            i=0
            while find_digit_reversed:
                if reversed_line[i].isdigit():
                    digit2 = reversed_line[i]
                    find_digit_reversed = False
                else:
                    i += 1
            c_sum += int (digit1 + digit2)
        print(f'The final calibration sum is : {c_sum}')

    calibration_sum(calibration_data)


if __name__ == '__main__':
    main()
