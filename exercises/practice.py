def lcmAndGcd(a, b):
    output = []

    def GCD(a, b):
        if a > b:
            x = a
        else:
            x = b
        gcd = 0
        for i in range(1, x + 1):
            if a % i == 0 and b % i == 0:
                gcd = i
        return gcd

    def LCM(a, b, gcd):
        return abs(a * b) // gcd

    gcd = GCD(a=a, b=b)
    lcm = LCM(a=a, b=b, gcd=gcd)

    output.append(lcm)
    output.append(gcd)

    return output


print(lcmAndGcd(5, 10))
