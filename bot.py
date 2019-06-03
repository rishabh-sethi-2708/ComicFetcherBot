import telegram
import time

from telegram.ext import CommandHandler,Updater,MessageHandler,Filters
from selenium import webdriver
token='707408566:AAEMMdTnkCYyrD4pXsFDhtzLhWLlALUFIhs'
updater = Updater(token)

def main():

	def start(bot,update):
	    bot.send_message(chat_id=update.message.chat_id, text="Hello! I'm a bot, How can I help you?")

	def echo(bot,update):
		bot.send_message(chat_id=update.message.chat_id, text="Wrong command entered")

	def daily(bot,update):
		bot.send_message(chat_id=update.message.chat_id, text="Daily image")
		#browser = webdriver.Firefox(executable_path=r'C:\Users\Rishabh Sethi\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
		browser = webdriver.PhantomJS(executable_path=r'C:\Users\Rishabh Sethi\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
		browser.get('http://explosm.net/comics/5258/')
		img = browser.find_element_by_id('main-comic')
		src = img.get_attribute('src')
		bot.sendPhoto(chat_id=update.message.chat_id, photo=src)
		bot.send_message(chat_id=update.message.chat_id, text="Daily image 1")
		browser.close()

	def random(bot,update):
		bot.send_message(chat_id=update.message.chat_id, text="Random image")
		#browser = webdriver.Firefox(executable_path=r'C:\Users\Rishabh Sethi\Downloads\geckodriver-v0.24.0-win64\geckodriver.exe')
		browser = webdriver.PhantomJS(executable_path=r'C:\Users\Rishabh Sethi\Downloads\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
		browser.get('http://explosm.net/comics/5258/')
		button = browser.find_element_by_class_name('nav-random')
		button.click() 
		time.sleep(5)
		img = browser.find_element_by_id('main-comic')
		src = img.get_attribute('src')
		bot.sendPhoto(chat_id=update.message.chat_id, photo=src)
		bot.send_message(chat_id=update.message.chat_id, text="Random image 1")
		browser.close()	

	dispatcher = updater.dispatcher

	start_handler = CommandHandler('start', start)
	dispatcher.add_handler(start_handler)

	daily_handler = CommandHandler('daily', daily)
	dispatcher.add_handler(daily_handler)

	random_handler = CommandHandler('random', random)
	dispatcher.add_handler(random_handler)

	echo_handler = MessageHandler(Filters.text, echo)
	dispatcher.add_handler(echo_handler)

	updater.start_polling(clean = True)
	updater.idle()

if __name__ == "__main__":
	main()