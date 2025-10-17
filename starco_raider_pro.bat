@echo off
title STARCO DISCORD RAIDER
color 0B

echo.
echo.
echo                           STARCO DISCORD RAIDER
echo.
echo                                    YUSUF INC.
echo.
echo ================================================================================
echo                           STARCO DISCORD RAIDER INSTALLER
echo ================================================================================
echo.

echo [INFO] Python kontrol ediliyor...
python --version
if errorlevel 1 (
    echo [ERROR] Python bulunamadi! Lutfen Python yukleyin.
    pause
    exit
)

echo [OK] Python bulundu!
echo.

echo [INFO] Paketler yukleniyor...
pip install requests colorama
echo.

echo [INFO] Dosyalar kontrol ediliyor...
if not exist "starco_launcher.py" (
    echo [ERROR] starco_launcher.py bulunamadi!
    pause
    exit
)

if not exist "tokens.txt" (
    echo [INFO] tokens.txt olusturuluyor...
    echo # Discord Token'lari > tokens.txt
    echo # Her satira bir token yazin >> tokens.txt
    echo. >> tokens.txt
)

echo [OK] Tum dosyalar hazir!
echo.
echo [INFO] Program baslatiliyor...
echo.
pause

python starco_launcher.py

echo.
echo [INFO] Program kapatildi.
pause