import tkinter as tk
import time

calisiyor=False
baslangic=0
gecen=0

def guncelle():
    if calisiyor:
        s=time.time()-baslangic+gecen
        saat.config(text=f"{s:.1f} sn")
    pencere.after(100,guncelle)

def baslat():
    global calisiyor, baslangic
    if not calisiyor:
        baslangic=time.time()
        calisiyor=True

def durdur():
    global calisiyor, gecen, baslangic
    if calisiyor:
        gecen += time.time()-baslangic
        calisiyor=False

def sifirla():
    global calisiyor, gecen
    calisiyor=False
    gecen=0
    saat.config(text="0.0 sn")

pencere=tk.Tk()
pencere.title("Kronometre")
pencere.geometry("350x220")
saat=tk.Label(pencere,text="0.0 sn",font=("Arial",28))
saat.pack(pady=20)
tk.Button(pencere,text="Başlat",command=baslat).pack(fill="x")
tk.Button(pencere,text="Durdur",command=durdur).pack(fill="x")
tk.Button(pencere,text="Sıfırla",command=sifirla).pack(fill="x")
guncelle()
pencere.mainloop()
