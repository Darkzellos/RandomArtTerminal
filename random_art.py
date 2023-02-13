import random
def random_art():
	lenlist = 14
	result = []
	symbols = [" ", " ", " ",  " ", " ", "o","=","+","X",".","@"]
	end_list = len(symbols) - 1
	for i in range(lenlist):
		random_symbol = random.choice(symbols)
		result.append(random_symbol)
	result[0] = "|"
	result.append("|")
	result = "".join(result)
	print(result)
	pass
print("+--" +	"[ID" + str(random.randint(1000, 44444)) + "]" + "--+")
for i in range(9):
	random_art()
print("+---" +	"[KEY" + str(random.randint(10, 99)) + "]" + "---+")