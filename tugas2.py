import numpy as np
import matplotlib.pyplot as mpl

def rotasi(teta):
    return np.array([
        [np.cos(teta), -np.sin(teta), 0], 
        [np.sin(teta), np.cos(teta), 0] , 
        [0, 0, 1]])
def panjang(l):
    return np.array([
        [1, 0 ,l], 
        [0, 1, 0], 
        [0, 0, 1]])

teta1= np.deg2rad(float(input("Masukkan derajat pertama: ")))
teta2= np.deg2rad(float(input("Masukkan derajat kedua: ")))
l1= float(input("Masukkan panjang pertama: "))
l2= float(input("Masukkan panjang kedua: "))
transformasi1 = rotasi(teta1) @ panjang(l1)
transformasi2 = rotasi(teta2) @ panjang(l2)
matriksakhir = transformasi1 @ transformasi2
print(matriksakhir)

xakhir = matriksakhir[0,2]
yakhir =  matriksakhir[1,2]
print("titik akhir (x,y) adalah ", "(",xakhir,", ",yakhir,")")

titikx1 = [0, transformasi1[0,2]]
titiky1 = [0, transformasi1[1,2]]
titikx2 = [transformasi1[0,2], xakhir]
titiky2 = [transformasi1[1,2], yakhir]

mpl.figure(figsize=(5, 5))
mpl.plot(titikx1, titiky1)
mpl.plot(titikx2, titiky2)
#mpl.plot(xkoor, ykoor)
mpl.show()


yn = input("Mau nyoba invers untuk cari sudut? (Y/N): ")

#inverse
def inv1(x, y, l1, l2):
    inv = np.arccos((x**2 + y**2 - l1**2 - l2**2) / (2*l1*l2))
    return inv
def inv2(x, y, l1, l2, sudut2):
    inv = np.arctan(y/x) - np.arctan((l2*np.sin(sudut2))/(l1 + l2*np.cos(sudut2)))
    return inv
if yn == "Y":
    xakhir = float(input("Masukkan titik x akhir: "))
    yakhir = float(input("Masukkan titik y akhir: "))
    l1 = float(input("Masukkan panjang pertama: "))
    l2 = float(input("Masukkan panjang kdeua: "))
    sudut_kedua = inv1(xakhir, yakhir, l1, l2)
    sudut_pertama = inv2(xakhir, yakhir, l1, l2, sudut_kedua)
    print("sudut kedua adalah: ", sudut_kedua)
    print("sudut pertama adalah: ", sudut_pertama)
else: 
    print("Ok deh")
