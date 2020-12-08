import requests
from bs4 import  BeautifulSoup

# hangi siteden veri cekmek istiyoruz?
url = "http://www.imdb.com/chart/top"

# requests.get(url) diyerek 'url' icindeki sayfaya ulasmaya calisiyoruz
response = requests.get(url)

# sayfa icerigine ulasip ulasamadigimizi response ile donen degerden kontrol ediyoruz
# (200-> basarili, yani internetten veriyi almis bulunuyoruz)
# artik veri ile ilgili her sey 'response' degiskeni icindedir.
# print(response)

# simdi 'response' degiskeni icinden sayfanin kaynagini aliyoruz
sayfa_html_icerik = response.content

# Bir tane 'BeautifulSoup' nesnesi olusturarak 'sayfa_html_icerik' icindeki html verileri parse ediyoruz
soup = BeautifulSoup(sayfa_html_icerik,"html.parser")

# Tarayicidan sayfa icinde filmlerin bulundugu yeri buluyoruz.
# film isimleri html icerik icinde 'td' taglari icinde tutulmus ve class olarak 'titleColumn' denilmis.
# Simdi classi 'titleColumn' olan html taglari icindeki valuelari aliyoruz.

#for i in soup.find_all("td",{"class":"titleColumn"}):
    # print(i) --> bu sekilde tum '<td class="titleColumn"></td>' taglarin arasindaki tum tdleri cekmis olduk.
    #print(i)

    # print(i.text) --> bu sekilde td taglari icindeki text(value) degerlerini cekmis olduk
    # print(i.text)
    # print("-----")

# filmleri ve imdb puanlarini listelere aldik. Her filmin bir imdb puani olmali.
filmler = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

# Kullanicinin girdigi bir imdb puanindan daha buyuk imdbye sahip olan filmleri cekelim
imdb = float(input("Imdb giriniz: "))

# Her filmin bir imdb puani olacagi icin bu iki listeyi birlestiriyoruz. Ve bir demet yapisi olusturmus oluyoruz.
for film,rating in zip(filmler,ratingler):

    # gorunumun daha duzenli olmasi icin strim() ve replace fonksiyonlarini kullaniyoruz
    film = film.text
    film = film.strip()
    film = film.replace("\n","")

    rating = rating.text
    rating = rating.strip()
    rating = rating.replace("\n", "")


    # print("Film:", film)
    # print("Rating:", rating)

    if(float(rating)> imdb):
        print("Film: {}----Imdb: {}".format(film,rating))

