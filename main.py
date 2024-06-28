def main():

    N = int(input('Enter the number N: '))
    result = []

    """
    ########################################
    Code Your Program here
    ########################################
    """
    V = 1
    for i in range(N +1):
        result.append(V)
        #print(result)
        V = V*2
    #print(result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
