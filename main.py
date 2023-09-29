import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("kaç harf olsun?"))
sifre = ""
for i in range(uzunluk):
    sifre += random.choice(karakterler)
print(sifre)