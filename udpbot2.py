
import telegram
from telegram.ext import Updater, CommandHandler
from urllib.request import urlopen

def scrape_proxy_list(web_url):
    
        page = urlopen(web_url)
        proxy_list = []
        for line in page:
            line = line.decode("utf-8")
            if "IP" in line:
                ip_address = line.split('\t')[0]
                port = line.split('\t')[1]
                proxy = ip_address + ':' + port
                proxy_list.append(proxy)
        return proxy_list
    except Exception as e:
        print('Error occured:', e)

def upload_query_result(update, context):
  
    url = 'https://www.sslproxies.org/'
    proxy_list = scrape_proxy_list(url)

 
    text = ""
    for proxy in proxy_list:
        text += proxy + "\n"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text) 
   
bot = telegram.Bot(token="1234567890:abcdefghijklmnopqrstuvwxyz")
updater = Updater(token="1234567890:abcdefghijklmnopqrstuvwxyz", use_context=True)
dispatcher = updater.dispatcher
upload_handler = CommandHandler('upload_list', upload_query_result)
dispatcher.add_handler(upload_handler)

#Start polling
updater.start_polling()
