import requests
from concurrent.futures import ThreadPoolExecutor
import time

API_KEY = "1f67cd4aa973dd153bbc2474c904ab3f"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
	url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
	try:
		response = requests.get(url, timeout=5)
		if response.status_code == 200:
			data = response.json()
			temp = data['main']['temp']
			print(f"{city }  :  {temp}°C")
			return (city, temp)
		else:
			print(f"{city}  :  Error: {response.status_code}")
	except Exception as e:
		print(f"{city}  :  Failed: {e}")

def main():
	cities = [
		"Anakapalle", "Srikakulam", "Vijayanagaram", "Guntur", "Nellore", "Hyderabad",
		"Tirumala", "Ooty", "Bangalore", "Odisha", "Kollam", "Kanyakumari",
		"Mumbai", "Bhubaneswar", "West Bengal", "Amaravathi", "Coimbatore", "Mysuru",
		"Visakhapatnam", "Noida"
	]

	start = time.time()

	max_threads = min(10, len(cities))
	results = []

	with ThreadPoolExecutor(max_workers = max_threads) as executor:
		for result in executor.map(fetch_weather, cities):
			if result:
				results.append(result)
	#print(result)

	end = time.time()
	print(f"\nTotal time taken: {end - start:.2f} seconds")

main()
