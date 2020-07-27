# Hacker Rank Problem Solution
# Link to the problem : https://www.hackerrank.com/challenges/30-scope/problem?h_r=email&unlock_token=23f4b2ea5247a99b04521646a2076b03976bae00&utm_campaign=30_days_of_code_continuous&utm_medium=email&utm_source=daily_reminder

class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0
        self.max_num = 0

    def computeDifference(self):
        minn = min(self.__elements)
        maxx = max(self.__elements)
        self.maximumDifference = abs(maxx - minn)
        return self.maximumDifference


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
