# IP Sorgu Aracı

Bu araç, kullanıcıların IP adresleri hakkında bilgi almasını sağlar. IP adresi sorgulandığında, araç IP adresine ait detayları (lokasyon, ISP bilgisi vb.) sağlar.

![Örnek Görüntü](https://github.com/infinitylinkkk/ip-sorgu/blob/935756b7f98c5c4e3e98f9a724dbf6e190ea6f63/IMG_20240807_123045.jpg)

## Özellikler

- IP adresi sorgulama
- Lokasyon bilgisi (şehir, ülke)
- İnternet Servis Sağlayıcı (ISP) bilgisi
- Detaylı IP bilgisi

## Kurulum

1. Bu depoyu klonlayın veya zip olarak indirin:
    ```bash
    git clone https://github.com/infinitylinkkk/ip-sorgu.git
    ```
   
2. Gerekli bağımlılıkları yükleyin:
    ```bash
    cd infinitylinkkk
    pip install requests
    ```

## Kullanım

1. Aracı çalıştırın:
    ```bash
    python infinitylink-ip.py
    ```
    
2. IP adresini girin ve Enter tuşuna basın. Arayüz IP adresine ait bilgileri gösterecektir.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi (IP bilgisi almak için kullanılıyor)
- `prettytable` kütüphanesi (isteğe bağlı, tablolu gösterim için)

## Örnek

IP sorgulama aracını çalıştırdığınızda aşağıdaki gibi bir çıktı alabilirsiniz:
