luoti = 13.3
naula = luoti * 32
leiviska = naula * 20

leiviskat = float(input("Anna leiviskät: \n"))
naulat = float(input("Anna naulat: \n"))
luodit = float(input("Anna luodit: \n"))

massa_gramm = luodit * luoti + naulat * naula + leiviskat * leiviska

kilogrammat = massa_gramm // 1000
grammat = massa_gramm % 1000

print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa. ")
