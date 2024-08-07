import requests

def print_large_text():
    """Büyük metin yazdırır."""
    print("\033[1;96m")  # Kalın ve yeşil renk
    print("===================================")
    print("     İ N F İ N İ T Y L İ N K")
    
    print("===================================")
    print("\033[0m")  # Renk ve kalınlığı sıfırlar

def check_server_status():
    """Sunucunun çevrimiçi olup olmadığını kontrol eder."""
    try:
        r = requests.get("https://ipinfo.io/")
        r.raise_for_status()  # Hata durumunda bir istisna fırlatır
        print("\n\033[91m[+] Sorgulanıyor...\n\033[0m")
    except requests.RequestException:
        print("\n\033[91m[!] Sorgulanamadı\n\033[0m")
        exit()

def get_ip_info(ip):
    """Verilen IP adresine ilişkin bilgileri alır."""
    try:
        data = {}
        endpoints = ["country", "city", "region", "postal", "timezone", "org", "loc"]
        for endpoint in endpoints:
            response = requests.get(f"https://ipinfo.io/{ip}/{endpoint}/")
            response.raise_for_status()
            data[endpoint] = response.text.strip()
        return data
    except requests.RequestException as e:
        print(f"\n\033[91m[!] Hata: {e}\n\033[0m")
        exit()

print_large_text()

# Kırmızı renkte input istemi
ip = input("\033[91mLütfen hedef IP adresini giriniz:\033[0m ")

check_server_status()

# IP bilgilerini al
info = get_ip_info(ip)

# Kullanıcıya girdileri yeşil renkte göstermek
print("\033[92mIP: {}\033[0m".format(ip))
print("\033[92mÜlke: {}\033[0m".format(info['country']))
print("\033[92mŞehir: {}\033[0m".format(info['city']))
print("\033[92mBölge: {}\033[0m".format(info['region']))
print("\033[92mPosta Kodu: {}\033[0m".format(info['postal']))
print("\033[92mZaman Dilimi: {}\033[0m".format(info['timezone']))
print("\033[92mOrganizasyon: {}\033[0m".format(info['org']))
print("\033[92mLokasyon: {}\033[0m".format(info['loc']))

# Parlak açık mavi renkte URL bağlantısı
print("\033[96m[+] Daha fazla bilgi için: https://t.me/infinitylinkk\033[0m")