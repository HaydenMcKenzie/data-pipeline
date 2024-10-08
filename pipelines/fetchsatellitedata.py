import requests

def fetch_satellite_data():
	url = f"https://api.n2yo.com/rest/v1/satellite/above/-37.8136/144.9631/0/10/&apiKey=AA5E5C-L8M6T2-3DWWUN-5CLU"

	response = requests.get(url)
	if response.status_code == 200:
		return response.json()
	else:
		return {"error": response.status_code, "message": response.text}

satellite_data = fetch_melbourne_satellites()
print(satellite_data)
