#Suhu Reamur ke celcius

class Suhu:
    @staticmethod
    def Reamur_to_celcius(R):
        C = 5/4*R
        return C

# Contoh penggunaan
R = 30
C = Suhu.Reamur_to_celcius(R)

print("Konversi", R, "derajat Reamur adalah:", C, "derajat Celcius")

#Latihan 2 PBO Reamur ke Kelvin

class Suhu:
    @staticmethod
    def Reamur_to_Kelvin(R):
        K = 5/4*R+273
        return K

# Contoh penggunaan
R = 100
K = Suhu.Reamur_to_Kelvin(R)

print("Konversi", R, "derajat Reamur adalah:", K, "derajat Kelvin")

#Latihan 3 PBO Reamur ke Fahrenhet

class Suhu:
    @staticmethod
    def Reamur_to_fahrenheit(R):
        F = 9/5*R+32
        return F
    
R = 150
F = Suhu.Reamur_to_fahrenheit(R)
print("Konversi", R, "derajat Reamur adalah:",F, "derajat Fahrenheit")
