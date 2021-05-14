
##Program odev.txt dosyasından aldığı verileri özel karakter ve sayılardan ayırarak temiz veriyi odevclr.txt adında bir dosyaya yazdırır.
##Daha önceden odevclr.txt adında bir dosyanızın varlığını kontrol ediniz aksi taktirde varolan verilerinizi kaybedebilirsiniz.

fs = open("odev.txt")
ft = open("odevclr.txt","w")
c = ""

while fs.readline() != "":
    for i in fs.readline():
        if i.isalpha():
            c = c + i
    ft.write("{} \n".format(c))
    c = ""





