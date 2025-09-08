import requests
import json

x = requests.get('https://www.elprisetjustnu.se/api/v1/prices/kvartspris_demo.json')
json_text = json.loads(x.text)
output = json_text[0]["SEK_per_kWh"]
print(output)