#Suhu Fahrenheit ke celcius

class Suhu:
    @staticmethod
    def Fahrenheit_to_celcius(F):
        C = 5/9*(F-32)
        return C

# Contoh penggunaan
F = 100
C = Suhu.Fahrenheit_to_celcius(F)

print("Konversi", F, "derajat Fahrenheit adalah:", C, "derajat Celcius")

#Latihan 2 PBO Fahrenheit ke Reamur

class Suhu:
    @staticmethod
    def Fahrenheit_to_reamur(F):
        R = 4/9*(F-32)
        return R

# Contoh penggunaan
F = 70
R = Suhu.Fahrenheit_to_reamur(F)

print("Konversi", F, "derajat Fahrenheit adalah:", R, "derajat Reamur")

#Latihan 3 PBO Fahrenheit ke Kevin

class Suhu:
    @staticmethod
    def Fahrenheit_to_Kelvin(F):
        K = 5/9*(F+459.4)
        return K
    
F = 470
K = Suhu.Fahrenheit_to_Kelvin(F)
print("Konversi", F, "derajat Fahrenheit adalah:",K, "derajat Kelvin")
