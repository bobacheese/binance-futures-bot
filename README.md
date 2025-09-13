# 🤖 Bot Trading Binance Futures

<div align="center">

![Bot Trading Banner](https://user-images.githubusercontent.com/YOUR_USERNAME/bot-trading-banner.png)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CCXT](https://img.shields.io/badge/CCXT-Latest-green.svg)](https://github.com/ccxt/ccxt)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Telegram](https://img.shields.io/badge/Telegram-Channel-blue.svg)](https://t.me/your_channel)
![Profile Views](https://komarev.com/ghpvc/?username=bobacheese&color=brightgreen&label=Profile+Views)
[![GitHub Visitors](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fbobacheese%2Fbinance-bot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=visitors&edge_flat=false)](https://hits.seeyoufarm.com)

*Bot trading otomatis untuk Binance Futures dengan Machine Learning dan manajemen risiko canggih* 🚀

[Mulai Trading](#panduan-instalasi) • 
[Dokumentasi](#dokumentasi) • 
[FAQ](#faq) • 
[Support](#support)

</div>

---

## 🌟 Fitur Utama

<div align="center">

| 🎯 Trading Otomatis | 🧠 Machine Learning | 📊 Multi-Timeframe | 🛡️ Risk Management |
|:------------------:|:-------------------:|:-----------------:|:-----------------:|
| Entry & Exit Otomatis | Prediksi Arah Market | Analisis 4 Timeframe | Stop Loss Dinamis |
| Take Profit Bertingkat | Retraining Otomatis | Konfirmasi Trend | Position Sizing |
| Trailing Stop | Pattern Recognition | Volume Analysis | Risk-Reward Ratio |

</div>

## 📚 Daftar Isi

```
binance_bot/
├── config/         # File konfigurasi
├── models/         # Model machine learning
├── utils/          # Fungsi utilitas
├── logs/          # File log
└── README.md      # Dokumentasi
```

## Panduan Scalping Timeframe Kecil

1. **Optimasi untuk Scalping**
   - Fokus pada timeframe 1m, 3m, 5m
   - Take profit kecil tapi sering (0.3% - 0.6%)
   - Stop loss sangat ketat (0.3%)
   - Spread maksimal 0.03%
   - Analisa super cepat

2. **Strategi Scalping**
   a. Entry Criteria:
      - Konfirmasi 3 timeframe
      - Volume spike
      - Tight spread
      - Clear trend direction
   
   b. Exit Strategy:
      - Take profit bertahap
      - Trailing stop agresif
      - Quick exit saat reversal
      - Cut loss cepat
   
   c. Momentum Trading:
      - EMA crossover (3,5,8)
      - RSI divergence
      - Volume confirmation
      - Price action patterns

3. **Risk Management Scalping**
   - Posisi lebih kecil
   - Stop loss lebih dekat
   - Take profit bertahap
   - No overnight positions
   - Quick exit strategy

## Panduan Trading Modal Kecil (50-150rb)

1. **Persiapan Modal**
   - Siapkan modal 50-150 ribu rupiah (± 3-10 USDT)
   - Gunakan konfigurasi khusus modal kecil: `config_modal_kecil.yaml`
   - Leverage yang digunakan: 20x (bisa disesuaikan)
   - Ukuran posisi sangat kecil untuk keamanan

2. **Keamanan untuk Modal Kecil**
   - Stop loss lebih ketat: 0.5%
   - Take profit bertahap: 0.5% dan 1%
   - Maksimal loss harian: 3%
   - Hanya 1 posisi terbuka
   - Safety net yang lebih ketat

3. **Strategi Khusus Modal Kecil**
   - Fokus di timeframe pendek (1m-15m)
   - Profit target lebih kecil tapi lebih sering
   - Risk:Reward minimal 1:2
   - Scalping dengan konfirmasi kuat
   - Gunakan DCA dengan sangat hati-hati

4. **Tips Modal Kecil**
   - Mulai dengan testnet
   - Jangan terburu-buru mengejar profit
   - Fokus pada win rate tinggi
   - Monitor spread dengan ketat
   - Perhatikan fee trading
   - Tunggu sinyal yang sangat kuat (>80% confidence)

## Cara Menggunakan

1. Install dependencies:
```bash
pip install ccxt pandas numpy ta scikit-learn python-telegram-bot rich pyyaml joblib
```

2. Cara mendapatkan API Binance:
   a. Login ke akun Binance Futures anda
   b. Klik menu "API Management" di pengaturan akun
   c. Klik "Create API"
   d. Masukkan nama untuk API (misal: "Trading Bot")
   e. Aktifkan fitur futures trading
   f. Salin API Key dan Secret Key yang diberikan
   g. Untuk keamanan, batasi akses IP dan aktifkan whitelist IP

3. Setup API di config.yaml:
   a. Buka file `config/config.yaml`
   b. Isi bagian API dengan format:
      ```yaml
      api_key: "PASTE_API_KEY_ANDA_DISINI"
      api_secret: "PASTE_SECRET_KEY_ANDA_DISINI"
      ```
   c. (Opsional) Setup Telegram bot:
      - Buat bot di @BotFather di Telegram
      - Dapatkan token bot
      - Mulai chat dengan bot dan dapatkan chat ID
      - Isi di config:
        ```yaml
        telegram_token: "BOT_TOKEN_ANDA"
        telegram_chat_id: "CHAT_ID_ANDA"
        ```

4. Pengaturan Keamanan API (PENTING):
   a. Aktifkan 2FA di akun Binance anda
   
   b. Pengaturan IP:
      Untuk Data Seluler/IP Dinamis:
      - TIDAK PERLU membatasi IP jika menggunakan data seluler
      - IP data seluler berubah-ubah, sulit untuk diwhitelist
      - Sebagai gantinya, tingkatkan keamanan dengan:
        * Aktifkan notifikasi email untuk aktivitas API
        * Monitor transaksi secara regular
        * Set limit trading yang aman
        * Gunakan IP whitelist hanya saat menggunakan WiFi tetap
      
      Untuk IP Statis (WiFi Tetap):
      - Cek IP anda di: https://www.whatismyip.com
      - Catat IP publik yang muncul
      - Masukkan IP tersebut ke whitelist di Binance
      - Perbarui jika IP berubah
   
   c. Hanya berikan izin untuk:
      - Futures Trading
      - Membaca informasi akun
      - JANGAN berikan izin withdrawal
   
   d. Simpan API Key dan Secret dengan aman
   
   e. Pengamanan Tambahan:
      - Set limit trading harian yang aman
      - Aktifkan notifikasi email untuk semua aktivitas API
      - Periksa aktivitas API minimal sekali sehari
      - Segera nonaktifkan API jika mencurigakan
      - Backup API key dan secret dengan aman
      - Jangan share API key dengan siapapun

5. Jalankan bot:
   ```bash
   python run.py
   ```
   
6. Mode Testing (WAJIB untuk Pemula):
   a. Buat akun Binance Futures Testnet
   b. Dapatkan API testnet dari: https://testnet.binancefuture.com
   c. Gunakan API testnet di config untuk testing
   d. Set `mode.live: false` di config.yaml
   
7. Memantau Bot Trading:
   a. Monitor via Telegram:
      - Semua sinyal trading
      - Status posisi terbuka
      - Alert profit/loss
      - Notifikasi error
   
   b. Monitor via Terminal:
      - Display real-time chart
      - Status indikator teknikal
      - Confidence level ML
      - Performa trading
   
   c. Statistik Trading:
      - Win rate harian/mingguan
      - Profit/loss total
      - Rata-rata profit per trade
      - Drawdown maksimal
   
   d. Keamanan:
      - Auto-shutdown saat loss limit tercapai
      - Alert saat deviation terdeteksi
      - Monitoring error dan anomali
      - Backup sistem otomatis

## Sistem Eksekusi Otomatis

1. **Proses Deteksi dan Eksekusi**
   a. Scanning Market:
      - Memindai market setiap detik
      - Analisa real-time semua timeframe
      - Deteksi setup yang memenuhi kriteria
   
   b. Verifikasi Sinyal:
      - Minimal 80% confidence dari ML
      - Konfirmasi dari minimal 3 timeframe
      - Validasi volume dan volatilitas
      - Cek kondisi market (trending/sideways)
   
   c. Proses Eksekusi:
      - Entry otomatis saat semua kriteria terpenuhi
      - Penempatan stop loss otomatis
      - Setting take profit bertingkat
      - Aktivasi trailing stop
   
   d. Manajemen Posisi:
      - Monitoring posisi 24/7
      - Penyesuaian stop loss otomatis
      - Take profit parsial otomatis
      - DCA otomatis jika diaktifkan

2. **Sistem Kill-Switch Otomatis**
   - Stop trading jika loss harian tercapai
   - Stop saat free margin di bawah batas
   - Tutup posisi jika error terdeteksi
   - Cancel semua order saat market volatile

3. **Notifikasi Real-time**
   Anda akan mendapat notifikasi Telegram untuk:
   - Sinyal terdeteksi
   - Order dieksekusi
   - Take profit hit
   - Stop loss hit
   - Perubahan posisi
   - Warning dan error

4. **Kontrol Manual (Override)**
   Bot tetap bisa dikontrol manual untuk:
   - Stop trading sementara
   - Tutup semua posisi
   - Batalkan semua order
   - Ubah parameter trading
   - Emergency stop

## Cara Kerja Bot

1. **Analisis Multi-Timeframe**
   - Menganalisa chart BNBUSDT dalam 4 timeframe (1m, 5m, 15m, 1h)
   - Menghitung indikator teknikal untuk setiap timeframe
   - Melakukan konfirmasi trend dari berbagai timeframe
   - Memberikan bobot berbeda untuk setiap timeframe

2. **Sistem Machine Learning**
   - Menggunakan ensemble Random Forest dan Gradient Boosting
   - Mempelajari pola dari data historis
   - Fitur yang dianalisa:
     * Indikator teknikal (RSI, MACD, BB, dll)
     * Volume profile
     * Price action patterns
     * Market regime detection
   - Melakukan retraining otomatis setiap 24 jam

3. **Sistem Pengambilan Keputusan**
   a. Analisa Market Regime:
      - Mengklasifikasi kondisi market (trending/sideways)
      - Mengukur volatilitas market
      - Mendeteksi momentum
   
   b. Konfirmasi Sinyal:
      - Analisa trend multi-timeframe
      - Konfirmasi volume
      - Divergence RSI
      - Support/Resistance
   
   c. Machine Learning Prediction:
      - Prediksi arah market
      - Kalkulasi confidence level
      - Minimum confidence: 70%

4. **Manajemen Risiko**
   a. Position Sizing:
      - Maksimal risiko 2% per trade
      - Ukuran posisi disesuaikan dengan volatilitas
      - Multiple take profit levels
   
   b. Stop Loss Dinamis:
      - Base stop loss: 1.5%
      - Trailing stop setelah profit 1%
      - Penyesuaian berdasarkan ATR
   
   c. Take Profit Bertingkat:
      - Level 1: 1.5% (30% posisi)
      - Level 2: 2.5% (30% posisi)
      - Level 3: 4.0% (40% posisi)

5. **Money Management**
   - Maksimal loss harian: 5%
   - Maksimal loss mingguan: 15%
   - Minimal free margin: 50%
   - Maksimal 3 posisi terbuka
   - DCA pada -1% dan -2%

6. **Sistem Monitoring**
   - Real-time position tracking
   - Notifikasi Telegram untuk:
     * Entry/Exit signals
     * Take profit hits
     * Stop loss hits
     * Error warnings
   - Logging semua aktivitas
   - Statistik performa real-time

7. **Batasan dan Filter**
   - Minimum volume 24h: 1M USDT
   - Maksimal spread: 0.1%
   - Minimum risk:reward ratio: 1.5
   - Batasan volatilitas
   - Market regime filtering

## Fitur Utama

- Machine Learning untuk prediksi
- Multi-timeframe analysis
- Manajemen risiko canggih
- Notifikasi Telegram
- Interface yang mudah digunakan
- Bahasa Indonesia

## Peringatan

- Selalu test di testnet terlebih dahulu
- Mulai dengan modal kecil
- Monitor performa bot secara regular
- Pahami risiko trading futures

## Support

Jika ada pertanyaan atau masalah, silakan buat issue di repository ini.

