import praw
import requests
from bs4 import BeautifulSoup
import csv
import time

class notification(object):
	def reddit_notification():
		reddit = praw.Reddit(client_id="yruq0VWhhMUUHQ",client_secret="c8Edp8djyOedVVMiNm6niWBT1PQ",username="kinkness213",password="kinkpassword",user_agent="userr_agent")

		subreddit = reddit.subreddit('Jobs4Bitcoins+forhire')
		hot_thread = subreddit.new(limit=8)
		keywords = ['python', 'Python', 'Developer', 'Javascript', 'javascript', 'Script', 'script',  'Scraper','Webscraper', 'scraper','webscraper', 'Telegram bot', 'telegram bot', 'bot', 'Bot','website','web app', 'django', 'full stack', 'react', 'reactjs', 'Reddit bot', 'reddit bot']
		for sub in hot_thread:
			if sub.stickied == False:
				sub = sub.title
				print(sub)
				try:
					sub = sub.split(']')
					if sub[0] == '[Hiring' or sub[0] == '[HIRING' or sub[0] == '[hiring':
						print(sub)
						for keyword in keywords:
							if keyword in sub[1]:
								print('there is one')
								submission = ''.join(sub)
								return submission
							else:
								print('there is none')
								submission = ''
								
					else:
						if 'Looking for' in sub[0] or 'looking for' in sub[0] or 'LOOKING FOR' in sub[0]:
							for keyword in keywords:
								if keyword in sub[1]:
									print('there is one')
									submission = ''.join(sub)
									return submission
								else:
									print('there is none')
									submission = ''
									
				except:
					print('somethin went wrong')
		submission = ''
		return submission


	def bitcointalk_notification():
		url_request = requests.get('https://bitcointalk.org/index.php?board=52.0').text
		Html_element = BeautifulSoup(url_request, 'lxml')

		all_article = Html_element.findAll('span')
		first_article = all_article[7].text
		keywords = ['python', 'Python', 'Developer', 'Javascript', 'javascript', 'Script', 'script',  'Scraper','Webscraper', 'scraper','webscraper', 'Telegram bot', 'telegram bot', 'bot', 'Bot','raffle bot', 'Raffle bot', 'Reddit bot', 'reddit bot']
		

		try:
			article = first_article.split(']')
			if article[0] == '[Hiring' or article[0] == '[HIRING' or article[0] == '[hiring':
				print(sub)
				for keyword in keywords:
					if keyword in article[1]:
						print('there is one')
						submission = ''.join(article)
						return submission
					else:
						print('there is none')
						submission = ''
						
			else:
				if 'Looking for' in article[0] or 'looking for' in article[0] or 'LOOKING FOR' in article[0]:
					for keyword in keywords:
						if keyword in article[1]:
							print('there is one')
							submission = ''.join(article)
							return submission
						else:
							print('there is none')
							submission = ''
							
		except:
			print('somethin went wrong')
		submission = ''

		return submission

	def is_new(article):
		csv_file = open('seen_data', 'a')
		csv_writer = csv.writer(csv_file)
		
		csv_writer.writerow(article)
		
		with open('seen_data', 'r+') as f:
			csv_reader = csv.reader(f)
			counter = 0
			for ids, row in enumerate(csv_reader):
				print('pass')
				if len(row)> 0:
					print('pass')
					if ids == counter:
						if article == ''.join(row):
							print(article)
							return True
				counter += 1

			if counter > 1000:
				csv_file = open('seen_data', 'w')

	def send_notification(article_name):
		TOKEN = '903078328:AAGHPU6Xt8jYEa1m8ExOVneTIsurh80Tal4'
		BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
		UPDATE_TELEGRAM_URL = 'https://api.telegram.org/bot{}/getUpdates'.format(TOKEN)
		TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}'
			
		print('send message')
		chat_id = '689752132'
		Send_message = BASE_TELEGRAM_URL+'/sendMessage?chat_id={}&text={}'.format(chat_id, article_name)
		requests.get(Send_message)




		

while True:
	notif = notification

	##########Reddit################
	content = notif.reddit_notification()
	print(content)
	result = notif.is_new(content)
	print(result)
	
	##########Bitcointalk#############
	content1 = notif.bitcointalk_notification()
	print(content1)
	result1 = notif.is_new(content1)
	print(result)
	
	###########SendModule#############
	if content != '' and result != True :
		notif.send_notification(content)

	if content1 != '' and result1 != True :
		notif.send_notification(content1)

	time.sleep(60)
	


	