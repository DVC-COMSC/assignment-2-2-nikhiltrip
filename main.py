def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celcius fahrenheit 
    ##################################################
    """
    celcius=int(input("Enter the temperature in Celsius: "))
    fahrenheit=(9*celcius)/5+32
    print("Fahrenheit: {:.2f}".format(fahrenheit))

    """
    ########################################
    # Do not delete the return statement
    ########################################
    """
    return celcius, fahrenheit


if __name__ == '__main__':
    main()
