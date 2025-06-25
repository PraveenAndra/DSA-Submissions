class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        fraction = []
        if (numerator >= 0) != (denominator>=0):
            fraction.append("-")
        numerator,denominator = abs(numerator),abs(denominator)
        remainder = numerator % denominator
        fraction.append(str(numerator//denominator))
        if remainder == 0:
            return "".join(fraction)
        lookup = {}
        fraction.append(".")
        while remainder !=0:
            if remainder in lookup:
                fraction.insert(lookup[remainder],"(")
                fraction.append(")")
                break
            lookup[remainder] =  len(fraction)
            remainder *= 10
            divisor = remainder // denominator
            fraction.append(str(divisor))
            remainder %= denominator
        return "".join(fraction)

        