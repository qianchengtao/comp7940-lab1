def main():
    x = 52633
    factors = []
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    print("Factors of", x, "are:", factors)
if __name__ == '__main__':
    main()


