def s1(data):
    r_lim = 12
    g_lim = 13
    b_lim = 14
    games = 0
    for i, line in enumerate(data):

        # assuming that the game is true, and checking that
        possible_game = True

        # getting every set from a game, then every cube per color
        sets = line.split(':')[1].split(';')
        for cubes in sets:
            cubes_per_color = cubes.split(',')
            #print(f'cubes per color {cubes_per_color}')
            # getting every color from every set and checking the condition
            for color_att in cubes_per_color:
                #print(f'color att {color_att}')

                # green
                if 'green' in color_att:
                    digits = ''
                    for char in color_att:
                        if char.isdigit():
                            digits += char
                    g_occ = int(digits)
                    if g_occ > g_lim:
                        possible_game = False
                # red
                elif 'red' in color_att:
                    digits = ''
                    for char in color_att:
                        if char.isdigit():
                            digits += char
                    r_occ = int(digits)
                    if r_occ > r_lim:
                        possible_game = False
                # blue
                elif 'blue' in color_att:
                    digits = ''
                    for char in color_att:
                        if char.isdigit():
                            digits += char
                    b_occ = int(digits)
                    if b_occ > b_lim:
                        possible_game = False
        if possible_game:
            games += i + 1


    print(f'The final calibration sum is : {games}')

def s2(data):
    power = 0
    for i, line in enumerate(data):

        # assuming that the game is true, and checking that
        r_max = 0
        b_max = 0
        g_max = 0

        # getting every set from a game, then every cube per color
        sets = line.split(':')[1].split(';')
        for cubes in sets:
            cubes_per_color = cubes.split(',')
            #print(f'cubes per color {cubes_per_color}')
            # getting every color from every set and adding the maximum
            for color_att in cubes_per_color:
                #print(f'color att {color_att}')
                # green
                if 'green' in color_att:
                    digits = ''
                    for char in color_att:
                        if char.isdigit():
                            digits += char
                    g_occ = int(digits)
                    if g_occ > g_max:
                        g_max = g_occ
                # red
                elif 'red' in color_att:
                    digits = ''
                    for char in color_att:
                        if char.isdigit():
                            digits += char
                    r_occ = int(digits)
                    if r_occ > r_max:
                        r_max = r_occ
                # blue
                elif 'blue' in color_att:
                    digits = ''
                    for char in color_att:
                        if char.isdigit():
                            digits += char
                    b_occ = int(digits)
                    if b_occ > b_max:
                        b_max = b_occ

        power += r_max * g_max * b_max

        # print(f'line {line} , --- rmax {r_max}, bmax {b_max}, gmax {g_max}')
    print(f'The final calibration sum is : {power}')
