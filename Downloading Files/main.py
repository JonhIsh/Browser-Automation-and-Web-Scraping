import requests

from_date = input("Enter start date in yyyy-mm-dd format:")
to_date = input("Enter end date in yyyy-mm-dd format:")
ticker = input("Enter ticker:")

url = f"https://api.nasdaq.com/api/quote/{ticker}/historical?assetclass=stocks&fromdate={from_date}&limit=99999&todate={to_date}&random=37"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).json()

def write_section(file, section):
    str = ""
    for value in section:
        str += f"{value};"
    str = str[:-1]
    str += "\n"
    file.write(str)
    

with open("data.csv", 'w') as file:
    write_section(file, content.get("data").get("tradesTable").get("headers"))
    for value in content.get("data").get("tradesTable").get("rows"):
        write_section(file, value.values())