# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը: (123 -> 1 + 2 + 3)


def num(n):
	summary = 0
	for i in str(n):
		summary += int(i)
	return summary


x = num(543)
print(x)
