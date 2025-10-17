import requests
import asyncio
import json
import os
import random
import time
import threading
from datetime import datetime

class DiscordRaider:
    def __init__(self):
        self.session = requests.Session()
        self.token = None
        self.guild_id = None
        self.tokens = []
        self.current_token_index = 0
        self.user_info = None
        
     
        self.base_url = "https://discord.com/api/v9"
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Europe/Istanbul',
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwLjAuMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNzQ0NzMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
        })
        
    def load_tokens_from_file(self, filename="tokens.txt"):
        try:
            if not os.path.exists(filename):
                print(f"[ERROR] {filename} dosyasi bulunamadi!")
                return False
                
            with open(filename, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
            self.tokens = []
            for line in lines:
                token = line.strip()
                    self.tokens.append(token)
                    
            if self.tokens:
                print(f"[OK] {len(self.tokens)} token yuklendi!")
                return True
            else:
                print("[ERROR] Gecerli token bulunamadi!")
                return False
                
        except Exception as e:
            print(f"[ERROR] Token dosyasi okuma hatasi: {e}")
            return False
            
    def get_random_token(self):
        if not self.tokens:
            return None
        return random.choice(self.tokens)
        
    def get_next_token(self):
        if not self.tokens:
            return None
        token = self.tokens[self.current_token_index]
        self.current_token_index = (self.current_token_index + 1) % len(self.tokens)
        return token
        
    def list_tokens(self):
        if not self.tokens:
            print("[ERROR] Hic token yuklenmemis!")
            return
            
        print(f"\n[INFO] Yuklenen Token'lar ({len(self.tokens)} adet):")
        for i, token in enumerate(self.tokens, 1):
            masked_token = token[:10] + "..." + token[-10:] if len(token) > 20 else token[:10] + "..."
            print(f"{i}. {masked_token}")
        
    def login(self, token):
        try:
            self.token = token
            self.session.headers.update({
                'Authorization': token,
                'Content-Type': 'application/json'
            })
            
            response = self.session.get(f"{self.base_url}/users/@me")
            
            if response.status_code == 200:
                self.user_info = response.json()
                print(f"[OK] Giris yapildi: {self.user_info['username']}#{self.user_info['discriminator']}")
                return True
            else:
                print(f"[ERROR] Giris basarisiz! Status: {response.status_code}")
                if response.status_code == 401:
                    print("[ERROR] Gecersiz token!")
                return False
                
        except Exception as e:
            print(f"[ERROR] Giris hatasi: {e}")
            return False
            
    def join_server(self, invite_url):
        try:
            if 'discord.gg/' in invite_url:
                invite_code = invite_url.split('discord.gg/')[-1]
            elif 'discord.com/invite/' in invite_url:
                invite_code = invite_url.split('discord.com/invite/')[-1]
            else:
                invite_code = invite_url.split('/')[-1]
            
            invite_code = invite_code.split('?')[0].split('#')[0]
            
            print(f"[INFO] Invite kodu: {invite_code}")
            
            invite_info_response = self.session.get(f"{self.base_url}/invites/{invite_code}")
            
            if invite_info_response.status_code != 200:
                print(f"[ERROR] Invite bilgisi alinamadi! Status: {invite_info_response.status_code}")
                print(f"[ERROR] Response: {invite_info_response.text}")
                return False
            
            invite_info = invite_info_response.json()
            print(f"[INFO] Sunucu: {invite_info['guild']['name']}")
            
            methods = [
                {"url": f"{self.base_url}/invites/{invite_code}", "data": None},
                {"url": f"{self.base_url}/invites/{invite_code}", "data": {"session_id": None}},
                {"url": f"{self.base_url}/invites/{invite_code}?with_counts=true&with_expiration=true", "data": None}
            ]
            
            for i, method in enumerate(methods, 1):
                print(f"[INFO] Yontem {i}: {method['url']}")
                
                if method['data']:
                    response = self.session.post(method['url'], json=method['data'])
                else:
                    response = self.session.post(method['url'])
                
                print(f"[INFO] Status: {response.status_code}")
                print(f"[INFO] Response: {response.text[:200]}...")
                
                if response.status_code == 200:
                    guild_info = response.json()
                    print(f"[OK] Sunucuya katildi: {guild_info['guild']['name']}")
                    return True
                elif response.status_code == 400:
                    print(f"[WARNING] 400 hatasi - baska yontem deneniyor...")
                    continue
                else:
                    print(f"[ERROR] Sunucuya katilma hatasi! Status: {response.status_code}")
                    
                    if response.status_code == 403:
                        print("[ERROR] Bu sunucuya katilma yetkiniz yok!")
                    elif response.status_code == 404:
                        print("[ERROR] Gecersiz invite linki!")
                    elif response.status_code == 429:
                        print("[ERROR] Rate limit! Biraz bekleyin.")
                        
                    return False
            
            print("[ERROR] Tum yontemler basarisiz!")
            return False
                
        except Exception as e:
            print(f"[ERROR] Sunucuya katilma hatasi: {e}")
            return False
            
    def get_server_info(self, guild_id):
        try:
            response = self.session.get(f"{self.base_url}/guilds/{guild_id}")
            
            if response.status_code == 200:
                guild_info = response.json()
                print(f"\n[INFO] Sunucu Bilgileri:")
                print(f"Isim: {guild_info['name']}")
                print(f"ID: {guild_info['id']}")
                print(f"Uye sayisi: {guild_info.get('member_count', 'Bilinmiyor')}")
                print(f"Kanal sayisi: {len(guild_info.get('channels', []))}")
                print(f"Rol sayisi: {len(guild_info.get('roles', []))}")
                return guild_info
            else:
                print(f"[ERROR] Sunucu bilgisi alma hatasi! Status: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"[ERROR] Sunucu bilgisi alma hatasi: {e}")
            return None
            
    def send_message_to_channel(self, channel_id, message):
        try:
            data = {
                "content": message
            }
            
            response = self.session.post(f"{self.base_url}/channels/{channel_id}/messages", json=data)
            
            if response.status_code == 200:
                print(f"[OK] Mesaj gonderildi!")
                return True
            else:
                print(f"[ERROR] Mesaj gonderme hatasi! Status: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"[ERROR] Mesaj gonderme hatasi: {e}")
            return False
            
    def create_channels(self, guild_id, channel_name, count=1):
        try:
            created_channels = 0
            
            for i in range(count):
                data = {
                    "name": f"{channel_name}-{i+1}",
                    "type": 0  # Text channel
                }
                
                response = self.session.post(f"{self.base_url}/guilds/{guild_id}/channels", json=data)
                
                if response.status_code == 201:
                    created_channels += 1
                else:
                    print(f"[ERROR] Kanal olusturma hatasi! Status: {response.status_code}")
                    
            if created_channels > 0:
                print(f"[OK] {created_channels} kanal olusturuldu: {channel_name}")
                return True
            else:
                print("[ERROR] Hic kanal olusturulamadi!")
                return False
                
        except Exception as e:
            print(f"[ERROR] Kanal olusturma hatasi: {e}")
            return False
            
    def create_roles(self, guild_id, role_name, count=1):
        try:
            created_roles = 0
            
            for i in range(count):
                data = {
                    "name": f"{role_name}-{i+1}",
                    "color": 0
                }
                
                response = self.session.post(f"{self.base_url}/guilds/{guild_id}/roles", json=data)
                
                if response.status_code == 200:
                    created_roles += 1
                else:
                    print(f"[ERROR] Rol olusturma hatasi! Status: {response.status_code}")
                    
            if created_roles > 0:
                print(f"[OK] {created_roles} rol olusturuldu: {role_name}")
                return True
            else:
                print("[ERROR] Hic rol olusturulamadi!")
                return False
                
        except Exception as e:
            print(f"[ERROR] Rol olusturma hatasi: {e}")
            return False
            
    def list_servers(self):
        try:
            response = self.session.get(f"{self.base_url}/users/@me/guilds")
            
            if response.status_code == 200:
                guilds = response.json()
                print(f"\n[INFO] Sunucu Listesi ({len(guilds)} adet):")
                for i, guild in enumerate(guilds, 1):
                    print(f"{i}. {guild['name']} (ID: {guild['id']})")
                return guilds
            else:
                print(f"[ERROR] Sunucu listesi alma hatasi! Status: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"[ERROR] Sunucu listesi alma hatasi: {e}")
            return []
            
    def get_server_channels(self, guild_id):
        try:
            response = self.session.get(f"{self.base_url}/guilds/{guild_id}/channels")
            
            if response.status_code == 200:
                channels = response.json()
                return text_channels
            else:
                print(f"[ERROR] Kanal listesi alma hatasi! Status: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"[ERROR] Kanal listesi alma hatasi: {e}")
            return []
            
    def spam_to_server(self, guild_id, message, delay=1):
        try:
            channels = self.get_server_channels(guild_id)
            
            if not channels:
                print("[ERROR] Bu sunucuda text kanali bulunamadi!")
                return False
                
            print(f"[INFO] {len(channels)} kanala spam gonderiliyor...")
            success_count = 0
            
            for i, channel in enumerate(channels, 1):
                try:
                    print(f"[INFO] Kanal {i}/{len(channels)}: {channel['name']}")
                    
                    data = {
                        "content": message
                    }
                    
                    response = self.session.post(f"{self.base_url}/channels/{channel['id']}/messages", json=data)
                    
                    if response.status_code == 200:
                        success_count += 1
                        print(f"[OK] Mesaj gonderildi!")
                    elif response.status_code == 403:
                        print(f"[WARNING] Bu kanala mesaj gonderme yetkiniz yok!")
                    elif response.status_code == 429:
                        print(f"[WARNING] Rate limit! Bekleniyor...")
                        time.sleep(5)
                    else:
                        print(f"[ERROR] Mesaj gonderme hatasi! Status: {response.status_code}")
                    
                    if i < len(channels):
                        time.sleep(delay)
                        
                except Exception as e:
                    print(f"[ERROR] Kanal {channel['name']} hatasi: {e}")
                    continue
            
            print(f"[OK] {success_count}/{len(channels)} kanala spam gonderildi!")
            return success_count > 0
            
        except Exception as e:
            print(f"[ERROR] Spam gonderme hatasi: {e}")
            return False
            
    def spam_to_multiple_servers(self, guild_ids, message, delay=1):
        try:
            total_success = 0
            
            for i, guild_id in enumerate(guild_ids, 1):
                print(f"\n[INFO] Sunucu {i}/{len(guild_ids)}: {guild_id}")
                
                guild_response = self.session.get(f"{self.base_url}/guilds/{guild_id}")
                if guild_response.status_code == 200:
                    guild_info = guild_response.json()
                    print(f"[INFO] Sunucu: {guild_info['name']}")
                else:
                    print(f"[WARNING] Sunucu bilgisi alinamadi!")
                
                success = self.spam_to_server(guild_id, message, delay)
                if success:
                    total_success += 1
                
                if i < len(guild_ids):
                    time.sleep(2)
            
            print(f"\n[OK] Toplam {total_success}/{len(guild_ids)} sunucuya spam gonderildi!")
            return total_success > 0
            
        except Exception as e:
            print(f"[ERROR] Coklu spam gonderme hatasi: {e}")
            return False
            
    def multi_token_spam(self, guild_ids, message, delay=1, loop_count=None, loop_delay=5):
        try:
            if not self.tokens:
                print("[ERROR] Hic token yuklenmemis!")
                return False
                
            print(f"[INFO] {len(self.tokens)} token ile spam baslatiliyor...")
            print(f"[INFO] Hedef sunucu sayisi: {len(guild_ids)}")
            print(f"[INFO] Loop sayisi: {'Sonsuz' if loop_count is None else loop_count}")
            
            loop_counter = 0
            
            while True:
                loop_counter += 1
                print(f"\n{'='*50}")
                print(f"[INFO] LOOP {loop_counter} BASLADI")
                print(f"{'='*50}")
                
                for token_index, token in enumerate(self.tokens, 1):
                    print(f"\n[INFO] Token {token_index}/{len(self.tokens)} kullaniliyor...")
                    
                    if not self.login(token):
                        print(f"[ERROR] Token {token_index} ile giris basarisiz!")
                        continue
                    
                    for guild_id in guild_ids:
                        try:
                            guild_response = self.session.get(f"{self.base_url}/guilds/{guild_id}")
                            if guild_response.status_code == 200:
                                guild_info = guild_response.json()
                                print(f"[INFO] Spam gonderiliyor: {guild_info['name']}")
                            else:
                                print(f"[WARNING] Sunucu bilgisi alinamadi: {guild_id}")
                                continue
                            
                            success = self.spam_to_server(guild_id, message, delay)
                            
                            if success:
                                print(f"[OK] Token {token_index} - {guild_info['name']} basarili!")
                            else:
                                print(f"[ERROR] Token {token_index} - {guild_info['name']} basarisiz!")
                            
                            time.sleep(2)
                            
                        except Exception as e:
                            print(f"[ERROR] Token {token_index} - Sunucu {guild_id} hatasi: {e}")
                            continue
                    
                    if token_index < len(self.tokens):
                        print(f"[INFO] Sonraki token icin bekleniyor...")
                        time.sleep(3)
                
                print(f"\n[INFO] LOOP {loop_counter} TAMAMLANDI")
                
                if loop_count is not None and loop_counter >= loop_count:
                    print(f"[OK] Belirlenen loop sayisi ({loop_count}) tamamlandi!")
                    break
                
                if loop_count is None or loop_counter < loop_count:
                    print(f"[INFO] Sonraki loop icin {loop_delay} saniye bekleniyor...")
                    time.sleep(loop_delay)
            
            print(f"\n[OK] Multi-token spam tamamlandi!")
            return True
            
        except KeyboardInterrupt:
            print(f"\n[INFO] Spam durduruldu! (Ctrl+C)")
            return False
        except Exception as e:
            print(f"[ERROR] Multi-token spam hatasi: {e}")
            return False
            
    def continuous_spam(self, guild_ids, message, delay=1, loop_delay=5):
        return self.multi_token_spam(guild_ids, message, delay, None, loop_delay)
        
    def spam_to_specific_channels(self, channel_ids, message, delay=1):
        try:
            if not channel_ids:
                print("[ERROR] Kanal ID listesi bos!")
                return False
                
            print(f"[INFO] {len(channel_ids)} kanala spam gonderiliyor...")
            success_count = 0
            
            for i, channel_id in enumerate(channel_ids, 1):
                try:
                    print(f"[INFO] Kanal {i}/{len(channel_ids)}: {channel_id}")
                    
                    data = {
                        "content": message
                    }
                    
                    response = self.session.post(f"{self.base_url}/channels/{channel_id}/messages", json=data)
                    
                    if response.status_code == 200:
                        success_count += 1
                        print(f"[OK] Mesaj gonderildi!")
                    elif response.status_code == 403:
                        print(f"[WARNING] Bu kanala mesaj gonderme yetkiniz yok!")
                    elif response.status_code == 429:
                        print(f"[WARNING] Rate limit! Bekleniyor...")
                        time.sleep(5)
                    else:
                        print(f"[ERROR] Mesaj gonderme hatasi! Status: {response.status_code}")
                    
                    if i < len(channel_ids):
                        time.sleep(delay)
                        
                except Exception as e:
                    print(f"[ERROR] Kanal {channel_id} hatasi: {e}")
                    continue
            
            print(f"[OK] {success_count}/{len(channel_ids)} kanala spam gonderildi!")
            return success_count > 0
            
        except Exception as e:
            print(f"[ERROR] Kanal spam gonderme hatasi: {e}")
            return False
            
    def parallel_token_spam(self, channel_ids, message, delay=1, loop_delay=5):
        try:
            if not self.tokens:
                print("[ERROR] Hic token yuklenmemis!")
                return False
                
            print(f"[INFO] {len(self.tokens)} token paralel spam baslatiliyor...")
            print(f"[INFO] Hedef kanal sayisi: {len(channel_ids)}")
            print(f"[WARNING] Ctrl+C ile durdurabilirsiniz!")
            
            threads = []
            stop_event = threading.Event()
            
            def token_spam_worker(token, token_index):
                try:
                    session = requests.Session()
                    session.headers.update({
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                        'Accept': '*/*',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'DNT': '1',
                        'Connection': 'keep-alive',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-origin',
                        'X-Discord-Locale': 'en-US',
                        'X-Discord-Timezone': 'Europe/Istanbul',
                        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InRyIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTIwLjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwLjAuMCIsInJlZmVycmVyIjoiIiwicmVmZXJyaW5nX2RvbWFpbiI6IiIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyNzQ0NzMsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                        'Authorization': token,
                        'Content-Type': 'application/json'
                    })
                    
                    loop_counter = 0
                    
                    while not stop_event.is_set():
                        loop_counter += 1
                        print(f"[INFO] Token {token_index} - Loop {loop_counter} basladi")
                        
                        user_response = session.get(f"{self.base_url}/users/@me")
                        if user_response.status_code != 200:
                            print(f"[ERROR] Token {token_index} gecersiz!")
                            break
                        
                        for channel_id in channel_ids:
                            if stop_event.is_set():
                                break
                                
                            try:
                                data = {"content": message}
                                response = session.post(f"{self.base_url}/channels/{channel_id}/messages", json=data)
                                
                                if response.status_code == 200:
                                    print(f"[OK] Token {token_index} - Kanal {channel_id} basarili!")
                                elif response.status_code == 403:
                                    print(f"[WARNING] Token {token_index} - Kanal {channel_id} yetki yok!")
                                elif response.status_code == 429:
                                    print(f"[WARNING] Token {token_index} - Rate limit!")
                                    time.sleep(5)
                                else:
                                    print(f"[ERROR] Token {token_index} - Kanal {channel_id} hata: {response.status_code}")
                                
                                if not stop_event.is_set():
                                    time.sleep(delay)
                                    
                            except Exception as e:
                                print(f"[ERROR] Token {token_index} - Kanal {channel_id} exception: {e}")
                                continue
                        
                        if not stop_event.is_set():
                            print(f"[INFO] Token {token_index} - Loop {loop_counter} tamamlandi, {loop_delay}s bekleniyor...")
                            time.sleep(loop_delay)
                    
                    print(f"[INFO] Token {token_index} thread'i sonlandi!")
                    
                except Exception as e:
                    print(f"[ERROR] Token {token_index} thread hatasi: {e}")
            
            for i, token in enumerate(self.tokens, 1):
                thread = threading.Thread(target=token_spam_worker, args=(token, i))
                thread.daemon = True
                thread.start()
                threads.append(thread)
                print(f"[INFO] Token {i} thread'i baslatildi!")
            
            print(f"[OK] {len(threads)} token paralel olarak calisiyor!")
            print(f"[INFO] Ctrl+C ile durdurmak icin bekleyin...")
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                print(f"\n[INFO] Durdurma sinyali alindi...")
                stop_event.set()
                
                for thread in threads:
                    thread.join(timeout=5)
                
                print(f"[OK] Tum thread'ler sonlandi!")
                return True
                
        except Exception as e:
            print(f"[ERROR] Paralel spam hatasi: {e}")
            return False
            
    def disconnect(self):
        self.session.close()
        print("[INFO] Baglanti kesildi")

raider = DiscordRaider()