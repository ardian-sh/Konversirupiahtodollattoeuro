def Main():
    RupiahToDollar = 15000
    RupiahToEuro = 16134.35
    EuroToDollar = 1.13

    while True:
        print("PROGRAM KONVERSI MATA UANG")
        print("==========================")
        print("MENU")
        print("1. Konversi dari DOLLAR ke RUPIAH ke EURO!")
        print("2. Konversi dari RUPIAH ke DOLLAR ke EURO!")
        print("3. Konversi dari EURO ke RUPIAH ke DOLLAR!")
        print("4. Keluar")

        Pilihan = ValidasiPilihan("Pilih menu sesuai angka : ",1,4)
        if(Pilihan == 1):
            UsdToRpToEuro(RupiahToDollar,EuroToDollar)
        elif(Pilihan == 2):
            RpToUsdToEuro(RupiahToDollar,RupiahToEuro)
        elif(Pilihan == 3):
            EuroToRpToUsd(RupiahToEuro,EuroToDollar)
        else:
            print("Goodbye")
            exit()

        print("\n")
        Pertanyaan = ValidasiString("kembali ke menu? [y/t]: ","y","t")
        if(Pertanyaan == "t"):
            print("Goodbye")
            exit()

def UsdToRpToEuro(RupiahToDollar:int,EuroToDollar:int):
    print("\nKonversi dari DOLLAR ke RUPIAH ke EURO!")

    Dollar = validasi_int("Masukan nominal Dollar: $. ")
    ConvertToRupiah = round((Dollar * RupiahToDollar))
    ConvertToEuro = round((Dollar/EuroToDollar))

    print("Nominal Dollar :$ {0}".format(Dollar))
    print("Dollar ke Rupiah :Rp {0}".format(formatrupiah(ConvertToRupiah)))
    print("Dollar ke Euro :€ {0}".format(ConvertToEuro))


def RpToUsdToEuro(RupiahToDollar:int,RupiahToEuro:int):
    print("\nKonversi dari RUPIAH ke DOLLAR ke EURO!")

    Rupiah = validasi_int("Masukan nominal Rupiah: Rp. ")
    ConvertToDollar = round((Rupiah / float(RupiahToDollar)))
    ConvertToEuro = round((Rupiah / float(RupiahToEuro)))

    print("Nominal Rupiah :Rp {0}".format(Rupiah))
    print("Rupiah ke Dollar :$ {0}".format(ConvertToDollar))
    print("Rupiah ke Euro :€ {0}".format(ConvertToEuro))


def EuroToRpToUsd(RupiahToEuro:int,EuroToDollar:int):
    print("\nKonversi dari EURO ke RUPIAH ke DOLLAR!")

    Euro = validasi_int("Masukan nominal Euro: € ")
    ConvertToRupiah = round((Euro * RupiahToEuro))
    ConvertToDollar = round((Euro * EuroToDollar))

    print("Nominal Euro :$ {0}".format(Euro))
    print("Euro ke Rupiah :Rp {0}".format(formatrupiah(ConvertToRupiah)))
    print("Euro ke Dollar :€ {0}".format(ConvertToDollar))

def validasi_int(judul):
    while True:
        try:
            pertanyaan = input(judul)
            if (pertanyaan==""):
                print("Inputan tidak boleh kosong")
            else:
                pertanyaan = int(pertanyaan)
                return pertanyaan
        except ValueError as e:
            print("inputan harus berupa angka")
        except Exception as e:
            print("error found :",e)

def ValidasiPilihan(judul:str, pilihan1:int, pilihan2: int):
    while True:
        try:
            Pilihan = input(judul)
            if (Pilihan==""):
                print("Inputan tidak boleh kosong")
            else:
                Pilihan = int(Pilihan)
                if(Pilihan >= pilihan1 and Pilihan <= pilihan2):
                    return Pilihan
                else:
                    print(str(Pilihan) + " tidak ada dalam menu")
        except ValueError as e:
            print("inputan harus berupa angka")
        except Exception as e:
            print("error found :",e)

def ValidasiString(judul:str, pilihan1:str, pilihan2: str):
    while True:
        try:
            Pilihan = input(judul)
            if (Pilihan==""):
                print("Inputan tidak boleh kosong")
            else:
                Pilihan = Pilihan.lower()
                if(Pilihan != pilihan1 and Pilihan != pilihan2):
                    print(Pilihan + " tidak ada dalam menu")
                else:
                    return Pilihan
        except ValueError as e:
            print(Pilihan + " tidak ada dalam menu")
        except Exception as e:
            print("error found :",e)

def formatrupiah(uang):
    y = str(uang)
    if len(y) <= 3 :
        return y
    else :
        p = y[-3:]
        q = y[:-3]
        return  formatrupiah(q) + '.' + p

if __name__ == '__main__':
    Main()