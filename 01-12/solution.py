def s1(data):
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
        i = 0
        while find_digit_reversed:
            if reversed_line[i].isdigit():
                digit2 = reversed_line[i]
                find_digit_reversed = False
            else:
                i += 1
        c_sum += int(digit1 + digit2)
    print(f'The final calibration sum is : {c_sum}')


def s2(data):
    # calculation function for the data
    # data : str

    digits_transform = {"one": 1,
                        "two": 2,
                        "three": 3,
                        "four": 4,
                        "five": 5,
                        "six": 6,
                        "seven": 7,
                        "eight": 8,
                        "nine": 9}
    real_digits = digits_transform.keys()
    c_sum = 0
    for line in data:

        # adding first digit
        i = 0
        find_digit = True
        while find_digit:
            if line[i].isdigit():
                digit = line[i]
                location_digit = i
                find_digit = False
            else:
                i += 1
        # finding words
        l_number = []
        l_index = []
        for num in real_digits:
            if num in line:
                l_number.append(num)
                l_index.append(line.lower().find(num.lower()))

        #finding the lowest
            if len(l_index) > 0:
                lowest_index = l_index.index(min(l_index))
                if -1 < l_index[lowest_index] < location_digit:
                    digit1 = str(digits_transform[l_number[lowest_index]])
                else:
                    digit1 = digit
            else:
                digit1 = digit

        # adding second digit
        reversed_line = line[::-1]
        find_digit_reversed = True
        i = 0
        while find_digit_reversed:
            if reversed_line[i].isdigit():
                digit = reversed_line[i]
                location_digit = i
                find_digit_reversed = False
            else:
                i += 1

        # finding words
        l_number = []
        l_index = []
        for num in real_digits:
            if num[::-1] in reversed_line:
                l_number.append(num)
                l_index.append(reversed_line.lower().find(num[::-1].lower()))

        #finding the lowest
            if len(l_index) > 0:
                lowest_index = l_index.index(min(l_index))
                if -1 < l_index[lowest_index] < location_digit:
                    digit2 = str(digits_transform[l_number[lowest_index]])
                else:
                    digit2 = digit
            else:
                digit2 = digit

        c_sum += int(digit1 + digit2)
    print(f'The final calibration sum is : {c_sum}')
