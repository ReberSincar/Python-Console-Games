import random

class oyun():
	def __init__(self):
		self.matris=[[0]*4 for i in range(4)]
		self.puan=0
		self.sayi = 1
		self.Rastgele()
		self.Rastgele()
		self.MatrisYazdir()
		self.HamleAl()

	def HamleAl(self):
		while True:
			hamle = int(input("Hamleyi girin:"))
			if hamle == 2:
				self.Hamle2Kaydir()
				self.Hamle2Topla()
				self.Hamle2Kaydir()
				self.Rastgele()
				self.MatrisYazdir()
				self.OyunKontrol()
			elif hamle == 4:
				self.Hamle4Kaydir()
				self.Hamle4Topla()
				self.Hamle4Kaydir()
				self.Rastgele()
				self.MatrisYazdir()
				self.OyunKontrol()
			elif hamle == 6:
				self.Hamle6Kaydir()
				self.Hamle6Topla()
				self.Hamle6Kaydir()
				self.Rastgele()
				self.MatrisYazdir()
				self.OyunKontrol()
			elif hamle == 8:
				self.Hamle8Kaydir()
				self.Hamle8Topla()
				self.Hamle8Kaydir()
				self.Rastgele()
				self.MatrisYazdir()
				self.OyunKontrol()
			else:
				print ("Yanlis hamle girdiniz")


	def Rastgele(self):
		while True:
			satir=random.randint(0,3)
			sutun=random.randint(0,3)
			if self.matris[satir][sutun]==0:
				self.matris[satir][sutun] = 2
				break

	def MatrisYazdir(self):
		for i in range(4):
			for j in range(4):
				print (str(self.matris[i][j])+"\t",end=" ")
			print ("\n\n")
		print ("Puaniniz : ",self.puan)

	def Hamle8Kaydir(self):
		for k in range(3):
			for i in range(0,3):
				for j in range(4):
					if self.matris[i][j]==0 and self.matris[i+1][j]!=0:
						self.matris[i+1][j],self.matris[i][j]=self.matris[i][j],self.matris[i+1][j]

	def Hamle8Topla(self):
		for i in range(0, 3):
			for j in range(4):
				if self.matris[i][j]==self.matris[i+1][j]:
					self.matris[i][j]=2*self.matris[i][j]
					self.matris[i+1][j]=0
					self.puan = self.puan + self.matris[i][j]


	def Hamle2Kaydir(self):
		for k in range(3):
			for i in range(3,0,-1):
				for j in range(4):
					if self.matris[i][j] == 0 and self.matris[i - 1][j] != 0:
						self.matris[i-1][j],self.matris[i][j]=self.matris[i][j],self.matris[i-1][j]

	def Hamle2Topla(self):
		for i in range(3, 0, -1):
			for j in range(4):
				if self.matris[i][j]==self.matris[i-1][j]:
					self.matris[i][j]=2*self.matris[i][j]
					self.matris[i-1][j]=0
					self.puan = self.puan + self.matris[i][j]

	def Hamle4Kaydir(self):
		for k in range(3):
			for i in range(4):
				for j in range(0,3):
					if self.matris[i][j]==0 and self.matris[i][j+1] != 0:
						self.matris[i][j+1],self.matris[i][j]=self.matris[i][j],self.matris[i][j+1]

	def Hamle4Topla(self):
		for i in range(4):
			for j in range(0, 3):
				if self.matris[i][j]==self.matris[i][j+1]:
					self.matris[i][j]=2*self.matris[i][j]
					self.matris[i][j+1]=0
					self.puan = self.puan + self.matris[i][j]

	def Hamle6Kaydir(self):
		for k in range(3):
			for i in range(4):
				for j in range(3,0,-1):
					if self.matris[i][j]==0 and self.matris[i][j-1] != 0:
						self.matris[i][j-1],self.matris[i][j]=self.matris[i][j],self.matris[i][j-1]

	def Hamle6Topla(self):
		for i in range(4):
			for j in range(3,0,-1):
				if self.matris[i][j]==self.matris[i][j-1]:
					self.matris[i][j]=2*self.matris[i][j]
					self.matris[i][j-1]=0
					self.puan = self.puan + self.matris[i][j]

	def OyunKontrol(self):
		liste = []
		for i in range(4):
			for j in range(4):
				liste.append(self.matris[i][j])

		if max(liste) == 2048:
			print ("Tebrikler Kazandiniz")
		elif 0 not in liste:
			print ("Oyun bitti.Puaniniz: ", self.puan)
			quit()

if __name__ == '__main__':
	ikibinkirksekiz=oyun()