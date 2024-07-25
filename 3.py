# Գրել ֆունկցիա, որը ստանում է list և տպում է list-ի էլեմենտները էկրանին։

def foo(ls):
	for i in ls:
		print(i, end=' ')

ls = [1, 2, 3]
foo(ls)
