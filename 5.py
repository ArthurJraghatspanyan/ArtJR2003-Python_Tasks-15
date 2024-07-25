# Իրականացնել ֆունկցիա, որը ստանում է տող և վերադարձնում տողում առաջին հանդիպած մեծատառը։

def first_uppercase(string):
	for i in string:
		if 65 <= ord(i) <= 90:
			print(i)
			break

first_uppercase('heLloWoRld')
