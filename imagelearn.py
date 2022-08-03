import instaloader

instagram = instaloader.Instaloader()


def beniTakipetmeyenler(kullanici_adi):
    profile = instaloader.Profile.from_username(instagram.context, kullanici_adi)
    takipciler = profile.get_followers()
    takip_edilenler = profile.get_followees()

    takipciler_listesi = list()
    takip_edilenler_listesi = list()

    for i in takipciler:
        takipciler_listesi.append(i.username)

    for j in takip_edilenler:
        takip_edilenler_listesi.append(j.username)

    sayac = 0
    for i in takip_edilenler_listesi:
        if i not in takipciler_listesi:
            print(i, " kullanicisi seni takip etmiyor")
            sayac += 1
    print("Sana geri takip yapmayan kullanici sayisi", sayac)


def usernameSearch():
    kullanici_adi = input("Kullanıcı Adı Giriniz:")

    profile = instaloader.Profile.from_username(instagram.context, kullanici_adi)
    takipciler = profile.get_followers()
    takip_edilenler = profile.get_followees()

    takipciler_listesi = list()
    takip_edilenler_listesi = list()

    for i in takipciler:
        takipciler_listesi.append(i.username)

    for j in takip_edilenler:
        takip_edilenler_listesi.append(j.username)

    print(takipciler_listesi)
    print(takip_edilenler_listesi)


def Menu(isLogin, username):
    if isLogin:
        print("1.Beni Takit Etmeyenleri Göster")
        print("2.Kullanıcı Adı ile arama yap")
    else:
        print("2.Kullanıcı Adı ile arama yap")

    menuTwo = input("Seçiniz: ")
    if  int(menuTwo) == 1:
        beniTakipetmeyenler(username)
    else:
        usernameSearch()


def girisYap():
    kullanici_adi = input("Kullanıcı Adı Giriniz:")
    parola = input("Şifre Giriniz:")

    print("Giriş Yapılıyor...")
    instagram.login(kullanici_adi, parola)
    profile = instaloader.Profile.from_username(instagram.context, kullanici_adi)
    print("Giriş Yapılıdı.")

    print("-----------------------------")
    print("Post sayısı", profile.mediacount)
    print("Takip ettiği kişi sayısı:", profile.followees)
    print("Takipçi sayısı:", profile.followers)
    print("Biyografi:", profile.biography)
    print("İnternet Sitesi", profile.external_url)
    print("-----------------------------")
    Menu(True, kullanici_adi)


print("Welcome to Stolker App")

print("1.Giriş Yap")

print("2.Giriş yapmadan devam et(Gizli Profiler Göntülenemez Giriş Yamanız gerekir")

menuOne = input("Seçiniz:")
if int(menuOne) == 1:
    girisYap()
else:
    Menu(False, None)