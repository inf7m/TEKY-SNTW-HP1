def BauTroiDaySao():
    number_of_lines = input("Nhập số dòng: ")
    number_of_lines = int(number_of_lines)
    for i in range(1, number_of_lines + 1):
        print("*" * i)
    for i in range(number_of_lines - 1, 0, -1):
        print("*" * i)


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi("SNLTW - HP1 - B3")
    BauTroiDaySao()
