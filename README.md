# STARCO DISCORD RAIDER RS+ - YUSUF INC.

![STARCO](https://img.shields.io/badge/STARCO-RS+-red?style=for-the-badge&logo=discord)
![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-Educational-green?style=for-the-badge)

## 🚀 STARCO Discord Raider RS+ Hakkında

**STARCO Discord Raider RS+**, YUSUF INC. tarafından geliştirilen gelişmiş Discord raider aracıdır. Bu araç, Discord sunucularında çoklu token desteği ile paralel spam işlemleri gerçekleştirmenizi sağlar.

### ✨ Özellikler

- **🎯 Single Raid**: Tek sunucuya odaklı spam işlemleri
- **⚡ Multi Paralel Spam**: Birden fazla kanala aynı anda paralel spam
- **🔧 Token Management**: Çoklu token yönetimi ve kontrolü
- **🪝 Webhook Operations**: Webhook spam, silme ve oluşturma
- **🛠️ Advanced Tools**: Token checker, sunucu bilgileri, kanal bilgileri
- **🎨 Modern Interface**: Renkli ve kullanıcı dostu arayüz
- **📊 Real-time Monitoring**: Gerçek zamanlı işlem takibi

### 🔥 Multi Paralel Spam Özellikleri

**Multi Paralel Spam**, STARCO'nun en güçlü özelliğidir:

- **Çoklu Token Desteği**: Aynı anda birden fazla token kullanır
- **Paralel Kanal Spam**: Birden fazla kanala eş zamanlı mesaj gönderir
- **Akıllı Delay Sistemi**: Kanal arası ve loop arası özelleştirilebilir gecikme
- **Otomatik Token Rotation**: Token'lar arasında otomatik geçiş
- **Hata Toleransı**: Başarısız token'ları otomatik atlar
- **Gerçek Zamanlı İstatistikler**: Gönderilen mesaj sayısı ve başarı oranı

## 📦 Kurulum

### 🎯 Otomatik Kurulum (Önerilen)

1. **STARCO Raider Pro.bat** dosyasını çift tıklayın
2. Program otomatik olarak:
   - Python kontrolü yapar
   - Gerekli paketleri yükler (`requests`, `colorama`)
   - `tokens.txt` dosyasını oluşturur
   - Programı başlatır

### 🔧 Manuel Kurulum

1. **Python 3.6+** yüklü olduğundan emin olun
2. Gerekli paketleri yükleyin:
```bash
pip install requests colorama
```

3. Programı çalıştırın:
```bash
python starco_launcher.py
```

## 🎮 Kullanım

### 🏠 Ana Menü

Program başladığında ana menüde şu seçenekler bulunur:

```
[01] Settings   - Ayarlar ve sistem bilgileri
[02] Raider     - Raid işlemleri
[03] Webhooks   - Webhook işlemleri  
[04] Tools       - Gelişmiş araçlar
[05] Exit       - Programdan çıkış
```

### ⚡ Raider Menüsü

**Single Raid:**
- Tek sunucuya odaklı spam
- Rastgele token seçimi
- Özelleştirilebilir mesaj ve delay

**Multi Paralel Spam:**
- Birden fazla kanal ID'si girin (virgülle ayırın)
- Çoklu token ile paralel spam
- Kanal arası ve loop arası delay ayarları
- Gerçek zamanlı performans takibi

### 🔧 Settings Menüsü

- **Token Check**: Token dosyası kontrolü
- **Token List**: Token listesi görüntüleme
- **Install Packages**: Paket yükleme
- **System Info**: Sistem bilgileri

### 🪝 Webhooks Menüsü

- **Webhook Spam**: Webhook'lara spam gönderme
- **Webhook Delete**: Webhook silme
- **Webhook Create**: Yeni webhook oluşturma

### 🛠️ Tools Menüsü

- **Token Checker**: Token geçerlilik kontrolü
- **Server Info**: Sunucu bilgileri
- **Channel Info**: Kanal bilgileri

## 📝 Token Dosyası Hazırlama

1. `tokens.txt` dosyasını açın
2. Her satıra bir Discord token'ı yazın
3. `#` ile başlayan satırlar yorum olarak kabul edilir
4. Boş satırlar otomatik olarak atlanır

**Örnek `tokens.txt` formatı:**
```
# Discord Bot Token'ları
# Her satıra bir token yazın
MTIzNDU2Nzg5MDEyMzQ1Njc4.GhIjKl.MnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz
MTIzNDU2Nzg5MDEyMzQ1Njc4.GhIjKl.MnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrStUvWxYz
```

## 🔑 Token Alma

### 🌐 Tarayıcıdan Token Alma

1. Discord'a giriş yapın
2. **F12** ile Developer Tools'u açın
3. **Network** sekmesine gidin
4. Herhangi bir işlem yapın (mesaj gönderin)
5. `Authorization` header'ından token'ı kopyalayın

### 💻 JavaScript Console ile Token Alma

1. Discord web'de **F12** açın
2. **Console**'a şu kodu yazın:
```javascript
window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.getToken !== undefined) {return copy(m.default.getToken())}if (m.getToken !== undefined) {return copy(m.getToken())}}}]); console.log('%cWorked!', 'font-size: 50px'); console.log(`%cYou now have your token in the clipboard!`, 'font-size: 16px')
```

## ⚠️ Önemli Uyarılar

- **🎓 Eğitim Amaçlı**: Bu proje sadece öğrenme amaçlıdır
- **📋 Hizmet Şartları**: Discord'un hizmet şartlarına uygun kullanın
- **🔒 Güvenlik**: Token'larınızı güvenli tutun
- **🚫 Kötüye Kullanım**: Kötüye kullanım yapmayın
- **⚖️ Sorumluluk**: Kullanım sorumluluğu kullanıcıya aittir

## 🏆 STARCO RS+ Avantajları

- **🚀 Yüksek Performans**: Paralel işlem desteği
- **🎯 Akıllı Sistem**: Otomatik hata yönetimi
- **🔄 Esnek Yapı**: Özelleştirilebilir ayarlar
- **📊 Detaylı Raporlama**: Gerçek zamanlı istatistikler
- **🛡️ Güvenli**: Token koruma sistemi

## 📞 Destek

**YUSUF INC.** tarafından geliştirilmiştir.

---

*STARCO Discord Raider RS+ - Eğitim amaçlı geliştirilmiştir. Sorumlu kullanın.*