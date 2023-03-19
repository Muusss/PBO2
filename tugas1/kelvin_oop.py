#Suhu kelvin ke celcius

class Suhu:
    @staticmethod
    def kelvin_to_celcius(k):
        C = k-273
        return C

# Contoh penggunaan
K = 300
C = Suhu.kelvin_to_celcius(K)

print("Konversi", K, "derajat Kelvin adalah:", C, "derajat Celcius")

#Latihan 2 PBO Kelvin ke Reamur

class Suhu:
    @staticmethod
    def kelvin_to_reamur(K):
        r = 4/5*(K-273)
        return r

# Contoh penggunaan
K = 300
R = Suhu.kelvin_to_reamur(K)

print("Konversi", K, "derajat Kelvin adalah:", R, "derajat Reamur")

#Latihan 3 PBO Kelvin ke Fahrenhet

class Suhu:
    @staticmethod
    def kelvin_to_fahrenheit(K):
        f = (9/5*K)-459.4
        return f
    
K = 470
F = Suhu.kelvin_to_fahrenheit(K)
print("Konversi", K, "derajat Kelvin adalah:",F, "derajat Fahrenheit")
