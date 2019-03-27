import time
import random
"""
Level 1 --> 50      # sure -->10
Level 2 --> 100     # sure -->9
Level 3 --> 150     # sure -->8
.                   # sure -->7
.
.
.
.
.
.
.
Level 10 --> 500     # sure -->5
"""

#amac matristeki sayılardan size verilen sayıya tam bölen sayıları bulmak.

class BolmeOyunu():
	def __init__(self,level=1):
		self.asalListe=[2,3,5,7,11]
		self.asal=self.asalListe[random.randint(0,4)]
		self.level=level
		self.boyut=level*2+2
		self.zaman=10
		self.bas=1
		self.hak=3
		self.puan=0
		self.matris=[]
		self.MatrisOlustur()
		self.Hamle()

	def RandomAta(self): #Matrise random sayi atama fonksiyonu
		for i in range(self.boyut):
			for j in range(self.boyut):
				self.matris[i][j]=random.randint(self.bas,self.level*50)
	
	def MatrisYazdir(self): #Matris yazdirma fonksiyonu
		for i in range(self.boyut):
			for j in range(self.boyut):
				print str(self.matris[i][j])+"\t",
			print "\n"
	
	def KontrolMatris(self): #Kontrol fonksiyonu matristeki asal sayiya bolunen sayilari kontrol eder
		sayac=0
		for i in range(self.boyut):
			for j in range(self.boyut):
				if self.matris[i][j]%self.asal==0: #Matriste kac tane bolunen sayi oldugunu bulduk
					sayac=sayac+1
		for i in range(11-self.level-sayac):
			while True:
				satir = random.randint(0, self.boyut - 1)
				sutun = random.randint(0, self.boyut - 1)
				if self.matris[satir][sutun]%self.asal != 0:
					self.matris[satir][sutun]=self.asal*i*self.level
					break
	
	def MatrisOlustur(self): #Matris olusturma
		self.matris = [[""] * self.boyut for i in range(self.boyut)]
	
	def KontrolOyun(self): #Level yukseltme fonksiyonu
		if self.puan >=self.level*100:
			print "Tebrikler %d. Leveli atladiniz." %self.level
			self.bas = self.level * 50
			self.level=self.level+1
			self.zaman=self.zaman-1
			self.boyut = self.boyut + 1
			self.MatrisOlustur()

	def Hamle(self):
		while True:
			self.asal= self.asalListe[random.randint(0, 4)]
			print "\n\nSayiniz %d\n\n" % self.asal
			self.RandomAta()
			self.KontrolMatris()
			self.MatrisYazdir()
			baslangic = time.time()
			satir = input("Satir no:")
			sutun = input("Sutun no:")
			bitis=time.time()
			sure=bitis-baslangic
			if self.matris[satir-1][sutun-1] % self.asal == 0 and sure<=self.zaman:
				print "Basarili Hamle! Devam!"
				self.puan += self.matris[satir-1][sutun-1] // self.asal
				print "Puaniniz : ",self.puan
				self.KontrolOyun()
	
			elif self.matris[satir-1][sutun-1] % self.asal == 0 and sure>self.zaman:
				self.hak=self.hak-1
				print "Sure Doldu! Kalan Hak %d" % self.hak
				print "Puaniniz : ", self.puan
				if self.hak == 0:
					print "Oyun bitti! Puanin %d" % self.puan
					quit()
			elif self.matris[satir-1][sutun-1] % self.asal != 0 and sure>self.zaman:
				self.hak = self.hak - 1
				print "Sure Doldu! Kalan Hak %d" % self.hak
				print "Puaniniz : ", self.puan
				if self.hak == 0:
					print "Oyun bitti! Puanin %d" % self.puan
					quit()
			else:
				self.hak = self.hak - 1
				print "Hatali Hamle! Kalan Hak %d" % self.hak
				print "Puaniniz : ", self.puan
	
				if self.hak == 0:
					print "Oyun bitti! Puanin %d" % self.puan
					quit()

if __name__ == '__main__':
	oyun=BolmeOyunu()