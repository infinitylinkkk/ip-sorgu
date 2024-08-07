# IP Sorgu Aracı

Bu araç, kullanıcıların IP adresleri hakkında bilgi almasını sağlar. IP adresi sorgulandığında, araç IP adresine ait detayları (lokasyon, ISP bilgisi vb.) sağlar.

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
    pip install -r requirements.txt
    ```

## Kullanım

1. Aracı çalıştırın:
    ```bash
    python İnfinitylink-İpSorgu.py
    ```
    
2. IP adresini girin ve Enter tuşuna basın. Arayüz IP adresine ait bilgileri gösterecektir.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi (IP bilgisi almak için kullanılıyor)
- `prettytable` kütüphanesi (isteğe bağlı, tablolu gösterim için)

## Örnek

IP sorgulama aracını çalıştırdığınızda aşağıdaki gibi bir çıktı alabilirsiniz:
