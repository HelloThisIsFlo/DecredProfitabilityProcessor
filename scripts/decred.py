class Decred:
    def __init__(self, amount):
        pass

    def to_euro(self):
        return 0


class Processor:
    def __init__(self):
        pass

    def set_decred_per_hour(self, decred_per_hour):
        self.decred_per_hour = decred_per_hour

    def set_dollar_to_euro(self, dollar_to_euro):
        self.dollar_to_euro = dollar_to_euro

    def set_decred_to_dollar(self, decred_to_dollar):
        self.decred_to_dollar = decred_to_dollar

    def set_price_kwh(self, price_kwh):
        self.price_kwh = price_kwh

    def set_consumption(self, consumption):
        self.consumption = consumption

    def earnings_in_euro(self, hours):
        if hours is 0:
            return 0
        self.__compute_earning_rate()
        return hours * self.earning_rate

    def __compute_earning_rate(self):
        try:
            self.__compute_earning_rate_with_all_parameters()
        except AttributeError:
            raise ParameterNotSetException()

    def __compute_earning_rate_with_all_parameters(self):
        self.earning_rate = (self.decred_per_hour * self.decred_to_dollar * self.dollar_to_euro) \
                            - (self.consumption * self.price_kwh)


class RateNotSetException(Exception):
    pass


class ParameterNotSetException(Exception):
    pass
