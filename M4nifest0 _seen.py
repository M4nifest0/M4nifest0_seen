#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ☠️ M4nifest0 Black Hat Hacking Team™💪🏴‍☠️
# 💀 Made by ☠️👊 𝕿𝖍𝖎𝖘 𝕴𝖘 𝕿𝖍𝖊 𝓜4𝓷𝓲𝓯𝓮𝓼𝓽0 𝕿𝖊𝖆𝖒™💪🏴‍☠️
# ☠️ Author 🏴‍☠️ hack4lx 👊 | erfan4lx
# ♾ Monday - 2020 12 October 💪
# 👁‍🗨 Version 1.0.0💪
# 👌 Disclaimer:Any misuse is the responsibility of the user


import requests
import threading
import sys

print ("")
print ("$$\                           $$\       $$\   $$\ $$\  ")         
print ("$$ |                          $$ |      $$ |  $$ |$$ | ")         
print ("$$$$$$$\   $$$$$$\   $$$$$$$\ $$ |  $$\ $$ |  $$ |$$ |$$\   $$\ ")
print ("$$  __$$\  \____$$\ $$  _____|$$ | $$  |$$$$$$$$ |$$ |\$$\ $$  |")
print ("$$ |  $$ | $$$$$$$ |$$ /      $$$$$$  / \_____$$ |$$ | \$$$$  / ")
print ("$$ |  $$ |$$  __$$ |$$ |      $$  _$$<        $$ |$$ | $$  $$<  ")
print ("$$ |  $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\       $$ |$$ |$$  /\$$\ ")
print ("\__|  \__| \_______| \_______|\__|  \__|      \__|\__|\__/  \__|")
print ("")


max = threading.Semaphore(value=500) 
threads = []
list = open('proxies.txt', 'r')
proxies = list.readlines()
list.close()

def fetchData(channel='google', post='1', proxy=None):
	try:
		r = requests.get('https://t.me/'+channel+'/'+post+'?embed=1', timeout=20, proxies={'https':proxy})
		cookie = r.headers['set-cookie'].split(';')[0]
		key = r.text.split('data-view="')[1].split('"')[0]
		if 'stel_ssid' in cookie: 
			return {'key':key,'cookie':cookie}
		else:
			return False
	except Exception as e:
		return False
		
def addViewToPost(channel='google', post='1', key=None, cookie=None, proxy=None):
	try:
		r = requests.get('https://t.me/v/?views='+key, timeout=20, headers={
		'x-requested-with':'XMLHttpRequest',
		'user-agent':'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'referer':'https://t.me/'+channel+'/'+post+'?embed=1',
        'cookie':cookie}, proxies={'https':proxy}
		)
		return r.text
	except Exception as e:
		return False
		
def run(channel, post, proxy):
	max.acquire()
	s = fetchData(channel, post, 'https://'+proxy)
	if (type(s) is dict):
		l = addViewToPost(channel, post, s['key'], s['cookie'], 'https://'+proxy)
		if l != False: print('Proxy '+proxy+' finished its job successfully!')
	max.release()
	print('Thread with proxy '+proxy+' has been terminated.')

for proxy in proxies:
	p = proxy.split('\n')[0]
	thread = threading.Thread(target=run,args=(sys.argv[1],sys.argv[2],p))
	threads.append(thread)
	thread.start()
	print('Started new thread with proxy '+p)