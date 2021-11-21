def isPalindrom(x):
       return x == x[::-1]

x = input("Masukkan kata/kalimat: ")
if isPalindrom(x):
	print("palindrom")
else:
	print("not palindrom")