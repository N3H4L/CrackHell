#!/usr/bin/python3

import argparse
import requests
import sys
from bs4 import BeautifulSoup

def requestMD5DecryptAPI(url, hash):
	data = {"hash":hash, "decrypt":"Decrypt"}

	response = requests.post(url, data=data)
	if "Sorry, this hash is not in our database" in response.text:
		print("[-] Hash not found in the database.")
		return None
	else:
		soup = BeautifulSoup(response.content, "html5lib")
		results = soup.find_all("b")
		cracked = results[0].get_text()
		print(f"[*] Cracked hash - {cracked}")
		return cracked

def identifyHash(hash):
	length = len(hash)

	if length == 32:
		print("[*] Found hash type - MD5")
		return "md5"

	elif length == 40:
		print("[*] Found hash type - SHA1")
		return "sha1"

	elif length == 64:
		print("[*] Found hash type - SHA256")
		return "sha256"

	elif length == 128:
		print("[*] Found hash type - SHA512")
		return "sha512"

	else: 
		print("[-] Could not find hash type.")

def md5crack(hash):
	print("[*] Trying to decrypt MD5 hash.")
	
	url = "https://md5decrypt.net/en/"
	cracked = requestMD5DecryptAPI(url, hash)

	return cracked

def sha1crack(hash):
	print("[*] Trying to decrypt SHA1 hash.")
	
	url = "https://md5decrypt.net/en/Sha1/"
	cracked = requestMD5DecryptAPI(url, hash)

	return cracked

def sha256crack(hash):
	print("[*] Trying to decrypt SHA256 hash.")
	
	url = "https://md5decrypt.net/en/Sha256/"
	cracked = requestMD5DecryptAPI(url, hash)

def sha512crack(hash):
	print("[*] Trying to decrypt SHA512 hash.")
	
	url = "https://md5decrypt.net/en/Sha512/"
	cracked = requestMD5DecryptAPI(url, hash)

	return cracked

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-c", "--crack", help="Hash to crack")
	parser.add_argument("-t", "--type", help="Hash type to crack")
	arg = parser.parse_args()

	banner = "-----------------------------------------------------\n"
	banner += "|                  CrackHell v1.0                   |\n"
	banner += "|---------------------------------------------------|\n"
	banner += "| Coded by : Nehal Zaman                            |\n"
	banner += "| Github   : https://github.com/N3H4L/CrackHell     |\n"
	banner += "-----------------------------------------------------\n"

	if arg.crack == None:
		parser.print_usage()
	
	else:
		print(banner)
		hash = arg.crack
		hash_type = arg.type

		print(f"[*] Your hash - {hash}")
		
		if hash_type == None:
			print("[*] Identifying hash type.")
			hash_type = identifyHash(hash)
			if hash_type == None:
				sys.exit()

		if hash_type.lower() == "md5":
			plain = md5crack(hash)

		elif hash_type.lower() == "sha1":
			plain = sha1crack(hash)

		elif hash_type.lower() == "sha256":
			plain = sha256crack(hash)

		elif hash_type.lower() == "sha512":
			plain = sha512crack(hash)
