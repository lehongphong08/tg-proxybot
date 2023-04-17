
import requests, re 
from telebot import TeleBot

bot = TeleBot ("your api key")

pages = [
    "https://free-proxy-list.net",
    "https://www.sslproxies.org",
    "https://us-proxy.org"
]

proxies_list = []
for page in pages:
    response = requests.get(page)
    matches = re.findall(r"\d+\.\d+\.\d+\.\d+:\d+", response.text)
    proxies_list.extend(matches)


for proxy in proxies_list:
    bot.send_message(chat_id="your-chat-id", text=f"Proxy found: {proxy}")