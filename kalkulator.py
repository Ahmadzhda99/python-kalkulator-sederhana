# import library untuk langsung menyudahi sistem
import sys

# Penjumlahan
def tambah(x,y):
	return x + y

# pengurangan
def kurang(x,y):
	return x - y

# pembagian
def bagi(x,y):
	return x/y

# perkalian
def kali(x,y):
	return x*y

def kalkulator():
	num1 = 0
	num2 = 0
	print "Pilih Operasi:"
	print "1. Penjumlahan"
	print "2. Perkalian"
	print "3. Pengurangan"
	print "4. Pembagian"
	choice = raw_input("Masukkan pilihan: ")
	return cek(choice)

def cek(choice):
	if choice == "1":
		print " =========== Penjumlahan =========== "
		input(choice)
		print num1, " + ", num2, " = ", tambah(num1, num2)
	elif choice == "2":
		print " =========== Perkalian =========== "
		input(choice)
		print num1, " * ", num2, " = ", kali(num1, num2)
	elif choice == "3":
		print " =========== Pengurangan =========== "
		input(choice)
		print num1, " - ", num2, " = ", kurang(num1, num2)
	elif choice == "4":
		print " =========== Pembagian =========== "
		input(choice)
		print num1, " / ", num2, " = ", bagi(num1, num2)
	else:
		print "=== SALAH PILIH OPERASI! ==="
	return kalkulator()

def input(choice):
	num1 = int(raw_input("Masukkan bilangan 1: "))
	num2 = int(raw_input("Masukkan bilangan 2: "))
	return hasil(choice ,num1, num2)

def hasil(choice, num1, num2):
	if choice == "1":
		print num1, " + ", num2, " = ", tambah(num1, num2)
	elif choice == "2":
		print num1, " * ", num2, " = ", kali(num1, num2)
	elif choice == "3":
		print num1, " - ", num2, " = ", kurang(num1, num2)
	else:
		print num1, " / ", num2, " = ", bagi(num1, num2)
	return tanyalagi()

def tanyalagi():
	lagi = raw_input("> Lagi?[y/t]: ")
	if lagi == str("y"):
		kalkulator()
	else:
		sys.exit()

kalkulator()