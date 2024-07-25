# Իրականացնել ֆունկցիա, որը ստանում է list և վերադարձնում list-ի ամենափոքր (ամենամեծ) էլեմենտը։

ls = [12, 645, 32, 5, 1448, 814]

def max_in_ls(ls):
	maximum = ls[0]
	for i in range(len(ls)):
		if maximum < ls[i]:
			maximum = ls[i]
	return maximum

x = max_in_ls(ls)
print(x)
