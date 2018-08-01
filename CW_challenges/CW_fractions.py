class PriceDisplayFraction(object):
    def __init__(self, denominator=16):
        self.denominator = denominator

    def to_display(self, cents):
        cents_int = int(cents)
        cents_flt = int((cents - cents_int) * self.denominator)
        return f'{cents_int/100}/{cents_flt}'

    def to_internal(self, display):
        cents = display.split('/')
        internal = (float(cents[0]) * 100) + (int(cents[1])/self.denominator)
        return internal

