import base64
import sys, socket, select
import os
import hashlib
import signal
from selenium import webdriver
from getpass import getpass
from cryptography.fernet import Fernet

def encrypt(secret,data):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
	cipher = AES.new(secret)
	encoded = EncodeAES(cipher, data)
	return encoded


username = input('Enter your username or email id: ')
key = Fernet.generate_key()
f = Fernet(key)
usernametoken = f.encrypt(b'username')
password = getpass('Enter your password : ')
key = Fernet.generate_key()
f = Fernet(key)
usernametoken = f.encrypt(b'password')

def decrypt(secret,data):
	BLOCK_SIZE = 32
	PADDING = '{'
	pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
	DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
	cipher = AES.new(secret)
	decoded = DecodeAES(cipher, data)
	return decoded

webdriver = webdriver.Chrome()
webdriver.get('https://www.facebook.com/')

username_box = webdriver.find_element_by_id('email')
username_box.send_keys(username)

password_box = webdriver.find_element_by_id('pass')
password_box.send_keys(password)

login_btn = webdriver.find_element_by_id('u_0_2')
login_btn.submit()