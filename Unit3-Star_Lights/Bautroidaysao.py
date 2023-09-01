def BauTroiDaySao():
    # improve using while loop - break - continue
    # print out * as a star
    # print out " " as a space
    number_of_lines = input("Nhập số dòng: ")
    number_of_lines = int(number_of_lines)
    while number_of_lines > 0:
        print("*" * number_of_lines)
        number_of_lines -= 1
    number_of_lines += 2
    while number_of_lines <= 5:
        print("*" * number_of_lines)
        number_of_lines += 1


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi("SNLTW - HP1 - B3")
    BauTroiDaySao()
