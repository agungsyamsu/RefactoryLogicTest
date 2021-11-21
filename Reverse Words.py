def balikKata(kalimat):
       kumpulanKata = kalimat.split(" ")
       kataBaru = [kata[::-1] for kata in kumpulanKata]
       kalimatBaru = " ".join(kataBaru)
       return kalimatBaru

kalimat = input("Masukkan kata/kalimat: ")
print(balikKata(kalimat))