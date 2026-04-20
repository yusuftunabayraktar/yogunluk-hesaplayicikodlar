import os

def hesapla():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        try:
            # Sayıları tek tek girip Enter'a basmalısın
            m = float(input("Kütle (g): "))
            v = float(input("Hacim (cm3): "))
            sivi_d = float(input("Sıvı d (g/cm3): "))

            if v <= 0:
                print("\nHata: Hacim 0 olamaz.")
                input("\nDevam etmek için Enter...")
                continue

            cisim_d = m / v
            oran = (cisim_d / sivi_d) * 100

            if oran > 100:
                oran = 100.0
                durum = "BATAR"
            elif round(oran, 2) == 100.0:
                durum = "ASKIDA"
            else:
                durum = "YÜZER"

            print("-" * 25)
            print(f"Cisim d : {cisim_d:.2f} g/cm3")
            print(f"Batan   : %{oran:.1f}") # Buradaki hata düzeltildi
            print(f"Durum   : {durum}")
            print("-" * 25)

        except ValueError:
            print("\nHata: Lütfen sayıları tek tek girip Enter'a basın.")

        if input("\nTekrar? (e/h): ").lower() != 'e':
            break

if __name__ == "__main__":
    hesapla()