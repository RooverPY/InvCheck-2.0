import os
import random
import string
import asyncio
import itertools
import aiohttp
headers={"user-agent": "Mozilla/5.0 (Linux; Android 12; 21081111RG Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/98.0.4758.101 Mobile Safari/537.36 UCURSOS/v1.6_269-android"}
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
CYAN = '\033[96m'
chars = []
chars[:0] = string.ascii_letters + string.digits
if os.stat("proxies.txt").st_size > 0:
	global proxies
	proxies = itertools.cycle(open("proxies.txt", "r+").read().splitlines())
else:
	print(f"{RED}	Proxies are required")
	quit()

async def gen(amount: int):
	async with aiohttp.ClientSession() as session:
		prox = False
		for i in range(amount):
			code = "".join(random.choices(chars, k=8))
			if prox is False:
				check = await session.get(f"https://discord.com/api/v9/invites/{code}?with_counts=true&with_expiration=true",headers=headers)
			else:
				check = await session.get(f"https://discord.com/api/v9/invites/{code}?with_counts=true&with_expiration=true",proxy=f"http://{next(proxies)}", headers=headers)

			if check.status == 200:
				print(f"{GREEN}	Valid {i} : {code}")	
			elif check.status == 429:
				print(f"{BLUE}	Ratelimited {i+1} :{code}")		
				prox = True
			else:
				print(f"{RED}	Invalid {i+1} {code}")

def start():
	print("	"+ f"{RED}-"*69)
	print(RED + """
	██╗███╗░░██╗██╗░░░██╗██╗████████╗███████╗  ░██████╗░███████╗███╗░░██╗ by github.com/Mewzax
	██║████╗░██║██║░░░██║██║╚══██╔══╝██╔════╝  ██╔════╝░██╔════╝████╗░██║ and github.com/Rooverpy
	██║██╔██╗██║╚██╗░██╔╝██║░░░██║░░░█████╗░░  ██║░░██╗░█████╗░░██╔██╗██║
	██║██║╚████║░╚████╔╝░██║░░░██║░░░██╔══╝░░  ██║░░╚██╗██╔══╝░░██║╚████║
	██║██║░╚███║░░╚██╔╝░░██║░░░██║░░░███████╗  ╚██████╔╝███████╗██║░╚███║
	╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝
		  """)
	print(CYAN + '	A powerful tool to generate, check and store Discord Invites ✉️\n')
	while True:
		try:
			amount = int(input(GREEN + "	How many invites do you want to generate? "))
			print("\n")
			break
		except Exception as e:
			print(f"	~ {YELLOW}Input Failure | {e}")	
			pass
	asyncio.run(gen(amount))

if __name__ == "__main__":
	os.system("cls" if os.name == "nt" else "clear")
	start()
