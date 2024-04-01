#Nurten Yıldız
#dışarıdan girilen bir String içeriğindeki palindromları bulan ve bunları karekter boyutuna göre büyükten küçüğe sıralayan, aynı palindromlardan birden fazla kez var
# ise bunların kaç kere tekrarlandığını bulan bir uygulama yazınız. Örneğin 323, 6336, 7895987 veya Kak, Kaçak, 

metin=input("Metin giriniz: ")
A=metin.split() #girilen metni listeye çevirme

B=[] #palindrom sayıları eklemek için liste
for i in A:   #metin listesinin her bir elemanına tek tek ulaşmak için döngü kullandım
    
    length=len(i)-1
    rev=""
    while length>=0: #elemanların tersini bulma
        rev += i[length]
        length-=1
    
    
    if i==rev: #ters ve düzü aynı olan yani palindrom sayıları onay süreci
        #print(i+" " +"bir palindromdur.") #kontrol amaçlı
        B.append(i)  #palindrom olanlar B listesine
        
        
sorted_numbers = sorted(B,key=len, reverse=True)   #liste elemanlarını karakter uzunluklarına göre sıralama 
print(sorted_numbers) #sıralı eleman gösterimi
#
#sıralı elemanların listede kaç tane olduğunu bulma
sayac = {}

for eleman in sorted_numbers:
    if eleman in sayac:
        sayac[eleman] += 1
    else:
        sayac[eleman] = 1

for eleman, sayi in sayac.items():
    print(f"{eleman} listede {sayi} defa geçiyor.")