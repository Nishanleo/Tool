import os
import sys
import time
from colorama import Fore, init, Style
from discord_raider import DiscordRaider

init(autoreset=True)

class StarcoRaider:
    def __init__(self):
        self.banner_art = r'''



                          _____ __                             ____  _____     
                         / ___// / _____ _______________      / __ \/ ___/  __ 
                         \__ \/  __/ __ `/ ___/ ___/ __ \    / /_/ /\__ \__/ /_
                         ___/ / /_/ /_/ / /  / /__/ /_/ /   / _, _/___/ /_  __/
                        /____/\__/\__,_/_/   \___/\____/   /_/ |_|/____/ /_/                                         
'''
        self.home_art = r'''                                                                                         YUSUF INC.
                    
                     [01] Settings  

                     [02] Raider                              [04] Tools
                    
                     [03] Webhooks                            [05] Exit
                    
                                                           
'''
        self.raider_art = r'''



                           _____ __                             ____  _____     
                          / ___// / _____ _______________      / __ \/ ___/  __ 
                          \__ \/ __ / __ `/ ___/ ___/ __ \    / /_/ /\__ \__/ /_
                          ___/ / /_/ /_/ / /  / /__/ /_/ /   / _, _/___/ /_  __/
                         /____/\__/\__,_/_/   \___/\____/   /_/ |_|/____/ /_/                                         
                                  
                                          
                        
                    RAIDER KONTROLLERI:
                    
                    
                    [01] Back
                    
                    [02] Single Raid                          [03] Multi Paralel Spam
                    
                    [04] Exit
                    

'''
        self.raider = DiscordRaider()
        self.setup()

    def setup(self):
        os.system('cls')
        self.homemenu()

    def banner(self):
        print(Fore.CYAN + self.banner_art + Fore.RESET)
    
    def homemenu(self):
        while True:
            os.system('title STARCO DISCORD RAIDER')
            os.system('cls')
            self.banner()
            print(Fore.CYAN + self.home_art + Fore.RESET)
            inp = input(Fore.CYAN + "[starco@MENU] > " + Fore.RESET)

            if inp == "1":
                self.settingsmenu()
            elif inp == "2":
                self.raidermenu()
            elif inp == "3":
                self.webhooksmenu()
            elif inp == "4":
                self.toolsmenu()
            elif inp == "5":
                self.exit_program()
            else:
                print(Fore.CYAN + "[-] Gecersiz secim, tekrar deneyin!" + Fore.RESET)
                time.sleep(1)

    def settingsmenu(self):
        while True:
            os.system('title STARCO@SETTINGS')
            os.system('cls')
            settings_art = r'''



                             _____ __                             ____  _____     
                            / ___// /_____ _______________       / __ \/ ___/  __ 
                            \__ \/ __/ __ `/ ___/ ___/ __ \     / /_/ /\__ \__/ /_
                           ___/ / /_/ /_/ / /  / /__/ /_/ /    / _, _/___/ /_  __/
                          /____/\__/\__,_/_/   \___/\____/    /_/ |_|/____/ /_/                                         
                                  
                                          
                        
                    SETTINGS KONTROLLERI:
                    
                    
                    [01] Back
                    
                    [02] Token Check                          [03] Token List
                    
                    [04] Install Packages                     [05] System Info
                    
                    [06] Exit
                    

'''
            print(Fore.CYAN + settings_art + Fore.RESET)
            inp = input(Fore.CYAN + "[starco@SETTINGS] > " + Fore.RESET)

            if inp == "1":
                self.homemenu()
            elif inp == "2":
                self.token_check()
            elif inp == "3":
                self.token_list()
            elif inp == "4":
                self.install_packages()
            elif inp == "5":
                self.system_info()
            elif inp == "6":
                self.exit_program()
            else:
                print(Fore.CYAN + "[-] Gecersiz secim, tekrar deneyin!" + Fore.RESET)
                time.sleep(1)

    def raidermenu(self):
        while True:
            os.system('title STARCO@RAIDER')
            os.system('cls')
            print(Fore.CYAN + self.raider_art + Fore.RESET)
            inp = input(Fore.CYAN + "[starco@RAIDER] > " + Fore.RESET)

            if inp == "1":
                self.homemenu()
            elif inp == "2":
                self.single_raid()
            elif inp == "3":
                self.multi_parallel_spam()
            elif inp == "4":
                self.exit_program()
            else:
                print(Fore.CYAN + "[-] Gecersiz secim, tekrar deneyin!" + Fore.RESET)
                time.sleep(1)

    def webhooksmenu(self):
        while True:
            os.system('title STARCO@WEBHOOKS')
            os.system('cls')
            webhooks_art = r'''



                             _____ __                             ____  _____     
                            / ___// /_____ _______________       / __ \/ ___/  __ 
                            \__ \/ __/ __ `/ ___/ ___/ __ \     / /_/ /\__ \__/ /_
                           ___/ / /_/ /_/ / /  / /__/ /_/ /    / _, _/___/ /_  __/
                          /____/\__/\__,_/_/   \___/\____/    /_/ |_|/____/ /_/                                         
                                  
                                          
                        
                    WEBHOOKS KONTROLLERI:
                    
                    
                    [01] Back
                    
                    [02] Webhook Spam                          [03] Webhook Delete
                    
                    [04] Webhook Create
                    
                    [05] Exit
                    

'''
            print(Fore.CYAN + webhooks_art + Fore.RESET)
            inp = input(Fore.CYAN + "[starco@WEBHOOKS] > " + Fore.RESET)

            if inp == "1":
                self.homemenu()
            elif inp == "2":
                print(Fore.YELLOW + "[INFO] Webhook spam ozelligi gelistiriliyor..." + Fore.RESET)
                input("Devam etmek icin Enter'a basin...")
            elif inp == "3":
                print(Fore.YELLOW + "[INFO] Webhook delete ozelligi gelistiriliyor..." + Fore.RESET)
                input("Devam etmek icin Enter'a basin...")
            elif inp == "4":
                print(Fore.YELLOW + "[INFO] Webhook create ozelligi gelistiriliyor..." + Fore.RESET)
                input("Devam etmek icin Enter'a basin...")
            elif inp == "5":
                self.exit_program()
            else:
                print(Fore.CYAN + "[-] Gecersiz secim, tekrar deneyin!" + Fore.RESET)
                time.sleep(1)

    def toolsmenu(self):
        while True:
            os.system('title STARCO@TOOLS')
            os.system('cls')
            tools_art = r'''



                          _____ __                             ____  _____     
                         / ___// /_____ _______________       / __ \/ ___/  __ 
                         \__ \/ __/ __ `/ ___/ ___/ __ \     / /_/ /\__ \__/ /_
                        ___/ / /_/ /_/ / /  / /__/ /_/ /    / _, _/___/ /_  __/
                       /____/\__/\__,_/_/   \___/\____/    /_/ |_|/____/ /_/                                         
                                  
                                          
                        
                    TOOLS KONTROLLERI:
                    
                    
                    [01] Back
                    
                    [02] Token Checker                         [03] Server Info
                    
                    [04] Channel Info
                    
                    [05] Exit
                    

'''
            print(Fore.CYAN + tools_art + Fore.RESET)
            inp = input(Fore.CYAN + "[starco@TOOLS] > " + Fore.RESET)

            if inp == "1":
                self.homemenu()
            elif inp == "2":
                self.token_check()
            elif inp == "3":
                print(Fore.YELLOW + "[INFO] Server info ozelligi gelistiriliyor..." + Fore.RESET)
                input("Devam etmek icin Enter'a basin...")
            elif inp == "4":
                print(Fore.YELLOW + "[INFO] Channel info ozelligi gelistiriliyor..." + Fore.RESET)
                input("Devam etmek icin Enter'a basin...")
            elif inp == "5":
                self.exit_program()
            else:
                print(Fore.CYAN + "[-] Gecersiz secim, tekrar deneyin!" + Fore.RESET)
                time.sleep(1)

    def single_raid(self):
        os.system('cls')
        print(Fore.RED + "[INFO] Single Raid baslatiliyor..." + Fore.RESET)
        
        print(Fore.YELLOW + "[INFO] Tokenler otomatik yukleniyor..." + Fore.RESET)
        self.raider.load_tokens_from_file("tokens.txt")
        
        if not self.raider.tokens:
            print(Fore.RED + "[ERROR] tokens.txt dosyasinda token bulunamadi!" + Fore.RESET)
            print(Fore.YELLOW + "[INFO] tokens.txt dosyasina token ekleyin." + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + f"[OK] {len(self.raider.tokens)} token yuklendi!" + Fore.RESET)
        
        print(Fore.YELLOW + "[INFO] Rastgele token ile giris yapiliyor..." + Fore.RESET)
        random_token = self.raider.get_random_token()
        if not self.raider.login(random_token):
            print(Fore.RED + "[ERROR] Giris basarisiz!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + "[OK] Giris basarili!" + Fore.RESET)
        
        self.spam_single_server()
        
    def spam_single_server(self):
        """Tek sunucuya spam gönder"""
        print(Fore.CYAN + "\n[+] Tek sunucuya spam gonder:" + Fore.RESET)
        
        guilds = self.raider.list_servers()
        if not guilds:
            print(Fore.RED + "[ERROR] Hic sunucu bulunamadi!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + f"[OK] {len(guilds)} sunucu bulundu!" + Fore.RESET)
        
        try:
            choice = int(input(Fore.CYAN + "\nSunucu secin (numara): " + Fore.RESET).strip())
            if 1 <= choice <= len(guilds):
                selected_guild = guilds[choice-1]
                print(Fore.GREEN + f"[INFO] Secilen sunucu: {selected_guild['name']}" + Fore.RESET)
                
                message = input(Fore.CYAN + "Spam mesajini girin: " + Fore.RESET).strip()
                if not message:
                    print(Fore.RED + "[ERROR] Mesaj bos olamaz!" + Fore.RESET)
                    input("Devam etmek icin Enter'a basin...")
                    return
                
                try:
                    delay = float(input(Fore.CYAN + "Delay (saniye, varsayilan: 1): " + Fore.RESET).strip() or "1")
                except ValueError:
                    delay = 1.0
                
                print(Fore.GREEN + f"[OK] Spam baslatiliyor..." + Fore.RESET)
                print(Fore.YELLOW + "[WARNING] Ctrl+C ile durdurabilirsiniz!" + Fore.RESET)
                
                try:
                    success = self.raider.spam_to_server(selected_guild['id'], message, delay)
                    if success:
                        print(Fore.GREEN + "[OK] Spam tamamlandi!" + Fore.RESET)
                    else:
                        print(Fore.RED + "[ERROR] Spam basarisiz!" + Fore.RESET)
                except KeyboardInterrupt:
                    print(Fore.YELLOW + "\n[INFO] Spam durduruldu!" + Fore.RESET)
                except Exception as e:
                    print(Fore.RED + f"[ERROR] Hata: {e}" + Fore.RESET)
                    
            else:
                print(Fore.RED + "[ERROR] Gecersiz secim!" + Fore.RESET)
                
        except ValueError:
            print(Fore.RED + "[ERROR] Gecersiz numara!" + Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"[ERROR] Hata: {e}" + Fore.RESET)
            
        input("Devam etmek icin Enter'a basin...")

    def multi_parallel_spam(self):
        os.system('cls')
        print(Fore.RED + "[INFO] Multi Paralel Spam baslatiliyor..." + Fore.RESET)
        
        print(Fore.YELLOW + "[INFO] Tokenler otomatik yukleniyor..." + Fore.RESET)
        self.raider.load_tokens_from_file("tokens.txt")
        
        if not self.raider.tokens:
            print(Fore.RED + "[ERROR] tokens.txt dosyasinda token bulunamadi!" + Fore.RESET)
            print(Fore.YELLOW + "[INFO] tokens.txt dosyasina token ekleyin." + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + f"[OK] {len(self.raider.tokens)} token yuklendi!" + Fore.RESET)
        
        print(Fore.CYAN + "\n[+] Kanal ID'lerini girin (virgul ile ayirin):" + Fore.RESET)
        channel_input = input("Kanal ID'leri: ").strip()
        
        if not channel_input:
            print(Fore.RED + "[ERROR] Kanal ID'leri bos olamaz!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        channel_ids = [cid.strip() for cid in channel_input.split(',')]
        print(Fore.GREEN + f"[OK] {len(channel_ids)} kanal ID'si alindi!" + Fore.RESET)
        
        print(Fore.CYAN + "\n[+] Spam mesajini girin:" + Fore.RESET)
        message = input("Mesaj: ").strip()
        
        if not message:
            print(Fore.RED + "[ERROR] Mesaj bos olamaz!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.CYAN + "\n[+] Delay ayarlari:" + Fore.RESET)
        try:
            delay = float(input("Kanal arasi delay (saniye, varsayilan: 1): ").strip() or "1")
            loop_delay = float(input("Loop arasi delay (saniye, varsayilan: 5): ").strip() or "5")
        except ValueError:
            print(Fore.RED + "[ERROR] Gecersiz delay degeri!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + f"[OK] Multi Paralel Spam baslatiliyor..." + Fore.RESET)
        print(Fore.YELLOW + f"[INFO] {len(self.raider.tokens)} token, {len(channel_ids)} kanal" + Fore.RESET)
        print(Fore.YELLOW + "[WARNING] Ctrl+C ile durdurabilirsiniz!" + Fore.RESET)
        
        try:
            success = self.raider.parallel_token_spam(channel_ids, message, delay, loop_delay)
            if success:
                print(Fore.GREEN + "[OK] Multi Paralel Spam tamamlandi!" + Fore.RESET)
            else:
                print(Fore.RED + "[ERROR] Multi Paralel Spam basarisiz!" + Fore.RESET)
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[INFO] Multi Paralel Spam durduruldu!" + Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"[ERROR] Hata: {e}" + Fore.RESET)
        
        input("Devam etmek icin Enter'a basin...")

    def start_raider(self):
        os.system('cls')
        print(Fore.YELLOW + "[INFO] Discord Raider baslatiliyor..." + Fore.RESET)
        
        print(Fore.YELLOW + "[INFO] Python kontrol ediliyor..." + Fore.RESET)
        if sys.version_info < (3, 6):
            print(Fore.RED + "[ERROR] Python 3.6+ gerekli!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + f"[OK] Python {sys.version.split()[0]} bulundu!" + Fore.RESET)
        
        print(Fore.YELLOW + "[INFO] Paketler kontrol ediliyor..." + Fore.RESET)
        try:
            import requests
            print(Fore.GREEN + "[OK] requests paketi hazir!" + Fore.RESET)
        except ImportError:
            print(Fore.YELLOW + "[INFO] Paketler yukleniyor..." + Fore.RESET)
            os.system("pip install requests")
        
        if not self.raider.tokens:
            print(Fore.YELLOW + "[INFO] Token dosyasi yukleniyor..." + Fore.RESET)
            self.raider.load_tokens_from_file("tokens.txt")
        
        if not self.raider.tokens:
            print(Fore.RED + "[ERROR] Token bulunamadi! tokens.txt dosyasina token ekleyin." + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        print(Fore.GREEN + f"[OK] {len(self.raider.tokens)} token bulundu!" + Fore.RESET)
        print(Fore.GREEN + "[OK] Discord Raider baslatiliyor..." + Fore.RESET)
        print(Fore.CYAN + "[INFO] Ctrl+C ile durdurabilirsiniz..." + Fore.RESET)
        print()
        
        try:
            from main import CMDInterface
            interface = CMDInterface()
            interface.run()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[INFO] Discord Raider durduruldu!" + Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"[ERROR] Hata: {e}" + Fore.RESET)
        
        input("Devam etmek icin Enter'a basin...")

    def quick_start(self):
        os.system('cls')
        self.banner()
        print(Fore.YELLOW + "[INFO] Hizli baslatma..." + Fore.RESET)
        
        if sys.version_info < (3, 6):
            print(Fore.RED + "[ERROR] Python 3.6+ gerekli!" + Fore.RESET)
            input("Devam etmek icin Enter'a basin...")
            return
        
        try:
            import requests
        except ImportError:
            print(Fore.YELLOW + "[INFO] Paketler yukleniyor..." + Fore.RESET)
            os.system("pip install requests")
        
        if not os.path.exists("tokens.txt"):
            print(Fore.YELLOW + "[INFO] tokens.txt olusturuluyor..." + Fore.RESET)
            with open("tokens.txt", "w", encoding="utf-8") as f:
                f.write("# Discord Bot Token'lari\n")
                f.write("# Her satira bir token yazin\n")
                f.write("# # ile baslayan satirlar yorum olarak kabul edilir\n\n")
                f.write("# Token'larinizi buraya ekleyin:\n")
        
        print(Fore.GREEN + "[OK] Tum kontroller tamamlandi!" + Fore.RESET)
        print(Fore.GREEN + "[OK] Discord Raider baslatiliyor..." + Fore.RESET)
        
        try:
            from main import CMDInterface
            interface = CMDInterface()
            interface.run()
        except KeyboardInterrupt:
            print(Fore.YELLOW + "\n[INFO] Discord Raider durduruldu!" + Fore.RESET)
        except Exception as e:
            print(Fore.RED + f"[ERROR] Hata: {e}" + Fore.RESET)
        
        input("Devam etmek icin Enter'a basin...")

    def token_check(self):
        os.system('cls')
        print(Fore.YELLOW + "[INFO] Token kontrol ediliyor..." + Fore.RESET)
        
        if not os.path.exists("tokens.txt"):
            print(Fore.RED + "[ERROR] tokens.txt dosyasi bulunamadi!" + Fore.RESET)
            print(Fore.YELLOW + "[INFO] Ornek dosya olusturuluyor..." + Fore.RESET)
            with open("tokens.txt", "w", encoding="utf-8") as f:
                f.write("# Discord Bot Token'lari\n")
                f.write("# Her satira bir token yazin\n")
                f.write("# # ile baslayan satirlar yorum olarak kabul edilir\n\n")
                f.write("# Token'larinizi buraya ekleyin:\n")
            print(Fore.GREEN + "[OK] tokens.txt dosyasi olusturuldu!" + Fore.RESET)
        else:
            print(Fore.GREEN + "[OK] tokens.txt dosyasi bulundu!" + Fore.RESET)
        
        self.raider.load_tokens_from_file("tokens.txt")
        token_count = len(self.raider.tokens)
        
        if token_count == 0:
            print(Fore.YELLOW + "[WARNING] Hic token bulunamadi!" + Fore.RESET)
            print(Fore.YELLOW + "[INFO] tokens.txt dosyasina token ekleyin." + Fore.RESET)
        else:
            print(Fore.GREEN + f"[OK] {token_count} token bulundu!" + Fore.RESET)
        
        print()
        print(Fore.CYAN + "[INFO] Token dosyasi icerigi:" + Fore.RESET)
        print("=" * 50)
        if os.path.exists("tokens.txt"):
            with open("tokens.txt", "r", encoding="utf-8") as f:
                print(f.read())
        print("=" * 50)
        
        input("Devam etmek icin Enter'a basin...")

    def token_list(self):
        os.system('cls')
        print(Fore.YELLOW + "[INFO] Token listesi:" + Fore.RESET)
        
        if os.path.exists("tokens.txt"):
            self.raider.load_tokens_from_file("tokens.txt")
            if self.raider.tokens:
                print("=" * 50)
                for i, token in enumerate(self.raider.tokens, 1):
                    masked_token = token[:10] + "..." + token[-10:] if len(token) > 20 else token
                    print(f"{i}. {masked_token}")
                print("=" * 50)
            else:
                print(Fore.YELLOW + "[WARNING] Hic token bulunamadi!" + Fore.RESET)
        else:
            print(Fore.RED + "[ERROR] tokens.txt dosyasi bulunamadi!" + Fore.RESET)
        
        input("Devam etmek icin Enter'a basin...")

    def install_packages(self):
        os.system('cls')
        print(Fore.YELLOW + "[INFO] Paketler yukleniyor..." + Fore.RESET)
        
        if not os.path.exists("requirements.txt"):
            print(Fore.YELLOW + "[INFO] requirements.txt olusturuluyor..." + Fore.RESET)
            with open("requirements.txt", "w", encoding="utf-8") as f:
                f.write("requests>=2.31.0\n")
                f.write("asyncio\n")
            print(Fore.GREEN + "[OK] requirements.txt olusturuldu!" + Fore.RESET)
        
        print(Fore.YELLOW + "[INFO] Paketler yukleniyor..." + Fore.RESET)
        result = os.system("pip install -r requirements.txt")
        
        if result == 0:
            print(Fore.GREEN + "[OK] Paketler basariyla yuklendi!" + Fore.RESET)
        else:
            print(Fore.RED + "[ERROR] Paket yukleme basarisiz!" + Fore.RESET)
            print(Fore.YELLOW + "[INFO] Manuel yukleme deneniyor..." + Fore.RESET)
            os.system("pip install requests")
        
        input("Devam etmek icin Enter'a basin...")

    def system_info(self):
        os.system('cls')
        print(Fore.YELLOW + "[INFO] Sistem bilgileri toplaniyor..." + Fore.RESET)
        print()
        
        print("=" * 50)
        print(Fore.CYAN + "PYTHON BILGILERI:" + Fore.RESET)
        print("=" * 50)
        print(f"Python Version: {sys.version}")
        print(f"Python Path: {sys.executable}")
        print()
        
        print("=" * 50)
        print(Fore.CYAN + "PAKET BILGILERI:" + Fore.RESET)
        print("=" * 50)
        try:
            import requests
            print(Fore.GREEN + "[OK] requests paketi yuklu" + Fore.RESET)
        except ImportError:
            print(Fore.RED + "[ERROR] requests paketi yuklu degil" + Fore.RESET)
        
        try:
            import asyncio
            print(Fore.GREEN + "[OK] asyncio paketi yuklu" + Fore.RESET)
        except ImportError:
            print(Fore.RED + "[ERROR] asyncio paketi yuklu degil" + Fore.RESET)
        print()
        
        print("=" * 50)
        print(Fore.CYAN + "DOSYA BILGILERI:" + Fore.RESET)
        print("=" * 50)
        files = ["main.py", "discord_raider.py", "requirements.txt", "tokens.txt"]
        for file in files:
            if os.path.exists(file):
                print(Fore.GREEN + f"[OK] {file} bulundu" + Fore.RESET)
            else:
                print(Fore.RED + f"[ERROR] {file} bulunamadi" + Fore.RESET)
        
        input("Devam etmek icin Enter'a basin...")

    def exit_program(self):
        os.system('cls')
        print(Fore.YELLOW + "[INFO] Starco Discord Raider kapatiliyor..." + Fore.RESET)
        print(Fore.GREEN + "[INFO] Tesekkurler!" + Fore.RESET)
        print(Fore.GREEN + "[INFO] Ogrenme amacli kullandiginiz icin tesekkurler!" + Fore.RESET)
        print()
        time.sleep(2)
        sys.exit(0)

if __name__ == "__main__":
    try:
        starco = StarcoRaider()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n[INFO] Program durduruldu!" + Fore.RESET)
        sys.exit(0)
    except Exception as e:
        print(Fore.RED + f"[ERROR] Hata: {e}" + Fore.RESET)
        input("Devam etmek icin Enter'a basin...")
