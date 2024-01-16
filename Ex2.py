def main():
    x = int(input("请输入数字："))
    print_factor(x)

def print_factor(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    print("Factors of", x, "are:", factors)
if __name__ == '__main__':
    main()


