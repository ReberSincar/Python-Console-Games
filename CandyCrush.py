# >>>>RENK KODLARI<<<<

# Mavi ---->1
# Kirmizi ---->2
# Turuncu ---->3
# Yesil ---->4
# Mor ---->5

# >>>>HAMLE PUANLARI<<<<

# 3'lu >>> 1 puan
# 4'li >>> 2 puan
# 5'li >>> 3 puan

# >>>>LEVEL PUANLARI<<<<

# level 1 50 puan -->  10x10
# level 2 80 puan -->  10x10
# level 3 100 puan -->  10x10
# level 4 150 puan -->  15x15
# level 5 300 puan -->  15x15
# level 6 500 puan -->  15x15
# level 7 1000 puan --> 15x15
# level 8 2000 puan --> 30x30
# level 9 3000 puan --> 30x30
# level 10 5000 puan -->30x30
# RENKLER SIRALI GELECEK
# LEVELLERI KULLANICI SECECEK

import random


class CandyCrush():
	def __init__(self):
		self.level = 0
		self.LevelSec()
		self.levelPuan = self.level*50
		self.oyuncuPuan=0
		self.matris=[]
		self.MatrisOlustur()
		self.MatrisRandom()
		self.MatrisYazdir()
		self.Hamle()

	def LevelSec(self):
		while True:
			try:
				self.level = int(input(
					"""
					Level secin\n
					Level 1 --> [1]
				    Level 2 --> [2]
				    Level 3 --> [3]
				    Level 4 --> [4]
				    Level 5 --> [5]
				    Level 6 --> [6]
				    Level 7 --> [7]
				    Level 8 --> [8]
				    Level 9 --> [9]
				    Level 10 -> [10]\n
				    Secim: """))
				if 11<self.level<0:
					print "Yanlis bir deger girdiniz 1-10 araliginda bir deger girmelisiniz."
				else:
					break
			except:
				print "Yanlis bir deger girdiniz.Tekrar deneyin."

	def MatrisOlustur(self):
		if self.level in range(1, 4):
			self.matris = [[0] * 10 for i in range(10)]
			self.boyut = 10
		elif self.level in range(4, 8):
			self.matris = [[0] * 15 for i in range(15)]
			self.boyut = 15
		else:
			self.matris = [[0] * 30 for i in range(30)]
			self.boyut = 30

	def MatrisRandom(self):
		for i in range(self.boyut):
			for j in range(self.boyut):
				self.matris[i][j] = random.randint(1, 5)

	def MatrisYazdir(self):
		for i in range(self.boyut):
			for j in range(self.boyut):
				print str(self.matris[i][j]) + "\t",
			print "\n"
		print "Puaniniz : ", self.oyuncuPuan


	def KontrolDikey(self):
		sayac=0
		for j in range(self.boyut):
			for i in range(self.boyut-1):
				if self.matris[i][j]==self.matris[i+1][j]:
					sayac += 1
				else:
					if sayac==4:
						self.oyuncuPuan+=3
						for k in range(5):
							self.matris[i-k][j]=0
					elif sayac==3:
						self.oyuncu_puan += 2
						for k in range(4):
							self.matris[i - k][j] = 0
					elif sayac==2:
						self.oyuncu_puan += 1
						for k in range(3):
							self.matris[i - k][j] = 0
					sayac=0

	def KontrolYatay(self):
		sayac = 0
		for i in range(self.boyut):
			for j in range(self.boyut-1):
				if self.matris[i][j] == self.matris[i][j+1]:
					sayac = sayac + 1
				else:
					if sayac == 4:
						self.oyuncuPuan += 3
						for k in range(5):
							self.matris[i][j - k] = 0
					elif sayac == 3:
						self.oyuncuPuan += 2
						for k in range(4):
							self.matris[i][j - k] = 0
					elif sayac == 2:
						self.oyuncuPuan += 1
						for k in range(3):
							self.matris[i][j - k] = 0
					sayac = 0
	def Kaydir(self):
		for i in range(self.boyut):
			for j in range(1, self.boyut):
				k = j
				if self.matris[j][i] == 0:
					while k != 0:
						self.matris[k][i], self.matris[k - 1][i] = self.matris[k - 1][i], self.matris[k][i]
						k -= 1
	def SifirlariDoldur(self):
		for i in range(self.boyut):
			for j in range(self.boyut):
				if self.matris[i][j]==0:
					self.matris[i][j]=random.randint(1,5)

	def KontrolOyun(self):
		if self.oyuncuPuan>=self.levelPuan:
			print "Tebrikler Basariyla Leveli tamamladiniz."
			return self.__init__()

	def Hamle(self):
		while True:
			while True:
				try:

					satir1 = int(input("Degistirelecek 1. cismin satir no: "))
					sutun1 = int(input("Degistirelecek 1. cismin sutun no: "))
					satir2 = int(input("Degistirelecek 2. cismin satir no: "))
					sutun2 = int(input("Degistirelecek 2. cismin sutun no: "))

					if (abs(satir2 - satir1) == 1 or (abs(sutun2 - sutun1) == 1)):
						break
					else:
						print "Hatali bir giris yaptiniz.Girdiginiz noktalar yanyana veya alt alta olmalidir"

				except:
					print "Hatali bir giris yaptiniz tekrar deneyin"
			self.matris[satir1][sutun1],self.matris[satir2][sutun2]=self.matris[satir2][sutun2],self.matris[satir1][sutun1]
			self.KontrolYatay()
			self.Kaydir()
			self.KontrolDikey()
			self.Kaydir()
			self.SifirlariDoldur()
			self.MatrisYazdir()
			self.KontrolOyun()




if __name__ == '__main__':
	oyun=candycrush()