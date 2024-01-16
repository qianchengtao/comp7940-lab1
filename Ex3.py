def main():
    l = [52633, 8137, 1024, 999]
    for i in l:
        print_factor(i)

def print_factor(x):
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    print("Factors of", x, "are:", factors)
if __name__ == '__main__':
    main()