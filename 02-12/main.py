from solution import s1, s2
def main():
    with open('data.txt') as raw_data:
        cubes_data = raw_data.readlines()
        raw_data.close()

    print('Which solution are you looking for ?')
    print('Solution first part -> Type 1')
    print('Solution second part -> Type 2')
    choice= input()
    if choice == '1':
        s1(cubes_data)
    elif choice == '2':
        s2(cubes_data)

if __name__ == '__main__':
    main()
