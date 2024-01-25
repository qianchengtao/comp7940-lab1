def main():
    l = [52633, 8137, 1024, 999]
    factors = []
    for i in l:
        list = print_factor(i)
        factors.extend(list)
    newFactors = remove_duplicates(factors)
    print(newFactors)


def print_factor(x):
    factor = []
    for i in range(1, x + 1):
        if x % i == 0:
            factor.append(i)
    return factor

def remove_duplicates(list):
    res_list = []
    for one in list:
        if not one in res_list:
            res_list.append(one)
    return res_list

if __name__ == '__main__':
    main()