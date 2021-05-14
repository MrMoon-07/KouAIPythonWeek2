
##Program odev.txt dosyasından aldığı verileri özel karakter ve sayıları ayırarak temiz veriyi odevclr.txt dosyasına yazdırır

fs = open("odev.txt")
ft = open("odevclr.txt","w")

list1 = []
c = ""

while fs.readline() != "":
    for i in fs.readline():
        if i.isalpha():
            c = c + i
    ft.write("{} \n".format(c))
    c = ""





