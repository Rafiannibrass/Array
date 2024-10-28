# Deklarasi matriks
matriks = []

# Meminta input pengguna untuk mengisi matriks 3x3
print("memasukan elemen untuk matriks 3x3:")
for i in range(3):
    baris = []
    for j in range (3):
        nilai = int(input(f"masukan elemen baris {1+1}, kolom {j+1}: "))
        baris.append(nilai)
    matriks.append(baris)

# Transpose matriks
transpose = []
for i in range(3):
    baris = []
    for j in range(3):
        baris.append(matriks[j][i])
    transpose.append(baris)

# Menampilkan hasil transpose
print("\nHasil transpose matriks:")
for baris in transpose:
    print(baris)