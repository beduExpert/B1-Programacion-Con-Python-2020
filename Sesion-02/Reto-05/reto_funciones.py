def min_com_multiplo (num1, num2):
    divisor = 2
    mcm = 1
    while num1 > 1 or num2 > 1:
        if num1 % divisor == 0:
            num1 = num1 / divisor
            dividido = True
        if num2 % divisor == 0:
            num2 = num2 / divisor
            dividido = True
        if dividido:
            mcm *= divisor
            dividido = False
        else:
            divisor += 1
    return mcm

print(min_com_multiplo(18,91))
