# if __name__ == '__main__':
#     decred_to_dollar = 2.68
#     idle_consumption = 0.063
#     mining_consumption = 0.315
#     dollar_to_euro = 0.91
#     decred_per_hour = 0.0916324
#     price_kwh = 0.35
#
#
#
#     euro_mined_per_hour = decred_per_hour * decred_to_dollar * dollar_to_euro
#
#     extra_consumption_when_mining = mining_consumption - idle_consumption
#     euro_spent_per_hour = extra_consumption_when_mining * price_kwh
#
#     earned_per_hour = euro_mined_per_hour - euro_spent_per_hour
#
#     print("Mined : " + str(euro_mined_per_hour))
#     print("Spent : " + str(euro_spent_per_hour))
#     print("Earned : " + str(earned_per_hour))
#
#     hours = 1
#     while hours > 0:
#         hours = int(input('Enter number of hours : '))
#         if hours > 0:
#             earned = hours * earned_per_hour
#             print("Earned in " + str(hours) + "h : " + str(earned) + "!")
#